#!/usr/bin/python3
""" """

import functools
import re
from typing import Dict, Optional

from ..helps.log import logger


class FormatData:
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
        self.pattern = self.keys_to_pattern()

    def keys_to_pattern(self) -> Optional[re.Pattern[str]]:
        """Build a case-insensitive regex over lowercased keys of data_list."""
        if not self.data_list_ci:
            return None
        keys_sorted = sorted(self.data_list_ci.keys(), key=lambda x: -x.count(" "))

        # self.data_pattern = r"\b(" + "|".join(map(re.escape, keys_sorted)) + r")\b"
        alternation = "|".join(map(re.escape, keys_sorted))

        self.data_pattern = fr"(?<!\w)({alternation})(?!\w)"

        return re.compile(self.data_pattern, re.I)

    @functools.lru_cache(maxsize=None)
    def match_key(self, category: str) -> str:
        """Return canonical lowercased key from data_list if found; else empty."""
        if not self.pattern:
            return ""
        # Normalize the category by removing extra spaces
        normalized_category = " ".join(category.split())
        match = self.pattern.search(f" {normalized_category} ")
        return match.group(1).lower() if match else ""

    @functools.lru_cache(maxsize=None)
    def apply_pattern_replacement(self, template_label: str, sport_label: str) -> str:
        """Replace value placeholder once template is chosen."""
        final_label = template_label.replace(self.value_placeholder, sport_label)

        if self.value_placeholder not in final_label:
            return final_label

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

    def normalize_category_with_key(self, category) -> tuple[str, str]:
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

    def get_template(self, sport_key: str, category: str) -> str:
        """Lookup template in a case-insensitive dict."""
        normalized = self.normalize_category(category, sport_key)
        logger.debug(f"normalized xoxo : {normalized}")
        # Case-insensitive key lookup
        return self.formated_data_ci.get(normalized.lower(), "")

    def get_template_ar(self, template_key: str) -> str:
        """Lookup template in a case-insensitive dict."""
        # Case-insensitive key lookup
        return self.formated_data_ci.get(template_key.lower(), "")

    def get_key_label(self, sport_key: str) -> str:
        """Return the Arabic label mapped to the provided key if present."""
        return self.data_list_ci.get(sport_key)

    def _search(self, category: str) -> str:
        """End-to-end resolution."""
        logger.debug("++++++++ start FormatData ++++++++ ")
        sport_key = self.match_key(category)

        if not sport_key:
            logger.debug(f'No sport key matched for category: "{category}"')
            return ""

        sport_label = self.get_key_label(sport_key)
        if not sport_label:
            logger.debug(f'No sport label matched for sport key: "{sport_key}"')
            return ""

        template_label = self.get_template(sport_key, category)
        if not template_label:
            logger.debug(f'No template label matched for sport key: "{sport_key}" and category: "{category}"')
            return ""

        result = self.apply_pattern_replacement(template_label, sport_label)
        logger.debug(f"result: {result}")
        logger.debug("++++++++ end FormatData ++++++++ ")

        return result

    @functools.lru_cache(maxsize=None)
    def search(self, category: str) -> str:
        """Public wrapper around ``_search`` with caching."""
        return self._search(category)

    def replace_value_placeholder(self, label, value) -> str:
        # Replace placeholder
        return label.replace(self.value_placeholder, value)


def format_data_sample() -> bool:
    """
    This function demonstrates how to use the FormatData class to format and transform data.
    It creates a mapping of template patterns to their localized versions and applies them.
    """
    # Define a dictionary of formatted patterns with placeholders
    formatted_data = {
        "{sport}": "{sport_label}",
        "{sport} managers": "مدراء {sport_label}",
        "{sport} coaches": "مدربو {sport_label}",
        "{sport} people": "أعلام {sport_label}",
        "{sport} playerss": "لاعبو {sport_label}",
        "{sport} players": "لاعبو {sport_label}",
        "men's {sport} matches": "مباريات {sport_label} رجالية",
        "men's {sport} navigational boxes": "صناديق تصفح {sport_label} رجالية",
        "men's {sport} lists": "قوائم {sport_label} رجالية",
        "amateur {sport} home stadiums": "ملاعب {sport_label} للهواة",
        "amateur {sport} templates": "قوالب {sport_label} للهواة",
        "amateur {sport} rivalries": "دربيات {sport_label} للهواة",
        "amateur {sport} receivers": "مستقبلو {sport_label} للهواة",
        "amateur {sport} wide receivers": "مستقبلون واسعون {sport_label} للهواة",
        "amateur {sport} tackles": "مصطدمو {sport_label} للهواة",
        "amateur {sport} utility players": "لاعبو مراكز متعددة {sport_label} للهواة",
    }

    # Define a dictionary with actual sport name mappings
    data_list = {
        "gridiron football": "كرة قدم أمريكية شمالية",
        "american football": "كرة قدم أمريكية",
        "canadian football": "كرة قدم كندية",
        "wheelchair australian rules football": "كرة قدم أسترالية على كراسي متحركة",
        "volleyball racing": "سباق كرة طائرة",
        "wheelchair volleyball": "كرة طائرة على كراسي متحركة",
        "middle-distance running racing": "سباق ركض مسافات متوسطة",
        "wheelchair gaelic football": "كرة قدم غالية على كراسي متحركة",
        "kick boxing racing": "سباق كيك بوكسينغ",
        "wheelchair cycling road race": "سباق دراجات على الطريق على كراسي متحركة",
        "wheelchair auto racing": "سباق سيارات على كراسي متحركة",
    }

    # Create a FormatData instance with the defined patterns and mappings
    bot = FormatData(formatted_data, data_list, key_placeholder="{sport}", value_placeholder="{sport_label}")

    # Search for a specific pattern and get its localized version
    label = bot.search("american football players")
    # Verify if the result matches the expected output
    result = label == "لاعبو كرة قدم أمريكية"

    # Return the formatted label
    return result
