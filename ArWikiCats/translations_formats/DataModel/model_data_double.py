#!/usr/bin/python3
""" """

import functools
import re
from typing import Dict, Optional

from ...helps.log import logger
from .model_data_base import FormatDataBase


class FormatDataDouble(FormatDataBase):
    def __init__(
        self,
        formatted_data: Dict[str, str],
        data_list: Dict[str, str],
        key_placeholder: str = "xoxo",
        value_placeholder: str = "xoxo",
        text_after: str = "",
        text_before: str = "",
    ):
        """Prepare helpers for matching and formatting template-driven labels."""
        super().__init__(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder=key_placeholder,
            text_after=text_after,
            text_before=text_before,
        )
        self.value_placeholder = value_placeholder
        self.keys_to_split = {}
        self.put_label_last = {}
        self.search_multi_cache = {}

        self.data_pattern_double = ""
        self.pattern_double = None

        self.keys_to_pattern()

    def update_put_label_last(self, data: list[str] | set[str]) -> None:
        self.put_label_last = data

    def keys_to_pattern(self) -> Optional[re.Pattern[str]]:
        """Build a case-insensitive regex over lowercased keys of data_list."""
        if not self.data_list_ci:
            return None

        # to fix bug that selected "black" instead of "black-and-white"
        keys_sorted = sorted(
            self.data_list_ci.keys(),
            key=lambda k: (-k.count(" "), -len(k))
        )

        alternation = "|".join(map(re.escape, keys_sorted))

        self.data_pattern = fr"(?<!\w)({alternation})(?!\w)"
        self.pattern = re.compile(self.data_pattern, re.I)

        self.data_pattern_double = fr"(?<!\w)({alternation}) ({alternation})(?!\w)"
        # logger.debug(f">> keys_to_pattern: {self.data_pattern_double}")

        self.pattern_double = re.compile(self.data_pattern_double, re.I)

    @functools.lru_cache(maxsize=None)
    def match_key(self, category: str) -> str:
        """Return canonical lowercased key from data_list if found; else empty."""
        if not self.pattern:
            return ""

        # Normalize the category by removing extra spaces
        normalized_category = " ".join(category.split())
        logger.debug(f">> match_key: {normalized_category=}")

        if self.data_list_ci.get(normalized_category.lower()):
            return normalized_category.lower()

        match = self.pattern_double.search(f" {normalized_category} ")
        if match:
            first_key = match.group(1).lower()
            second_key = match.group(2).lower()
            result = f"{first_key} {second_key}"
            self.keys_to_split[result] = [first_key, second_key]
            return result

        match2 = self.pattern.search(f" {normalized_category} ")
        return match2.group(1).lower() if match2 else ""

    @functools.lru_cache(maxsize=None)
    def apply_pattern_replacement(self, template_label: str, sport_label: str) -> str:
        """Replace value placeholder once template is chosen."""
        final_label = template_label.replace(self.value_placeholder, sport_label)

        if self.value_placeholder not in final_label:
            return final_label.strip()

        return ""

    def normalize_category_with_key(self, category: str) -> tuple[str, str]:
        """
        Normalize nationality placeholders within a category string.

        Example:
            category='{nat_en} action drama films', key='action drama', result='{nat_en} {film_key} films'
        """
        key = self.match_key(category)
        result = ""
        if key:
            result = self.normalize_category(category, key)
            logger.debug(f">>> normalize_category_with_key: {category=}, {key=}, {result=}")

        return key, result

    @functools.lru_cache(maxsize=None)
    def create_label_from_keys(self, part1: str, part2: str):
        """
        if "upcoming" in self.put_label_last we using:
            "أفلام قادمة رعب يمنية inested of "أفلام رعب قادمة يمنية"
        """

        first_label = self.data_list_ci.get(part1)
        second_label = self.data_list_ci.get(part2)

        if not first_label or not second_label:
            return ""

        label = f"{first_label} {second_label}"

        if part1 in self.put_label_last and part2 not in self.put_label_last:
            label = f"{second_label} {first_label}"

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
        return label.replace(self.value_placeholder, value)
