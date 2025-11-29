#!/usr/bin/python3
"""
Classes for formatting
"""
from typing import Dict
from .DataModel import FormatData, YearFormatData, FormatMultiDataNew

# -----------------------
#
# -----------------------

YEAR_PARAM = "{year1}"
COUNTRY_PARAM = "{country1}"


def FormatYearCountryData(
    formatted_data: Dict[str, str],
    data_list: Dict[str, str],
    key_placeholder: str = COUNTRY_PARAM,
    value_placeholder: str = COUNTRY_PARAM,
    key2_placeholder: str = YEAR_PARAM,
    value2_placeholder: str = YEAR_PARAM,
    text_after: str = "",
    text_before: str = "",
) -> FormatMultiDataNew:
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

    return FormatMultiDataNew(
        country_bot=country_bot,
        other_bot=other_bot,
    )
