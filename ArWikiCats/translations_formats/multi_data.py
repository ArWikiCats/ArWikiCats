#!/usr/bin/python3
"""
Provides classes for formatting template-driven translation labels.
- format_multi_data: Handles complex formatting involving two sets of data lists (e.g., nationality and sport).

test at tests.translations_formats.test_format_2_data.py
"""

from typing import Dict

from ..helps.log import logger
from .DataModel import MultiDataFormatterBase, FormatData, FormatDataV2, MultiDataFormatterBaseV2

YEAR_PARAM = "xoxo"
COUNTRY_PARAM = "natar"


def get_other_data(
    formatted_data: dict[str, str],
    key_placeholder: str,
    value_placeholder: str,
    key2_placeholder: str,
    value2_placeholder: str
) -> dict:
    other_formatted_data = {
        x: v for x, v in formatted_data.items()
        if key2_placeholder in x and key_placeholder not in x
        and value2_placeholder in v and value_placeholder not in v
    }
    logger.debug(f"len other_formatted_data: {len(other_formatted_data):,}")

    return other_formatted_data


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
    use_other_formatted_data: bool=False,
    search_first_part: bool=False,
    data_to_find: Dict[str, str] = {},
) -> MultiDataFormatterBase:
    """
    Prepare helpers for matching and formatting template-driven labels.
    """

    # Country bot (FormatData)
    country_bot = FormatData(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder=key_placeholder,
        value_placeholder=value_placeholder,
        text_after=text_after,
        text_before=text_before,
    )

    other_formatted_data = get_other_data(
        formatted_data=formatted_data,
        key_placeholder=key_placeholder,
        value_placeholder=value_placeholder,
        key2_placeholder=key2_placeholder,
        value2_placeholder=value2_placeholder
    ) if use_other_formatted_data else {}

    other_bot = FormatData(
        formatted_data=other_formatted_data,  # to use from search_all
        data_list=data_list2,
        key_placeholder=key2_placeholder,
        value_placeholder=value2_placeholder,
    )

    return MultiDataFormatterBase(
        country_bot=country_bot,
        other_bot=other_bot,
        search_first_part=search_first_part,
        data_to_find=data_to_find,
    )


def format_multi_data_v2(
    formatted_data: Dict[str, str],
    data_list: Dict[str, str],
    key_placeholder: str,
    data_list2: Dict[str, str] = {},
    key2_placeholder: str = YEAR_PARAM,
    text_after: str = "",
    text_before: str = "",
    use_other_formatted_data: bool=False,
    search_first_part: bool=False,
) -> MultiDataFormatterBaseV2:

    country_bot = FormatDataV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder=key_placeholder,
        text_after=text_after,
        text_before=text_before,
    )

    other_formatted_data = {
        x: v for x, v in formatted_data.items()
        if key2_placeholder in x and key_placeholder not in x
    } if use_other_formatted_data else {}

    other_bot = FormatDataV2(
        formatted_data=other_formatted_data,
        data_list=data_list2,
        key_placeholder=key2_placeholder,
        text_after=text_after,
        text_before=text_before,
    )

    return MultiDataFormatterBaseV2(
        country_bot=country_bot,
        other_bot=other_bot,
        search_first_part=search_first_part,
    )


__all__ = [
    "format_multi_data",
    "format_multi_data_v2",
]
