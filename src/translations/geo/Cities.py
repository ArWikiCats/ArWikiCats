"""Utilities for loading localized city label datasets.

This module consolidates Arabic translations for city names from several JSON
sources, applies manual overrides for edge cases, and exposes the resulting
datasets with compatibility aliases matching the legacy API.
"""

from __future__ import annotations

import sys

from ...helps import len_print
from ..utils.json_dir import open_json

CITY_TRANSLATIONS = open_json("geo/all_cities.json") or {}
CITY_TRANSLATIONS_SUPPLEMENT = open_json("geo/Cities_tab2.json") or {}
CITY_LABEL_PATCHES = open_json("geo/yy2.json") or {}
CITY_OVERRIDES_ADDITIONAL = open_json("geo/CITY_OVERRIDES.json") or {}

# merge CITY_TRANSLATIONS and CITY_TRANSLATIONS_SUPPLEMENT
CITY_TRANSLATIONS |= CITY_TRANSLATIONS_SUPPLEMENT

del CITY_TRANSLATIONS_SUPPLEMENT

CITY_OVERRIDES = {"Tubas": "طوباس", "Tulkarm": "طولكرم", "Nablus": "نابلس", "Zion": "صهيون", "Chords Bridge": "جسر القدس الصاري المعلق", "Charles Warren": "تشارلز وارن", "Burj al Luq Luq Community Centre and Society": "جمعية مركز برج اللقلق المجتمعية", "Bethlehem Association": "منظمة بيت لحم", "Beitar Jerusalem F.C.": "بيتار القدس", "Beitar Illit": "بيتار عيليت", "Hanunu": "هانونو"}

CITY_OVERRIDES.update(CITY_OVERRIDES_ADDITIONAL)

# merge CITY_TRANSLATIONS and CITY_OVERRIDES
CITY_TRANSLATIONS |= CITY_OVERRIDES

CITY_TRANSLATIONS_LOWER = {x.lower(): xar for x, xar in CITY_TRANSLATIONS.items()}

# with open(f"{Dir2}/jsons/all_cities.json", "w", encoding="utf-8") as f:
#     json.dump(CITY_TRANSLATIONS, f, indent=2, ensure_ascii=False)

memory_sizes = {
    "CITY_TRANSLATIONS": CITY_TRANSLATIONS,
    "CITY_LABEL_PATCHES": CITY_LABEL_PATCHES,
}

len_print.data_len("cities.py", memory_sizes)

__all__ = [
    "CITY_TRANSLATIONS",
    "CITY_LABEL_PATCHES",
    "CITY_TRANSLATIONS_LOWER",
]
