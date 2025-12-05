#!/usr/bin/python3
"""
Classes for formatting
"""
from typing import Dict
from .DataModel import FormatData, FormatDataDouble, MultiDataFormatterDataDouble

# -----------------------
#
# -----------------------


def format_films_country_data(
    formatted_data: Dict[str, str],
    data_list: Dict[str, str],
    key_placeholder: str = "{nat_en}",
    value_placeholder: str = "{nat_ar}",
    data_list2: Dict[str, str] = {},
    other_formatted_data: Dict[str, str] = {},
    key2_placeholder: str = "{film_key}",
    value2_placeholder: str = "{film_ar}",
    text_after: str = "",
    text_before: str = "",
) -> MultiDataFormatterDataDouble:
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

    other_bot = FormatDataDouble(
        formatted_data=other_formatted_data,  # to use from search_all
        data_list=data_list2,
        key_placeholder=key2_placeholder,
        value_placeholder=value2_placeholder,
    )

    return MultiDataFormatterDataDouble(
        country_bot=country_bot,
        other_bot=other_bot,
    )
