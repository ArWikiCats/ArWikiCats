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

from ..formats_logger import logger

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
        Normalize both nationality and sport tokens in the category.

        Example:
            input: "british softball championships", output: "natar xoxo championships"
        """
        # Normalize the category by removing extra spaces
        normalized_category = " ".join(category.split())

        nat_key, template_key = self.country_bot.normalize_category_with_key(normalized_category)
        other_key, template_key = self.other_bot.normalize_category_with_key(template_key)

        return template_key

    def create_nat_label(self, category: str) -> str:
        return self.country_bot.search(category)

    def replace_placeholders(self, template_ar: str, country_ar: str, other_ar: str) -> str:
        label = self.country_bot.replace_value_placeholder(template_ar, country_ar)
        label = self.other_bot.replace_value_placeholder(label, other_ar)

        return label.strip()

    @functools.lru_cache(maxsize=1000)
    def create_label(self, category: str) -> str:
        """
        Create a localized label by combining nationality and sport templates.

        Example:
            category: "ladies british softball tour", output: "بطولة المملكة المتحدة للكرة اللينة للسيدات"
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
        return self.create_label(category)

    def check_placeholders(self, category: str, result: str) -> str:
        if "{" in result:
            logger.warning(f">>> search_all_category Found unprocessed placeholders in {category=}: {result=}")
            return ""
        return result

    def search_all(self, category: str) -> str:
        result = (
            self.create_label(category) or self.country_bot.search(category) or self.other_bot.search(category) or ""
        )
        return result

    def search_all_other_first(self, category: str) -> str:
        result = (
            self.other_bot.search(category) or self.country_bot.search(category) or self.create_label(category) or ""
        )

        return self.check_placeholders(category, result)

    def search_all_category(self, category: str) -> str:
        logger.debug("--" * 5)
        logger.debug(">> search_all_category start")

        normalized_category = category.lower().replace("category:", "")
        result = self.search_all(normalized_category)

        if result and category.lower().startswith("category:"):
            result = "تصنيف:" + result

        result = self.check_placeholders(category, result)
        logger.debug(">> search_all_category end")
        return result
