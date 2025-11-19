#!/usr/bin/python3
"""
Nationality system with full refactoring and full type hints.
All comments are in English only.
"""

from __future__ import annotations

from typing import Any, Dict, List, Tuple, TypedDict

from ...helps import len_print
from ..utils.json_dir import open_json_file

# =====================================================================
# Type aliases
# =====================================================================


class NationalityEntry(TypedDict):
    """Represents one nationality block with all fields always present as strings."""

    men: str
    mens: str
    women: str
    womens: str
    en: str
    ar: str


AllNatDict = Dict[str, NationalityEntry]
LookupTable = Dict[str, str]


# =====================================================================
# Section 1: Load and prepare JSON sources
# =====================================================================


def load_sources() -> Dict[str, NationalityEntry]:
    """
    Load nationality JSON data and merge All_Nat_o + uu_nats + Sub_Nat.
    Ensures all entries follow the NationalityEntry structure (string values only).
    """

    raw_all_nat_o: Dict[str, Any] = open_json_file("All_Nat_o") or {}
    raw_uu_nats: Dict[str, Any] = open_json_file("uu_nats") or {}
    raw_sub_nat: Dict[str, Any] = open_json_file("Sub_Nat") or {}

    # Fix hindustani
    if raw_uu_nats.get("hindustani"):
        raw_uu_nats["hindustan"] = raw_uu_nats["hindustani"]

    # Merge JSONs into All_Nat_o
    for key, val in raw_uu_nats.items():
        raw_all_nat_o[key] = val

    for key, val in raw_sub_nat.items():
        raw_all_nat_o[key] = val

    # Cleanup temporary JSON sources
    del raw_uu_nats
    del raw_sub_nat

    # Convert everything to NationalityEntry ensuring all fields exist
    normalized: Dict[str, NationalityEntry] = {}

    for key, val in raw_all_nat_o.items():
        # Build guaranteed structure
        entry: NationalityEntry = {
            "men": val.get("men", "") if isinstance(val, dict) else "",
            "mens": val.get("mens", "") if isinstance(val, dict) else "",
            "women": val.get("women", "") if isinstance(val, dict) else "",
            "womens": val.get("womens", "") if isinstance(val, dict) else "",
            "en": val.get("en", "") if isinstance(val, dict) else "",
            "ar": val.get("ar", "") if isinstance(val, dict) else "",
        }

        normalized[key] = entry

    return normalized


# =====================================================================
# Section 2: Normalize aliases
# =====================================================================


def normalize_aliases(all_nat_o: Dict[str, NationalityEntry]) -> Dict[str, NationalityEntry]:
    """
    Apply alias equivalence and one-off corrections.
    Ensures the resulting dictionary keys all map to NationalityEntry.
    """

    alias_map: Dict[str, str] = {
        "equatorial guinean": "equatoguinean",
        "south ossetian": "ossetian",
        "republic-of-the-congo": "the republic of the congo",
        "republic of the congo": "the republic of the congo",
        "democratic republic of the congo": "democratic republic of the congo",
        "democratic-republic-of-the-congo": "democratic republic of the congo",
        "dominican republic": "dominican republic",
        "caribbean": "caribbeans",
        "russians": "russian",
        "bangladesh": "bangladeshi",
        "yemenite": "yemeni",
        "arabian": "arab",
        "jewish": "jews",
        "bosnia and herzegovina": "bosnian",
        "turkish cypriot": "northern cypriot",
        "somali": "somalian",
        "saudi": "saudiarabian",
        "canadians": "canadian",
        "salvadoran": "salvadorean",
        "ivoirian": "ivorian",
        "the republic-of ireland": "irish",
        "trinidadian": "trinidad and tobago",
        "trinidadians": "trinidad and tobago",
        "comoran": "comorian",
        "slovakian": "slovak",
        "emirian": "emirati",
        "austro-hungarian": "austrianhungarian",
        "emiri": "emirati",
        "roman": "romanian",
        "ancient-roman": "ancient-romans",
        "ancient romans": "ancient-romans",
        "mosotho": "lesotho",
        "singapore": "singaporean",
        "luxembourg": "luxembourgish",
        "kosovar": "kosovan",
        "argentinean": "argentine",
        "argentinian": "argentine",
        "lao": "laotian",
        "israeli": "israeli11111",
        "slovene": "slovenian",
        "vietnamesei": "vietnamese",
        "nepali": "nepalese",
    }

    # Apply simple alias redirection
    for alias, target in alias_map.items():
        if target in all_nat_o:
            all_nat_o[alias] = all_nat_o[target]

    # Special defined nationality
    all_nat_o["papua new guinean x "] = {
        "men": "غيني",
        "mens": "غينيون",
        "women": "غينية",
        "womens": "غينيات",
        "en": "papua new guinea",
        "ar": "بابوا غينيا الجديدة",
    }

    # Handle Georgia (country)
    if "georgian" in all_nat_o:
        ge = all_nat_o["georgian"]
        all_nat_o["georgia (country)"] = {
            "men": ge["men"],
            "mens": ge["mens"],
            "women": ge["women"],
            "womens": ge["womens"],
            "en": "georgia (country)",
            "ar": ge["ar"],
        }

    # Add southwest asian nationality
    all_nat_o["southwest asian"] = {
        "men": "جنوب غرب آسيوي",
        "mens": "جنوبيون غربيون آسيويين",
        "women": "جنوب غربي آسيوية",
        "womens": "جنوبيات غربيات آسيويات",
        "en": "southwest asia",
        "ar": "جنوب غرب آسيا",
    }

    return all_nat_o


# =====================================================================
# Section 3: Build American forms
# =====================================================================


def build_american_forms(all_nat: AllNatDict, all_nat_o: Dict[str, NationalityEntry]) -> Tuple[AllNatDict, int]:
    """
    Build '-american' and 'x american' nationality forms.
    Returns: (updated_all_nat, count_of_added_items)
    """

    count_added: int = 0

    for nat_key, entry in all_nat_o.items():
        men, mens = entry["men"], entry["mens"]
        women, womens = entry["women"], entry["womens"]

        if not any([men, mens, women, womens]):
            continue  # skip if no gender fields present

        new_entry: NationalityEntry = {
            "men": f"أمريكي {men}" if men else "",
            "mens": f"أمريكيون {mens}" if mens else "",
            "women": f"أمريكية {women}" if women else "",
            "womens": f"أمريكيات {womens}" if womens else "",
            "en": "",
            "ar": "",
        }

        key_lower = nat_key.lower()
        all_nat[f"{key_lower}-american"] = new_entry
        count_added += 1

        # Special case
        if key_lower == "jewish":
            all_nat[f"{key_lower} american"] = new_entry

    return all_nat, count_added


# =====================================================================
# Section 4: Build lookup tables
# =====================================================================


def build_lookup_tables(all_nat: AllNatDict, all_nat_o: Dict[str, NationalityEntry]) -> Dict[str, Any]:
    """
    Build all nationality lookup tables used throughout the system.
    """

    Nat_men: LookupTable = {}
    Nat_mens: LookupTable = {}
    Nat_women: LookupTable = {}
    Nat_Womens: LookupTable = {}

    ar_Nat_men: LookupTable = {}
    contries_from_nat: LookupTable = {}

    all_country_ar: LookupTable = {}
    all_country_with_nat: AllNatDict = {}
    all_country_with_nat_ar: AllNatDict = {}
    all_country_with_nat_keys_is_en: Dict[str, NationalityEntry] = {}
    en_nats_to_ar_label: LookupTable = {}

    for nat_key, entry in all_nat.items():
        en: str = entry["en"].lower()
        ar: str = entry["ar"]
        en_norm: str = en[4:] if en.startswith("the ") else en

        # Gender tables
        if entry["men"]:
            Nat_men[nat_key] = entry["men"]
            ar_Nat_men[entry["men"]] = nat_key
        if entry["mens"]:
            Nat_mens[nat_key] = entry["mens"]
        if entry["women"]:
            Nat_women[nat_key] = entry["women"]
        if entry["womens"]:
            Nat_Womens[nat_key] = entry["womens"]

        # English → Arabic country mapping
        if en and ar:
            all_country_ar[en_norm] = ar
            contries_from_nat[en_norm] = ar

            if en_norm.startswith("the "):
                contries_from_nat[en_norm[4:]] = ar

        # Full nationality entry mapping
        if ar:
            all_country_with_nat_ar[nat_key] = entry
            en_nats_to_ar_label[nat_key] = ar

        if en:
            all_country_with_nat[nat_key] = entry
            all_country_with_nat_keys_is_en[en_norm] = entry

    # Special case: Iran
    if "iranian" in all_nat:
        all_country_with_nat_keys_is_en["islamic republic of iran"] = all_nat["iranian"]

    return {
        "Nat_men": Nat_men,
        "Nat_mens": Nat_mens,
        "Nat_women": Nat_women,
        "Nat_Womens": Nat_Womens,
        "ar_Nat_men": ar_Nat_men,
        "contries_from_nat": contries_from_nat,
        "all_country_ar": all_country_ar,
        "all_country_with_nat": all_country_with_nat,
        "all_country_with_nat_ar": all_country_with_nat_ar,
        "all_country_with_nat_keys_is_en": all_country_with_nat_keys_is_en,
        "en_nats_to_ar_label": en_nats_to_ar_label,
    }


# =====================================================================
# Main Execution (same logic as before)
# =====================================================================

All_Nat_o: Dict[str, NationalityEntry] = load_sources()
All_Nat_o = normalize_aliases(All_Nat_o)

All_Nat: AllNatDict = {k.lower(): v for k, v in All_Nat_o.items()}

All_Nat, American_nat = build_american_forms(All_Nat, All_Nat_o)
result_tables = build_lookup_tables(All_Nat, All_Nat_o)

Nat_men = result_tables["Nat_men"]
Nat_mens = result_tables["Nat_mens"]
Nat_women = result_tables["Nat_women"]
Nat_Womens = result_tables["Nat_Womens"]

ar_Nat_men = result_tables["ar_Nat_men"]
contries_from_nat = result_tables["contries_from_nat"]
all_country_ar = result_tables["all_country_ar"]
all_country_with_nat = result_tables["all_country_with_nat"]
all_country_with_nat_ar = result_tables["all_country_with_nat_ar"]
all_country_with_nat_keys_is_en = result_tables["all_country_with_nat_keys_is_en"]
en_nats_to_ar_label = result_tables["en_nats_to_ar_label"]

nats_to_add = {}

len_print.data_len(
    "nationality.py",
    {
        "Nat_mens": Nat_mens,
        "Nat_Womens": Nat_Womens,
        "All_Nat": All_Nat,
        "All_Nat with ar name": all_country_with_nat_ar,
        "All_Nat with en name": all_country_with_nat,
        "American_nat": American_nat,
    },
)
