#!/usr/bin/python3
"""
Classes for formatting
"""

import functools
import re
from typing import Dict

from ..helps.log import logger
from .format_data import FormatData
from ..new.time_to_arabic import (
    convert_time_to_arabic,
    match_time_en_first,
)


class YearFormatData:
    """
    A dynamic wrapper that allows FormatData to handle year patterns.
    It mimics FormatData behavior but for time values extracted by regex.
    """

    def __init__(self, key_placeholder: str, value_placeholder: str):
        self.key_placeholder = key_placeholder
        self.value_placeholder = value_placeholder

    def match_key(self, text: str) -> str:
        """Extract English year/decade and return it as the key."""
        result = match_time_en_first(text)
        return result if result else ""

    def get_key_label(self, key: str) -> str:
        """Convert the year expression to Arabic."""
        if not key:
            return ""
        return convert_time_to_arabic(key)

    def normalize_category(self, text: str, key: str) -> str:
        """Replace matched year with placeholder."""
        if not key:
            return text
        return re.sub(
            re.escape(key), self.key_placeholder, text, flags=re.IGNORECASE
        )

    def normalize_category_with_key(self, category) -> tuple[str, str]:
        """
        Normalize nationality placeholders within a category string.

        Example:
            category:"Yemeni national football teams", result: "natar national football teams"
        """
        key = self.match_key(category)
        result = ""
        if key:
            result = self.normalize_category(category, key)
        return key, result


YEAR_PARAM = "{year1}"
COUNTRY_PARAM = "{country1}"


class FormatYearCountryData:
    """
    Works EXACTLY like FormatMultiData but with:
        - year_bot instead of sport_bot
    """

    def __init__(
        self,
        formatted_data: Dict[str, str],
        data_list: Dict[str, str],
        key_placeholder: str = COUNTRY_PARAM,
        value_placeholder: str = COUNTRY_PARAM,
        key_placeholder_year: str = YEAR_PARAM,
        value_placeholder_year: str = YEAR_PARAM,
        text_after: str = "",
        text_before: str = "",
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""
        # Store originals
        self.formatted_data = formatted_data

        # Placeholders
        self.key_placeholder = key_placeholder
        self.value_placeholder = value_placeholder

        self.key_year = key_placeholder_year
        self.val_year = value_placeholder_year

        # Country bot (FormatData)
        self.country_bot = FormatData(
            formatted_data={},
            data_list=data_list,
            key_placeholder=self.key_placeholder,
            value_placeholder=self.value_placeholder,
        )

        # Year bot (custom FormatData-like wrapper)
        self.year_bot = YearFormatData(
            key_placeholder=self.key_year,
            value_placeholder=self.val_year,
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
    def normalize_year_label(self, category) -> str:
        key = self.year_bot.match_key(category)
        result = ""
        if key:
            result = self.year_bot.normalize_category(category, key)
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
        new_category = self.normalize_year_label(new_category)

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
        normalized_category = " ".join(category.split())
        # template_key = self.normalize_both(normalized_category)

        nat_key, template_key = self.country_bot.normalize_category_with_key(normalized_category)
        year_key, template_key = self.year_bot.normalize_category_with_key(template_key)

        if not nat_key or not year_key:
            return ""

        # Must match a template
        if template_key not in self.formatted_data:
            return ""

        # cate = natar xoxo championships
        template_ar = self.formatted_data[template_key]
        logger.debug(f"{template_ar=}")

        # Get Arabic equivalents
        country_ar = self.country_bot.get_key_label(nat_key)
        year_ar = self.year_bot.get_key_label(year_key)

        if not country_ar or not year_ar:
            return ""

        # Replace placeholders
        label = template_ar.replace(self.value_placeholder, country_ar).replace(
            self.val_year, year_ar
        )

        logger.debug(f"Translated {category=} → {label=}")
        return label
