#!/usr/bin/python3
"""Base class for FormatData classes with shared functionality."""

import functools
import re
from typing import Any, Dict, Optional, Union

from ...helps.log import logger


class FormatDataBase:
    """Base class containing shared functionality for all FormatData classes."""

    def __init__(
        self,
        formatted_data: Dict[str, str],
        data_list: Dict[str, Any],
        key_placeholder: str = "xoxo",
        text_after: str = "",
        text_before: str = "",
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""
        # Store originals
        self.formatted_data = formatted_data
        self.data_list = data_list
        self.text_after = text_after
        self.text_before = text_before

        # Case-insensitive mirrors
        self.formatted_data_ci: Dict[str, str] = {k.lower(): v for k, v in formatted_data.items()}
        self.data_list_ci: Dict[str, Any] = {k.lower(): v for k, v in data_list.items()}

        self.key_placeholder = key_placeholder
        self.alternation: str = None
        self.pattern: Optional[re.Pattern[str]] = None
        self.pattern_double: Optional[re.Pattern[str]] = None

    def add_formatted_data(self, key: str, value: str) -> None:
        """Add a key-value pair to the data_list."""
        self.formatted_data[key] = value
        self.formatted_data_ci[key.lower()] = value

    def create_alternation(self) -> str:
        """Create regex alternation from data_list_ci keys."""
        if not self.data_list_ci:
            return ""

        if len(self.data_list_ci) > 1000:
            print(f">keys_to_pattern(): len(new_pattern keys) = {len(self.data_list_ci):,}")

        # to fix bug that selected "black" instead of "black-and-white"
        keys_sorted = sorted(
            self.data_list_ci.keys(),
            key=lambda k: (-k.count(" "), -len(k))
        )

        return "|".join(map(re.escape, keys_sorted))

    def keys_to_pattern(self) -> Optional[re.Pattern[str]]:
        """
        Build a case-insensitive regex over lowercased keys of data_list.
        """
        if not self.data_list_ci:
            return None

        if self.alternation is None:
            self.alternation = self.create_alternation()

        data_pattern = fr"(?<!\w)({self.alternation})(?!\w)"
        return re.compile(data_pattern, re.I)

    @functools.lru_cache(maxsize=None)
    def match_key(self, category: str) -> str:
        """Return canonical lowercased key from data_list if found; else empty."""
        if not self.pattern:
            return ""
        # Normalize the category by removing extra spaces
        normalized_category = " ".join(category.split())
        logger.debug(f">> match_key: {normalized_category=}")

        # TODO: check this
        if self.data_list_ci.get(normalized_category.lower()):
            return normalized_category.lower()

        match = self.pattern.search(f" {normalized_category} ")
        return match.group(1).lower() if match else ""

    def handle_texts_before_after(self, normalized: str) -> str:
        """Handle text before and after the key placeholder."""
        if not self.text_before and not self.text_after:
            return normalized

        logger.debug(f"handle_texts_before_after: {normalized=}")

        # no need for further processing
        # (text_before="the ") but key: ("the {nat_en} actors") already in formatted_data_ci so no need to replace

        if self.formatted_data_ci.get(normalized.strip(), ""):
            logger.debug(f"handle_texts_before_after: found directly {normalized=} in formatted_data_ci")
            return normalized

        if self.text_before:
            if f"{self.text_before}{self.key_placeholder}" in normalized:
                normalized = normalized.replace(f"{self.text_before}{self.key_placeholder}", self.key_placeholder)

            # no need for further processing
            # (text_after=" people") but key: ("{nat_en} people actors") already in formatted_data_ci so no need to replace
            if self.formatted_data_ci.get(normalized.strip(), ""):
                return normalized

        if self.text_after:
            if f"{self.key_placeholder}{self.text_after}" in normalized:
                normalized = normalized.replace(f"{self.key_placeholder}{self.text_after}", self.key_placeholder)

        return normalized

    @functools.lru_cache(maxsize=None)
    def normalize_category(self, category: str, sport_key: str) -> str:
        """Replace the matched sport key with the key placeholder."""
        # Normalize the category by removing extra spaces
        normalized_category = " ".join(category.split())

        normalized = re.sub(
            rf"(?<!\w){re.escape(sport_key)}(?!\w)",
            f"{self.key_placeholder}",
            f" {normalized_category.strip()} ",
            flags=re.IGNORECASE,
        )

        normalized = self.handle_texts_before_after(normalized)
        return normalized.strip()

    def normalize_category_with_key(self, category: str) -> tuple[str, str]:
        """
        Normalize nationality placeholders within a category string.

        Example:
            normal:
                category:"Yemeni national football teams", result: "natar national football teams"
            model_data_double:
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
        return self.formatted_data_ci.get(normalized.lower(), "")

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

    def get_key_label(self, sport_key: str) -> Any:
        """Return the Arabic label mapped to the provided key if present."""
        return self.data_list_ci.get(sport_key)

    def _search(self, category: str) -> str:
        """End-to-end resolution."""
        logger.debug("><><><>< start _search(): ")
        logger.debug(f"++++++++ _search {self.__class__.__name__} ++++++++ ")

        if self.formatted_data_ci.get(category):
            return self.formatted_data_ci[category]

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

        logger.debug(f"++++++++ end {self.__class__.__name__} ++++++++ ")

        return result

    def apply_pattern_replacement(self, template_label: str, sport_label: Any) -> str:
        """Replace value placeholder once template is chosen. Override in subclasses."""
        raise NotImplementedError("Subclasses must implement apply_pattern_replacement")

    def replace_value_placeholder(self, label: str, value: Any) -> str:
        """Replace placeholder. Override in subclasses if needed."""
        raise NotImplementedError("Subclasses must implement replace_value_placeholder")

    @functools.lru_cache(maxsize=None)
    def search(self, category: str) -> str:
        """Public wrapper around ``_search`` with caching."""
        return self._search(category)

    @functools.lru_cache(maxsize=None)
    def create_label(self, category: str) -> str:
        """Public wrapper around ``_search`` with caching."""
        return self._search(category)

    @functools.lru_cache(maxsize=None)
    def search_all(self, category: str) -> str:
        """Public wrapper around ``_search`` with caching."""
        return self._search(category)

    def search_all_category(self, category: str) -> str:
        logger.debug("--"*20)
        logger.debug(">> search_all_category start")
        normalized_category = category.lower().replace("category:", "")

        result = self._search(normalized_category)

        if result and category.lower().startswith("category:"):
            result = "تصنيف:" + result
        logger.debug(">> search_all_category end")
        return result
