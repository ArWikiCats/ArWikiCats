#!/usr/bin/python3
"""
"""
import re
from ....helps import logger
# from .model_data_time import YearFormatData
from .model_multi_data_base import MultiDataFormatterBaseHelpers


class FormatDataFrom:
    """
    A dynamic wrapper
    """

    def __init__(
        self,
        formatted_data: dict[str, str],
        key_placeholder: str,
        value_placeholder: str,
        search_callback: callable,
        match_key_callback: callable,
        fixing_callback: None | callable = None,
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
        result = self.formatted_data_ci.get(template_key, "")

        if not result:
            if template_key.startswith("category:"):
                template_key = template_key.replace("category:", "")
                result = self.formatted_data_ci.get(template_key, "")
            else:
                result = self.formatted_data_ci.get(f"category:{template_key}", "")

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
    """

    def __init__(
        self,
        country_bot: FormatDataFrom,
        year_bot: FormatDataFrom,
        search_first_part: bool = False,
        data_to_find: dict[str, str] | None = None,
        other_key_first: bool = False,
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""

        self.search_first_part = search_first_part
        self.country_bot = country_bot
        self.other_bot = year_bot
        self.data_to_find = data_to_find
        self.other_key_first = other_key_first
