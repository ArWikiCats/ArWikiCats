#!/usr/bin/python3
"""
Module for multi-formatter category translation classes.

This module provides classes that combine two formatter instances to handle
categories with two dynamic elements (e.g., nationality and sport, country
and year). Each class orchestrates a "country_bot" and "other_bot" to
normalize and translate complex category strings.

Classes:
    MultiDataFormatterBase: Combines two FormatData instances.
    MultiDataFormatterBaseYear: Combines FormatData with YearFormatData.
    MultiDataFormatterBaseYearV2: Combines FormatDataV2 with YearFormatData.

Example:
    >>> from ArWikiCats.translations_formats.DataModel import MultiDataFormatterBase, FormatData
    >>> country_bot = FormatData(...)  # nationality formatter
    >>> sport_bot = FormatData(...)  # sport formatter
    >>> bot = MultiDataFormatterBase(country_bot, sport_bot)
    >>> bot.create_label("british football players")
    'لاعبو كرة القدم بريطانيون'

test at tests.translations_formats.test_format_2_data.py
"""

from typing import Dict

from ..DataModel import FormatData, FormatDataV2, YearFormatData
from .model_multi_data_base import MultiDataFormatterBaseHelpers


class MultiDataFormatterBase(MultiDataFormatterBaseHelpers):
    """
    Combines two FormatData instances for dual-element category translations.

    This class orchestrates two FormatData formatter instances to handle
    categories that contain two dynamic elements (e.g., nationality and sport).
    It normalizes the category by replacing both elements with placeholders,
    then uses templates to generate the final Arabic translation.

    Attributes:
        country_bot (FormatData): Formatter for the first dynamic element (e.g., nationality).
        other_bot (FormatData): Formatter for the second dynamic element (e.g., sport).
        search_first_part (bool): If True, search using only the first part after normalization.
        data_to_find (Dict[str, str] | None): Optional direct lookup dictionary for category labels.

    Example:
        >>> bot = MultiDataFormatterBase(country_bot, sport_bot)
        >>> bot.create_label("british football championships")
        'بطولات كرة القدم البريطانية'
    """

    def __init__(
        self,
        country_bot: FormatData,
        other_bot: FormatData,
        search_first_part: bool = False,
        data_to_find: Dict[str, str] | None = None,
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""

        # Country bot (FormatData)
        self.search_first_part = search_first_part
        self.country_bot = country_bot
        self.other_bot = other_bot
        self.data_to_find = data_to_find


class MultiDataFormatterBaseYear(MultiDataFormatterBaseHelpers):
    """
    Combines FormatData with YearFormatData for year-based category translations.

    This class orchestrates a FormatData instance for nationality/country
    elements and a YearFormatData instance for temporal elements. It handles
    categories like "14th-century British writers" by normalizing both the
    century and nationality, then combining them into an Arabic translation.

    Attributes:
        country_bot (FormatData): Formatter for nationality/country elements.
        other_bot (YearFormatData): Formatter for year/decade/century elements.
        search_first_part (bool): If True, search using only the first part after normalization.
        data_to_find (Dict[str, str] | None): Optional direct lookup dictionary for category labels.

    Example:
        >>> bot = MultiDataFormatterBaseYear(country_bot, year_bot)
        >>> bot.create_label("14th-century british writers")
        'كتاب بريطانيون في القرن 14'
    """

    def __init__(
        self,
        country_bot: FormatData,
        other_bot: YearFormatData,
        search_first_part: bool = False,
        data_to_find: Dict[str, str] | None = None,
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""

        self.search_first_part = search_first_part
        self.country_bot = country_bot
        self.other_bot = other_bot
        self.data_to_find = data_to_find


class MultiDataFormatterBaseYearV2(MultiDataFormatterBaseHelpers):
    """
    Combines FormatDataV2 with YearFormatData for advanced year-based translations.

    This class orchestrates a FormatDataV2 instance (supporting dictionary values)
    for nationality/country elements and a YearFormatData instance for temporal
    elements. The other_key_first parameter controls which element is processed
    first during normalization.

    Attributes:
        country_bot (FormatDataV2): Formatter for nationality/country elements with dict support.
        other_bot (YearFormatData): Formatter for year/decade/century elements.
        search_first_part (bool): If True, search using only the first part after normalization.
        data_to_find (Dict[str, str] | None): Optional direct lookup dictionary for category labels.
        other_key_first (bool): If True, process year element before nationality element.

    Example:
        >>> bot = MultiDataFormatterBaseYearV2(country_bot, year_bot, other_key_first=True)
        >>> bot.create_label("14th-century yemeni writers")
        'كتاب يمنيون في القرن 14'
    """

    def __init__(
        self,
        country_bot: FormatDataV2,
        other_bot: YearFormatData,
        search_first_part: bool = False,
        data_to_find: Dict[str, str] | None = None,
        other_key_first: bool = False,
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""

        self.search_first_part = search_first_part
        self.country_bot = country_bot
        self.other_bot = other_bot
        self.data_to_find = data_to_find
        self.other_key_first = other_key_first
