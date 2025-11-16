#!/usr/bin/python3
"""
from .Nationality import nats_to_add, NATdd, CON_NAT, The_Nat_women, All_Nat, All_Nat_o, Nat_men, Nat_mens, Nat_women, Nat_Womens, contries_from_nat, all_country_with_nat, all_country_ar, all_country_with_nat_ar, all_country_with_nat_keys_is_en, ar_Nat_men, wsss_Womens, A_Nat, en_nats_to_ar_label

# العرقيات
SELECT DISTINCT
(concat(', "' , ?itee ,'" :')  as ?ss)
(concat('"' , ?itema ,'"')  as ?ss2)

WHERE {

  ?item wdt:P31 wd:Q41710.
  ?item rdfs:label ?itema filter (lang(?itema) = "ar") .
  ?item rdfs:label ?itee filter (lang(?itee) = "en") .
    FILTER(CONTAINS(LCASE(?itee), "people"))

    }
LIMIT 1000
"""

from ..utils.json_dir import open_json_file
from ...helps import len_print

# ---
All_Nat_o = open_json_file("All_Nat_o") or {}
uu_nats = open_json_file("uu_nats") or {}
# ---
nats_to_add = {}
# ---
if uu_nats.get("hindustani"):
    uu_nats["hindustan"] = uu_nats["hindustani"]
# ---
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
# ---
CON_NAT = {}
for nationality_key, country_label in NATdd.items():
    CON_NAT[nationality_key.lower()] = country_label
# ---
# Category:Trinidad_and_Tobago_people
# Category:Yoruba_people
# ---
Sub_Nat = open_json_file("Sub_Nat") or {}
# ---
The_Nat_women = {
    "cape verdean": "رأس أخضرية",
    "south sudanese": "جنوب سودانية",
    "southern european": "أوروبية جنوبية",
    "south african": "جنوب إفريقية",
    "south american": "أمريكية جنوبية",
    "south korean": "كورية جنوبية",
}
# ---
All_Nat = {}
# ---
for nationality_key, nationality_labels in uu_nats.items():
    All_Nat_o[nationality_key] = nationality_labels
for nationality_key, nationality_labels in Sub_Nat.items():
    All_Nat_o[nationality_key] = nationality_labels
# ---
All_Nat_o["equatorial guinean"] = All_Nat_o["equatoguinean"]  # غينيا الاستوائية
All_Nat_o["south ossetian"] = All_Nat_o["ossetian"]  # غينيا الاستوائية
# ---
All_Nat_o["republic-of-the-congo"] = All_Nat_o["the republic of the congo"]
All_Nat_o["republic of the congo"] = All_Nat_o["the republic of the congo"]

All_Nat_o["democratic republic of the congo"] = All_Nat_o["democratic republic of the congo"]
All_Nat_o["democratic-republic-of-the-congo"] = All_Nat_o["democratic republic of the congo"]

All_Nat_o["dominican republic"] = All_Nat_o["dominican republic"]
All_Nat_o["caribbean"] = All_Nat_o["caribbeans"]
All_Nat_o["russians"] = All_Nat_o["russian"]
All_Nat_o["bangladesh"] = All_Nat_o["bangladeshi"]
All_Nat_o["yemenite"] = All_Nat_o["yemeni"]
# All_Nat_o["americans"] = All_Nat_o["american"]
All_Nat_o["arabian"] = All_Nat_o["arab"]
All_Nat_o["jewish"] = All_Nat_o["jews"]
All_Nat_o["bosnia and herzegovina"] = All_Nat_o["bosnian"]
All_Nat_o["turkish cypriot"] = All_Nat_o["northern cypriot"]
All_Nat_o["somali"] = All_Nat_o["somalian"]
All_Nat_o["saudi"] = All_Nat_o["saudiarabian"]  # saudi arabian
All_Nat_o["canadians"] = All_Nat_o["canadian"]
All_Nat_o["salvadoran"] = All_Nat_o["salvadorean"]
All_Nat_o["ivoirian"] = All_Nat_o["ivorian"]
All_Nat_o["the republic-of ireland"] = All_Nat_o["irish"]
# All_Nat_o["eritrean"] = All_Nat_o["eritrean"]
# ---
All_Nat_o["trinidadian"] = All_Nat_o["trinidad and tobago"]
All_Nat_o["trinidadians"] = All_Nat_o["trinidad and tobago"]
All_Nat_o["comoran"] = All_Nat_o["comorian"]  # قمري
All_Nat_o["slovakian"] = All_Nat_o["slovak"]  #
All_Nat_o["emirian"] = All_Nat_o["emirati"]  # إماراتي
All_Nat_o["austro-hungarian"] = All_Nat_o["austrianhungarian"]
All_Nat_o["emiri"] = All_Nat_o["emirati"]  # إماراتي
All_Nat_o["roman"] = All_Nat_o["romanian"]  #
All_Nat_o["ancient-roman"] = All_Nat_o["ancient-romans"]  #
All_Nat_o["ancient romans"] = All_Nat_o["ancient-romans"]  #
All_Nat_o["mosotho"] = All_Nat_o["lesotho"]  # ليسوثوي
All_Nat_o["singapore"] = All_Nat_o["singaporean"]  # سنغافوري
All_Nat_o["luxembourg"] = All_Nat_o["luxembourgish"]  # لوكسمبورغي
All_Nat_o["kosovar"] = All_Nat_o["kosovan"]  # كوسوفي
All_Nat_o["argentinean"] = All_Nat_o["argentine"]  # أرجنتيني
All_Nat_o["argentinian"] = All_Nat_o["argentine"]  # أرجنتيني
All_Nat_o["lao"] = All_Nat_o["laotian"]  # لاوسي
All_Nat_o["israeli"] = All_Nat_o["israeli11111"]  # إسرائيلي
All_Nat_o["slovene"] = All_Nat_o["slovenian"]  # سلوفيني
All_Nat_o["vietnamesei"] = All_Nat_o["vietnamese"]  # فيتنامي

All_Nat_o["nepali"] = All_Nat_o["nepalese"]  # نيبالي
All_Nat_o["papua new guinean x "] = {
    "men": "غيني",
    "mens": "غينيون",
    "women": "غينية",
    "womens": "غينيات",
    "en": "papua new guinea",
    "ar": "بابوا غينيا الجديدة",
}
# ---
Nat_men = {}
Nat_mens = {}
Nat_women = {}
Nat_Womens = {}
contries_from_nat = {}
all_country_with_nat = {}
all_country_ar = {}  # عربي وانجليزي اسم البلد
all_country_with_nat_ar = {}
# ---
all_country_with_nat_keys_is_en = {}
all_country_with_nat_keys_is_en["islamic republic of iran"] = All_Nat_o["iranian"]
# ---
All_Nat_o["georgia (country)"] = All_Nat_o["georgian"]
All_Nat_o["georgia (country)"]["en"] = "georgia (country)"

# ---
All_Nat_o["southwest asian"] = {
    "men": "جنوب غرب آسيوي",
    "mens": "جنوبيون غربيون آسيويين",
    "women": "جنوب غربي آسيوية",
    "womens": "جنوبيات غربيات آسيويات",
    "en": "southwest asia",
    "ar": "جنوب غرب آسيا",
}

# ---
for nationality_key, nationality_labels in All_Nat_o.items():
    All_Nat[nationality_key.lower()] = nationality_labels
# ---
ar_Nat_men = {}
# ---
American_nat = 0
# ---
for nationality_key in All_Nat_o.keys():
    kb = {"men": "", "mens": "", "women": "", "womens": "", "en": "", "ar": ""}
    rog = False
    # ---
    if All_Nat_o[nationality_key].get("men", "") != "":
        kb["men"] = f"أمريكي {All_Nat_o[nationality_key]['men']}"
        rog = True
    # ---
    if All_Nat_o[nationality_key]["mens"]:
        kb["mens"] = f"أمريكيون {All_Nat_o[nationality_key]['mens']}"
        rog = True
    # ---
    if All_Nat_o[nationality_key]["women"]:
        kb["women"] = f"أمريكية {All_Nat_o[nationality_key]['women']}"
        rog = True
    # ---
    if All_Nat_o[nationality_key]["womens"]:
        kb["womens"] = f"أمريكيات {All_Nat_o[nationality_key]['womens']}"
        rog = True
    # ---
    if rog:
        American_nat += 1
        All_Nat[f"{nationality_key.lower()}-American"] = kb
        if nationality_key.lower() == "jewish":
            All_Nat[f"{nationality_key.lower()} american"] = kb
# ---
en_nats_to_ar_label = {}
# ---
for papa, papa_tab in All_Nat.items():
    papa2 = papa.lower()
    # ---
    en_ll = papa_tab["en"].lower()
    en_ll2 = en_ll
    if en_ll.startswith("the "):
        en_ll2 = en_ll[len("the ") :]
    # ---
    if papa_tab.get("men", "") != "":
        ar_Nat_men[papa_tab["men"]] = papa
        Nat_men[papa2] = papa_tab["men"]
    # ---
    if papa_tab["mens"]:
        Nat_mens[papa2] = papa_tab["mens"]
    # ---
    if papa_tab["women"]:
        Nat_women[papa2] = papa_tab["women"]
    # ---
    if papa_tab["womens"]:
        Nat_Womens[papa2] = papa_tab["womens"]
    # ---
    if papa_tab["ar"] and papa_tab["en"]:
        all_country_ar[en_ll2] = papa_tab["ar"]
    # ---
    if papa_tab["ar"]:
        all_country_with_nat_ar[papa2] = papa_tab
        en_nats_to_ar_label[papa2] = papa_tab["ar"]
    # ---
    if papa_tab["en"]:
        all_country_with_nat[papa] = papa_tab
        all_country_with_nat_keys_is_en[en_ll2.lower()] = papa_tab
    # ---
    # contries_from_nat["yemen"] = "اليمن"
    if papa_tab["en"] and papa_tab["ar"]:
        en_name = papa_tab["en"].lower()
        contries_from_nat[en_name] = papa_tab["ar"]
        if en_name.startswith("the "):
            en_name2 = en_name[len("the ") :]
            contries_from_nat[en_name2.lower()] = papa_tab["ar"]
# ---
len_print.data_len("nationality.py", {
    "All_Nat": All_Nat,
    "All_Nat with ar name": all_country_with_nat_ar,
    "All_Nat with en name": all_country_with_nat,
    "American_nat": American_nat,
})
# ---
del uu_nats
del Sub_Nat
