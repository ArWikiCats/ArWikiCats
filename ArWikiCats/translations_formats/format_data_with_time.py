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

    def fixing(self, text: str) -> str:
        """Fix text."""
        text = re.sub(r"(انحلالات|تأسيسات)\s*سنة\s*(عقد|القرن|الألفية)", r"\g<1> \g<2>", text)
        return text

    def replace_value_placeholder(self, label, value) -> str:
        # Replace placeholder
        result = label.replace(self.value_placeholder, value)
        result = self.fixing(result)
        return result

# -----------------------
#
# -----------------------


YEAR_PARAM = "{year1}"
COUNTRY_PARAM = "{country1}"


class FormatYearCountryData:
    """
    """

    def __init__(
        self,
        formatted_data: Dict[str, str],
        data_list: Dict[str, str],
        key_placeholder: str = COUNTRY_PARAM,
        value_placeholder: str = COUNTRY_PARAM,
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

        # Country bot (FormatData)
        self.country_bot = FormatData(
            formatted_data=self.formatted_data,
            data_list=data_list,
            key_placeholder=self.key_placeholder,
            value_placeholder=self.value_placeholder,
            text_after=text_after,
            text_before=text_before,
        )

        self.other_bot = YearFormatData(
            key_placeholder=key2_placeholder,
            value_placeholder=value2_placeholder,
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
    def normalize_other_label(self, category) -> str:
        """
        Normalize sport placeholders within a category string.

        Example:
            category:"Yemeni national football teams", result: "Yemeni national xoxo teams"
        """
        key = self.other_bot.match_key(category)
        result = ""
        if key:
            result = self.other_bot.normalize_category(category, key)
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
        new_category = self.normalize_other_label(new_category)

        return new_category

    @functools.lru_cache(maxsize=2000)
    def create_nat_label(self, category: str) -> str:
        return self.country_bot.search(category)

    def replace_placeholders(self, template_ar: str, country_ar: str, other_ar: str) -> str:
        label = self.country_bot.replace_value_placeholder(template_ar, country_ar)
        label = self.other_bot.replace_value_placeholder(label, other_ar)

        return label

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
        other_key, template_key = self.other_bot.normalize_category_with_key(template_key)

        if not nat_key or not other_key:
            return ""

        # Must match a template
        # if template_key not in self.formatted_data: return ""
        # cate = natar xoxo championships
        # template_ar = self.formatted_data[template_key]
        template_ar = self.country_bot.get_template_ar(template_key)
        logger.debug(f"{template_ar=}")

        # Get Arabic equivalents
        country_ar = self.country_bot.get_key_label(nat_key)
        other_ar = self.other_bot.get_key_label(other_key)

        if not country_ar or not other_ar:
            return ""

        # Replace placeholders
        label = self.replace_placeholders(template_ar, country_ar, other_ar)

        logger.debug(f"Translated {category=} → {label=}")
        return label
