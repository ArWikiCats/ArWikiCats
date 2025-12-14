#!/usr/bin/python3
"""
Classes for formatting
"""
from typing import Dict
from .DataModel import (
    FormatData,
    YearFormatData,
    MultiDataFormatterBaseYear,
    FormatDataV2,
    MultiDataFormatterBaseYearV2
)

YEAR_PARAM = "{year1}"
COUNTRY_PARAM = "{country1}"


def format_year_country_data_v2(
    formatted_data: Dict[str, str],
    data_list: Dict[str, str],
    key_placeholder: str = COUNTRY_PARAM,
    text_after: str = "",
    text_before: str = "",
    key2_placeholder: str = YEAR_PARAM,
    value2_placeholder: str = YEAR_PARAM,
    data_to_find: Dict[str, str] = {},
) -> MultiDataFormatterBaseYearV2:
    """Prepare helpers for matching and formatting template-driven labels."""
    # Store originals

    # Country bot (FormatDataV2)
    country_bot = FormatDataV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder=key_placeholder,
        text_after=text_after,
        text_before=text_before,
    )

    other_bot = YearFormatData(
        key_placeholder=key2_placeholder,
        value_placeholder=value2_placeholder,
    )

    return MultiDataFormatterBaseYearV2(
        country_bot=country_bot,
        other_bot=other_bot,
        data_to_find=data_to_find,
    )

# -----------------------
#
# -----------------------


def format_year_country_data(
    formatted_data: Dict[str, str],
    data_list: Dict[str, str],
    key_placeholder: str = COUNTRY_PARAM,
    value_placeholder: str = COUNTRY_PARAM,
    key2_placeholder: str = YEAR_PARAM,
    value2_placeholder: str = YEAR_PARAM,
    text_after: str = "",
    text_before: str = "",
    data_to_find: Dict[str, str] = {},
) -> MultiDataFormatterBaseYear:
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

    other_bot = YearFormatData(
        key_placeholder=key2_placeholder,
        value_placeholder=value2_placeholder,
    )

    return MultiDataFormatterBaseYear(
        country_bot=country_bot,
        other_bot=other_bot,
        data_to_find=data_to_find,
    )
