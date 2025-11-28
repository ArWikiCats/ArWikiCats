"""Translation helpers for United States counties, states, and parties."""

from __future__ import annotations

from collections.abc import Mapping

from ...helps import len_print
from ..utils.json_dir import open_json_file
from ._shared import load_json_mapping


def normalize_state(ar_name: str) -> str:
    if "ولاية ولاية" in ar_name:
        ar_name = ar_name.replace("ولاية ولاية", "ولاية")

    return ar_name


STATE_NAME_TRANSLATIONS = {
    "washington, d.c.": "واشنطن العاصمة",
    "georgia (u.s. state)": "ولاية جورجيا",
    "washington (state)": "ولاية واشنطن",
    "new york (state)": "ولاية نيويورك",

    "ohio": "أوهايو",
    "louisiana": "لويزيانا",
    "new mexico": "نيومكسيكو",
    "nebraska": "نبراسكا",
    "georgia": "جورجيا",
    "wisconsin": "ويسكونسن",
    "montana": "مونتانا",
    "iowa": "آيوا",
    "arizona": "أريزونا",
    "washington": "واشنطن",
    "idaho": "أيداهو",
    "massachusetts": "ماساتشوستس",
    "maryland": "ماريلند",
    "rhode island": "رود آيلاند",
    "west virginia": "فيرجينيا الغربية",
    "new york": "نيويورك",
    "pennsylvania": "بنسلفانيا",
    "new jersey": "نيوجيرسي",
    "tennessee": "تينيسي",
    "arkansas": "أركنساس",
    "hawaii": "هاواي",
    "illinois": "إلينوي",
    "alaska": "ألاسكا",
    "connecticut": "كونيتيكت",
    "colorado": "كولورادو",
    "south dakota": "داكوتا الجنوبية",
    "virginia": "فرجينيا",
    "minnesota": "منيسوتا",
    "alabama": "ألاباما",
    "mississippi": "مسيسيبي",
    "north carolina": "كارولاينا الشمالية",
    "oregon": "أوريغون",
    "utah": "يوتا",
    "delaware": "ديلاوير",
    "new hampshire": "نيوهامشير",
    "michigan": "ميشيغان",
    "texas": "تكساس",
    "north dakota": "داكوتا الشمالية",
    "nevada": "نيفادا",
    "california": "كاليفورنيا",
    "wyoming": "وايومنغ",
    "south carolina": "كارولاينا الجنوبية",
    "kansas": "كانساس",
    "florida": "فلوريدا",
    "maine": "مين",
    "missouri": "ميزوري",
    "kentucky": "كنتاكي",
    "indiana": "إنديانا",
    "oklahoma": "أوكلاهوما",
    "vermont": "فيرمونت",
}


_STATE_SUFFIX_TEMPLATES_BASE = {
    " senate": "مجلس شيوخ ولاية %s",
    " house-of-representatives elections": "انتخابات مجلس نواب ولاية %s",
    " house-of-representatives": "مجلس نواب ولاية %s",
    " house of representatives": "مجلس نواب ولاية %s",
    " state politics": "سياسة ولاية %s",
    " state attorneys general": "مدعي ولاية %s العام",
    " attorneys general": "مدعي %s العام",
    " gubernatorial elections": "انتخابات حاكم %s",
    " politics": "سياسة %s",
    " state senators": "أعضاء مجلس شيوخ ولاية %s",
    " senators": "أعضاء مجلس شيوخ ولاية %s",
    # " ballot measures":"استفتاءات عامة %s",
    " ballot measures": "إجراءات اقتراع %s",
    " ballot propositions": "اقتراحات اقتراع %s",
    " referendums": "استفتاءات %s",
    " territory": "إقليم %s",
    " territory officials": "مسؤولو إقليم %s",
    " territory judges": "قضاة إقليم %s",
    " law": "قانون %s",
    " city councils": "مجالس مدن %s",
    # " councils" : "مجالس %s",
    " state courts": "محكمة ولاية %s",
    " state court judges": "قضاة محكمة ولاية %s",
    " court judges": "قضاة محكمة %s",
    " court of appeals": "محكمة استئناف %s",
    " court of appeals judges‎": "قضاة محكمة استئناف %s",
    " appellate court judges": "قضاة محكمة استئناف %s",
    " state superior court judges": "قضاة محكمة ولاية %s العليا",
    " superior court judges": "قضاة محكمة %s العليا",
    " supreme court justices": "قضاة محكمة %s العليا",
    " supreme court": "محكمة %s العليا",
    " state legislature": "هيئة ولاية %s التشريعية",
    " territorial legislature": "هيئة %s التشريعية الإقليمية",
    " legislature": "هيئة %s التشريعية",
    " legislative assembly": "هيئة %s التشريعية",
    " general assembly": "جمعية %s العامة",
    " state assembly": "جمعية ولاية %s",
    " board of health": "مجلس الصحة في ولاية %s",
    " board of education": "مجلس التعليم في ولاية %s",
    " local politicians": "سياسيون محليون في %s",
    " politicians": "سياسيو %s",
    " sheriffs": "مأمورو %s",
    " lawyers": "محامون من ولاية %s",
    " jacksonians": "جاكسونيون من ولاية %s",
    " republicans": "جمهوريون من ولاية %s",
    " democrats": "ديمقراطيون من ولاية %s",
    " independents": "مستقلون من ولاية %s",
}

PARTY_ROLE_SUFFIXES = {
    "candidates for member of parliament": "مرشحو %s لعضوية البرلمان",
    "candidates for member-of-parliament": "مرشحو %s لعضوية البرلمان",
    "candidates": "مرشحو %s",
    "leaders": "قادة %s",
    "politicians": "سياسيو %s",
    "members": "أعضاء %s",
    "state governors": "حكام ولايات من %s",
}

USA_PARTY_LABELS = {
    "democratic republican": "الحزب الديمقراطي الجمهوري",
    "democratic-republican": "الحزب الديمقراطي الجمهوري",
    "democratic-republican party": "الحزب الديمقراطي الجمهوري",
    "anti-Administration party": "حزب معاداة الإدارة",
    "anti Administration party": "حزب معاداة الإدارة",
    "Pro Administration Party": "حزب دعم الإدارة",
    "Pro-Administration Party": "حزب دعم الإدارة",
    "Anti-Monopoly Party": "حزب مكافحة الاحتكار",
    "Free Soil Party": "حزب التربة الحرة",
    "Liberty Party (1840)": "حزب الحرية 1840",
    "Opposition Party": "أوبوسيشن بارتي",
    "Readjuster Party": "ريدجوستر بارتي",
    "Silver Republican Party": "الحزب الجمهوري الفضي",
    "conditional Union Party": "حزب الاتحاد المشروط",
    "Unconditional Union Party": "حزب الاتحاد غير المشروط",
    "Asian-American": "",
    "Censured or reprimanded": "",
    # 'Expelled' : 'مطرودون' ,
    "Independent": "",
    "Jewish": "",
    "Nonpartisan League": "",
    "democratic party": "الحزب الديمقراطي",
    "republican party": "الحزب الجمهوري",
    "jacksonian": "جاكسونيون",
    "whig party": "حزب اليمين",
    "National Republican Party": "الحزب الجمهوري الوطني",
    "National Republican": "الحزب الجمهوري الوطني",
    "Unionist Party": "الحزب الوحدوي",
    "Unionist": "الحزب الوحدوي",
    "Know-Nothing": "حزب لا أدري",
    "Know Nothing": "حزب لا أدري",
    "alaskan independence Party": "حزب استقلال ألاسكا",
    "anti-masonic Party": "حزب مناهضة الماسونية",
    "anti masonic Party": "حزب مناهضة الماسونية",
    "constitutional union Party": "حزب الاتحاد الدستوري",
    # 'Country Party (Rhode Island)' : 'حزب الدولة (رود آيلاند)',
    "Greenback Party": "حزب الدولار الأمريكي",
    "Farmer–Labor Party": "حزب العمال المزارعين",
    "Farmer Labor Party": "حزب العمال المزارعين",
    "Federalist Party": "الحزب الفيدرالي الأمريكي",
    # 'Independent' : 'مستقلون',
    "Independent Voters Association": "رابطة الناخبين المستقلين",
    "Law and Order Party of Rhode Island": "حزب القانون والنظام في رود آيلاند",
    "Liberal Republican Party": "الحزب الجمهوري الليبرالي",
    "Nonpartisan League state": "الرابطة غير الحزبية",
    "Nullifier Party": "حزب الرفض",
    "People's Party": "حزب الشعب",
    "Peoples Party": "حزب الشعب",
    "Silver Party": "الحزب الفضي",
    "Green Party": "حزب الخضر",
    "Green": "حزب الخضر",
    "Citizens Party": "حزب المواطنين",
    "Solidarity": "حزب التضامن",
    "Socialist Party USA": "الحزب الاشتراكي",
    "Socialist Party": "الحزب الاشتراكي",
    "Liberty Union Party": "حزب الحرية المتحد",
}


def _extend_state_suffix_templates(
    base_templates: Mapping[str, str], party_labels: Mapping[str, str]
) -> dict[str, str]:
    extended_templates = dict(base_templates)

    for party_name, party_label in party_labels.items():
        normalized_party_name = party_name.lower()
        extended_templates[f" {normalized_party_name}s"] = f"أعضاء {party_label} في %s"
        simplified_party_name = normalized_party_name.replace(" party", "")
        extended_templates[f" {simplified_party_name}s"] = f"أعضاء {party_label} في %s"

    return extended_templates


def _build_party_derived_keys(party_labels: Mapping[str, str]) -> dict[str, str]:
    derived_keys: dict[str, str] = {}

    for party_name, party_label in party_labels.items():
        normalized_party_name = party_name.lower()

        if not party_label.strip():
            continue

        derived_keys[normalized_party_name] = party_label
        derived_keys[f"{normalized_party_name} (united states)"] = party_label
        derived_keys[f"{normalized_party_name}s (united states)"] = party_label

        # derived_keys[ '%s members of the united states congress' % normalized_party_name ] = 'أعضاء الكونغرس الأمريكي من %s' % party_label
        derived_keys[f"{normalized_party_name} united states senators"] = f"أعضاء مجلس الشيوخ الأمريكي من {party_label}"
        derived_keys[f"{normalized_party_name} members"] = f"أعضاء {party_label}"
        derived_keys[f"{normalized_party_name} members of the united states house of representatives"] = (
            f"أعضاء مجلس النواب الأمريكي من {party_label}"
        )
        derived_keys[f"{normalized_party_name} members of the united states house-of-representatives"] = (
            f"أعضاء مجلس النواب الأمريكي من {party_label}"
        )

        derived_keys[f"{normalized_party_name} presidential nominees"] = f"مرشحون لمنصب الرئيس من {party_label}"
        derived_keys[f"{normalized_party_name} vice presidential nominees"] = (
            f"مرشحون لمنصب نائب الرئيس من {party_label}"
        )

        derived_keys[f"{normalized_party_name} (united states) vice presidential nominees"] = (
            f"مرشحون لمنصب نائب الرئيس من {party_label}"
        )
        derived_keys[f"{normalized_party_name} (united states) presidential nominees"] = (
            f"مرشحون لمنصب الرئيس من {party_label}"
        )

        derived_keys[f"{normalized_party_name} (united states) politicians"] = f"سياسيو {party_label}"
        derived_keys[f"{normalized_party_name} politicians"] = f"سياسيو {party_label}"

        derived_keys[f"{normalized_party_name} vice presidents of the united states"] = (
            f"نواب رئيس الولايات المتحدة من {party_label}"
        )
        derived_keys[f"{normalized_party_name} presidents of the united states"] = (
            f"رؤساء الولايات المتحدة من {party_label}"
        )
        derived_keys[f"{normalized_party_name} state governors"] = f"حكام ولايات من {party_label}"
        derived_keys[f"{normalized_party_name} state governors of the united states"] = (
            f"حكام ولايات أمريكية من {party_label}"
        )

    return derived_keys


def _build_state_key_mappings(state_labels: Mapping[str, str]) -> dict[str, str]:
    state_keys: dict[str, str] = {}

    for english_name, arabic_label in state_labels.items():
        normalized_state = english_name.lower()
        state_keys[normalized_state] = arabic_label

        base_variants = [normalized_state, f"{normalized_state} state"]
        house_template = "مجلس نواب ولاية %s"
        if arabic_label.startswith("ولاية "):
            house_template = "مجلس نواب %s"

        for variant in base_variants:
            state_keys[f"{variant} house of representatives"] = house_template % arabic_label
            state_keys[f"{variant} house-of-representatives"] = house_template % arabic_label
            state_keys[f"{variant} politics"] = f"سياسة {arabic_label}"
            state_keys[f"{variant} law"] = f"قانون {arabic_label}"
            state_keys[f"{variant} city councils"] = f"مجالس مدن {arabic_label}"
            state_keys[f"{variant} councils"] = f"مجالس {arabic_label}"
            state_keys[f"{variant} legislature"] = f"هيئة {arabic_label} التشريعية"
            state_keys[f"{variant} legislative assembly"] = f"هيئة {arabic_label} التشريعية"
            state_keys[f"{variant} general assembly"] = f"جمعية {arabic_label} العامة"
            state_keys[f"{variant} local politicians"] = f"سياسيون محليون في {arabic_label}"

    return state_keys


# COUNTY_TRANSLATIONS = load_json_mapping("geography/us_counties.json")
COUNTY_TRANSLATIONS = open_json_file("geography/us_counties.json") or {}

STATE_SUFFIX_TEMPLATES = _extend_state_suffix_templates(_STATE_SUFFIX_TEMPLATES_BASE, USA_PARTY_LABELS)

STATE_NAME_KEY_MAPPINGS = {}
# STATE_NAME_KEY_MAPPINGS = _build_state_key_mappings(STATE_NAME_TRANSLATIONS)

USA_PARTY_DERIVED_KEYS = _build_party_derived_keys(USA_PARTY_LABELS)

# Backwards compatible aliases ---------------------------------------
STATE_NAME_TRANSLATIONS_LOWER = {
    english_name.lower(): arabic_name for english_name, arabic_name in STATE_NAME_TRANSLATIONS.items()
}

US_State = STATE_NAME_TRANSLATIONS
US_State_lower = STATE_NAME_TRANSLATIONS_LOWER
kk_end_US_State = STATE_SUFFIX_TEMPLATES
party_end_keys = PARTY_ROLE_SUFFIXES
USA_newkeys = USA_PARTY_DERIVED_KEYS
Counties = COUNTY_TRANSLATIONS
usa_parties = USA_PARTY_LABELS

__all__ = [
    "normalize_state",
    "COUNTY_TRANSLATIONS",
    "STATE_NAME_TRANSLATIONS",
    "STATE_NAME_TRANSLATIONS_LOWER",
    "STATE_SUFFIX_TEMPLATES",
    "PARTY_ROLE_SUFFIXES",
    "USA_PARTY_LABELS",
    "USA_PARTY_DERIVED_KEYS",
    # Backwards-compatible exports
    "US_State",
    "US_State_lower",
    "kk_end_US_State",
    "party_end_keys",
    "USA_newkeys",
    "Counties",
    "usa_parties",
]

len_print.data_len(
    "us_counties.py",
    {
        "COUNTY_TRANSLATIONS": COUNTY_TRANSLATIONS,
        "STATE_NAME_TRANSLATIONS": STATE_NAME_TRANSLATIONS,
        "STATE_NAME_TRANSLATIONS_LOWER": STATE_NAME_TRANSLATIONS_LOWER,
        "STATE_SUFFIX_TEMPLATES": STATE_SUFFIX_TEMPLATES,
        "PARTY_ROLE_SUFFIXES": PARTY_ROLE_SUFFIXES,
        "USA_PARTY_LABELS": USA_PARTY_LABELS,
        "USA_PARTY_DERIVED_KEYS": USA_PARTY_DERIVED_KEYS,
        "US_State": US_State,
        "US_State_lower": US_State_lower,
        "kk_end_US_State": kk_end_US_State,
        "party_end_keys": party_end_keys,
        "USA_newkeys": USA_newkeys,
        "Counties": Counties,
        "usa_parties": usa_parties,
    },
)
