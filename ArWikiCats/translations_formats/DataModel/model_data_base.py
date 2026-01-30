#!/usr/bin/python3
"""
Base module for category translation formatter classes.

This module provides the FormatDataBase class which serves as the foundation
for all single-element category translation formatters. It contains shared
functionality for pattern matching, template lookup, and placeholder replacement.

Classes:
    FormatDataBase: Abstract base class for all FormatData-type formatters.

The FormatDataBase class provides:
    - Regex pattern building from data_list keys
    - Case-insensitive key matching and template lookup
    - Placeholder normalization and replacement
    - Caching for performance optimization

Example:
    >>> # FormatDataBase is an abstract class - use FormatData instead
    >>> from ArWikiCats.translations_formats.DataModel import FormatData
    >>> bot = FormatData(
    ...     formatted_data={"{sport} players": "لاعبو {sport_label}"},
    ...     data_list={"football": "كرة القدم"},
    ...     key_placeholder="{sport}",
    ...     value_placeholder="{sport_label}",
    ... )
    >>> bot.search("football players")
    'لاعبو كرة القدم'
"""

import logging
import re
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class FormatDataBase:
    """
    Abstract base class for single-element category translation formatters.

    This class provides the core functionality for translating category strings
    by matching keys from a data_list and replacing them using template patterns.
    It is meant to be subclassed by specific formatter implementations.

    Attributes:
        formatted_data (Dict[str, str]): Template patterns mapping English patterns to Arabic templates.
        formatted_data_ci (Dict[str, str]): Case-insensitive version of formatted_data.
        data_list (Dict[str, Any]): Key-to-Arabic-label mappings for replacements.
        data_list_ci (Dict[str, Any]): Case-insensitive version of data_list.
        key_placeholder (str): Placeholder string for the key in patterns.
        text_after (str): Optional text that appears after the key.
        text_before (str): Optional text that appears before the key.
        regex_filter (str): Regex pattern for word boundary detection.
        alternation (str): Regex alternation string built from data_list keys.
        pattern (re.Pattern): Compiled regex pattern for key matching.

    Methods:
        match_key: Find and return a matching key from the category.
        normalize_category: Replace matched key with placeholder.
        get_template: Get Arabic template for a category.
        get_template_ar: Get Arabic template by normalized key.
        get_key_label: Get Arabic label for a key.
        search: End-to-end translation of a category string.
        create_label: Alias for search.

    Note:
        Subclasses must implement apply_pattern_replacement and replace_value_placeholder.

    Example:
        >>> # This is an abstract class - see FormatData for usage
        >>> from ArWikiCats.translations_formats.DataModel import FormatData
    """

    def __init__(
        self,
        formatted_data: Dict[str, str],
        data_list: Dict[str, Any],
        key_placeholder: str = "xoxo",
        text_after: str = "",
        text_before: str = "",
        regex_filter: str = r"\w",
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""
        # Store originals
        self.formatted_data = formatted_data
        self.data_list = data_list
        self.text_after = text_after
        self.regex_filter = regex_filter or r"\w"  # [\w-]
        self.text_before = text_before

        # Case-insensitive mirrors
        self.formatted_data_ci: Dict[str, str] = {k.lower(): v for k, v in formatted_data.items()}
        self.data_list_ci: Dict[str, Any] = {k.lower(): v for k, v in data_list.items()}

        self.key_placeholder = key_placeholder
        self.alternation: str = None
        self.pattern: Optional[re.Pattern[str]] = None
        self.pattern_double: Optional[re.Pattern[str]] = None

    def add_formatted_data(self, key: str, value: str) -> None:
        """Add a key-value pair to the data_list."""
        self.formatted_data[key] = value
        self.formatted_data_ci[key.lower()] = value

    def create_alternation(self) -> str:
        """Create regex alternation from data_list_ci keys."""
        if not self.data_list_ci:
            return ""

        if len(self.data_list_ci) > 1000:
            logger.debug(f">keys_to_pattern(): len(new_pattern keys) = {len(self.data_list_ci):,}")

        # to fix bug that selected "black" instead of "black-and-white"
        keys_sorted = sorted(self.data_list_ci.keys(), key=lambda k: (-k.count(" "), -len(k)))

        return "|".join(map(re.escape, keys_sorted))

    def keys_to_pattern(self) -> Optional[re.Pattern[str]]:
        """
        Create a compiled, case-insensitive regular expression that matches any key from the case-insensitive data list as a standalone token using the configured word-boundary filter.

        Returns:
            re.Pattern[str] | None: A compiled regex matching any key bounded by the `regex_filter`, or `None` if `data_list_ci` is empty.
        """
        if not self.data_list_ci:
            return None

        if self.alternation is None:
            self.alternation = self.create_alternation()

        data_pattern = rf"(?<!{self.regex_filter})({self.alternation})(?!{self.regex_filter})"
        return re.compile(data_pattern, re.I)

    def match_key(self, category: str) -> str:
        """
        Finds the canonical key present in the given category string.

        Returns:
                lowercased key from data_list if a matching key is found, otherwise an empty string.
        """
        if not self.pattern:
            return ""
        # Normalize the category by removing extra spaces
        normalized_category = " ".join(category.split())
        logger.debug(f">!> match_key: {normalized_category=}")

        # TODO: check this
        if self.data_list_ci.get(normalized_category.lower()):
            logger.debug(f">>!!>> match_key: found in data_list_ci {normalized_category=}")
            return normalized_category.lower()

        match = self.pattern.search(f" {normalized_category} ")
        result = match.group(1).lower() if match else ""
        logger.debug(f"==== match_key {result=}")
        return result

    def handle_texts_before_after(self, normalized: str) -> str:
        """
        Normalize a category string by removing configured text_before or text_after surrounding the key placeholder when appropriate.

        Parameters:
            normalized (str): Input string that may contain the key placeholder.

        Returns:
            str: The adjusted string where occurrences of `text_before + key_placeholder` or `key_placeholder + text_after` have been replaced by `key_placeholder` when applicable; otherwise the original string.
        """
        if not self.text_before and not self.text_after:
            return normalized

        logger.debug(f"handle_texts_before_after: {normalized=}")
        # no need for further processing
        # (text_before="the ") but key: ("the {nat_en} actors") already in formatted_data_ci so no need to replace
        if self.formatted_data_ci.get(normalized.strip(), ""):
            logger.debug(f"handle_texts_before_after: found directly {normalized.strip()=} in formatted_data_ci")
            return normalized

        if self.text_before:
            if f"{self.text_before}{self.key_placeholder}" in normalized:
                normalized = normalized.replace(f"{self.text_before}{self.key_placeholder}", self.key_placeholder)

            # no need for further processing
            # (text_after=" people") but key: ("{nat_en} people actors") already in formatted_data_ci so no need to replace
            if self.formatted_data_ci.get(normalized.strip(), ""):
                return normalized

        if self.text_after:
            if f"{self.key_placeholder}{self.text_after}" in normalized:
                normalized = normalized.replace(f"{self.key_placeholder}{self.text_after}", self.key_placeholder)

        return normalized

    def normalize_category(self, category: str, sport_key: str) -> str:
        """
        Replace the first occurrence of sport_key in category with the configured key placeholder and apply any configured text_before/text_after adjustments.

        Parameters:
                category (str): The original category string to normalize.
                sport_key (str): The key to find and replace; matching is case-insensitive and respects word boundaries as defined by the instance's regex_filter.

        Returns:
                normalized (str): The resulting string with the first matched sport_key replaced by the key placeholder, surrounding text adjustments applied, and leading/trailing whitespace removed.
        """
        # Normalize the category by removing extra spaces
        normalized_category = " ".join(category.split())

        normalized = re.sub(
            rf"(?<!{self.regex_filter}){re.escape(sport_key)}(?!{self.regex_filter})",
            f"{self.key_placeholder}",
            f" {normalized_category.strip()} ",
            flags=re.IGNORECASE,
            count=1,
        )

        normalized = self.handle_texts_before_after(normalized)
        return normalized.strip()

    def normalize_category_with_key(self, category: str) -> tuple[str, str]:
        """
        Normalize nationality placeholders within a category string.

        Example:
            normal:
                category:"Yemeni national football teams", result: "natar national football teams"
            model_data_double:
                category='{nat_en} action drama films', key='action drama', result='{nat_en} {film_key} films'
        """
        key = self.match_key(category)
        result = ""
        if key:
            result = self.normalize_category(category, key)
            logger.debug(f">>> {category=}, {key=}, {result=}")

        return key, result

    def get_template(self, sport_key: str, category: str) -> str:
        """Lookup template in a case-insensitive dict."""
        normalized = self.normalize_category(category, sport_key)
        logger.debug(f"[] {normalized=}")
        # Case-insensitive key lookup
        return self.formatted_data_ci.get(normalized.lower(), "")

    def get_template_ar(self, template_key: str) -> str:
        """Lookup template in a case-insensitive dict."""
        # Case-insensitive key lookup
        template_key = template_key.lower()
        logger.debug(f"{template_key=}")
        result = self.formatted_data_ci.get(template_key, "")

        if not result:
            if template_key.startswith("category:"):
                template_key = template_key.replace("category:", "")
                result = self.formatted_data_ci.get(template_key, "")
            else:
                result = self.formatted_data_ci.get(f"category:{template_key}", "")

        logger.debug(f"{template_key=}, {result=}")
        return result

    def get_key_label(self, sport_key: str) -> Any:
        """Return the Arabic label mapped to the provided key if present."""
        return self.data_list_ci.get(sport_key)

    def _search(self, category: str) -> str:
        """End-to-end resolution."""
        logger.debug("$$$ start _search(): ")
        logger.debug(f"++++++++ _search {self.__class__.__name__} ++++++++ ")

        if self.formatted_data_ci.get(category):
            return self.formatted_data_ci[category]

        sport_key = self.match_key(category)

        if not sport_key:
            logger.debug(f"No sport key matched for {category=}")
            return ""

        sport_label = self.get_key_label(sport_key)
        if not sport_label:
            logger.debug(f'No sport label matched for sport key: "{sport_key}"')
            return ""

        template_label = self.get_template(sport_key, category)
        if not template_label:
            logger.debug(f'No template label matched for sport key: "{sport_key}" and {category=}')
            return ""

        result = self.apply_pattern_replacement(template_label, sport_label)
        logger.debug(f"[] {result=}")

        logger.debug(f"++++++++ end {self.__class__.__name__} ++++++++ ")

        return result

    def apply_pattern_replacement(self, template_label: str, sport_label: Any) -> str:
        """Replace value placeholder once template is chosen. Override in subclasses."""
        raise NotImplementedError("Subclasses must implement apply_pattern_replacement")

    def replace_value_placeholder(self, label: str, value: Any) -> str:
        """
        Replace the placeholder in a template label with a provided value.

        Parameters:
            label (str): Template string containing one or more placeholders to be replaced.
            value (Any): Value to substitute into the placeholder(s); conversion/formatting is implementation-defined.

        Returns:
            str: The label with the placeholder(s) replaced by the provided value.

        Raises:
            NotImplementedError: Always raised by the base implementation; subclasses must override this method.
        """
        raise NotImplementedError("Subclasses must implement replace_value_placeholder")

    def search(self, category: str) -> str:
        """
        Return a translated label for the given category using a cached lookup.

        Parameters:
                category (str): The category string to translate.

        Returns:
                result (str): The translated label, or an empty string if no translation is found.
        """
        return self._search(category)

    def create_label(self, category: str) -> str:
        """
        Produce the translated label for a category string.

        Parameters:
            category (str): The input category to translate.

        Returns:
            str: The translated Arabic label for the category, or an empty string if no translation is available.
        """
        return self._search(category)

    def prepend_arabic_category_prefix(self, category, result) -> str:
        """
        Prepend the Arabic category prefix "تصنيف:" to `result` when `category` begins with "category:" and `result` is not already prefixed.

        Parameters:
            category (str): The original category string; checked case-insensitively for the "category:" prefix.
            result (str): The result string to modify.

        Returns:
            str: `result` with "تصنيف:" prepended when applicable, otherwise the original `result`.
        """
        if result and category.lower().startswith("category:") and not result.startswith("تصنيف:"):
            result = "تصنيف:" + result
        return result

    def search_all(self, category: str, add_arabic_category_prefix: bool = False) -> str:
        """
        Compute the Arabic translation for a category and optionally prepend the Arabic "تصنيف:" prefix.

        Parameters:
            category (str): The input category to translate; may include a "category:" prefix.
            add_arabic_category_prefix (bool): If True and the input starts with "category:", ensure the returned label is prefixed with "تصنيف:" when the translation does not already start with that prefix.

        Returns:
            str: The translated Arabic label for the category, or an empty string if no translation is found.
        """
        result = self._search(category)

        if add_arabic_category_prefix:
            result = self.prepend_arabic_category_prefix(category, result)
        return result

    def check_placeholders(self, category: str, result: str) -> str:
        """
        Validate that the translated result contains no unprocessed placeholders.

        If the result contains a literal "{" character, a warning is logged (including the original category) and an empty string is returned; otherwise the original result is returned.

        Parameters:
            category (str): Original category string used for context in warnings.
            result (str): Translated/processed string to check for unprocessed placeholders.

        Returns:
            str: The original `result` if it contains no "{", otherwise an empty string.
        """
        if "{" in result:
            logger.warning(f">>> Found unprocessed placeholders in {category=}: {result=}")
            return ""
        return result

    def search_all_category(self, category: str) -> str:
        """
        Translate a category string through full normalization, Arabic prefix handling, and placeholder validation.

        Normalizes the input by lowercasing and removing a leading "category:" prefix, performs the translation lookup, prepends the Arabic prefix "تصنيف:" when the original input started with "category:" and the result does not already start with that prefix, and returns an empty string if translation fails or unprocessed placeholders remain.

        Returns:
            str: Final translated label, or an empty string if no valid translation is found or placeholders are unprocessed.
        """
        logger.debug("--" * 5)
        logger.debug(">> start")
        normalized_category = category.lower().replace("category:", "")

        result = self._search(normalized_category)

        result = self.prepend_arabic_category_prefix(category, result)

        result = self.check_placeholders(category, result)

        logger.debug(">> end")
        return result
