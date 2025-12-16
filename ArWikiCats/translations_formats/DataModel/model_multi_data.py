#!/usr/bin/python3
"""
Provides classes for formatting template-driven translation labels.
- format_multi_data: Handles complex formatting involving two sets of data lists (e.g., nationality and sport).

test at tests.translations_formats.test_format_2_data.py
"""

from typing import Dict
from .model_data_2 import FormatDataV2
from .model_data import FormatData
from .model_data_time import YearFormatData
from .model_data_double import FormatDataDouble
from .model_multi_data_base import MultiDataFormatterBaseHelpers


class MultiDataFormatterBase(MultiDataFormatterBaseHelpers):
    """
    Handles complex formatting involving two sets of data lists (e.g.,
    nationality and sport, or country and year). It orchestrates two
    formatter instances (`FormatData` or `YearFormatData`) to normalize
    and translate category strings.
    """

    def __init__(
        self,
        country_bot: FormatData,
        other_bot: FormatData,
        search_first_part: bool = False,
        data_to_find: Dict[str, str] = {},
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""

        # Country bot (FormatData)
        self.search_first_part = search_first_part
        self.country_bot = country_bot
        self.other_bot = other_bot
        self.data_to_find = data_to_find


class MultiDataFormatterBaseYear(MultiDataFormatterBaseHelpers):
    """
    """

    def __init__(
        self,
        country_bot: FormatData,
        other_bot: YearFormatData,
        search_first_part: bool = False,
        data_to_find: Dict[str, str] = {},
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""

        self.search_first_part = search_first_part
        self.country_bot = country_bot
        self.other_bot = other_bot
        self.data_to_find = data_to_find


class MultiDataFormatterBaseYearV2(MultiDataFormatterBaseHelpers):
    """
    """

    def __init__(
        self,
        country_bot: FormatDataV2,
        other_bot: YearFormatData,
        search_first_part: bool = False,
        data_to_find: Dict[str, str] = {},
        other_key_first: bool = False,
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""

        self.search_first_part = search_first_part
        self.country_bot = country_bot
        self.other_bot = other_bot
        self.data_to_find = data_to_find
        self.other_key_first = other_key_first


class MultiDataFormatterDataDouble(MultiDataFormatterBaseHelpers):
    """
    Handles complex formatting involving two sets of data lists (e.g.,
    nationality and sport, or country and year). It orchestrates two
    formatter instances (`FormatData` or `YearFormatData`) to normalize
    and translate category strings.
    """

    def __init__(
        self,
        country_bot: FormatData,
        other_bot: FormatDataDouble,
        search_first_part: bool = False,
        data_to_find: Dict[str, str] = {},
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""

        self.search_first_part = search_first_part
        self.country_bot = country_bot
        self.other_bot = other_bot
        self.data_to_find = data_to_find


class MultiDataFormatterBaseV2(MultiDataFormatterBaseHelpers):
    """
    """

    def __init__(
        self,
        country_bot: FormatDataV2,
        other_bot: FormatDataV2,
        search_first_part: bool = False,
        data_to_find: Dict[str, str] = {},
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""

        self.search_first_part = search_first_part
        self.country_bot = country_bot
        self.other_bot = other_bot
        self.data_to_find = data_to_find
