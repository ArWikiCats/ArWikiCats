#!/usr/bin/python3
"""
Module for double-key category translation formatting.

This module provides the FormatDataDouble class for translating category strings
that contain two dynamic elements that need to be matched and combined. It is used
for categories like "action drama films" where both "action" and "drama" are
separate keys that need to be identified and their labels combined.

Classes:
    FormatDataDouble: Handles double-key template-driven category translations.

Example:
    >>> from ArWikiCats.translations_formats.DataModel import FormatDataDouble
    >>> formatted_data = {
    ...     "{film_key} films": "أفلام {film_label}",
    ... }
    >>> data_list = {
    ...     "action": "أكشن",
    ...     "drama": "دراما",
    ...     "comedy": "كوميدي",
    ... }
    >>> bot = FormatDataDouble(formatted_data, data_list, key_placeholder="{film_key}", value_placeholder="{film_label}")
    >>> bot.search("action drama films")
    'أفلام أكشن دراما'
"""

import functools
import re
import logging
from typing import Dict, Optional

from ..DataModel.model_data_base import FormatDataBase

logger = logging.getLogger(__name__)


class FormatDataDouble(FormatDataBase):
    """
    Handles double-key template-driven category translations.

    This class extends FormatDataBase to handle categories where two adjacent
    keys from the data_list appear together (e.g., "action drama films").
    It can match both single keys and pairs of keys, combining their Arabic
    labels in the correct order.

    Attributes:
        formatted_data (Dict[str, str]): Template patterns mapping English patterns to Arabic templates.
        data_list (Dict[str, str]): Key-to-Arabic-label mappings for replacements.
        key_placeholder (str): Placeholder used in formatted_data keys.
        value_placeholder (str): Placeholder used in formatted_data values.
        text_after (str): Text to append after the translated label.
        text_before (str): Text to prepend before the translated label.
        splitter (str): Separator used between keys in input strings.
        ar_joiner (str): Separator used between Arabic labels in output.
        sort_ar_labels (bool): Whether to sort Arabic labels alphabetically.
        alternation (str): Regex alternation string for keys.
        pattern (re.Pattern): Regex pattern for single key matching.
        pattern_double (re.Pattern): Regex pattern for matching two adjacent keys.
        keys_to_split (dict): Cache mapping combined keys to their component parts.
        put_label_last (dict): Keys whose labels should appear last in combinations.
        search_multi_cache (dict): Cache for combined label lookups.

    Example:
        >>> data_list = {
        ...     "action": "أكشن",
        ...     "drama": "دراما",
        ... }
        >>> bot = FormatDataDouble(
        ...     formatted_data={"{genre} films": "أفلام {genre_label}"},
        ...     data_list=data_list,
        ...     key_placeholder="{genre}",
        ...     value_placeholder="{genre_label}",
        ... )
        >>> bot.search("action drama films")
        'أفلام أكشن دراما'
    """

    def __init__(
        self,
        formatted_data: Dict[str, str],
        data_list: Dict[str, str],
        key_placeholder: str = "xoxo",
        value_placeholder: str = "xoxo",
        text_after: str = "",
        text_before: str = "",
        splitter: str = " ",
        ar_joiner: str = " ",
        sort_ar_labels: bool = False,
        log_multi_cache: bool = True,
    ):
        """Prepare helpers for matching and formatting template-driven labels."""
        super().__init__(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder=key_placeholder,
            text_after=text_after,
            text_before=text_before,
        )
        self.log_multi_cache = log_multi_cache
        self.sort_ar_labels = sort_ar_labels
        self.value_placeholder = value_placeholder
        self.keys_to_split = {}
        self.put_label_last = {}
        self.search_multi_cache = {}
        self.splitter = splitter or " "
        self.ar_joiner = ar_joiner or " "

        self.alternation: str = self.create_alternation()
        self.pattern = self.keys_to_pattern()

        self.pattern_double = self.keys_to_pattern_double()

    def update_put_label_last(self, data: list[str] | set[str]) -> None:
        self.put_label_last = data

    def keys_to_pattern_double(self) -> Optional[re.Pattern[str]]:
        """
        Create a case-insensitive regex that matches two adjacent keys separated by the configured splitter.

        The resulting pattern targets whole-word matches of the form `key1{splitter}key2` using lookaround assertions and the class's alternation of lowercased keys. Returns `None` when no keys are available to build the pattern.

        Returns:
            re.Pattern[str] | None: Compiled, case-insensitive regex for two-key matches, or `None` if `data_list_ci` is empty.
        """
        if not self.data_list_ci:
            return None

        if self.alternation is None:
            self.alternation = self.create_alternation()

        data_pattern = rf"(?<!\w)({self.alternation})({self.splitter})({self.alternation})(?!\w)"
        return re.compile(data_pattern, re.I)

    @functools.lru_cache(maxsize=10000)
    def match_key(self, category: str) -> str:
        """
        Determine the canonical lowercase key that corresponds to a given category string.

        The input is normalized by collapsing consecutive spaces. If an exact case-insensitive key exists it is returned. Otherwise the method attempts to match two adjacent keys (with the configured splitter) and, on success, caches their components in `keys_to_split` and returns the combined key. If that fails it tries a single-key match. If no match is found, an empty string is returned.

        Returns:
            str: The matched canonical key in lowercase, or an empty string if no match is found.
        """
        if not self.pattern:
            return ""

        # Normalize the category by removing extra spaces
        normalized_category = " ".join(category.split())
        logger.debug(f">!> match_key: {normalized_category=}")

        # TODO: check this
        if self.data_list_ci.get(normalized_category.lower()):
            logger.debug(f">>!!>> match_key: found in data_list_ci {normalized_category=}")
            return normalized_category.lower()

        match = self.pattern_double.search(f" {normalized_category} ")
        if match:
            first_key = match.group(1).lower()
            splitter = match.group(2).lower()
            second_key = match.group(3).lower()
            result = f"{first_key}{splitter}{second_key}"

            logger.debug(f">!> match_key: {first_key=}, {second_key=}")
            logger.debug(f">!> match_key: {result=}")
            self.keys_to_split[result] = [first_key, second_key]
            return result

        match2 = self.pattern.search(f" {normalized_category} ")
        result = match2.group(1).lower() if match2 else ""
        logger.debug(f"==== match_key {result=}")

        return result

    @functools.lru_cache(maxsize=10000)
    def apply_pattern_replacement(self, template_label: str, sport_label: str) -> str:
        """
        Insert the provided sport label into the template by replacing the value placeholder.

        Parameters:
            template_label (str): Template string that contains the value placeholder.
            sport_label (str): String to substitute for the value placeholder.

        Returns:
            str: The template with the placeholder replaced and trimmed if no value placeholder remains; otherwise an empty string.
        """
        final_label = template_label.replace(self.value_placeholder, sport_label)

        if self.value_placeholder not in final_label:
            return final_label.strip()

        return ""

    @functools.lru_cache(maxsize=5000)
    def create_label_from_keys(self, part1: str, part2: str):
        """
        Compose an Arabic label by combining the labels for two key parts.

        Parameters:
                part1 (str): The first key whose Arabic label will be looked up.
                part2 (str): The second key whose Arabic label will be looked up.

        Description:
                Looks up Arabic labels for `part1` and `part2` and joins them with `self.ar_joiner`. If either key is missing, returns an empty string. The final ordering of the two labels is affected by `self.put_label_last` (which forces a key's label to appear last when applicable) and by `self.sort_ar_labels` (which, when true, sorts the two labels alphabetically before joining). If `self.log_multi_cache` is enabled, the resulting label is stored in `self.search_multi_cache` under the key "`part2 part1`".

        Returns:
                A string containing the composed Arabic label, or an empty string if either key has no label.

        if "upcoming" in self.put_label_last we using:
            "أفلام قادمة رعب يمنية instead of "أفلام رعب قادمة يمنية"
        """

        first_label = self.data_list_ci.get(part1)
        second_label = self.data_list_ci.get(part2)

        if not first_label or not second_label:
            return ""

        label = f"{first_label}{self.ar_joiner}{second_label}"

        if part1 in self.put_label_last and part2 not in self.put_label_last:
            label = f"{second_label}{self.ar_joiner}{first_label}"

        if self.sort_ar_labels:
            labels_sorted = sorted([first_label, second_label])
            label = self.ar_joiner.join(labels_sorted)
        if self.log_multi_cache:
            self.search_multi_cache[f"{part2} {part1}"] = label

        return label

    def get_key_label(self, sport_key: str) -> str:
        """
        Return the Arabic label mapped to the provided key if present.
        Example:
            sport_key="action", result="أكشن"
            sport_key="action drama", result="أكشن دراما"
        """
        result = self.data_list_ci.get(sport_key)
        if result:
            return result

        if self.search_multi_cache.get(sport_key.lower()):
            return self.search_multi_cache[sport_key.lower()]

        if sport_key in self.keys_to_split:
            part1, part2 = self.keys_to_split[sport_key]
            return self.create_label_from_keys(part1, part2)

        return ""

    def replace_value_placeholder(self, label: str, value: str) -> str:
        # Replace placeholder
        logger.debug(f"!!!! replace_value_placeholder: {self.value_placeholder=}, {label=}, {value=}")
        return label.replace(self.value_placeholder, value)
