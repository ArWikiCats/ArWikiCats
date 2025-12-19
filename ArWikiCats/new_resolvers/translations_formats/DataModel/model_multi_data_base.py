#!/usr/bin/python3
"""
Provides classes for formatting template-driven translation labels.
- format_multi_data: Handles complex formatting involving two sets of data lists (e.g., nationality and sport).

test at tests.translations_formats.test_format_2_data.py
"""

import functools
from dataclasses import dataclass
from ....helps.log import logger

# -----------------------
#
# -----------------------


@dataclass
class NormalizeResult:
    """Data structure representing each processed category."""

    template_key_first: str
    category: str
    template_key: str
    nat_key: str
    other_key: str


class MultiDataFormatterBaseHelpers:
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
            input: "british softball championshipszz", output: "natar xoxo championshipszz"
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
            input: "british softball championshipszz", output: "natar xoxo championshipszz"
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

    def search_all(self, category: str) -> str:
        return (
            self.create_label(category) or
            self.country_bot.search(category) or
            self.other_bot.search(category) or
            ""
        )

    def search_all_other_first(self, category: str) -> str:
        return (
            self.other_bot.search(category) or
            self.country_bot.search(category) or
            self.create_label(category) or
            ""
        )

    def search_all_category(self, category: str) -> str:
        logger.debug("--"*5)
        logger.debug(">> search_all_category start")

        normalized_category = category.lower().replace("category:", "")
        result = self.search_all(normalized_category)

        if result and category.lower().startswith("category:"):
            result = "تصنيف:" + result
        logger.debug(">> search_all_category end")
        return result
