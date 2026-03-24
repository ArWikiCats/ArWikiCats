#!/usr/bin/python3
"""
Module for dual-element category translation formatting.

This module provides factory functions for creating formatters that handle
categories with two dynamic elements (e.g., nationality and sport, or
country and profession). It's the primary module for complex category
translations that require pattern matching on multiple elements.

Functions:
    format_multi_data: Creates MultiDataFormatterBase for dual-element translations.
    format_multi_data_v2: Creates MultiDataFormatterBaseV2 with dictionary support.
    get_other_data: Helper to extract templates containing only the second placeholder.

Constants:
    YEAR_PARAM: Default placeholder for the second element ("xoxo").
    COUNTRY_PARAM: Default placeholder for the first element ("natar").

Example:
    >>> from ArWikiCats.translations_formats import format_multi_data, MultiDataFormatterConfig, MultiDataFormatterSecondElementConfig
    >>> formatted_data = {"{nat} {sport} players": "لاعبو {sport_ar} {nat_ar}"}
    >>> data_list = {"british": "بريطانيون", "american": "أمريكيون"}
    >>> data_list2 = {"football": "كرة القدم", "basketball": "كرة السلة"}
    >>> first_config = MultiDataFormatterConfig(
    ...     formatted_data=formatted_data,
    ...     data_list=data_list,
    ...     key_placeholder="{nat}",
    ...     value_placeholder="{nat_ar}",
    ... )
    >>> second_config = MultiDataFormatterSecondElementConfig(
    ...     data_list=data_list2,
    ...     key_placeholder="{sport}",
    ...     value_placeholder="{sport_ar}",
    ... )
    >>> bot = format_multi_data(first_element_config=first_config, second_element_config=second_config)
    >>> bot.search("british football players")
    'لاعبو كرة القدم بريطانيون'

test at tests.translations_formats.test_format_2_data.py
"""

import logging
from typing import Dict, Optional

from .DataModel import FormatData, FormatDataV2
from .DataModelMulti import MultiDataFormatterBase, MultiDataFormatterBaseV2
from .classes import MultiDataFormatterConfig, MultiDataFormatterSecondElementConfig

logger = logging.getLogger(__name__)

YEAR_PARAM = "xoxo"
COUNTRY_PARAM = "natar"


def get_other_data(
    formatted_data: dict[str, str],
    key_placeholder: str,
    value_placeholder: str,
    key2_placeholder: str,
    value2_placeholder: str,
) -> dict:
    """
    Extract templates that contain only the second placeholder.

    This helper function filters formatted_data to find templates that
    contain the second placeholder (key2_placeholder/value2_placeholder)
    but not the first placeholder (key_placeholder/value_placeholder).
    This is useful for creating a separate formatter for single-element
    translations.

    Args:
        formatted_data: The full template dictionary to filter.
        key_placeholder: First element's key placeholder (to exclude).
        value_placeholder: First element's value placeholder (to exclude).
        key2_placeholder: Second element's key placeholder (to include).
        value2_placeholder: Second element's value placeholder (to include).

    Returns:
        dict: Filtered templates containing only the second placeholder.

    Example:
        >>> formatted_data = {
        ...     "{nat} {sport} players": "لاعبو {sport_ar} {nat_ar}",
        ...     "{sport} coaches": "مدربو {sport_ar}",
        ... }
        >>> other_data = get_other_data(formatted_data, "{nat}", "{nat_ar}", "{sport}", "{sport_ar}")
        >>> other_data
        {'{sport} coaches': 'مدربو {sport_ar}'}
    """
    other_formatted_data = {
        x: v
        for x, v in formatted_data.items()
        if key2_placeholder in x and key_placeholder not in x and value2_placeholder in v and value_placeholder not in v
    }
    logger.debug(f"len other_formatted_data: {len(other_formatted_data):,}")

    return other_formatted_data


def format_multi_data(
    first_element_config: MultiDataFormatterConfig,
    second_element_config: Optional[MultiDataFormatterSecondElementConfig] = None,
    *,
    other_formatted_data: Dict[str, str] = None,
    use_other_formatted_data: bool = False,
    search_first_part: bool = False,
    data_to_find: Dict[str, str] | None = None,
) -> MultiDataFormatterBase:
    """
    Create a MultiDataFormatterBase for dual-element category translations.

    This factory function creates a formatter that handles categories with
    two dynamic elements (e.g., nationality and sport). It creates two
    internal FormatData instances (country_bot and other_bot) and combines
    them using MultiDataFormatterBase.

    Args:
        first_element_config: Configuration for the first element (e.g., country/nationality).
        second_element_config: Configuration for the second element (e.g., sport/year).
        use_other_formatted_data: If True, extract single-element templates for other_bot.
        search_first_part: If True, search using only the first part after normalization.
        data_to_find: Optional direct lookup dictionary for category labels.

    Returns:
        MultiDataFormatterBase: A configured formatter for dual-element translations.

    Example:
        >>> first_element_config = MultiDataFormatterConfig(
        ...     formatted_data={"{nat} {sport} players": "لاعبو {sport_ar} {nat_ar}"},
        ...     data_list={"british": "بريطانيون"},
        ...     key_placeholder="{nat}",
        ...     value_placeholder="{nat_ar}",
        ... )
        >>> second_element_config = MultiDataFormatterSecondElementConfig(
        ...     data_list={"football": "كرة القدم"},
        ...     key_placeholder="{sport}",
        ...     value_placeholder="{sport_ar}",
        ... )
        >>> bot = format_multi_data(first_element_config, second_element_config)
        >>> bot.search("british football players")
        'لاعبو كرة القدم بريطانيون'
    """
    if second_element_config is None:
        second_element_config = MultiDataFormatterSecondElementConfig()

    # Country bot (FormatData)
    if other_formatted_data is None:
        other_formatted_data = {}

    country_bot = FormatData(
        formatted_data=first_element_config.formatted_data,
        data_list=first_element_config.data_list,
        key_placeholder=first_element_config.key_placeholder,
        value_placeholder=first_element_config.value_placeholder,
        text_after=first_element_config.text_after,
        text_before=first_element_config.text_before,
        regex_filter=first_element_config.regex_filter,
    )

    _other_formatted_data = other_formatted_data or (
        get_other_data(
            formatted_data=first_element_config.formatted_data,
            key_placeholder=first_element_config.key_placeholder,
            value_placeholder=first_element_config.value_placeholder,
            key2_placeholder=second_element_config.key_placeholder,
            value2_placeholder=second_element_config.value_placeholder,
        )
        if use_other_formatted_data
        else {}
    )

    other_bot = FormatData(
        formatted_data=_other_formatted_data,  # to use from search_all
        data_list=second_element_config.data_list,
        key_placeholder=second_element_config.key_placeholder,
        value_placeholder=second_element_config.value_placeholder,
        regex_filter=second_element_config.regex_filter,
    )

    return MultiDataFormatterBase(
        country_bot=country_bot,
        other_bot=other_bot,
        search_first_part=search_first_part,
        data_to_find=data_to_find,
    )


def format_multi_data_v2(
    first_element_config: MultiDataFormatterConfig,
    second_element_config: Optional[MultiDataFormatterSecondElementConfig] = None,
    use_other_formatted_data: bool = False,
    search_first_part: bool = False,
    data_to_find: Dict[str, str] | None = None,
) -> MultiDataFormatterBaseV2:
    """
    Create a MultiDataFormatterBaseV2 for dual-element translations with dictionary support.

    This factory function creates a formatter similar to format_multi_data but uses
    FormatDataV2 which supports dictionary values in data_list for complex
    placeholder replacements with multiple values per key.

    Args:
        first_element_config: Configuration for the first element (e.g., country/nationality).
            Uses FormatDataV2 which supports dictionary values in data_list.
        second_element_config: Configuration for the second element (e.g., sport/year).
        use_other_formatted_data: If True, extract single-element templates for other_bot.
        search_first_part: If True, search using only the first part after normalization.
        data_to_find: Optional direct lookup dictionary for category labels.

    Returns:
        MultiDataFormatterBaseV2: A configured formatter for dual-element translations.

    Example:
        >>> first_element_config = MultiDataFormatterConfig(
        ...     formatted_data={"{country} {sport} players": "{demonym} لاعبو {sport_ar}"},
        ...     data_list={"yemen": {"demonym": "يمنيون"}},
        ...     key_placeholder="{country}",
        ... )
        >>> second_element_config = MultiDataFormatterSecondElementConfig(
        ...     data_list={"football": {"sport_ar": "كرة القدم"}},
        ...     key_placeholder="{sport}",
        ... )
        >>> bot = format_multi_data_v2(first_element_config, second_element_config)
        >>> bot.search("yemen football players")
        'يمنيون لاعبو كرة القدم'
    """
    if second_element_config is None:
        second_element_config = MultiDataFormatterSecondElementConfig()

    country_bot = FormatDataV2(
        formatted_data=first_element_config.formatted_data,
        data_list=first_element_config.data_list,
        key_placeholder=first_element_config.key_placeholder,
        text_after=first_element_config.text_after,
        text_before=first_element_config.text_before,
        regex_filter=first_element_config.regex_filter,
    )

    other_formatted_data = (
        {x: v for x, v in first_element_config.formatted_data.items() if second_element_config.key_placeholder in x and first_element_config.key_placeholder not in x}
        if use_other_formatted_data
        else {}
    )

    other_bot = FormatDataV2(
        formatted_data=other_formatted_data,
        data_list=second_element_config.data_list,
        key_placeholder=second_element_config.key_placeholder,
        text_after=second_element_config.text_after,
        text_before=second_element_config.text_before,
        regex_filter=second_element_config.regex_filter,
    )

    return MultiDataFormatterBaseV2(
        country_bot=country_bot,
        other_bot=other_bot,
        search_first_part=search_first_part,
        data_to_find=data_to_find,
    )


__all__ = [
    "format_multi_data",
    "format_multi_data_v2",
    "MultiDataFormatterConfig",
    "MultiDataFormatterSecondElementConfig",
]
