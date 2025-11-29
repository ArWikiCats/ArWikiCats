#!/usr/bin/python3
"""
Provides classes for formatting template-driven translation labels.
- FormatMultiData: Handles complex formatting involving two sets of data lists (e.g., nationality and sport).
- FormatComparisonHelper: A helper class for comparison operations.

test at tests.translations_formats.test_format_2_data.py
"""

import functools
from typing import Dict

from ..helps.log import logger
from .format_data import FormatData


class FormatComparisonHelper:
    def __init__(self): ...

    def get_start_p17(self, cate) -> tuple[str, str]:
        """
        Get the start of a category string and its corresponding key.

        Example:
            category: "Yemeni national football teams", result: ("Yemeni", "natar")
        """
        new_category = self.normalize_nat_label(cate)
        key = self.country_bot.match_key(cate)
        return new_category, key


YEAR_PARAM = "{year1}"
COUNTRY_PARAM = "{country1}"

YEAR_PARAM = "xoxo"
COUNTRY_PARAM = "natar"


class FormatMultiData(FormatComparisonHelper):
    """

    """

    def __init__(
        self,
        formatted_data: Dict[str, str],
        data_list: Dict[str, str],
        key_placeholder: str = COUNTRY_PARAM,
        value_placeholder: str = COUNTRY_PARAM,
        data_list2: Dict[str, str] = {},
        key2_placeholder: str = YEAR_PARAM,
        value2_placeholder: str = YEAR_PARAM,
        text_after: str = "",
        text_before: str = "",
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""
        # Store originals
        self.formatted_data = formatted_data

        # Placeholders
        self.key_placeholder = key_placeholder
        self.value_placeholder = value_placeholder

        self.value2_placeholder = value2_placeholder
        self.key2_placeholder = key2_placeholder

        self.country_bot = FormatData(
            self.formatted_data,
            data_list,
            key_placeholder=self.key_placeholder,
            value_placeholder=self.value_placeholder,
            text_after=text_after,
            text_before=text_before,
        )

        self.sport_bot = FormatData(
            {},
            data_list2,
            key_placeholder=self.key2_placeholder,
            value_placeholder=self.value2_placeholder,
        )

    # ------------------------------------------------------
    # COUNTRY/NAT NORMALIZATION
    # ------------------------------------------------------
    def normalize_nat_label(self, category) -> str:
        """
        Normalize nationality placeholders within a category string.

        Example:
            category:"Yemeni national football teams", result: "natar national football teams"
        """
        key = self.country_bot.match_key(category)
        result = ""
        if key:
            result = self.country_bot.normalize_category(category, key)
        return result

    # ------------------------------------------------------
    # YEAR/SPORT NORMALIZATION
    # ------------------------------------------------------
    def normalize_sport_label(self, category) -> str:
        """
        Normalize sport placeholders within a category string.

        Example:
            category:"Yemeni national football teams", result: "Yemeni national xoxo teams"
        """
        key = self.sport_bot.match_key(category)
        result = ""
        if key:
            result = self.sport_bot.normalize_category(category, key)
        return result

    def normalize_both(self, category) -> str:
        """
        Normalize both nationality and sport tokens in the category.

        Example:
            input: "british softball championshipszz", output: "natar xoxo championshipszz"
        """
        # Normalize the category by removing extra spaces
        normalized_category = " ".join(category.split())

        new_category = self.normalize_nat_label(normalized_category)
        new_category = self.normalize_sport_label(new_category)

        return new_category

    @functools.lru_cache(maxsize=2000)
    def create_nat_label(self, category) -> str:
        return self.country_bot.search(category)

    @functools.lru_cache(maxsize=1000)
    def create_label(self, category: str) -> str:
        """
        Create a localized label by combining nationality and sport templates.

        Example:
            category: "ladies british softball tour", output: "بطولة المملكة المتحدة للكرة اللينة للسيدات"
        """
        # category = Yemeni football championships
        template_key = self.normalize_both(category)

        # Must match a template
        if template_key not in self.formatted_data:
            return ""

        # cate = natar xoxo championships
        template_ar = self.formatted_data[template_key]
        logger.debug(f"{template_ar=}")

        # Extract keys
        nat_key = self.country_bot.match_key(category)

        if not nat_key:
            return ""

        category2 = self.country_bot.normalize_category(category, nat_key)

        xoxo_key = self.sport_bot.match_key(category2)

        if not xoxo_key:
            return ""

        # Get Arabic equivalents
        country_ar = self.country_bot.get_key_label(nat_key)
        sport_ar = self.sport_bot.get_key_label(xoxo_key)

        if not country_ar or not sport_ar:
            return ""

        # Replace placeholders
        label = template_ar.replace(self.value_placeholder, country_ar).replace(
            self.value2_placeholder, sport_ar
        )

        logger.debug(f"Translated {category=} → {label=}")
        return label
