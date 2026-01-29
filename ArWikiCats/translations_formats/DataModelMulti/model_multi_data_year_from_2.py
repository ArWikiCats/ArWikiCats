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

from ..DataModel import FormatDataFrom
from .model_multi_data_base import MultiDataFormatterBaseHelpers


class MultiDataFormatterYearAndFrom2(MultiDataFormatterBaseHelpers):
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

    Example:
        >>> bot = MultiDataFormatterYearAndFrom(country_bot, year_bot, other_key_first=True)
        >>> bot.create_label("14th-century writers from Yemen")
        'كتاب من اليمن في القرن 14'

        >>> bot.get_relation_word("People from Germany")
        ('from', 'من')

        >>> bot.resolve_relation_label("People from Germany", "أشخاص")
        'أشخاص من'
    """

    def __init__(
        self,
        country_bot: FormatDataFrom,
        year_bot: FormatDataFrom,
        category_relation_mapping: dict[str, str] = {},
        search_first_part: bool = False,
        data_to_find: dict[str, str] | None = None,
        other_key_first: bool = False,
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels.

        Args:
            country_bot: FormatDataFrom instance for handling "from" relation patterns.
            year_bot: FormatDataFrom instance for handling year/time patterns.
            category_relation_mapping: Mapping of relation words to Arabic translations.
            search_first_part: If True, search using only the first part after normalization.
            data_to_find: Optional dictionary for direct category-to-label lookups.
            other_key_first: If True, process year/other key before country key.
        """
        self.search_first_part = search_first_part
        self.country_bot = country_bot
        self.other_bot = year_bot
        self.data_to_find = data_to_find
        self.other_key_first = other_key_first

        self.category_relation_mapping = dict(
            sorted(
                category_relation_mapping.items(),
                key=lambda k: (-k[0].count(" "), -len(k[0])),
            )
        )

    def get_relation_word(self, category: str) -> tuple[str, str]:
        """
        Find the first relation word in the category using category_relation_mapping.

        Searches for relation words (prepositions like "from", "in", "by") in the
        category string and returns the matching key and its Arabic translation.

        Note:
            The method returns the first match found based on the iteration order
            of category_relation_mapping dictionary (insertion order in Python 3.7+).
            Longer/more specific relation phrases should be defined before shorter ones
            in the mapping to ensure correct matching (e.g., "published by" before "by").

        Args:
            category: The English category string to search.

        Returns:
            A tuple of (relation_key, arabic_translation). Returns ("", "") if no match.

        Example:
            >>> bot.get_relation_word("People from Germany")
            ('from', 'من')
            >>> bot.get_relation_word("Buildings in France")
            ('in', 'في')
            >>> bot.get_relation_word("Works published by Oxford")
            ('published by', 'نشرتها')
        """
        for separator, separator_name in self.category_relation_mapping.items():
            separator_with_spaces = f" {separator} "
            if separator_with_spaces in category:
                return separator, separator_name
        return "", ""

    def resolve_relation_label(self, category: str, base_label: str) -> str:
        """
        Append the Arabic relation word to a base label based on the category.

        Finds the relation word in the category and appends its Arabic equivalent
        to the base label if appropriate.

        Args:
            category: The English category string containing a relation word.
            base_label: The Arabic base label to append the relation to.

        Returns:
            The base label with the Arabic relation word appended, or the original
            base label if no relation is found or if it's already present.

        Example:
            >>> bot.resolve_relation_label("Writers from Yemen", "كتاب")
            'كتاب من'
            >>> bot.resolve_relation_label("People in Germany", "أشخاص")
            'أشخاص في'
        """
        if not base_label or not category:
            return base_label

        relation_key, relation_ar = self.get_relation_word(category)

        if not relation_ar:
            return base_label

        # Avoid duplicate relation words by checking if it ends with the relation
        # or contains it as a complete word (surrounded by spaces or at boundaries)
        relation_ar_stripped = relation_ar.strip()
        if base_label.endswith(relation_ar_stripped) or base_label.endswith(f" {relation_ar_stripped}"):
            return base_label
        if f" {relation_ar_stripped} " in base_label:
            return base_label

        return f"{base_label} {relation_ar}".strip()

    def get_relation_mapping(self) -> dict[str, str]:
        """
        Return the category_relation_mapping dictionary.

        This provides access to the full relation word mapping for external use
        or inspection.

        Returns:
            The category_relation_mapping dictionary with English keys and Arabic values.

        Example:
            >>> mapping = bot.get_relation_mapping()
            >>> mapping["from"]
            'من'
            >>> mapping["published by"]
            'نشرتها'
        """
        return self.category_relation_mapping
