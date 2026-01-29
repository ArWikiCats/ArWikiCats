#!/usr/bin/python3
"""
Module providing base helper classes for multi-formatter category translations.

This module provides the MultiDataFormatterBaseHelpers class which contains
shared functionality for all multi-formatter classes. It handles the core
logic of normalizing categories with two dynamic elements and combining
their translations.

Classes:
    NormalizeResult: Dataclass storing the results of category normalization.
    MultiDataFormatterBaseHelpers: Base class with shared translation logic.

Example:
    >>> # This is a base class - use subclasses like MultiDataFormatterBase instead
    >>> from ArWikiCats.translations_formats.DataModel import MultiDataFormatterBase
    >>> bot = MultiDataFormatterBase(country_bot, sport_bot)
    >>> result = bot.normalize_both_new("british football championships")
    >>> result.nat_key
    'british'
    >>> result.other_key
    'football'

test at tests.translations_formats.test_format_2_data.py
"""

import functools
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)

# -----------------------
#
# -----------------------


@dataclass
class NormalizeResult:
    """
    Data structure representing the results of category normalization.

    This dataclass stores all the components extracted during the
    normalization of a category string, including the original category,
    the template keys, and the extracted dynamic elements.

    Attributes:
        template_key_first: The normalized template after first element replacement.
        category: The original normalized category string.
        template_key: The final normalized template with both elements replaced.
        nat_key: The extracted nationality/country key.
        other_key: The extracted other element key (e.g., sport, year).

    Example:
        >>> result = NormalizeResult(
        ...     template_key_first="{nat} football championships",
        ...     category="british football championships",
        ...     template_key="{nat} {sport} championships",
        ...     nat_key="british",
        ...     other_key="football",
        ... )
    """

    template_key_first: str
    category: str
    template_key: str
    nat_key: str
    other_key: str


class MultiDataFormatterBaseHelpers:
    """
    Base class providing shared functionality for multi-formatter translations.

    This class contains the core logic for normalizing and translating
    category strings that contain two dynamic elements. It is meant to
    be inherited by specific formatter classes that define the country_bot
    and other_bot attributes.

    Attributes:
        country_bot: Formatter for the first dynamic element (set by subclass).
        other_bot: Formatter for the second dynamic element (set by subclass).
        search_first_part (bool): If True, search using only the first part.
        data_to_find (dict | None): Optional direct lookup dictionary.
        other_key_first (bool): If True, process other_bot before country_bot.

    Methods:
        normalize_nat_label: Normalize nationality element in category.
        normalize_other_label: Normalize other element (sport, year) in category.
        normalize_both_new: Normalize both elements, returning NormalizeResult.
        normalize_both: Normalize both elements, returning template string.
        create_label: Create the final Arabic translation.
        search: Alias for create_label.
        search_all: Try create_label, then individual bot searches.
        search_all_category: search_all with "تصنيف:" prefix handling.

    Example:
        >>> # Subclass usage
        >>> class MyFormatter(MultiDataFormatterBaseHelpers):
        ...     def __init__(self, country_bot, other_bot):
        ...         self.country_bot = country_bot
        ...         self.other_bot = other_bot
        ...         self.data_to_find = None
    """

    def __init__(self) -> None:
        """Initialize the base multi-formatter with default values."""
        self.data_to_find = None

    # ------------------------------------------------------
    # COUNTRY/NAT NORMALIZATION
    # ------------------------------------------------------

    def normalize_nat_label(self, category: str) -> str:
        """
        Normalize nationality placeholders within a category string.

        Example:
            category:"Yemeni national football teams", result: "natar national football teams"
        """
        key, new_category = self.country_bot.normalize_category_with_key(category)
        return new_category

    # ------------------------------------------------------
    # YEAR/SPORT NORMALIZATION
    # ------------------------------------------------------
    def normalize_other_label(self, category: str) -> str:
        """
        Normalize sport placeholders within a category string.

        Example:
            category:"Yemeni national football teams", result: "Yemeni national xoxo teams"
        """
        key, new_category = self.other_bot.normalize_category_with_key(category)
        return new_category

    def normalize_both_new(self, category: str) -> NormalizeResult:
        """
        Normalize both nationality and sport tokens in the category.

        Example:
            input: "british softball championships", output: "natar xoxo championships"
        """
        # Normalize the category by removing extra spaces
        normalized_category = " ".join(category.split())

        if getattr(self, "other_key_first", False):
            other_key, template_key_first = self.other_bot.normalize_category_with_key(normalized_category)
            nat_key, template_key = self.country_bot.normalize_category_with_key(template_key_first)
        else:
            nat_key, template_key_first = self.country_bot.normalize_category_with_key(normalized_category)
            other_key, template_key = self.other_bot.normalize_category_with_key(template_key_first)

        return NormalizeResult(
            template_key_first=template_key_first,
            category=normalized_category,
            template_key=template_key,
            nat_key=nat_key,
            other_key=other_key,
        )

    def normalize_both(self, category: str) -> str:
        """
        Normalize both dynamic elements in a category and return the final template key.

        Strips extra spaces from the input, then applies country normalization followed by the other element normalization.

        Returns:
            template_key (str): The template string after normalizing the nationality and the other element.
        """
        # Normalize the category by removing extra spaces
        normalized_category = " ".join(category.split())

        nat_key, template_key = self.country_bot.normalize_category_with_key(normalized_category)
        other_key, template_key = self.other_bot.normalize_category_with_key(template_key)

        return template_key

    def create_nat_label(self, category: str) -> str:
        """
        Create a nationality label for the given category.

        Returns:
            The nationality label string for the category, or an empty string if no label is found.
        """
        return self.country_bot.search(category)

    def replace_placeholders(self, template_ar: str, country_ar: str, other_ar: str) -> str:
        """
        Replace country and other placeholders in an Arabic template and return the trimmed label.

        Parameters:
            template_ar (str): Arabic template containing placeholders for country and the other element.
            country_ar (str): Arabic text to replace the country placeholder.
            other_ar (str): Arabic text to replace the other-element placeholder.

        Returns:
            str: Arabic label with both placeholders replaced and surrounding whitespace removed.
        """
        label = self.country_bot.replace_value_placeholder(template_ar, country_ar)
        label = self.other_bot.replace_value_placeholder(label, other_ar)

        return label.strip()

    @functools.lru_cache(maxsize=1000)
    def create_label(self, category: str) -> str:
        """
        Create a localized Arabic label by combining the normalized country and other-element templates for the given category.

        If a cached mapping exists in self.data_to_find for the category, that value is returned. Otherwise the method normalizes the category to obtain country and other keys, retrieves the corresponding Arabic templates and key labels, replaces placeholders with the Arabic key labels, and returns the final Arabic label. Returns an empty string when normalization fails, required templates or key labels are missing, or placeholders remain unresolved.

        Parameters:
                category (str): The multi-element category to translate (e.g., "ladies british softball tour").

        Returns:
                str: The final Arabic label with placeholders replaced, or an empty string if no valid translation can be produced.
        """
        if self.data_to_find and self.data_to_find.get(category):
            return self.data_to_find[category]

        # category = Yemeni football championships
        template_data = self.normalize_both_new(category)

        logger.debug(f">>>create_label {template_data.nat_key=}, {template_data.other_key=}")
        # print(f"{template_data.template_key_first=}, {template_data.template_key=}\n"*20)

        if not template_data.nat_key or not template_data.other_key:
            return ""

        template_ar_first = self.country_bot.get_template_ar(template_data.template_key_first)
        template_ar = self.country_bot.get_template_ar(template_data.template_key)

        logger.debug(f">>>create_label {template_ar=}, {template_ar_first=}")

        if self.search_first_part and template_ar_first:
            return self.country_bot.search(category)

        if not template_ar:
            logger.debug(">>>create_label No template found")
            return ""
        # Get Arabic equivalents
        country_ar = self.country_bot.get_key_label(template_data.nat_key)
        other_ar = self.other_bot.get_key_label(template_data.other_key)
        logger.debug(f">>>create_label {country_ar=}, {other_ar=}")
        if not country_ar or not other_ar:
            return ""

        # Replace placeholders
        label = self.replace_placeholders(template_ar, country_ar, other_ar)

        logger.debug(f">>>create_label Translated {category=} → {label=}")

        return label

    def search(self, category: str) -> str:
        """
        Create a localized label for the given multi-element category.

        Returns:
            str: The localized label for the category, or an empty string if no translation is available.
        """
        return self.create_label(category)

    def check_placeholders(self, category: str, result: str) -> str:
        """
        Ensure the produced label contains no unprocessed placeholder characters.

        Logs a warning if unprocessed placeholders (`{`) are found in `result`, using `category` for context.

        Parameters:
            category (str): Original category string used in the warning message.
            result (str): The generated label to check for placeholders.

        Returns:
            str: The original `result` if it contains no `{` characters, otherwise an empty string.
        """
        if "{" in result:
            logger.warning(f">>> search_all_category Found unprocessed placeholders in {category=}: {result=}")
            return ""
        return result

    def prepend_arabic_category_prefix(self, category: str, result: str) -> str:
        """
        Prepend the Arabic category prefix "تصنيف:" to the result when the original category started with "category:" and the result lacks that prefix.

        Parameters:
            category (str): The original category string to inspect for the English "category:" prefix.
            result (str): The generated Arabic label that may require the Arabic category prefix.

        Returns:
            str: The possibly modified `result` with "تصنيف:" prepended when `category` starts with "category:" (case-insensitive) and `result` is non-empty and does not already start with "تصنيف:".
        """
        if result and category.lower().startswith("category:") and not result.startswith("تصنيف:"):
            result = "تصنيف:" + result
        return result

    def search_all(self, category: str, add_arabic_category_prefix: bool = False) -> str:
        """
        Attempt to build a combined Arabic label for a two-element category, falling back to individual bot searches.

        Parameters:
            category (str): The category key to resolve.
            add_arabic_category_prefix (bool): If True, prepend the Arabic category prefix when appropriate.

        Returns:
            str: The resolved label, or an empty string if no label is found.
        """
        result = (
            self.create_label(category) or self.country_bot.search(category) or self.other_bot.search(category) or ""
        )
        if add_arabic_category_prefix:
            result = self.prepend_arabic_category_prefix(category, result)
        return result

    def search_all_other_first(self, category: str) -> str:
        """
        Attempt to find a translation by querying the other bot first, then the country bot, then the combined label.

        Returns:
            str: The found translation with unprocessed placeholders removed; empty string if no translation is found or if placeholders remain.
        """
        result = (
            self.other_bot.search(category) or self.country_bot.search(category) or self.create_label(category) or ""
        )

        return self.check_placeholders(category, result)

    def search_all_category(self, category: str) -> str:
        """
        Perform a comprehensive lookup for a category label, applying normalization, Arabic-prefix handling, and placeholder validation.

        Parameters:
            category (str): The original category string; may include a leading "category:" prefix.

        Returns:
            str: The localized label for the category, or an empty string if no valid label is found or placeholder tokens remain.
        """
        logger.debug("--" * 5)
        logger.debug(">> search_all_category start")

        normalized_category = category.lower().replace("category:", "")
        result = self.search_all(normalized_category)

        result = self.prepend_arabic_category_prefix(category, result)

        result = self.check_placeholders(category, result)
        logger.debug(">> search_all_category end")
        return result
