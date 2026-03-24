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

from typing import Dict, Optional

from .DataModel import (
    FormatData,
    FormatDataV2,
    YearFormatData,
)
from .DataModelMulti import (
    MultiDataFormatterBaseYear,
    MultiDataFormatterBaseYearV2,
)
from .classes import YearCountryDataConfig, YearDataConfig

YEAR_PARAM = "{year1}"
COUNTRY_PARAM = "{country1}"


def format_year_country_data_v2(
    country_config: YearCountryDataConfig,
    year_config: Optional[YearDataConfig] = None,
    data_to_find: Dict[str, str] | None = None,
) -> MultiDataFormatterBaseYearV2:
    """
    Create a MultiDataFormatterBaseYearV2 for year+country translations with dictionary support.

    This factory function creates a formatter that handles categories with both
    temporal patterns (years, decades, centuries) and country/nationality elements.
    It uses FormatDataV2 which supports dictionary values in data_list for complex
    placeholder replacements.

    Args:
        country_config: Configuration for the country/nationality part.
            Uses FormatDataV2 which supports dictionary values in data_list.
        year_config: Configuration for the year part.
        data_to_find: Optional direct lookup dictionary for category labels.

    Returns:
        MultiDataFormatterBaseYearV2: A configured formatter for year+country translations.

    Example:
        >>> country_config = YearCountryDataConfig(
        ...     formatted_data={"{year1} {country1} writers": "{demonym} كتاب في {year1}"},
        ...     data_list={"yemen": {"demonym": "يمنيون"}},
        ...     key_placeholder="{country1}",
        ... )
        >>> year_config = YearDataConfig(key_placeholder="{year1}", value_placeholder="{year1}")
        >>> bot = format_year_country_data_v2(country_config, year_config)
        >>> bot.search("14th-century yemen writers")
        'يمنيون كتاب في القرن 14'
    """
    if year_config is None:
        year_config = YearDataConfig()

    # Country bot (FormatDataV2)
    country_bot = FormatDataV2(
        formatted_data=country_config.formatted_data,
        data_list=country_config.data_list,
        key_placeholder=country_config.key_placeholder,
        text_after=country_config.text_after,
        text_before=country_config.text_before,
    )

    other_bot = YearFormatData(
        key_placeholder=year_config.key_placeholder,
        value_placeholder=year_config.value_placeholder,
    )

    return MultiDataFormatterBaseYearV2(
        country_bot=country_bot,
        other_bot=other_bot,
        data_to_find=data_to_find,
    )


def format_year_country_data(
    country_config: YearCountryDataConfig,
    year_config: Optional[YearDataConfig] = None,
    data_to_find: Dict[str, str] | None = None,
) -> MultiDataFormatterBaseYear:
    """
    Create a MultiDataFormatterBaseYear for year+country translations.

    This factory function creates a formatter that handles categories with both
    temporal patterns (years, decades, centuries) and country/nationality elements.
    It uses FormatData for simple string-based placeholder replacements.

    Args:
        country_config: Configuration for the country/nationality part.
        year_config: Configuration for the year part.
        data_to_find: Optional direct lookup dictionary for category labels.

    Returns:
        MultiDataFormatterBaseYear: A configured formatter for year+country translations.

    Example:
        >>> country_config = YearCountryDataConfig(
        ...     formatted_data={"{year1} {country1} events": "{country1} أحداث في {year1}"},
        ...     data_list={"british": "بريطانية"},
        ...     key_placeholder="{country1}",
        ...     value_placeholder="{country1}",
        ... )
        >>> year_config = YearDataConfig(key_placeholder="{year1}", value_placeholder="{year1}")
        >>> bot = format_year_country_data(country_config, year_config)
        >>> bot.search("1990s british events")
        'بريطانية أحداث في عقد 1990'
    """
    if year_config is None:
        year_config = YearDataConfig()

    # Country bot (FormatData)
    country_bot = FormatData(
        formatted_data=country_config.formatted_data,
        data_list=country_config.data_list,
        key_placeholder=country_config.key_placeholder,
        value_placeholder=country_config.value_placeholder,
        text_after=country_config.text_after,
        text_before=country_config.text_before,
    )

    other_bot = YearFormatData(
        key_placeholder=year_config.key_placeholder,
        value_placeholder=year_config.value_placeholder,
    )

    return MultiDataFormatterBaseYear(
        country_bot=country_bot,
        other_bot=other_bot,
        data_to_find=data_to_find,
    )


__all__ = [
    "format_year_country_data",
    "format_year_country_data_v2",
    "YearCountryDataConfig",
    "YearDataConfig",
]
