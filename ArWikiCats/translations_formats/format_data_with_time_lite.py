#!/usr/bin/python3
"""
Classes for formatting
"""

import functools
import re
from typing import Dict

from ..helps.log import logger
from .format_data import FormatData
from ..new.time_to_arabic import (
    convert_time_to_arabic,
    match_time_en_first,
)

YEAR_PARAM = "{year1}"
COUNTRY_PARAM = "{country1}"


class FormatYearCountryData:
    """
    Works exactly like FormatMultiData, but for:
        - Country detection (same as nationality)
        - Year detection (instead of sport)
    """

    def __init__(
        self,
        formatted_data: Dict[str, str],
        countries_data: Dict[str, str],
        key_placeholder: str = COUNTRY_PARAM,
        value_placeholder: str = COUNTRY_PARAM,
        key2_placeholder: str = YEAR_PARAM,
        value2_placeholder: str = YEAR_PARAM,
    ) -> None:

        self.formatted_data = formatted_data

        self.key_country = key_placeholder
        self.val_country = value_placeholder

        self.key_year = key2_placeholder
        self.val_year = value2_placeholder

        # Normalize country dictionary to lower-case
        self.countries_data = {k.lower(): v for k, v in countries_data.items()}

    # ------------------------------------------------------
    # 1) COUNTRY MATCHING (like nat_bot)
    # ------------------------------------------------------
    def match_country(self, text: str) -> str:
        text = text.lower()
        for key in self.countries_data:
            if key in text:
                return key
        return ""

    def normalize_nat_label(self, category: str) -> str:
        key = self.match_country(category)
        if not key:
            return category

        pattern = re.escape(key)
        return re.sub(pattern, self.key_country, category, flags=re.IGNORECASE)

    def get_country_ar(self, key: str) -> str:
        return self.countries_data.get(key.lower(), "")

    # ------------------------------------------------------
    # 2) YEAR MATCHING (instead of sport)
    # ------------------------------------------------------
    def match_year(self, text: str) -> str:
        return match_time_en_first(text)

    def normalize_other_label(self, category: str) -> str:
        year = self.match_year(category)
        if not year:
            return category

        pattern = re.escape(year)
        return re.sub(pattern, self.key_year, category, flags=re.IGNORECASE)

    # ------------------------------------------------------
    # 3) Normalize Country + Year to template key
    # ------------------------------------------------------
    def normalize_both(self, category: str) -> str:
        category = " ".join(category.split())
        category = self.normalize_nat_label(category)
        category = self.normalize_other_label(category)
        return category

    # ------------------------------------------------------
    # 4) Create Arabic label (replace placeholders)
    # ------------------------------------------------------
    @functools.lru_cache(maxsize=1000)
    def create_label(self, category: str) -> str:
        template_key = self.normalize_both(category)

        if template_key not in self.formatted_data:
            return ""

        template_ar = self.formatted_data[template_key]

        # Extract real values again
        year_en = self.match_year(category)
        country_en = self.match_country(category)

        if not year_en or not country_en:
            return ""

        country_ar = self.get_country_ar(country_en)
        if not country_ar:
            return ""

        # Convert year to Arabic
        year_ar = convert_time_to_arabic(year_en)

        # Replace placeholders
        label = (
            template_ar
            .replace(self.val_country, country_ar)
            .replace(self.val_year, year_ar)
        )

        logger.debug(f"create_label: {category=} → {label=}")
        return label
