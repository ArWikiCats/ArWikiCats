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

from dataclasses import dataclass, field
from typing import Dict, Optional

from .DataModel import FormatData
from .DataModelDouble import FormatDataDouble, MultiDataFormatterDataDouble


@dataclass
class CountryBotConfig:
    """Configuration for the country/nationality part of the formatter."""

    formatted_data: Dict[str, str]
    data_list: Dict[str, str]
    key_placeholder: str = "{nat_en}"
    value_placeholder: str = "{nat_ar}"
    text_after: str = ""
    text_before: str = ""


@dataclass
class GenreBotConfig:
    """Configuration for the genre/film_key part of the formatter."""

    data_list: Dict[str, str] = field(default_factory=dict)
    formatted_data: Dict[str, str] = field(default_factory=dict)
    key_placeholder: str = "{film_key}"
    value_placeholder: str = "{film_ar}"


def format_films_country_data(
    country_config: CountryBotConfig,
    genre_config: Optional[GenreBotConfig] = None,
    data_to_find: Dict[str, str] | None = None,
) -> MultiDataFormatterDataDouble:
    """
    Create a MultiDataFormatterDataDouble for film category translations.

    This factory function creates a formatter that handles film categories
    with nationality and genre elements. The genre element supports double-key
    matching (e.g., "action drama" as two adjacent genre keys).

    Args:
        country_config: Configuration for the country-based formatter.
        genre_config: Configuration for the genre-based formatter.
        data_to_find: Optional direct lookup dictionary for category labels.

    Returns:
        MultiDataFormatterDataDouble: A configured formatter for film category translations.

    Example:
        >>> country_config = CountryBotConfig(
        ...     formatted_data={"{nat_en} {film_key} films": "أفلام {film_ar} {nat_ar}"},
        ...     data_list={"british": "بريطانية"}
        ... )
        >>> genre_config = GenreBotConfig(
        ...     data_list={"action": "أكشن", "drama": "دراما"}
        ... )
        >>> bot = format_films_country_data(country_config, genre_config)
        >>> bot.search("british action films")
        'أفلام أكشن بريطانية'
    """
    if genre_config is None:
        genre_config = GenreBotConfig()

    # Country bot (FormatData)
    country_bot = FormatData(
        formatted_data=country_config.formatted_data,
        data_list=country_config.data_list,
        key_placeholder=country_config.key_placeholder,
        value_placeholder=country_config.value_placeholder,
        text_after=country_config.text_after,
        text_before=country_config.text_before,
    )

    other_bot = FormatDataDouble(
        formatted_data=genre_config.formatted_data,  # to use from search_all
        data_list=genre_config.data_list,
        key_placeholder=genre_config.key_placeholder,
        value_placeholder=genre_config.value_placeholder,
    )

    return MultiDataFormatterDataDouble(
        country_bot=country_bot,
        other_bot=other_bot,
        data_to_find=data_to_find,
    )


__all__ = [
    "format_films_country_data",
    "CountryBotConfig",
    "GenreBotConfig",
]
