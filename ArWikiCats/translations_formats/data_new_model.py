#!/usr/bin/python3
"""
Module for film category translation formatting with double-key support.

This module provides the `format_films_country_data` factory function for
creating MultiDataFormatterDataDouble instances. It's designed for translating
film-related categories that contain both nationality and genre elements,
where the genre can have two adjacent keys (e.g., "action drama films").

Example:
    >>> from ArWikiCats.translations_formats import format_films_country_data
    >>> formatted_data = {"{nat_en} {film_key} films": "أفلام {film_ar} {nat_ar}"}
    >>> data_list = {"british": "بريطانية", "american": "أمريكية"}
    >>> data_list2 = {"action": "أكشن", "drama": "دراما", "comedy": "كوميدي"}
    >>> bot = format_films_country_data(
    ...     formatted_data=formatted_data,
    ...     data_list=data_list,
    ...     data_list2=data_list2,
    ... )
    >>> bot.search("british action drama films")
    'أفلام أكشن دراما بريطانية'
"""

from typing import Dict

from .DataModel import FormatData
from .DataModelDouble import FormatDataDouble, MultiDataFormatterDataDouble


def format_films_country_data(
    formatted_data: Dict[str, str],
    data_list: Dict[str, str],
    key_placeholder: str = "{nat_en}",
    value_placeholder: str = "{nat_ar}",
    data_list2: Dict[str, str] = None,
    other_formatted_data: Dict[str, str] = None,
    key2_placeholder: str = "{film_key}",
    value2_placeholder: str = "{film_ar}",
    text_after: str = "",
    text_before: str = "",
    data_to_find: Dict[str, str] | None = None,
) -> MultiDataFormatterDataDouble:
    """
    Create a MultiDataFormatterDataDouble for film category translations.

    This factory function creates a formatter that handles film categories
    with nationality and genre elements. The genre element supports double-key
    matching (e.g., "action drama" as two adjacent genre keys).

    Args:
        formatted_data: Template patterns mapping English patterns to Arabic templates.
            Keys should contain placeholders like "{nat_en}" and "{film_key}".
        data_list: Nationality key-to-Arabic-label mappings (e.g., {"british": "بريطانية"}).
        key_placeholder: Placeholder for nationality key in templates. Default: "{nat_en}".
        value_placeholder: Placeholder for nationality value in Arabic templates. Default: "{nat_ar}".
        data_list2: Genre key-to-Arabic-label mappings (e.g., {"action": "أكشن"}).
        other_formatted_data: Additional template patterns for genre-only translations.
        key2_placeholder: Placeholder for genre key in templates. Default: "{film_key}".
        value2_placeholder: Placeholder for genre value in Arabic templates. Default: "{film_ar}".
        text_after: Optional text that appears after the nationality key.
        text_before: Optional text that appears before the nationality key.
        data_to_find: Optional direct lookup dictionary for category labels.

    Returns:
        MultiDataFormatterDataDouble: A configured formatter for film category translations.

    Example:
        >>> formatted_data = {"{nat_en} {film_key} films": "أفلام {film_ar} {nat_ar}"}
        >>> data_list = {"british": "بريطانية"}
        >>> data_list2 = {"action": "أكشن", "drama": "دراما"}
        >>> bot = format_films_country_data(
        ...     formatted_data=formatted_data,
        ...     data_list=data_list,
        ...     data_list2=data_list2,
        ... )
        >>> bot.search("british action films")
        'أفلام أكشن بريطانية'
    """

    # Country bot (FormatData)
    if other_formatted_data is None:
        other_formatted_data = {}
    if data_list2 is None:
        data_list2 = {}
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
        data_to_find=data_to_find,
    )


__all__ = [
    "format_films_country_data",
]
