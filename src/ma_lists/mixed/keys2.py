"""Helper utilities and datasets for the mixed key collections.

This module historically exposed a collection of global dictionaries used by
several other ``ma_lists`` modules.  The refactored implementation keeps the
public API intact (``new_2019``, ``keys2_py`` and ``Add_in_table2``) while
building the underlying data via the shared :class:`~ma_lists.mixed.key_registry.KeyRegistry`
utility.  This ensures deterministic results, full type coverage and greatly
simplifies future maintenance.
"""

from __future__ import annotations

from typing import Final

from ...helps import len_print
from ..geo.us_counties import USA_newkeys
from ..medical.deaths import medical_keys
from .key_registry import KeyRegistry, load_json_mapping

__all__ = [
    "Add_in_table2",
    "ADD_IN_TABLE2",
    "PARTIES",
    "build_keys2_mapping",
    "build_keys2_py_mapping",
    "keys2_py",
    "new_2019",
]


ADD_IN_TABLE2: Final[list[str]] = [
    "censuses",  # تعداد السكان
]

# Backwards compatibility alias expected by legacy imports.
Add_in_table2 = ADD_IN_TABLE2


PARTIES: Final[dict[str, str]] = {
    "libertarian party of canada": "الحزب التحرري الكندي",
    "libertarian party-of-canada": "الحزب التحرري الكندي",
    "green party-of-quebec": "حزب الخضر في كيبيك",
    "balochistan national party (awami)": "حزب بلوشستان الوطني (عوامي)",
    "republican party-of armenia": "حزب أرمينيا الجمهوري",
    "republican party of armenia": "حزب أرمينيا الجمهوري",
    "green party of the united states": "حزب الخضر الأمريكي",
    "green party-of the united states": "حزب الخضر الأمريكي",
    "armenian revolutionary federation": "حزب الطاشناق",
    "telugu desam party": "حزب تيلوغو ديسام",
    "tunisian pirate party": "حزب القراصنة التونسي",
    "uk independence party": "حزب استقلال المملكة المتحدة",
    "motherland party (turkey)": "حزب الوطن الأم",
    "national action party (mexico)": "حزب الفعل الوطني (المكسيك)",
    "nationalist movement party": "حزب الحركة القومية",
    "new labour": "حزب العمال الجديد",
    "pakistan peoples party": "حزب الشعب الباكستاني",
    "party for freedom": "حزب من أجل الحرية",
    "party for the animals": "حزب من أجل الحيوانات",
    "party of democratic action": "حزب العمل الديمقراطي (البوسنة)",
    "party of european socialists": "حزب الاشتراكيين الأوروبيين",
    "party of labour of albania": "حزب العمل الألباني",
    "party of regions": "حزب الأقاليم",
    "party-of democratic action": "حزب العمل الديمقراطي (البوسنة)",
    "party-of european socialists": "حزب الاشتراكيين الأوروبيين",
    "party-of labour of albania": "حزب العمل الألباني",
    "party-of regions": "حزب الأقاليم",
    "people's democratic party (nigeria)": "حزب الشعب الديمقراطي (نيجيريا)",
    "people's party (spain)": "حزب الشعب (إسبانيا)",
    "people's party for freedom and democracy": "حزب الشعب من أجل الحرية والديمقراطية",
    "peoples' democratic party (turkey)": "حزب الشعوب الديمقراطي",
    "polish united workers' party": "حزب العمال البولندي الموحد",
    "progress party (norway)": "حزب التقدم (النرويج)",
    "red party (norway)": "حزب الحمر (النرويج)",
    "ruling party": "حزب حاكم",
    "spanish socialist workers' party": "حزب العمال الاشتراكي الإسباني",
    "swedish social democratic party": "حزب العمال الديمقراطي الاشتراكي السويدي",
    "swiss people's party": "حزب الشعب السويسري",
    "ulster unionist party": "حزب ألستر الوحدوي",
    "united development party": "حزب الاتحاد والتنمية",
    "welfare party": "حزب الرفاه",
    "whig party (united states)": "حزب اليمين (الولايات المتحدة)",
    "workers' party of korea": "حزب العمال الكوري",
    "workers' party-of korea": "حزب العمال الكوري",
    "national party of australia": "الحزب الوطني الأسترالي",
    "people's democratic party of afghanistan": "الحزب الديمقراطي الشعبي الأفغاني",
    "social democratic party of switzerland": "الحزب الاشتراكي الديمقراطي السويسري",
    "national party-of australia": "الحزب الوطني الأسترالي",
    "people's democratic party-of afghanistan": "الحزب الديمقراطي الشعبي الأفغاني",
    "social democratic party-of switzerland": "الحزب الاشتراكي الديمقراطي السويسري",
    "national party (south africa)": "الحزب الوطني (جنوب إفريقيا)",
    "national woman's party": "الحزب الوطني للمرأة",
    "new democratic party": "الحزب الديمقراطي الجديد",
    "parti québécois": "الحزب الكيبيكي",
    "republican party (united states)": "الحزب الجمهوري (الولايات المتحدة)",
    "revolutionary socialist party (india)": "الحزب الاشتراكي الثوري",
    "scottish national party": "الحزب القومي الإسكتلندي",
    "scottish socialist party": "الحزب الاشتراكي الإسكتلندي",
    "serbian radical party": "الحزب الراديكالي الصربي",
    "shining path": "الحزب الشيوعي في بيرو (الدرب المضيء)",
    "social democratic and labour party": "الحزب الاشتراكي العمالي",
    "socialist left party (norway)": "الحزب الاشتراكي اليساري (النرويج)",
    "the left (germany)": "الحزب اليساري الألماني",
    "united national party": "الحزب الوطني المتحد",
    "federalist party": "الحزب الفيدرالي الأمريكي",
    "socialist party of albania": "الحزب الإشتراكي (ألبانيا)",
    "socialist party-of albania": "الحزب الإشتراكي (ألبانيا)",
}


def build_keys2_mapping() -> dict[str, str]:
    """Return the base mapping historically stored in ``new_2019``."""

    registry = KeyRegistry(load_json_mapping("keys2"))
    registry.update(PARTIES)
    registry.update_lowercase(USA_newkeys)
    return registry.data


def build_keys2_py_mapping() -> dict[str, str]:
    """Return the mapping previously stored in ``keys2_py``."""

    registry = KeyRegistry(load_json_mapping("keys2_py"))
    registry.update(medical_keys)
    return registry.data


new_2019: dict[str, str] = build_keys2_mapping()
keys2_py: dict[str, str] = build_keys2_py_mapping()

LEN_STATS = {"keys2_py": len(keys2_py)}
len_print.lenth_pri("keys2.py", LEN_STATS)
