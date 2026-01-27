#!/usr/bin/python3
"""
Module for time-based category translation formatting.

This module provides classes for handling year, decade, and century patterns
in category strings. It converts temporal expressions from English to Arabic
(e.g., "14th-century" → "القرن 14", "1990s" → "عقد 1990").

Classes:
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

from ...time_formats import (
    convert_time_to_arabic,
    match_time_en_first,
    standardize_time_phrases,
)
from .model_multi_data_year_from import FormatDataFrom


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
        fixing_callback=standardize_time_phrases,
    )
