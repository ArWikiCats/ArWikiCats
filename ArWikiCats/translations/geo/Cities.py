"""
Utilities for loading localized city label datasets.

This module consolidates Arabic translations for city names from several JSON
sources, applies manual overrides for edge cases, and exposes the resulting
datasets with compatibility aliases matching the legacy API.
"""

from __future__ import annotations

from ..helps import len_print
from ..utils import open_json_file

CITY_TRANSLATIONS_LOWER = open_json_file("cities/cities_full.json") or {}

len_print.data_len(
    "Cities.py",
    {
        "CITY_TRANSLATIONS_LOWER": CITY_TRANSLATIONS_LOWER,  # 10,788
    },
)


__all__ = [
    "CITY_TRANSLATIONS_LOWER",
]
