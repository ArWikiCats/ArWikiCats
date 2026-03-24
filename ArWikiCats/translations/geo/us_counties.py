"""Translation helpers for United States counties, states, and parties."""

from __future__ import annotations

from collections.abc import Mapping

from ..helps import len_print
from ..utils import open_json_file

_USA_PARTY_LABELS = {
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

USA_PARTY_LABELS = {x.strip(): y.strip() for x, y in _USA_PARTY_LABELS.items() if y.strip()}


def _build_party_derived_keys(party_labels: Mapping[str, str]) -> dict[str, str]:
    """
    Builds derived English translation keys for US political party names.

    Parameters:
        party_labels (Mapping[str, str]): Mapping from party name (English) to its Arabic label. Keys are used as source names and values provide the Arabic translations; entries with empty or whitespace-only translations are ignored.

    Returns:
        dict[str, str]: A mapping of generated English keys to Arabic labels. Generated keys use a lowercase normalized form of the input party name and include common variants (e.g., parenthetical " (united states)", plural forms, and several role- or office-specific phrases) that all map to the corresponding Arabic translation.
    """
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


# US_COUNTY_TRANSLATIONS = load_json_mapping("geography/us_counties.json")
US_COUNTY_TRANSLATIONS = open_json_file("geography/us_counties.json") or {}

USA_PARTY_DERIVED_KEYS = _build_party_derived_keys(USA_PARTY_LABELS)

__all__ = [
    "USA_PARTY_DERIVED_KEYS",
    "US_COUNTY_TRANSLATIONS",
    "USA_PARTY_LABELS",
]

len_print.data_len(
    "us_counties.py",
    {
        "USA_PARTY_LABELS": USA_PARTY_LABELS,
        "USA_PARTY_DERIVED_KEYS": USA_PARTY_DERIVED_KEYS,
        "US_COUNTY_TRANSLATIONS": US_COUNTY_TRANSLATIONS,
    },
)
