#!/usr/bin/python3
"""
Module for handling year-and-from based category translations.

This module provides classes for formatting template-driven translation labels
that combine temporal patterns (years, decades, centuries) with "from" relation
patterns (e.g., "writers from Yemen", "people from Germany").

The module integrates with category_relation_mapping to resolve relation words
(prepositions like "from", "in", "by") into their Arabic equivalents.

Classes:
    FormatDataFrom: A dynamic wrapper for handling category transformations
        with customizable callbacks for key matching and searching.
    MultiDataFormatterYearAndFrom: Combines year-based and "from" relation
        category translations using the parent class helpers.

Example:
    >>> from ArWikiCats.translations_formats import MultiDataFormatterYearAndFrom, FormatDataFrom
    >>> country_bot = FormatDataFrom(
    ...     formatted_data={"{year1} {country1}": "{country1} في {year1}"},
    ...     key_placeholder="{country1}",
    ...     value_placeholder="{country1}",
    ...     search_callback=get_label_func,
    ...     match_key_callback=match_key_func,
    ... )
    >>> year_bot = FormatDataFrom(
    ...     formatted_data={},
    ...     key_placeholder="{year1}",
    ...     value_placeholder="{year1}",
    ...     search_callback=convert_time_to_arabic,
    ...     match_key_callback=match_time_en_first,
    ... )
    >>> bot = MultiDataFormatterYearAndFrom(country_bot, year_bot, other_key_first=True)
    >>> bot.create_label("14th-century writers from Yemen")
    'كتاب من اليمن في القرن 14'
"""

from .model_multi_data_base import MultiDataFormatterBaseHelpers
from ..DataModel import FormatDataFrom


class MultiDataFormatterYearAndFrom(MultiDataFormatterBaseHelpers):
    """
    Combines year-based and "from" relation category translations.

    This class orchestrates two FormatDataFrom instances (country_bot and year_bot)
    to normalize and translate category strings that contain both temporal patterns
    and "from" relation patterns.

    The class integrates with category_relation_mapping to resolve relation words
    (prepositions like "from", "in", "by") into their Arabic equivalents when
    building labels.

    Attributes:
        country_bot (FormatDataFrom): Handles the "from" relation part (e.g., "writers from Yemen").
        other_bot (FormatDataFrom): Handles the year/time part (e.g., "14th-century").
        search_first_part (bool): If True, search using only the first part (after country normalization).
        data_to_find (dict[str, str] | None): Optional direct lookup dictionary for category labels.
        other_key_first (bool): If True, process the year/other key before the country key.

    """

    def __init__(
        self,
        country_bot: FormatDataFrom,
        year_bot: FormatDataFrom,
        search_first_part: bool = False,
        data_to_find: dict[str, str] | None = None,
        other_key_first: bool = False,
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels.

        Args:
            country_bot: FormatDataFrom instance for handling "from" relation patterns.
            year_bot: FormatDataFrom instance for handling year/time patterns.
            search_first_part: If True, search using only the first part after normalization.
            data_to_find: Optional dictionary for direct category-to-label lookups.
            other_key_first: If True, process year/other key before country key.
        """
        self.search_first_part = search_first_part
        self.country_bot = country_bot
        self.other_bot = year_bot
        self.data_to_find = data_to_find
        self.other_key_first = other_key_first
