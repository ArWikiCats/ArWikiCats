#!/usr/bin/python3
"""
# from .india_2 import SECONDARY_REGION_TRANSLATIONS

"""

from ..helps import len_print
from ..utils import open_json_file


def _load_india_region_translations() -> dict[str, str]:
    """
    Builds a mapping from India district names to their localized labels.
    
    Returns:
        dict[str, str]: A dictionary where keys are normalized (lowercase) district names and
        "<name> district" variants; values are the district label in the source language for
        the plain name key, and the Arabic prefixed form "مقاطعة {label}" for the
        "<name> district" key.
    """
    index_labels: dict[str, str] = {}

    india_district_labels = open_json_file("geography/India_dd.json") or {}

    for district_name, district_label in india_district_labels.items():
        normalized_name = district_name.lower()
        index_labels[normalized_name] = district_label
        index_labels[f"{normalized_name} district"] = f"مقاطعة {district_label}"

    return index_labels


def _load_secondary_region_translations(data: dict[str, str]) -> dict[str, str]:
    CENTRAL_AFRICAN_PREFECTURE = data.get("CENTRAL_AFRICAN_PREFECTURE", {})
    DJIBOUTI_REGION = data.get("DJIBOUTI_REGION", {})
    EGYPT_GOVERNORATE = data.get("EGYPT_GOVERNORATE", {})
    GUATEMALA_DEPARTMENT = data.get("GUATEMALA_DEPARTMENT", {})
    MONGOLIA_PROVINCE = data.get("MONGOLIA_PROVINCE", {})
    index_labels: dict[str, str] = {}

    for governorate_name, governorate_label in EGYPT_GOVERNORATE.items():
        normalized_name = governorate_name.lower()
        index_labels[normalized_name] = governorate_label
        index_labels[f"{normalized_name} governorate"] = f"محافظة {governorate_label}"

    for region_name, region_label in DJIBOUTI_REGION.items():
        normalized_name = region_name.lower()
        index_labels[normalized_name] = region_label
        index_labels[f"{normalized_name} region"] = f"منطقة {region_label}"

    for department_name, department_label in GUATEMALA_DEPARTMENT.items():
        normalized_name = department_name.lower()
        index_labels[normalized_name] = department_label
        index_labels[f"{normalized_name} department"] = f"إدارة {department_label}"

    for province_name, province_label in MONGOLIA_PROVINCE.items():
        normalized_name = province_name.lower()
        index_labels[normalized_name] = province_label
        index_labels[f"{normalized_name} province"] = f"محافظة {province_label}"

    for prefecture_name, prefecture_label in CENTRAL_AFRICAN_PREFECTURE.items():
        normalized_name = prefecture_name.lower()
        index_labels[normalized_name] = prefecture_label
        index_labels[f"{normalized_name} prefecture"] = f"محافظة {prefecture_label}"

    return index_labels


data = open_json_file("geography/regions2.json") or {}
SECONDARY_REGION_TRANSLATIONS = _load_secondary_region_translations(data)
INDIA_REGION_TRANSLATIONS = _load_india_region_translations()

__all__ = [
    "SECONDARY_REGION_TRANSLATIONS",
    "INDIA_REGION_TRANSLATIONS",
]

len_print.data_len(
    "regions2.py",
    {
        "SECONDARY_REGION_TRANSLATIONS": SECONDARY_REGION_TRANSLATIONS,
        "INDIA_REGION_TRANSLATIONS": INDIA_REGION_TRANSLATIONS,
    },
)