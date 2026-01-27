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
    >>> from ArWikiCats.translations_formats import format_multi_data
    >>> formatted_data = {"{nat} {sport} players": "لاعبو {sport_ar} {nat_ar}"}
    >>> data_list = {"british": "بريطانيون", "american": "أمريكيون"}
    >>> data_list2 = {"football": "كرة القدم", "basketball": "كرة السلة"}
    >>> bot = format_multi_data(
    ...     formatted_data=formatted_data,
    ...     data_list=data_list,
    ...     data_list2=data_list2,
    ...     key_placeholder="{nat}",
    ...     value_placeholder="{nat_ar}",
    ...     key2_placeholder="{sport}",
    ...     value2_placeholder="{sport_ar}",
    ... )
    >>> bot.search("british football players")
    'لاعبو كرة القدم بريطانيون'

test at tests.translations_formats.test_format_2_data.py
"""

from typing import Dict

from .DataModel import FormatData, FormatDataV2
from .DataModelMulti import MultiDataFormatterBase, MultiDataFormatterBaseV2
from .formats_logger import logger

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
    formatted_data: Dict[str, str],
    data_list: Dict[str, str],
    key_placeholder: str = COUNTRY_PARAM,
    value_placeholder: str = COUNTRY_PARAM,
    data_list2: Dict[str, str] = {},
    key2_placeholder: str = YEAR_PARAM,
    value2_placeholder: str = YEAR_PARAM,
    text_after: str = "",
    text_before: str = "",
    other_formatted_data: Dict[str, str] = {},
    use_other_formatted_data: bool = False,
    search_first_part: bool = False,
    data_to_find: Dict[str, str] | None = None,
    regex_filter: str | None = None,
) -> MultiDataFormatterBase:
    """
    Create a MultiDataFormatterBase for dual-element category translations.

    This factory function creates a formatter that handles categories with
    two dynamic elements (e.g., nationality and sport). It creates two
    internal FormatData instances (country_bot and other_bot) and combines
    them using MultiDataFormatterBase.

    Args:
        formatted_data: Template patterns mapping English patterns to Arabic templates.
            Keys should contain both placeholders (e.g., "{nat} {sport} players").
        data_list: First element key-to-Arabic-label mappings
            (e.g., {"british": "بريطانيون"}).
        key_placeholder: Placeholder for first element key. Default: "natar".
        value_placeholder: Placeholder for first element value. Default: "natar".
        data_list2: Second element key-to-Arabic-label mappings
            (e.g., {"football": "كرة القدم"}).
        key2_placeholder: Placeholder for second element key. Default: "xoxo".
        value2_placeholder: Placeholder for second element value. Default: "xoxo".
        text_after: Optional text that appears after the first element key.
        text_before: Optional text that appears before the first element key.
        use_other_formatted_data: If True, extract single-element templates for other_bot.
        search_first_part: If True, search using only the first part after normalization.
        data_to_find: Optional direct lookup dictionary for category labels.
        regex_filter: Custom regex pattern for word boundary detection.

    Returns:
        MultiDataFormatterBase: A configured formatter for dual-element translations.

    Example:
        >>> formatted_data = {"{nat} {sport} players": "لاعبو {sport_ar} {nat_ar}"}
        >>> data_list = {"british": "بريطانيون"}
        >>> data_list2 = {"football": "كرة القدم"}
        >>> bot = format_multi_data(
        ...     formatted_data=formatted_data,
        ...     data_list=data_list,
        ...     data_list2=data_list2,
        ...     key_placeholder="{nat}",
        ...     value_placeholder="{nat_ar}",
        ...     key2_placeholder="{sport}",
        ...     value2_placeholder="{sport_ar}",
        ... )
        >>> bot.search("british football players")
        'لاعبو كرة القدم بريطانيون'
    """
    # Country bot (FormatData)
    country_bot = FormatData(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder=key_placeholder,
        value_placeholder=value_placeholder,
        text_after=text_after,
        text_before=text_before,
        regex_filter=regex_filter,
    )

    _other_formatted_data = other_formatted_data or (
        get_other_data(
            formatted_data=formatted_data,
            key_placeholder=key_placeholder,
            value_placeholder=value_placeholder,
            key2_placeholder=key2_placeholder,
            value2_placeholder=value2_placeholder,
        )
        if use_other_formatted_data
        else {}
    )

    other_bot = FormatData(
        formatted_data=_other_formatted_data,  # to use from search_all
        data_list=data_list2,
        key_placeholder=key2_placeholder,
        value_placeholder=value2_placeholder,
        regex_filter=regex_filter,
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
    use_other_formatted_data: bool = False,
    search_first_part: bool = False,
    data_to_find: Dict[str, str] | None = None,
    regex_filter: str | None = None,
) -> MultiDataFormatterBaseV2:
    """
    Create a MultiDataFormatterBaseV2 for dual-element translations with dictionary support.

    This factory function creates a formatter similar to format_multi_data but uses
    FormatDataV2 which supports dictionary values in data_list for complex
    placeholder replacements with multiple values per key.

    Args:
        formatted_data: Template patterns mapping English patterns to Arabic templates.
            Keys should contain both placeholders.
        data_list: First element key-to-value mappings. Values can be strings or
            dictionaries with multiple placeholders.
        key_placeholder: Placeholder for first element key (required).
        data_list2: Second element key-to-value mappings.
        key2_placeholder: Placeholder for second element key. Default: "xoxo".
        text_after: Optional text that appears after the first element key.
        text_before: Optional text that appears before the first element key.
        use_other_formatted_data: If True, extract single-element templates for other_bot.
        search_first_part: If True, search using only the first part after normalization.
        data_to_find: Optional direct lookup dictionary for category labels.
        regex_filter: Custom regex pattern for word boundary detection.

    Returns:
        MultiDataFormatterBaseV2: A configured formatter for dual-element translations.

    Example:
        >>> formatted_data = {"{country} {sport} players": "{demonym} لاعبو {sport_ar}"}
        >>> data_list = {"yemen": {"demonym": "يمنيون"}}
        >>> data_list2 = {"football": {"sport_ar": "كرة القدم"}}
        >>> bot = format_multi_data_v2(
        ...     formatted_data=formatted_data,
        ...     data_list=data_list,
        ...     key_placeholder="{country}",
        ...     data_list2=data_list2,
        ...     key2_placeholder="{sport}",
        ... )
        >>> bot.search("yemen football players")
        'يمنيون لاعبو كرة القدم'
    """
    country_bot = FormatDataV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder=key_placeholder,
        text_after=text_after,
        text_before=text_before,
        regex_filter=regex_filter,
    )

    other_formatted_data = (
        {x: v for x, v in formatted_data.items() if key2_placeholder in x and key_placeholder not in x}
        if use_other_formatted_data
        else {}
    )

    other_bot = FormatDataV2(
        formatted_data=other_formatted_data,
        data_list=data_list2,
        key_placeholder=key2_placeholder,
        text_after=text_after,
        text_before=text_before,
        regex_filter=regex_filter,
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
]
