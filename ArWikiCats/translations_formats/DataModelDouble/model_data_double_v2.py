"""
Double-key template-driven translation model (v2).
This module provides the FormatDataDoubleV2 class, which handles categories
where two adjacent keys from a data list appear together.
"""

import functools
import re
import logging
from typing import Dict, Optional, Union

from ..DataModel.model_data_base import FormatDataBase

logger = logging.getLogger(__name__)


class FormatDataDoubleV2(FormatDataBase):
    """
    Handles double-key template-driven category translations.

    This class extends FormatDataBase to handle categories where two adjacent
    keys from the data_list appear together (e.g., "action drama films").
    It can match both single keys and pairs of keys, combining their Arabic
    labels in the correct order, with options to sort labels or place specific
    labels last.

    Attributes:
        formatted_data (Dict[str, str]): Template patterns mapping English patterns to Arabic templates.
        data_list (Dict[str, Union[str, Dict[str, str]]]): Key-to-Arabic-label mappings for replacements.
        key_placeholder (str): Placeholder used in formatted_data keys (default: "xoxo").
        text_after (str): Text to append after the formatted label (default: "").
        text_before (str): Text to prepend before the formatted label (default: "").
        splitter (str): Separator used in patterns for splitting keys (default: " ").
        ar_joiner (str): Joiner for combining Arabic labels (default: " ").
        sort_ar_labels (bool): Whether to sort Arabic labels alphabetically (default: False).
        keys_to_split (dict): Cache mapping combined keys to their component parts.
        put_label_last (set[str] | list[str]): Keys whose labels should appear last in combinations.
        search_multi_cache (dict): Cache for combined label lookups.
        alternation (str): Regex alternation string for keys.
        pattern (re.Pattern): Regex pattern for matching single keys.
        pattern_double (re.Pattern): Regex pattern for matching two adjacent keys.

    Example:
        >>> data_list = {
        ...     "action": {"genre_label": "أكشن"},
        ...     "drama": {"genre_label": "دراما"},
        ... }
        >>> bot = FormatDataDoubleV2(
        ...     formatted_data={"{genre} films": "أفلام {genre_label}"},
        ...     data_list=data_list,
        ...     key_placeholder="{genre}",
        ... )
        >>> bot.search("action drama films")
        'أفلام أكشن دراما'
    """

    def __init__(
        self,
        formatted_data: Dict[str, str],
        data_list: Dict[str, Union[str, Dict[str, str]]],
        key_placeholder: str = "xoxo",
        text_after: str = "",
        text_before: str = "",
        splitter: str = " ",
        ar_joiner: str = " ",
        sort_ar_labels: bool = False,
        log_multi_cache: bool = True,
    ):
        """
        Initialize FormatDataDoubleV2 and prepare caches, regex patterns, and configuration used for single- and double-key template matching and Arabic label assembly.

        Parameters:
            formatted_data: Mapping of English patterns to Arabic templates used for exact and template-based matches.
            data_list: Mapping of keys to Arabic labels or dicts of attribute-specific Arabic labels.
            key_placeholder: Placeholder token used inside templates for key substitution.
            text_after: Text appended to the final generated label.
            text_before: Text prepended to the final generated label.
            splitter: Separator expected between two adjacent keys in source categories (used when building double-key regex).
            ar_joiner: Joiner used to combine two Arabic labels when forming a composite label.
            sort_ar_labels: If True, sort the two Arabic labels alphabetically before joining.
            log_multi_cache: If True, enable caching/logging of multi-key composite label lookups.

        Side effects:
            - Initializes internal caches: keys_to_split, search_multi_cache, and put_label_last.
            - Builds regex alternation and compiles single- and double-key matching patterns (pattern, pattern_double).
        """
        super().__init__(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder=key_placeholder,
            text_after=text_after,
            text_before=text_before,
        )
        self.log_multi_cache = log_multi_cache
        self.sort_ar_labels = sort_ar_labels
        self.keys_to_split = {}
        self.put_label_last = {}
        self.search_multi_cache = {}
        self.splitter = splitter or " "
        self.ar_joiner = ar_joiner or " "

        self.alternation: str = self.create_alternation()
        self.pattern = self.keys_to_pattern()

        self.pattern_double = self.keys_to_pattern_double()

    def update_put_label_last(self, data: list[str] | set[str]) -> None:
        """Update the set of keys whose labels should be placed last in combinations."""
        self.put_label_last = data

    def _search(self, category: str) -> str:
        """
        Resolve a category string to its final formatted label using single- or double-key matching and template substitution.

        Parameters:
            category (str): The input category to match against single-key or adjacent double-key patterns.

        Returns:
            str: The formatted label produced by applying the matched template to the resolved key label, or an empty string if no matching key, label, or template is found.
        """
        logger.debug("$$$ start _search(): ")
        logger.debug(f"++++++++ _search {self.__class__.__name__} ++++++++ ")

        if self.formatted_data_ci.get(category):
            return self.formatted_data_ci[category]

        sport_key = self.match_key(category)

        if not sport_key:
            logger.debug(f"No sport key matched for {category=}")
            return ""

        sport_label = self.get_key_label(sport_key)
        if not sport_label:
            logger.debug(f'No sport label matched for sport key: "{sport_key}"')
            return ""

        logger.debug(f"sport label: {sport_label=}")

        template_label = self.get_template(sport_key, category)
        if not template_label:
            logger.debug(f'No template label matched for sport key: "{sport_key}" and {category=}')
            return ""

        logger.debug(f"template_label: {template_label=}")

        result = self.apply_pattern_replacement(template_label, sport_label)
        logger.debug(f"[] apply_pattern_replacement: {result=}")

        logger.debug(f"++++++++ end {self.__class__.__name__} ++++++++ ")

        return result

    def keys_to_pattern_double(self) -> Optional[re.Pattern[str]]:
        """
        Create a compiled case-insensitive regex that matches two adjacent keys separated by the configured splitter.

        Returns:
            re.Pattern[str] | None: A compiled regex that matches "key{splitter}key" (case-insensitive) for keys present in the instance, or `None` if there are no keys to match.
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
        Determine the canonical lowercased key that corresponds to the given category string.

        Matches the input against known single-key patterns or two-adjacent-key patterns; for two-key matches returns a combined key formed by the two parts and their separator. Leading/trailing and extra interior whitespace are ignored when matching.

        Parameters:
                category (str): Category text to match against known keys.

        Returns:
                matched_key (str): The canonical lowercased key if a match is found, otherwise an empty string.
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

    def apply_pattern_replacement(self, template_label: str, sport_label: Union[str, Dict[str, str]]) -> str:
        """
        Substitute placeholder tokens in a template with values from a mapping.

        Parameters:
                template_label (str): Template string containing placeholders in the form `{key}`.
                sport_label (Union[str, Dict[str, str]]): Mapping of placeholder names to replacement strings; if not a dict the template is returned unchanged.

        Returns:
                str: The template with placeholders replaced by their corresponding values, trimmed of surrounding whitespace.
        """
        logger.debug(f"[] apply_pattern_replacement: {template_label=}, ")
        logger.debug(f"[] apply_pattern_replacement: {sport_label=}, ")

        if not isinstance(sport_label, dict):
            logger.error("===> apply_pattern_replacement: sport_label not dict..")
            return template_label

        final_label = template_label

        if isinstance(sport_label, dict):
            for key, val in sport_label.items():
                if isinstance(val, str) and val:
                    final_label = final_label.replace(f"{{{key}}}", val)

        return final_label.strip()

    @functools.lru_cache(maxsize=5000)
    def create_label_from_keys(self, part1: str, part2: str):
        """
        Builds a mapping of Arabic labels for the two-part key combination.

        Constructs a dict whose keys are the union of subkeys found in both parts and whose values are the combined Arabic label for that subkey. Only subkeys that have labels in both parts are included. The produced label normally follows "first_label + ar_joiner + second_label"; if `part1` is present in `put_label_last` and `part2` is not, the order is switched to "second_label + ar_joiner + first_label". If `sort_ar_labels` is True, the two Arabic labels are alphabetically sorted before joining. When `log_multi_cache` is True, the resulting mapping is cached into `search_multi_cache` under the key "{part2} {part1}".

        Returns:
            dict: Mapping from subkey to combined Arabic label when both parts provide dict labels.
            str: Empty string if either part is missing or does not provide a dict of labels.

        if "upcoming" in self.put_label_last we using:
            "أفلام قادمة رعب يمنية instead of "أفلام رعب قادمة يمنية"
        """

        first_label = self.data_list_ci.get(part1)
        second_label = self.data_list_ci.get(part2)

        if not first_label or not second_label:
            logger.debug(f">>> create_label_from_keys: missing label for {part1=}, {part2=}")
            return ""

        if not isinstance(first_label, dict) or not isinstance(second_label, dict):
            logger.debug(f">>> create_label_from_keys: non-dict label for {part1=}, {part2=}")
            return ""

        keys_in_2_parts = list(first_label.keys()) + list(second_label.keys())

        logger.debug(f"!!! create_label_from_keys: found label for {part1=}, {part2=}")

        compound_data = {}

        for key in keys_in_2_parts:
            compound_data[key] = ""
            first_lab = first_label.get(key, "")
            second_lab = second_label.get(key, "")
            if first_lab and second_lab:
                label = f"{first_lab}{self.ar_joiner}{second_lab}"
                # logger.debug(f"!!! create_label_from_keys: label: {label}")

                if part1 in self.put_label_last and part2 not in self.put_label_last:
                    label = f"{second_lab}{self.ar_joiner}{first_lab}"

                if self.sort_ar_labels:
                    labels_sorted = sorted([first_lab, second_lab])
                    label = self.ar_joiner.join(labels_sorted)
                compound_data[key] = label
        if self.log_multi_cache:
            self.search_multi_cache[f"{part2} {part1}"] = compound_data

        return compound_data

    def get_key_label(self, sport_key: str) -> dict[str, str]:
        """
        Retrieve the Arabic label mapping for the given key, building or fetching combined labels for two-key entries when necessary.

        Returns:
            dict[str, str]: Mapping of attribute keys to Arabic label strings if found; empty string otherwise.
        """
        logger.debug(f"@@ get_key_label: {sport_key=}")

        result = self.data_list_ci.get(sport_key)
        if result:
            return result

        if self.search_multi_cache.get(sport_key.lower()):
            logger.debug(f"@@ get_key_label: found in search_multi_cache {sport_key=}")
            return self.search_multi_cache[sport_key.lower()]

        if sport_key in self.keys_to_split:
            part1, part2 = self.keys_to_split[sport_key]
            logger.debug(f"@@ get_key_label: found in keys_to_split {sport_key=}")
            return self.create_label_from_keys(part1, part2)

        return ""

    def replace_value_placeholder(self, label: str, value: Union[str, Dict[str, str]]) -> str:
        """
        Replace placeholders in a label string with corresponding values from a mapping.

        @param value: Mapping of placeholder names to replacement strings; keys are placeholder names (without braces). If `value` is not a mapping, the label is returned unchanged.
        @returns: The label with each `{key}` replaced by its corresponding string from `value`; unchanged if no replacements apply.
        """
        logger.debug(f"@@ replace_value_placeholder: {label=}, {value=}")

        if not isinstance(value, dict):
            return label

        final_label = label
        for key, val in value.items():
            if isinstance(val, str) and val:
                final_label = final_label.replace(f"{{{key}}}", val)

        return final_label
