"""
Static lookup tables used by multiple sports modules.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Final

from ...helps import len_print
from ._helpers import extend_with_templates, extend_with_year_templates

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

__all__ = [
    "AFTER_KEYS",
]

len_print.data_len(
    "sports_lists.py",
    {
        "AFTER_KEYS": AFTER_KEYS,
    },
)
