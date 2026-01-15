#!/usr/bin/python3
"""
Module for time-based category translation formatting.

This module provides classes for handling year, decade, and century patterns
in category strings. It converts temporal expressions from English to Arabic
(e.g., "14th-century" → "القرن 14", "1990s" → "عقد 1990").

Classes:
    YearFormatDataLegacy: Legacy class for year pattern handling (deprecated).
    YearFormatData: Factory function that creates a FormatDataFrom instance for time patterns.

Example:
    >>> from ArWikiCats.translations_formats.DataModel import YearFormatData
    >>> year_bot = YearFormatData(key_placeholder="{year1}", value_placeholder="{year1}")
    >>> year_bot.search("14th-century")
    'القرن 14'
    >>> year_bot.search("1990s")
    'عقد 1990'

Note:
    The YearFormatData function is the preferred way to create year formatters.
    It returns a FormatDataFrom instance configured with the appropriate callbacks
    for time conversion.
"""

import re

from ...time_resolvers import (
    convert_time_to_arabic,
    fixing,
    match_time_en_first,
)
from ..formats_logger import logger
from .model_multi_data_year_from import FormatDataFrom


class YearFormatDataLegacy:
    """
    Legacy class for handling year patterns in category strings (deprecated).

    This class provides functionality to extract and convert year patterns
    (years, decades, centuries) from English to Arabic. It is kept for
    backward compatibility but the YearFormatData factory function should
    be used for new code.

    Attributes:
        key_placeholder (str): Placeholder string for the year key (e.g., "{year1}").
        value_placeholder (str): Placeholder string for the year value in templates.

    Example:
        >>> bot = YearFormatDataLegacy(key_placeholder="{year1}", value_placeholder="{year1}")
        >>> bot.match_key("14th-century writers")
        '14th-century'
        >>> bot.search("14th-century")
        'القرن 14'

    Note:
        Use YearFormatData() factory function instead of this class for new code.
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
        logger.debug(f"!!!! replace_value_placeholder: {self.value_placeholder=}, {label=}, {value=}")
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
    """
    Factory function to create a FormatDataFrom instance for year/time patterns.

    This is the preferred way to create year formatters. It returns a FormatDataFrom
    instance configured with the appropriate callbacks for converting English
    temporal expressions to Arabic.

    Args:
        key_placeholder: Placeholder string for the year key (e.g., "{year1}").
        value_placeholder: Placeholder string for the year value in templates.

    Returns:
        FormatDataFrom: A configured formatter for handling year patterns.

    Example:
        >>> year_bot = YearFormatData(key_placeholder="{year1}", value_placeholder="{year1}")
        >>> year_bot.search("14th-century")
        'القرن 14'
        >>> year_bot.match_key("14th-century writers from Yemen")
        '14th-century'
    """
    return FormatDataFrom(
        formatted_data={},
        key_placeholder=key_placeholder,
        value_placeholder=value_placeholder,
        search_callback=convert_time_to_arabic,
        match_key_callback=match_time_en_first,
        fixing_callback=fixing,
    )
