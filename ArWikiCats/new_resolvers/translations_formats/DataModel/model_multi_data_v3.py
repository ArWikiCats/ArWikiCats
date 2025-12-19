#!/usr/bin/python3
"""
Provides classes for formatting template-driven translation labels.
- format_multi_data: Handles complex formatting involving two sets of data lists (e.g., nationality and sport).

test at tests.translations_formats.test_format_2_data.py
"""
import re
from .model_multi_data import MultiDataFormatterBase
from .model_data_time import YearFormatData
from .model_multi_data_base import MultiDataFormatterBaseHelpers


class V3Formats:
    """
    A dynamic wrapper that allows FormatData to handle year patterns.
    It mimics FormatData behavior but for time values extracted by regex.
    """

    def __init__(
        self,
        formatted_data: dict[str, str],
        bot: MultiDataFormatterBase,
        key_placeholder: str,
        value_placeholder: str,
    ) -> None:
        self.bot = bot
        self.key_placeholder = key_placeholder
        self.value_placeholder = value_placeholder
        # Case-insensitive dict for formatted data
        self.formatted_data_ci = {k.lower(): v for k, v in formatted_data.items()}

    def match_key(self, text: str) -> str:
        """Extract English year/decade and return it as the key."""
        return text.replace("{year1}", "").strip()

    def get_key_label(self, key: str) -> str:
        """Convert the year expression to Arabic."""
        return self.bot.search_all(key)

    def normalize_category(self, text: str, key: str) -> str:
        """Replace matched year with placeholder."""
        if not key:
            return text
        # print(f"Normalizing: {text} with key: {key}")
        return re.sub(re.escape(key), self.key_placeholder, text, flags=re.IGNORECASE)

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
        result = label.replace(self.value_placeholder, value)
        return result

    def search(self, text: str) -> str:
        """place holders"""
        return self.bot.search_all(text)

    def get_template_ar(self, template_key: str) -> str:
        """Lookup template in a case-insensitive dict."""
        # Case-insensitive key lookup
        template_key = template_key.lower()
        result = self.formatted_data_ci.get(template_key, "")

        if not result:
            if template_key.startswith("category:"):
                template_key = template_key.replace("category:", "")
                result = self.formatted_data_ci.get(template_key, "")
            else:
                result = self.formatted_data_ci.get(f"category:{template_key}", "")

        return result


class MultiDataFormatterBaseYearV3(MultiDataFormatterBaseHelpers):
    """
    """

    def __init__(
        self,
        country_bot: V3Formats,
        other_bot: YearFormatData,
        search_first_part: bool = False,
        data_to_find: dict[str, str] | None = None,
        other_key_first: bool = False,
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""

        self.search_first_part = search_first_part
        self.country_bot = country_bot
        self.other_bot = other_bot
        self.data_to_find = data_to_find
        self.other_key_first = other_key_first
