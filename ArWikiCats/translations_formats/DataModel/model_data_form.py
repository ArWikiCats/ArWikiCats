#!/usr/bin/python3
""" """

import logging
import re
from typing import Callable, Optional

logger = logging.getLogger(__name__)


class FormatDataFrom:
    """
    A dynamic wrapper for handling category transformations with customizable callbacks.

    This class provides a flexible way to normalize category strings by extracting
    keys (e.g., year patterns, country names) and replacing them with placeholders.
    It uses callback functions for key matching and searching, allowing customization
    for different category types.

    Attributes:
        formatted_data (dict[str, str]): Mapping of template patterns to Arabic translations.
        formatted_data_ci (dict[str, str]): Case-insensitive version of formatted_data.
        key_placeholder (str): Placeholder string for the key (e.g., "{year1}", "{country1}").
        value_placeholder (str): Placeholder string for the value in Arabic templates.
        search_callback (callable): Function to search/translate a key to its Arabic label.
        match_key_callback (callable): Function to extract a key from a category string.
        fixing_callback (callable | None): Optional callback for post-processing results.

    Example:
        >>> bot = FormatDataFrom(
        ...     formatted_data={"{year1} {country1}": "{country1} في {year1}"},
        ...     key_placeholder="{country1}",
        ...     value_placeholder="{country1}",
        ...     search_callback=lambda x: "كتاب من اليمن" if "yemen" in x.lower() else "",
        ...     match_key_callback=lambda x: x.replace("{year1}", "").strip(),
        ... )
        >>> bot.match_key("{year1} writers from yemen")
        'writers from yemen'
    """

    def __init__(
        self,
        formatted_data: dict[str, str],
        key_placeholder: str,
        value_placeholder: str,
        search_callback: Callable,
        match_key_callback: Callable,
        fixing_callback: Optional[Callable] = None,
    ) -> None:
        """
        Create a FormatDataFrom instance configured with templates, placeholders, and lookup/matching callbacks.

        Parameters:
            formatted_data (dict[str, str]): Mapping of template keys to their Arabic label templates.
            key_placeholder (str): Placeholder string used to replace matched keys in category templates (e.g., "{country1}").
            value_placeholder (str): Placeholder in Arabic templates to be replaced with the translated key value.
            search_callback (Callable): Function that takes a key string and returns its translated label.
            match_key_callback (Callable): Function that extracts the key from a category string; returns the matched substring or None.
            fixing_callback (Optional[Callable]): Optional post-processing function applied to final labels; receives the label and value and returns a fixed string.
        """
        self.search_callback = search_callback
        self.match_key_callback = match_key_callback

        self.key_placeholder = key_placeholder
        self.value_placeholder = value_placeholder
        self.formatted_data = formatted_data
        self.formatted_data_ci = {k.lower(): v for k, v in formatted_data.items()}
        self.fixing_callback = fixing_callback

    def match_key(self, text: str) -> str:
        """Extract English year/decade and return it as the key."""
        return self.match_key_callback(text)

    def normalize_category(self, text: str, key: str) -> str:
        """
        Replace matched year with placeholder.
        normalize_category: key='writers from yemen', text='{year1} writers from yemen'
        """
        logger.debug(f"normalize_category: {key=}, {text=}")
        if not key:
            return text
        result = re.sub(re.escape(key), self.key_placeholder, text, flags=re.IGNORECASE)
        logger.debug(f"normalize_category: {result=}")  # result='{year1} {country1}'
        return result

    def normalize_category_with_key(self, category: str) -> tuple[str, str]:
        """
        Extract the key from a category and return the key plus the category with that key replaced by the key placeholder.

        Parameters:
            category (str): Category string to analyze and normalize.

        Returns:
            tuple[str, str]: A tuple where the first element is the extracted key (empty string if none),
            and the second element is the category with the key replaced by the key placeholder
            (empty string if no key was found).
        """
        key = self.match_key(category)
        result = ""
        if key:
            result = self.normalize_category(category, key)
        return key, result

    def replace_value_placeholder(self, label: str, value: str) -> str:
        """
        Substitutes the instance's value placeholder in a label with the provided value and applies an optional post-processing callback.

        Parameters:
            label (str): Template string that may contain the instance's value placeholder.
            value (str): Text to replace the value placeholder with.

        Returns:
            str: The label with the placeholder replaced; if a fixing callback is configured, its output is returned.
        """
        # Replace placeholder
        logger.debug(f"!!!! replace_value_placeholder: {self.value_placeholder=}, {label=}, {value=}")
        result = label.replace(self.value_placeholder, value)
        if self.fixing_callback:
            result = self.fixing_callback(result)
        return result

    def get_template_ar(self, template_key: str) -> str:
        """
        Retrieve the Arabic template for a template key using a case-insensitive lookup and optional "category:" prefix handling.

        Parameters:
            template_key (str): Template key to look up; may include or omit the "category:" prefix.

        Returns:
            str: The matched Arabic template, or an empty string if no template is found.
        """
        # Case-insensitive key lookup
        template_key = template_key.lower()
        logger.debug(f"get_template_ar: {template_key=}")
        result = self.formatted_data_ci.get(template_key, "")

        if not result:
            if template_key.startswith("category:"):
                template_key = template_key.replace("category:", "")
                result = self.formatted_data_ci.get(template_key, "")
            else:
                result = self.formatted_data_ci.get(f"category:{template_key}", "")

        logger.debug(f"get_template_ar: {template_key=}, {result=}")
        return result

    def get_key_label(self, key: str) -> str:
        """
        Return the Arabic label for a matched key extracted from a category.

        Parameters:
            key (str): The extracted key (e.g., a country or year token) to translate.

        Returns:
            str: The Arabic label for `key`, or an empty string if `key` is empty.
        """
        if not key:
            return ""
        logger.debug(f"get_key_label: {key=}")
        return self.search(key)

    def search(self, text: str) -> str:
        """
        Translate the given text using the configured search callback.

        @returns The translated text produced by the search callback.
        """
        return self.search_callback(text)

    def prepend_arabic_category_prefix(self, category: str, result: str) -> str:
        """
        Ensure the Arabic prefix "تصنيف:" is present on `result` when `category` begins with "category:".

        Parameters:
            category (str): The original category string to check (case-insensitive).
            result (str): The label that may require the Arabic "تصنيف:" prefix.

        Returns:
            str: `result` with "تصنيف:" prepended if `category` started with "category:" and `result` did not already start with "تصنيف:", otherwise `result` unchanged.
        """
        if result and category.lower().startswith("category:") and not result.startswith("تصنيف:"):
            result = "تصنيف:" + result
        return result

    def search_all(self, key: str, add_arabic_category_prefix: bool = False) -> str:
        """
        Translate the provided key and optionally ensure the Arabic category prefix is present.

        Parameters:
            key (str): The category or token to translate.
            add_arabic_category_prefix (bool): If True, prefix the result with the Arabic category marker "تصنيف:" when appropriate.

        Returns:
            str: The translated label for the key (empty string if not found); possibly prefixed with "تصنيف:" when requested and applicable.
        """
        result = self.search(key)

        if add_arabic_category_prefix:
            result = self.prepend_arabic_category_prefix(key, result)
        return result
