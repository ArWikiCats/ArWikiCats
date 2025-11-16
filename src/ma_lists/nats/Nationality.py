#!/usr/bin/python3
"""
Nationality system (refactored into 4 main functions).
All comments are in English only.
"""

from ..utils.json_dir import open_json_file
from ...helps import len_print


# =====================================================================
# Section 1: Load and prepare primary JSON sources
# =====================================================================

def load_sources():
    """
    Load JSON nationality data and prepare the initial All_Nat_o dictionary.
    This function merges: All_Nat_o + uu_nats + Sub_Nat.
    It also applies specific key replacements (hindustani → hindustan).
    """
    # Load JSON files
    all_nat_o = open_json_file("All_Nat_o") or {}
    uu_nats = open_json_file("uu_nats") or {}
    sub_nat = open_json_file("Sub_Nat") or {}

    # Fix hindustani
    if uu_nats.get("hindustani"):
        uu_nats["hindustan"] = uu_nats["hindustani"]

    # Merge uu_nats → All_Nat_o
    for key, val in uu_nats.items():
        all_nat_o[key] = val

    # Merge Sub_Nat → All_Nat_o
    for key, val in sub_nat.items():
        all_nat_o[key] = val

    # Cleanup
    del uu_nats
    del sub_nat

    return all_nat_o


# =====================================================================
# Section 2: Normalize aliases and expand All_Nat_o
# =====================================================================

def normalize_aliases(all_nat_o: dict):
    """
    Apply all alias mappings and one-off corrections to All_Nat_o.
    """
    alias_map = {
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

    # Apply normal aliases
    for alias, target in alias_map.items():
        if target in all_nat_o:
            all_nat_o[alias] = all_nat_o[target]

    # Add special nationality:
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
        all_nat_o["georgia (country)"] = dict(all_nat_o["georgian"])
        all_nat_o["georgia (country)"]["en"] = "georgia (country)"

    # Add southwest asian block
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
# Section 3: Build American hybrid forms
# =====================================================================

def build_american_forms(all_nat: dict, all_nat_o: dict):
    """
    Generate '-American' and 'x american' nationality variants
    based on existing gendered Arabic forms.
    """
    american_count = 0

    for nat_key, labels in all_nat_o.items():

        new_entry = {
            "men": "",
            "mens": "",
            "women": "",
            "womens": "",
            "en": "",
            "ar": "",
        }

        changed = False
        key_lower = nat_key.lower()

        # Build Americanized nationality forms
        if labels.get("men"):
            new_entry["men"] = f"أمريكي {labels['men']}"
            changed = True
        if labels.get("mens"):
            new_entry["mens"] = f"أمريكيون {labels['mens']}"
            changed = True
        if labels.get("women"):
            new_entry["women"] = f"أمريكية {labels['women']}"
            changed = True
        if labels.get("womens"):
            new_entry["womens"] = f"أمريكيات {labels['womens']}"
            changed = True

        # If at least one field exists, register the Americanized version
        if changed:
            american_count += 1
            all_nat[f"{key_lower}-american"] = new_entry

            # Special case for "jewish american"
            if key_lower == "jewish":
                all_nat[f"{key_lower} american"] = new_entry

    return all_nat, american_count


# =====================================================================
# Section 4: Build lookup tables (men/women, country maps, etc.)
# =====================================================================

def build_lookup_tables(all_nat: dict, all_nat_o: dict):
    """
    Build Nat_men, Nat_women, en_nats_to_ar_label, contries_from_nat,
    and all other country/nationality lookup maps.
    """

    Nat_men = {}
    Nat_mens = {}
    Nat_women = {}
    Nat_Womens = {}

    contries_from_nat = {}
    all_country_with_nat = {}
    all_country_with_nat_ar = {}
    all_country_ar = {}
    all_country_with_nat_keys_is_en = {}
    en_nats_to_ar_label = {}
    ar_Nat_men = {}

    for nat_key, nat_tab in all_nat.items():

        en = nat_tab.get("en", "").lower()
        ar = nat_tab.get("ar", "")

        en_norm = en[4:] if en.startswith("the ") else en

        # Build gender dictionaries
        if nat_tab.get("men"):
            Nat_men[nat_key] = nat_tab["men"]
            ar_Nat_men[nat_tab["men"]] = nat_key
        if nat_tab.get("mens"):
            Nat_mens[nat_key] = nat_tab["mens"]
        if nat_tab.get("women"):
            Nat_women[nat_key] = nat_tab["women"]
        if nat_tab.get("womens"):
            Nat_Womens[nat_key] = nat_tab["womens"]

        # English → Arabic country names
        if en and ar:
            all_country_ar[en_norm] = ar
            contries_from_nat[en_norm] = ar

            # the X → X
            if en_norm.startswith("the "):
                contries_from_nat[en_norm[4:]] = ar

        # Full nationality entries
        if ar:
            all_country_with_nat_ar[nat_key] = nat_tab
            en_nats_to_ar_label[nat_key] = ar
        if en:
            all_country_with_nat[nat_key] = nat_tab
            all_country_with_nat_keys_is_en[en_norm] = nat_tab

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
# Main Execution (same results as original code)
# =====================================================================

# Load initial data
All_Nat_o = load_sources()

# Apply alias normalization
All_Nat_o = normalize_aliases(All_Nat_o)

# Lower-case index build for All_Nat
All_Nat = {k.lower(): v for k, v in All_Nat_o.items()}

# Build American hybrid nationalities
All_Nat, American_nat = build_american_forms(All_Nat, All_Nat_o)

# Build lookup dictionaries
result_tables = build_lookup_tables(All_Nat, All_Nat_o)

# Unpack final results as in original variables
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

# This will collect missing nationalities to add
nats_to_add = {}

# Print statistics
len_print.data_len("nationality.py", {
    "All_Nat": All_Nat,
    "All_Nat with ar name": all_country_with_nat_ar,
    "All_Nat with en name": all_country_with_nat,
    "American_nat": American_nat,
})
