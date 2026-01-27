#!/usr/bin/python3
"""
Module for year-based category translation formatting.

This module provides factory functions for creating formatters that handle
categories with temporal patterns (years, decades, centuries) combined with
other dynamic elements like nationality or country.

Functions:
    format_year_country_data: Creates MultiDataFormatterBaseYear for year+country translations.
    format_year_country_data_v2: Creates MultiDataFormatterBaseYearV2 with dictionary support.

Constants:
    YEAR_PARAM: Default placeholder for year values ("{year1}").
    COUNTRY_PARAM: Default placeholder for country values ("{country1}").

Example:
    >>> from ArWikiCats.translations_formats import format_year_country_data
    >>> formatted_data = {"{year1} {country1} events": "{country1} أحداث في {year1}"}
    >>> data_list = {"british": "بريطانية", "american": "أمريكية"}
    >>> bot = format_year_country_data(
    ...     formatted_data=formatted_data,
    ...     data_list=data_list,
    ... )
    >>> bot.search("14th-century british events")
    'بريطانية أحداث في القرن 14'
"""

from typing import Dict

from .DataModel import (
    FormatData,
    FormatDataV2,
    YearFormatData,
)

from .DataModelMulti import (
    MultiDataFormatterBaseYear,
    MultiDataFormatterBaseYearV2,
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
    data_to_find: Dict[str, str] | None = None,
) -> MultiDataFormatterBaseYearV2:
    """
    Create a MultiDataFormatterBaseYearV2 for year+country translations with dictionary support.

    This factory function creates a formatter that handles categories with both
    temporal patterns (years, decades, centuries) and country/nationality elements.
    It uses FormatDataV2 which supports dictionary values in data_list for complex
    placeholder replacements.

    Args:
        formatted_data: Template patterns mapping English patterns to Arabic templates.
            Keys should contain placeholders like "{country1}" and "{year1}".
        data_list: Country/nationality key-to-value mappings. Values can be strings
            or dictionaries with multiple placeholders.
        key_placeholder: Placeholder for country key in templates. Default: "{country1}".
        text_after: Optional text that appears after the country key.
        text_before: Optional text that appears before the country key.
        key2_placeholder: Placeholder for year key in templates. Default: "{year1}".
        value2_placeholder: Placeholder for year value in Arabic templates. Default: "{year1}".
        data_to_find: Optional direct lookup dictionary for category labels.

    Returns:
        MultiDataFormatterBaseYearV2: A configured formatter for year+country translations.

    Example:
        >>> formatted_data = {"{year1} {country1} writers": "{demonym} كتاب في {year1}"}
        >>> data_list = {"yemen": {"demonym": "يمنيون"}}
        >>> bot = format_year_country_data_v2(
        ...     formatted_data=formatted_data,
        ...     data_list=data_list,
        ... )
        >>> bot.search("14th-century yemen writers")
        'يمنيون كتاب في القرن 14'
    """
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


def format_year_country_data(
    formatted_data: Dict[str, str],
    data_list: Dict[str, str],
    key_placeholder: str = COUNTRY_PARAM,
    value_placeholder: str = COUNTRY_PARAM,
    key2_placeholder: str = YEAR_PARAM,
    value2_placeholder: str = YEAR_PARAM,
    text_after: str = "",
    text_before: str = "",
    data_to_find: Dict[str, str] | None = None,
) -> MultiDataFormatterBaseYear:
    """
    Create a MultiDataFormatterBaseYear for year+country translations.

    This factory function creates a formatter that handles categories with both
    temporal patterns (years, decades, centuries) and country/nationality elements.
    It uses FormatData for simple string-based placeholder replacements.

    Args:
        formatted_data: Template patterns mapping English patterns to Arabic templates.
            Keys should contain placeholders like "{country1}" and "{year1}".
        data_list: Country/nationality key-to-Arabic-label mappings
            (e.g., {"british": "بريطانية"}).
        key_placeholder: Placeholder for country key in templates. Default: "{country1}".
        value_placeholder: Placeholder for country value in Arabic templates. Default: "{country1}".
        key2_placeholder: Placeholder for year key in templates. Default: "{year1}".
        value2_placeholder: Placeholder for year value in Arabic templates. Default: "{year1}".
        text_after: Optional text that appears after the country key.
        text_before: Optional text that appears before the country key.
        data_to_find: Optional direct lookup dictionary for category labels.

    Returns:
        MultiDataFormatterBaseYear: A configured formatter for year+country translations.

    Example:
        >>> formatted_data = {"{year1} {country1} events": "{country1} أحداث في {year1}"}
        >>> data_list = {"british": "بريطانية"}
        >>> bot = format_year_country_data(
        ...     formatted_data=formatted_data,
        ...     data_list=data_list,
        ... )
        >>> bot.search("1990s british events")
        'بريطانية أحداث في عقد 1990'
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

    other_bot = YearFormatData(
        key_placeholder=key2_placeholder,
        value_placeholder=value2_placeholder,
    )

    return MultiDataFormatterBaseYear(
        country_bot=country_bot,
        other_bot=other_bot,
        data_to_find=data_to_find,
    )


__all__ = [
    "format_year_country_data",
    "format_year_country_data_v2",
]
