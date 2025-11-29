#!/usr/bin/python3
""" """

import re
from ..new.time_to_arabic import (
    convert_time_to_arabic,
    match_time_en_first,
)


class YearFormatData:
    """
    A dynamic wrapper that allows FormatData to handle year patterns.
    It mimics FormatData behavior but for time values extracted by regex.
    """

    def __init__(self, key_placeholder: str, value_placeholder: str):
        self.key_placeholder = key_placeholder
        self.value_placeholder = value_placeholder

    def match_key(self, text: str) -> str:
        """Extract English year/decade and return it as the key."""
        result = match_time_en_first(text)
        return result if result else ""

    def get_key_label(self, key: str) -> str:
        """Convert the year expression to Arabic."""
        if not key:
            return ""
        return convert_time_to_arabic(key)

    def normalize_category(self, text: str, key: str) -> str:
        """Replace matched year with placeholder."""
        if not key:
            return text
        return re.sub(
            re.escape(key), self.key_placeholder, text, flags=re.IGNORECASE
        )

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

    def fixing(self, text: str) -> str:
        """Fix text."""
        text = re.sub(r"(انحلالات|تأسيسات)\s*سنة\s*(عقد|القرن|الألفية)", r"\g<1> \g<2>", text)
        return text

    def replace_value_placeholder(self, label, value) -> str:
        # Replace placeholder
        result = label.replace(self.value_placeholder, value)
        result = self.fixing(result)
        return result
