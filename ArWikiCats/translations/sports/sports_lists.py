"""
Static lookup tables used by multiple sports modules.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Final

from ...helps import len_print
from ._helpers import extend_with_templates, extend_with_year_templates


def _build_new_tato_nat() -> dict[str, str]:
    """Construct the ``NEW_TATO_NAT`` dictionary.

    The data expands ``NAT_MENSTT33`` by adding templates for different age
    categories.  ``{nat}`` remains a placeholder in the resulting strings.
    """
    YEARS = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]

    NAT_MENSTT33: dict[str, str] = {
        "": "{nat}",
        "national": "{nat}",
        "national youth": "{nat} للشباب",
        "national amateur": "{nat} للهواة",
        "national junior men's": "{nat} للناشئين",
        "national junior women's": "{nat} للناشئات",
        "national men's": "{nat} للرجال",
        "national women's": "{nat} للسيدات",
        # "multi-national women's": "{nat} متعددة الجنسيات للسيدات",
        "national youth women's": "{nat} للشابات",
    }

    result: dict[str, str] = {}
    for template_key, template_label in NAT_MENSTT33.items():
        result[template_key] = template_label
        for year in YEARS:
            result[f"{template_key} under-{year}"] = template_label.format(nat=f"{{nat}} تحت {year} سنة")
    return result


NEW_TATO_NAT: Final[dict[str, str]] = _build_new_tato_nat()

# Keys appended after a base sport name when generating extended templates.
AFTER_KEYS: Final[dict[str, str]] = {
    "squads": "تشكيلات",
    "finals": "نهائيات",
    "positions": "مراكز",
    "tournaments": "بطولات",
    "films": "أفلام",
    "teams": "فرق",
    "venues": "ملاعب",
    "clubs": "أندية",
    "organizations": "منظمات",
    "non-profit organizations": "منظمات غير ربحية",
    "non-profit publishers": "ناشرون غير ربحيون",
    "organisations": "منظمات",
    "events": "أحداث",
    "umpires": "حكام",
    "trainers": "مدربو",
    "scouts": "كشافة",
    # "people" : "أعلام",
    "coaches": "مدربو",
    "leagues": "دوريات",
    "managers": "مدربو",
    # "managers" : "مدراء",
    # "captains" : "مدربو",
    "playerss": "لاعبو",
    "players": "لاعبو",
    "results": "نتائج",
    "matches": "مباريات",
    "navigational boxes": "صناديق تصفح",
    "lists": "قوائم",
    "home stadiums": "ملاعب",
    "templates": "قوالب",
    "rivalries": "دربيات",
    "champions": "أبطال",
    "competitions": "منافسات",
    "statistics": "إحصائيات",
    "records": "سجلات",
    "records and statistics": "سجلات وإحصائيات",
    "manager history": "تاريخ مدربو",
}


def _extend_suffix_mappings() -> dict[str, str]:
    """Populate ``AFTER_KEYS_NAT`` with variants."""

    AFTER_KEYS_NAT: dict[str, str] = {
        "": "{lab}",
        "second level leagues": "دوريات {lab} من الدرجة الثانية",
        "second tier leagues": "دوريات {lab} من الدرجة الثانية",
    }

    for suffix_key, suffix_label in AFTER_KEYS.items():
        AFTER_KEYS_NAT[suffix_key] = f"{suffix_label} {{lab}}"

    # (fifth|first|fourth|second|seventh|sixth|third|top)[ -](level|tier)
    LEVELS: Final[dict[str, str]] = {
        "top level": "الدرجة الأولى",
        "first level": "الدرجة الأولى",
        "first tier": "الدرجة الأولى",
        "second level": "الدرجة الثانية",
        "second tier": "الدرجة الثانية",
        "third level": "الدرجة الثالثة",
        "third tier": "الدرجة الثالثة",
        "fourth level": "الدرجة الرابعة",
        "fourth tier": "الدرجة الرابعة",
        "fifth level": "الدرجة الخامسة",
        "fifth tier": "الدرجة الخامسة",
        "sixth level": "الدرجة السادسة",
        "sixth tier": "الدرجة السادسة",
        "seventh level": "الدرجة السابعة",
        "seventh tier": "الدرجة السابعة",
    }

    for level_key, level_label in LEVELS.items():
        AFTER_KEYS_NAT[f"{level_key} league"] = f"دوريات {{lab}} من {level_label}"
        AFTER_KEYS_NAT[f"{level_key} leagues"] = f"دوريات {{lab}} من {level_label}"

    AFTER_KEYS_NAT["premier league"] = "دوريات {lab} من الدرجة الممتازة"
    AFTER_KEYS_NAT["premier leagues"] = "دوريات {lab} من الدرجة الممتازة"

    return AFTER_KEYS_NAT


AFTER_KEYS_NAT = _extend_suffix_mappings()


__all__ = [
    "AFTER_KEYS",
    "AFTER_KEYS_NAT",
    "NEW_TATO_NAT",
]

len_print.data_len(
    "sports_lists.py",
    {
        "AFTER_KEYS": AFTER_KEYS,
        "AFTER_KEYS_NAT": AFTER_KEYS_NAT,
        "NEW_TATO_NAT": NEW_TATO_NAT,
    },
)
