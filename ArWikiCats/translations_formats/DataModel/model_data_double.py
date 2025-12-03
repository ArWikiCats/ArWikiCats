#!/usr/bin/python3
""" """

import functools
import re
from typing import Dict, Optional

# from ...helps.log import logger
import logging
logger = logging.getLogger(__name__)


class FormatDataDouble:
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
        # Store originals
        self.formatted_data = formatted_data
        self.data_list = data_list
        self.text_after = text_after
        self.text_before = text_before

        # Case-insensitive mirrors
        self.formated_data_ci: Dict[str, str] = {k.lower(): v for k, v in formatted_data.items()}
        self.data_list_ci: Dict[str, str] = {k.lower(): v for k, v in data_list.items()}

        self.value_placeholder = value_placeholder
        self.key_placeholder = key_placeholder
        self.data_pattern = ""
        self.pattern = None
        self.keys_to_split = {}
        self.put_label_last = {}

        self.data_pattern_double = ""
        self.pattern_double = None

        self.keys_to_pattern()

    def update_put_label_last(self, data: list[str, str]) -> None:
        self.put_label_last = data

    def add_formatted_data(self, key: str, value: str) -> None:
        """Add a key-value pair to the data_list."""
        self.formatted_data[key] = value
        self.formated_data_ci[key.lower()] = value

    def keys_to_pattern(self) -> Optional[re.Pattern[str]]:
        """Build a case-insensitive regex over lowercased keys of data_list."""
        if not self.data_list_ci:
            return None
        keys_sorted = sorted(self.data_list_ci.keys(), key=lambda x: -x.count(" "))

        # self.data_pattern = r"\b(" + "|".join(map(re.escape, keys_sorted)) + r")\b"
        alternation = "|".join(map(re.escape, keys_sorted))

        self.data_pattern = fr"(?<!\w)({alternation})(?!\w)"
        self.pattern = re.compile(self.data_pattern, re.I)

        self.data_pattern_double = fr"(?<!\w)({alternation}) ({alternation})(?!\w)"
        # (?<!\w)(action|drama) (action|drama)(?!\w)
        logger.debug(">> keys_to_pattern:", self.data_pattern_double)

        self.pattern_double = re.compile(self.data_pattern_double, re.I)

    @functools.lru_cache(maxsize=None)
    def match_key(self, category: str) -> str:
        """Return canonical lowercased key from data_list if found; else empty."""
        if not self.pattern:
            return ""

        # Normalize the category by removing extra spaces
        normalized_category = " ".join(category.split())
        logger.debug(f">> match_key: {normalized_category=}")

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

    @functools.lru_cache(maxsize=None)
    def normalize_category(self, category: str, sport_key: str) -> str:
        """Replace the matched sport key with the key placeholder."""

        # Normalize the category by removing extra spaces
        normalized_category = " ".join(category.split())

        normalized = re.sub(
            rf" {re.escape(sport_key)} ",
            f" {self.key_placeholder} ",
            f" {normalized_category.strip()} ",
            flags=re.IGNORECASE,
        )

        if self.text_before and f"{self.text_before}{self.key_placeholder}" in normalized:
            normalized = normalized.replace(f"{self.text_before}{self.key_placeholder}", self.key_placeholder)

        if self.text_after and f"{self.key_placeholder}{self.text_after}" in normalized:
            normalized = normalized.replace(f"{self.key_placeholder}{self.text_after}", self.key_placeholder)

        return normalized.strip()

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

    def get_template(self, sport_key: str, category: str) -> str:
        """Lookup template in a case-insensitive dict."""
        normalized = self.normalize_category(category, sport_key)
        logger.debug(f"normalized xoxo : {normalized}")
        # Case-insensitive key lookup
        return self.formated_data_ci.get(normalized.lower(), "")

    def get_template_ar(self, template_key: str) -> str:
        """Lookup template in a case-insensitive dict."""
        # Case-insensitive key lookup
        template_key = template_key.lower()
        result = self.formated_data_ci.get(template_key, "")

        if not result:
            if template_key.startswith("category:"):
                template_key = template_key.replace("category:", "")
                result = self.formated_data_ci.get(template_key, "")
            else:
                result = self.formated_data_ci.get(f"category:{template_key}", "")

        return result

    def create_label_from_keys(self, part1: str, part2: str):
        """
        if "upcoming" in self.put_label_last we using:
            "أفلام قادمة رعب يمنية inested of "أفلام رعب قادمة يمنية"
        """
        part1_label = self.data_list_ci.get(part1)
        part2_label = self.data_list_ci.get(part2)
        if not part1_label or not part2_label:
            return ""

        label = f"{part1_label} {part2_label}"

        if part1 in self.put_label_last or part1_label in self.put_label_last:
            label = f"{part2_label} {part1_label}"

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

        if sport_key in self.keys_to_split:
            part1, part2 = self.keys_to_split[sport_key]
            return self.create_label_from_keys(part1, part2)

        return ""

    def _search(self, category: str) -> str:
        """End-to-end resolution."""
        logger.debug("++++++++ start FormatData ++++++++ ")
        sport_key = self.match_key(category)

        if not sport_key:
            logger.debug(f'No sport key matched for {category=}')
            return ""

        sport_label = self.get_key_label(sport_key)
        if not sport_label:
            logger.debug(f'No sport label matched for sport key: "{sport_key}"')
            return ""

        template_label = self.get_template(sport_key, category)
        if not template_label:
            logger.debug(f'No template label matched for sport key: "{sport_key}" and {category=}')
            return ""

        result = self.apply_pattern_replacement(template_label, sport_label)
        logger.debug(f" {result=}")
        logger.debug("++++++++ end FormatData ++++++++ ")

        return result

    def replace_value_placeholder(self, label: str, value: str) -> str:
        # Replace placeholder
        return label.replace(self.value_placeholder, value)

    @functools.lru_cache(maxsize=None)
    def search(self, category: str) -> str:
        """Public wrapper around ``_search`` with caching."""
        return self._search(category)

    @functools.lru_cache(maxsize=None)
    def search_all(self, category: str) -> str:
        """Public wrapper around ``_search`` with caching."""
        return self._search(category)


def format_data_sample() -> None:
    """
    This function demonstrates how to use the FormatData class to format and transform data.
    It creates a mapping of template patterns to their localized versions and applies them.
    """
    # Define a dictionary of formatted patterns with placeholders

    # Template data with both nationality and sport placeholders
    formatted_data = {
        "{film_key} films": "أفلام {film_ar}",
        "{film_key} television commercials": "إعلانات تجارية تلفزيونية {film_ar}",
    }

    # film_keys_for_female
    data_list2 = {
        "action comedy": "حركة كوميدية",
        "action thriller": "إثارة حركة",
        "action": "حركة",
        "drama": "درامية",
        "upcoming": "قادمة",
        "horror": "رعب",
        "black": "أبيض سوداء",
        "black-and-white": "أبيض وأسود",
        "psychological horror": "رعب نفسي",
    }

    # Create an instance of the FormatDataDouble class with the formatted data and data list
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list2,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
    )

    put_label_last = {
        "low-budget",
        "christmas",
        "lgbtq-related",
        "upcoming",
    }
    bot.update_put_label_last(put_label_last)
    test_data = {
        "black-and-white films": "أفلام أبيض وأسود",
        "drama action television commercials": "إعلانات تجارية تلفزيونية درامية حركة",
    }
    # Test the formatting function with sample data
    for key, value in test_data.items():
        # Search for a specific pattern and get its localized version
        label = bot.search(key)
        # Verify if the result matches the expected output
        result = label == value
        print("search result: ", key, result)

    test_data_match = {
        "black-and-white films": "black-and-white",
        "drama action television commercials": "drama action",
    }
    # Test the formatting function with sample data
    for text, value in test_data_match.items():
        # Search for a specific pattern and get its localized version
        key = bot.match_key(text)
        # Verify if the result matches the expected output
        result = key == value
        print(f"match_key result: ({key})<>({value})", result)

    # Return the formatted label


if __name__ == "__main__":
    format_data_sample()

# match_key result: (black)<>(black-and-white) False
