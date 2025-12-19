#!/usr/bin/python3
"""
This module provides the YearFormatData class, a specialized formatter for
handling time-based patterns (years, decades, centuries) in category strings.

TODO: use FormatDataFrom with:
        search_callback=lambda x: convert_time_to_arabic(x),
        match_key_callback=lambda x: match_time_en_first(x),
"""

import re
from ...helps import logger
from .model_multi_data_year_from import FormatDataFrom
from ...time_resolvers import (
    convert_time_to_arabic,
    match_time_en_first,
    fixing,
)


class YearFormatDataLegacy:
    """
    A dynamic wrapper that allows FormatData to handle year patterns.
    It mimics FormatData behavior but for time values extracted by regex.
    """

    def __init__(
        self,
        key_placeholder: str,
        value_placeholder: str,
    ) -> None:
        self.key_placeholder = key_placeholder
        self.value_placeholder = value_placeholder

    def match_key(self, text: str) -> str:
        """Extract English year/decade and return it as the key."""
        result = match_time_en_first(text)
        return result if result else ""

    def normalize_category(self, text: str, key: str) -> str:
        """
        Replace matched year with placeholder.
        """
        logger.debug(f"normalize_category: {key=}, {text=}")
        if not key:
            return text
        result = re.sub(re.escape(key), self.key_placeholder, text, flags=re.IGNORECASE)
        return result

    def normalize_category_with_key(self, category: str) -> tuple[str, str]:
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

    def replace_value_placeholder(self, label: str, value: str) -> str:
        # Replace placeholder
        # print(f"!!!! replace_value_placeholder: {self.value_placeholder=}, {label=}, {value=}")
        result = label.replace(self.value_placeholder, value)
        result = fixing(result)
        return result

    def get_key_label(self, key: str) -> str:
        """place holders"""
        if not key:
            return ""
        logger.debug(f"get_key_label: {key=}")
        return self.search(key)

    def search(self, text: str) -> str:
        """Convert the year expression to Arabic."""
        return convert_time_to_arabic(text)

    def search_all(self, key: str) -> str:
        """place holders"""
        return self.search(key)


def YearFormatData(
    key_placeholder: str,
    value_placeholder: str,
) -> FormatDataFrom:
    return FormatDataFrom(
        formatted_data={},
        key_placeholder=key_placeholder,
        value_placeholder=value_placeholder,
        search_callback=convert_time_to_arabic,
        match_key_callback=match_time_en_first,
        fixing_callback=fixing,
    )
