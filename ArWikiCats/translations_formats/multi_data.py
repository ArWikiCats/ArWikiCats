#!/usr/bin/python3
"""
Provides classes for formatting template-driven translation labels.
- format_multi_data: Handles complex formatting involving two sets of data lists (e.g., nationality and sport).

test at tests.translations_formats.test_format_2_data.py
"""

import functools
from dataclasses import dataclass
from typing import Dict

from ..helps.log import logger
from .DataModel import MultiDataFormatterBase, FormatData

YEAR_PARAM = "xoxo"
COUNTRY_PARAM = "natar"


def format_multi_data(
    formatted_data: Dict[str, str],
    data_list: Dict[str, str],
    key_placeholder: str = COUNTRY_PARAM,
    value_placeholder: str = COUNTRY_PARAM,
    data_list2: Dict[str, str] = {},
    key2_placeholder: str = YEAR_PARAM,
    value2_placeholder: str = YEAR_PARAM,
    text_after: str = "",
    text_before: str = "",
) -> MultiDataFormatterBase:
    """Prepare helpers for matching and formatting template-driven labels."""
    # Store originals

    # Country bot (FormatData)
    country_bot = FormatData(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder=key_placeholder,
        value_placeholder=value_placeholder,
        text_after=text_after,
        text_before=text_before,
    )
    other_bot = FormatData(
        formatted_data,  # to use from search_all
        data_list2,
        key_placeholder=key2_placeholder,
        value_placeholder=value2_placeholder,
    )
    return MultiDataFormatterBase(
        country_bot=country_bot,
        other_bot=other_bot,
    )
