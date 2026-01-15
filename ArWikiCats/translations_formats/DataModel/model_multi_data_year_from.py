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
import re

from ..formats_logger import logger

# from .model_data_time import YearFormatData
from .model_multi_data_base import MultiDataFormatterBaseHelpers


class FormatDataFrom:
    """
    A dynamic wrapper for handling category transformations with customizable callbacks.

    This class provides a flexible way to normalize category strings by extracting
    keys (e.g., year patterns, country names) and replacing them with placeholders.
    It uses callback functions for key matching and searching, allowing customization
    for different category types.

    Attributes:
        formatted_data (dict[str, str]): Mapping of template patterns to Arabic translations.
        formatted_data_ci (dict[str, str]): Case-insensitive version of formatted_data.
        key_placeholder (str): Placeholder string for the key (e.g., "{year1}", "{country1}").
        value_placeholder (str): Placeholder string for the value in Arabic templates.
        search_callback (callable): Function to search/translate a key to its Arabic label.
        match_key_callback (callable): Function to extract a key from a category string.
        fixing_callback (callable | None): Optional callback for post-processing results.

    Example:
        >>> bot = FormatDataFrom(
        ...     formatted_data={"{year1} {country1}": "{country1} في {year1}"},
        ...     key_placeholder="{country1}",
        ...     value_placeholder="{country1}",
        ...     search_callback=lambda x: "كتاب من اليمن" if "yemen" in x.lower() else "",
        ...     match_key_callback=lambda x: x.replace("{year1}", "").strip(),
        ... )
        >>> bot.match_key("{year1} writers from yemen")
        'writers from yemen'
    """

    def __init__(
        self,
        formatted_data: dict[str, str],
        key_placeholder: str,
        value_placeholder: str,
        search_callback: callable,
        match_key_callback: callable,
        fixing_callback: callable = None,
    ) -> None:
        self.search_callback = search_callback
        self.match_key_callback = match_key_callback

        self.key_placeholder = key_placeholder
        self.value_placeholder = value_placeholder
        self.formatted_data = formatted_data
        self.formatted_data_ci = {k.lower(): v for k, v in formatted_data.items()}
        self.fixing_callback = fixing_callback

    def match_key(self, text: str) -> str:
        """Extract English year/decade and return it as the key."""
        return self.match_key_callback(text)

    def normalize_category(self, text: str, key: str) -> str:
        """
        Replace matched year with placeholder.
        normalize_category: key='writers from yemen', text='{year1} writers from yemen'
        """
        logger.debug(f"normalize_category: {key=}, {text=}")
        if not key:
            return text
        result = re.sub(re.escape(key), self.key_placeholder, text, flags=re.IGNORECASE)
        logger.debug(f"normalize_category: {result=}")  # result='{year1} {country1}'
        return result

    def normalize_category_with_key(self, category: str) -> tuple[str, str]:
        """
        Normalize nationality placeholders within a category string.

        Example:
            category:"Yemeni national football teams", result: "natar national football teams"
        """
        key = self.match_key(category)
        result = ""
        if key:
            result = self.normalize_category(category, key)
        return key, result

    def replace_value_placeholder(self, label: str, value: str) -> str:
        # Replace placeholder
        logger.debug(f"!!!! replace_value_placeholder: {self.value_placeholder=}, {label=}, {value=}")
        result = label.replace(self.value_placeholder, value)
        if self.fixing_callback:
            result = self.fixing_callback(result)
        return result

    def get_template_ar(self, template_key: str) -> str:
        """Lookup template in a case-insensitive dict."""
        # Case-insensitive key lookup
        template_key = template_key.lower()
        logger.debug(f"get_template_ar: {template_key=}")
        result = self.formatted_data_ci.get(template_key, "")

        if not result:
            if template_key.startswith("category:"):
                template_key = template_key.replace("category:", "")
                result = self.formatted_data_ci.get(template_key, "")
            else:
                result = self.formatted_data_ci.get(f"category:{template_key}", "")

        logger.debug(f"get_template_ar: {template_key=}, {result=}")
        return result

    def get_key_label(self, key: str) -> str:
        """place holders"""
        if not key:
            return ""
        logger.debug(f"get_key_label: {key=}")
        return self.search(key)

    def search(self, text: str) -> str:
        """place holders"""
        return self.search_callback(text)

    def search_all(self, key: str) -> str:
        """place holders"""
        return self.search(key)


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
