#!/usr/bin/python3
"""
Refactored nationality mapping module.
All comments are in English as requested.
"""

from ..utils.json_dir import open_json_file
from ...helps import len_print


# ----------------------------------------------------------------------
# Section 1: Load JSON sources and initial dictionaries
# ----------------------------------------------------------------------

# Load basic nationality dictionaries from JSON
All_Nat_o = open_json_file("All_Nat_o") or {}
uu_nats = open_json_file("uu_nats") or {}
Sub_Nat = open_json_file("Sub_Nat") or {}

# This will collect missing nationalities to add
nats_to_add = {}

# Normalize hindustani → hindustan
if uu_nats.get("hindustani"):
    uu_nats["hindustan"] = uu_nats["hindustani"]

# Base nationalities mapped to country labels
NATdd = {
    "afghan": "afghanistan",
    "albanian": "albania",
    "algerian": "algeria",
    "andorran": "andorra",
    "angolan": "angola",
    "argentine": "argentina",
    "armenian": "armenia",
    "australian": "australia",
    "austrian": "austria",
    "azerbaijani": "azerbaijan",
    "bahamian": "bahamas",
    "bahraini": "bahrain",
    "bangladeshi": "bangladesh",
    "barbadian": "barbados",
    "belarusian": "belarus",
    "belgian": "belgium",
    "belizian": "belize",
    "beninese": "benin",
    "zimbabwean": "zimbabwe",
}

# Build country lookup from nationality → country
CON_NAT = {key.lower(): value for key, value in NATdd.items()}


# ----------------------------------------------------------------------
# Section 2: Merge and expand All_Nat_o with various sources
# ----------------------------------------------------------------------

# Merge sources into All_Nat_o
for key, val in uu_nats.items():
    All_Nat_o[key] = val

for key, val in Sub_Nat.items():
    All_Nat_o[key] = val

# Add known aliases or corrections
ALIASES = {
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

# Apply alias mapping
for alias, target in ALIASES.items():
    if target in All_Nat_o:
        All_Nat_o[alias] = All_Nat_o[target]

# Special explicit definition
All_Nat_o["papua new guinean x "] = {
    "men": "غيني",
    "mens": "غينيون",
    "women": "غينية",
    "womens": "غينيات",
    "en": "papua new guinea",
    "ar": "بابوا غينيا الجديدة",
}

# Add country disambiguation for Georgia
if "georgian" in All_Nat_o:
    All_Nat_o["georgia (country)"] = All_Nat_o["georgian"]
    All_Nat_o["georgia (country)"]["en"] = "georgia (country)"

# Add custom southwest asian entry
All_Nat_o["southwest asian"] = {
    "men": "جنوب غرب آسيوي",
    "mens": "جنوبيون غربيون آسيويين",
    "women": "جنوب غربي آسيوية",
    "womens": "جنوبيات غربيات آسيويات",
    "en": "southwest asia",
    "ar": "جنوب غرب آسيا",
}

# Rebuild All_Nat as lower-case indexed dictionary
All_Nat = {key.lower(): value for key, value in All_Nat_o.items()}


# ----------------------------------------------------------------------
# Section 3: Derive nationality categories including American hybrids
# ----------------------------------------------------------------------

Nat_men = {}
Nat_mens = {}
Nat_women = {}
Nat_Womens = {}

contries_from_nat = {}
all_country_with_nat = {}
all_country_with_nat_ar = {}
all_country_ar = {}
all_country_with_nat_keys_is_en = {}

ar_Nat_men = {}
en_nats_to_ar_label = {}

# Count the number of American-extended entries
American_nat = 0

# Build "-American" forms where possible
for nationality_key, labels in All_Nat_o.items():

    new_block = {
        "men": "",
        "mens": "",
        "women": "",
        "womens": "",
        "en": "",
        "ar": ""
    }

    inserted = False

    if labels.get("men"):
        new_block["men"] = f"أمريكي {labels['men']}"
        inserted = True
    if labels.get("mens"):
        new_block["mens"] = f"أمريكيون {labels['mens']}"
        inserted = True
    if labels.get("women"):
        new_block["women"] = f"أمريكية {labels['women']}"
        inserted = True
    if labels.get("womens"):
        new_block["womens"] = f"أمريكيات {labels['womens']}"
        inserted = True

    if inserted:
        American_nat += 1
        key_lower = nationality_key.lower()
        All_Nat[f"{key_lower}-american"] = new_block

        if key_lower == "jewish":
            All_Nat[f"{key_lower} american"] = new_block


# ----------------------------------------------------------------------
# Section 4: Build final lookup tables
# ----------------------------------------------------------------------

for nat_key, nat_tab in All_Nat.items():

    en_key = nat_tab.get("en", "").lower()
    ar_val = nat_tab.get("ar", "")

    # Normalize English key removing leading "the "
    en_key_norm = en_key[4:] if en_key.startswith("the ") else en_key

    # Build gender mappings
    if nat_tab.get("men"):
        ar_Nat_men[nat_tab["men"]] = nat_key
        Nat_men[nat_key] = nat_tab["men"]

    if nat_tab.get("mens"):
        Nat_mens[nat_key] = nat_tab["mens"]

    if nat_tab.get("women"):
        Nat_women[nat_key] = nat_tab["women"]

    if nat_tab.get("womens"):
        Nat_Womens[nat_key] = nat_tab["womens"]

    # English–Arabic country mapping
    if ar_val and en_key:
        all_country_ar[en_key_norm] = ar_val
        contries_from_nat[en_key_norm] = ar_val
        if en_key_norm.startswith("the "):
            contries_from_nat[en_key_norm[4:]] = ar_val

    # Full nationality dictionaries
    if ar_val:
        all_country_with_nat_ar[nat_key] = nat_tab
        en_nats_to_ar_label[nat_key] = ar_val

    if en_key:
        all_country_with_nat[nat_key] = nat_tab
        all_country_with_nat_keys_is_en[en_key_norm] = nat_tab


# Add special entry for Iran
if "iranian" in All_Nat:
    all_country_with_nat_keys_is_en["islamic republic of iran"] = All_Nat["iranian"]


# ----------------------------------------------------------------------
# Section 5: Print statistics
# ----------------------------------------------------------------------

len_print.data_len("nationality.py", {
    "All_Nat": All_Nat,
    "All_Nat with ar name": all_country_with_nat_ar,
    "All_Nat with en name": all_country_with_nat,
    "American_nat": American_nat,
})

# Cleanup
del uu_nats
del Sub_Nat
