"""Regional translation tables used across the geo modules."""

from __future__ import annotations

from ..helps import len_print
from ..utils import open_json_file


def load_regions_data(data: dict[str, str]) -> dict[str, str]:
    """
    Builds a consolidated mapping of region names and generated region-type variants to Arabic labels.
    
    The input `data` is expected to contain region-group mappings (e.g., "PRIMARY_REGION", "PERU_REGION", "SRI_LANKA_DISTRICT", "ALGERIA_PROVINCE", "VENEZUELA_STATE", "ECUADOR_PROVINCE", "LEGACY_UK_COUNTY", "UK_COUNTY"). This function merges primary and UK county entries and augments the mapping with generated keys for specific countries:
    - Peru: adds "region", "province", and "district" variants.
    - Sri Lanka: adds "district" variant.
    - Algeria: adds "province" variant.
    - Venezuela: adds "(state)" variant.
    - Ecuador: adds "province" variant.
    
    Parameters:
        data (dict[str, dict[str, str]]): Source mapping from region-group names to mappings of region name -> label.
    
    Returns:
        dict[str, str]: A mapping where keys are region names or generated region-type variants (for example "Lima province" or "Colombo district") and values are their corresponding Arabic labels.
    """
    ALGERIA_PROVINCE = data.get("ALGERIA_PROVINCE", {})
    ECUADOR_PROVINCE = data.get("ECUADOR_PROVINCE", {})
    LEGACY_UK_COUNTY = data.get("LEGACY_UK_COUNTY", {})
    UK_COUNTY = data.get("UK_COUNTY", {})
    SRI_LANKA_DISTRICT = data.get("SRI_LANKA_DISTRICT", {})
    VENEZUELA_STATE = data.get("VENEZUELA_STATE", {})
    PERU_REGION = data.get("PERU_REGION", {})

    PRIMARY_REGION = data.get("PRIMARY_REGION", {})

    index_labels: dict[str, str] = PRIMARY_REGION | LEGACY_UK_COUNTY | UK_COUNTY

    for region_name, region_label in PERU_REGION.items():
        index_labels[region_name] = region_label
        index_labels[f"{region_name} region"] = f"إقليم {region_label}"
        index_labels[f"{region_name} province"] = f"مقاطعة {region_label}"
        index_labels[f"{region_name} district"] = f"مديرية {region_label}"

    for district_name, district_label in SRI_LANKA_DISTRICT.items():
        index_labels[district_name] = district_label
        index_labels[f"{district_name} district"] = f"مديرية {district_label}"

    for province_name, province_label in ALGERIA_PROVINCE.items():
        index_labels[province_name] = province_label
        index_labels[f"{province_name} province"] = f"ولاية {province_label}"

    for state_name, state_label in VENEZUELA_STATE.items():
        index_labels[state_name] = state_label
        index_labels[f"{state_name} (state)"] = f"ولاية {state_label}"

    for province_name, province_label in ECUADOR_PROVINCE.items():
        index_labels[province_name] = province_label
        index_labels[f"{province_name} province"] = f"مقاطعة {province_label}"

    return index_labels


data = open_json_file("geography/regions.json") or {}
MAIN_REGION_TRANSLATIONS = load_regions_data(data)

__all__ = [
    "MAIN_REGION_TRANSLATIONS",
]

len_print.data_len(
    "regions.py",
    {
        "MAIN_REGION_TRANSLATIONS": MAIN_REGION_TRANSLATIONS,
    },
)