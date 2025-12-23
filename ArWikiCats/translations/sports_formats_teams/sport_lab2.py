#!/usr/bin/python3
"""
"""

import functools

# from ...helps.jsonl_dump import dump_data
from ...translations_formats import FormatData
from ..sports.Sport_key import (
    SPORTS_KEYS_FOR_JOBS,
    SPORTS_KEYS_FOR_LABEL,
    SPORTS_KEYS_FOR_TEAM,
)

new_team_xo_jobs = {
    "amateur xoxo": "xoxo للهواة",
    "amateur xoxo championships": "بطولات xoxo للهواة",
    "college xoxo": "xoxo الكليات",
    "current xoxo seasons": "مواسم xoxo حالية",
    "defunct indoor xoxo clubs": "أندية xoxo داخل الصالات سابقة",
    "defunct indoor xoxo coaches": "مدربو xoxo داخل الصالات سابقة",
    "defunct indoor xoxo competitions": "منافسات xoxo داخل الصالات سابقة",
    "defunct indoor xoxo cups": "كؤوس xoxo داخل الصالات سابقة",
    "defunct indoor xoxo leagues": "دوريات xoxo داخل الصالات سابقة",
    "defunct outdoor xoxo clubs": "أندية xoxo في الهواء الطلق سابقة",
    "defunct outdoor xoxo coaches": "مدربو xoxo في الهواء الطلق سابقة",
    "defunct outdoor xoxo competitions": "منافسات xoxo في الهواء الطلق سابقة",
    "defunct outdoor xoxo cups": "كؤوس xoxo في الهواء الطلق سابقة",
    "defunct outdoor xoxo leagues": "دوريات xoxo في الهواء الطلق سابقة",
    "defunct xoxo clubs": "أندية xoxo سابقة",
    "defunct xoxo coaches": "مدربو xoxo سابقة",
    "defunct xoxo competitions": "منافسات xoxo سابقة",
    "defunct xoxo cup competitions": "منافسات كؤوس xoxo سابقة",
    "defunct xoxo cups": "كؤوس xoxo سابقة",
    "defunct xoxo leagues": "دوريات xoxo سابقة",
    "defunct xoxo teams": "فرق xoxo سابقة",
    "domestic women's xoxo clubs": "أندية xoxo محلية للسيدات",
    "domestic women's xoxo coaches": "مدربو xoxo محلية للسيدات",
    "domestic women's xoxo competitions": "منافسات xoxo محلية للسيدات",
    "domestic women's xoxo cups": "كؤوس xoxo محلية للسيدات",
    "domestic women's xoxo leagues": "دوريات xoxo محلية للسيدات",
    "domestic xoxo": "xoxo محلية",
    "domestic xoxo clubs": "أندية xoxo محلية",
    "domestic xoxo coaches": "مدربو xoxo محلية",
    "domestic xoxo competitions": "منافسات xoxo محلية",
    "domestic xoxo cup": "كؤوس xoxo محلية",
    "domestic xoxo cups": "كؤوس xoxo محلية",
    "domestic xoxo leagues": "دوريات xoxo محلية",
    "fictional xoxo": "xoxo خيالية",
    "fifth level xoxo league": "دوريات xoxo من الدرجة الخامسة",
    "fifth level xoxo leagues": "دوريات xoxo من الدرجة الخامسة",
    "fifth tier xoxo league": "دوريات xoxo من الدرجة الخامسة",
    "fifth tier xoxo leagues": "دوريات xoxo من الدرجة الخامسة",
    "first level xoxo league": "دوريات xoxo من الدرجة الأولى",
    "first level xoxo leagues": "دوريات xoxo من الدرجة الأولى",
    "first tier xoxo league": "دوريات xoxo من الدرجة الأولى",
    "first tier xoxo leagues": "دوريات xoxo من الدرجة الأولى",
    "first-class xoxo": "xoxo من الدرجة الأولى",
    "first-class xoxo competitions": "منافسات xoxo من الدرجة الأولى",
    "first-class xoxo matches": "مباريات xoxo من الدرجة الأولى",
    "first-class xoxo records": "سجلات xoxo من الدرجة الأولى",
    "first-class xoxo teams": "فرق xoxo من الدرجة الأولى",
    "fourth level xoxo league": "دوريات xoxo من الدرجة الرابعة",
    "fourth level xoxo leagues": "دوريات xoxo من الدرجة الرابعة",
    "fourth tier xoxo league": "دوريات xoxo من الدرجة الرابعة",
    "fourth tier xoxo leagues": "دوريات xoxo من الدرجة الرابعة",
    "grand slam (xoxo)": "بطولات xoxo كبرى",
    "grand slam (xoxo) tournament champions": "أبطال بطولات xoxo كبرى",
    "grand slam (xoxo) tournaments": "بطولات xoxo كبرى",
    "indoor xoxo": "xoxo داخل الصالات",
    "indoor xoxo clubs": "أندية xoxo داخل الصالات",
    "indoor xoxo coaches": "مدربو xoxo داخل الصالات",
    "indoor xoxo competitions": "منافسات xoxo داخل الصالات",
    "indoor xoxo cups": "كؤوس xoxo داخل الصالات",
    "indoor xoxo leagues": "دوريات xoxo داخل الصالات",
    "international men's xoxo": "xoxo دولية للرجال",
    "international men's xoxo competitions": "منافسات xoxo رجالية دولية",
    "international men's xoxo players": "لاعبو xoxo دوليون",
    "international men's xoxo playerss": "لاعبو xoxo دوليون",
    "international women's xoxo": "xoxo دولية للسيدات",
    "international women's xoxo competitions": "منافسات xoxo نسائية دولية",
    "international women's xoxo players": "لاعبات xoxo دوليات",
    "international women's xoxo playerss": "لاعبات xoxo دوليات",
    "international xoxo": "xoxo دولية",
    "International xoxo competition tournaments": "بطولات منافسات xoxo دولية",
    "International xoxo competitions": "منافسات xoxo دولية",
    "international xoxo managers": "مدربو xoxo دوليون",
    "international xoxo players": "لاعبو xoxo دوليون",
    "international xoxo playerss": "لاعبو xoxo دوليون",
    "International xoxo races": "سباقات xoxo دولية",
    "International xoxo records and statistics": "سجلات وإحصائيات xoxo دولية",
    "International xoxo tournaments": "بطولات xoxo دولية",
    "international youth xoxo competitions": "منافسات xoxo شبابية دولية",
    "men's international xoxo": "xoxo دولية للرجال",
    "men's international xoxo players": "لاعبو xoxo دوليون",
    "men's international xoxo playerss": "لاعبو xoxo دوليون",
    "men's xoxo": "xoxo رجالية",
    "men's xoxo teams": "فرق xoxo رجالية",
    "military xoxo": "xoxo عسكرية",
    "military xoxo competitions": "منافسات xoxo عسكرية",
    "multi-national xoxo championships": "بطولات xoxo متعددة الجنسيات",
    "multi-national xoxo league": "دوريات xoxo متعددة الجنسيات",
    "multi-national xoxo leagues": "دوريات xoxo متعددة الجنسيات",
    "national a' xoxo teams": "منتخبات xoxo للمحليين",
    "national a. xoxo teams": "منتخبات xoxo للمحليين",
    "national b xoxo teams": "منتخبات xoxo رديفة",
    "national b. xoxo teams": "منتخبات xoxo رديفة",
    "national junior men's xoxo teams": "منتخبات xoxo وطنية للناشئين",
    "national junior xoxo teams": "منتخبات xoxo وطنية للناشئين",
    "national men's xoxo manager history": "تاريخ مدربو منتخبات xoxo وطنية للرجال",
    "national men's xoxo teams": "منتخبات xoxo وطنية رجالية",
    "national reserve xoxo teams": "منتخبات xoxo وطنية احتياطية",
    "national under-13 xoxo manager history": "تاريخ مدربو منتخبات xoxo تحت 13 سنة",
    "national under-14 xoxo manager history": "تاريخ مدربو منتخبات xoxo تحت 14 سنة",
    "national under-15 xoxo manager history": "تاريخ مدربو منتخبات xoxo تحت 15 سنة",
    "national under-16 xoxo manager history": "تاريخ مدربو منتخبات xoxo تحت 16 سنة",
    "national under-17 xoxo manager history": "تاريخ مدربو منتخبات xoxo تحت 17 سنة",
    "national under-18 xoxo manager history": "تاريخ مدربو منتخبات xoxo تحت 18 سنة",
    "national under-19 xoxo manager history": "تاريخ مدربو منتخبات xoxo تحت 19 سنة",
    "national under-20 xoxo manager history": "تاريخ مدربو منتخبات xoxo تحت 20 سنة",
    "national under-21 xoxo manager history": "تاريخ مدربو منتخبات xoxo تحت 21 سنة",
    "national under-23 xoxo manager history": "تاريخ مدربو منتخبات xoxo تحت 23 سنة",
    "national under-24 xoxo manager history": "تاريخ مدربو منتخبات xoxo تحت 24 سنة",
    "national women's xoxo manager history": "تاريخ مدربو منتخبات xoxo وطنية للسيدات",
    "national women's xoxo teams": "منتخبات xoxo وطنية نسائية",
    "national xoxo champions": "أبطال بطولات xoxo وطنية",
    "national xoxo championships": "بطولات xoxo وطنية",
    "national xoxo league": "دوريات xoxo وطنية",
    "national xoxo leagues": "دوريات xoxo وطنية",
    "national xoxo manager history": "تاريخ مدربو منتخبات xoxo وطنية",
    "national xoxo team results": "نتائج منتخبات xoxo وطنية",
    "national xoxo teams": "منتخبات xoxo وطنية",
    "national youth xoxo teams": "منتخبات xoxo وطنية شبابية",
    "outdoor xoxo": "xoxo في الهواء الطلق",
    "outdoor xoxo clubs": "أندية xoxo في الهواء الطلق",
    "outdoor xoxo coaches": "مدربو xoxo في الهواء الطلق",
    "outdoor xoxo competitions": "منافسات xoxo في الهواء الطلق",
    "outdoor xoxo cups": "كؤوس xoxo في الهواء الطلق",
    "outdoor xoxo leagues": "دوريات xoxo في الهواء الطلق",
    "premier xoxo league": "دوريات xoxo من الدرجة الممتازة",
    "premier xoxo leagues": "دوريات xoxo من الدرجة الممتازة",
    "professional xoxo clubs": "أندية xoxo للمحترفين",
    "professional xoxo coaches": "مدربو xoxo للمحترفين",
    "professional xoxo competitions": "منافسات xoxo للمحترفين",
    "professional xoxo cups": "كؤوس xoxo للمحترفين",
    "professional xoxo leagues": "دوريات xoxo للمحترفين",
    "reserve xoxo teams": "فرق xoxo احتياطية",
    "second level xoxo league": "دوريات xoxo من الدرجة الثانية",
    "second level xoxo leagues": "دوريات xoxo من الدرجة الثانية",
    "second tier xoxo league": "دوريات xoxo من الدرجة الثانية",
    "second tier xoxo leagues": "دوريات xoxo من الدرجة الثانية",
    "seventh level xoxo league": "دوريات xoxo من الدرجة السابعة",
    "seventh level xoxo leagues": "دوريات xoxo من الدرجة السابعة",
    "seventh tier xoxo league": "دوريات xoxo من الدرجة السابعة",
    "seventh tier xoxo leagues": "دوريات xoxo من الدرجة السابعة",
    "sixth level xoxo league": "دوريات xoxo من الدرجة السادسة",
    "sixth level xoxo leagues": "دوريات xoxo من الدرجة السادسة",
    "sixth tier xoxo league": "دوريات xoxo من الدرجة السادسة",
    "sixth tier xoxo leagues": "دوريات xoxo من الدرجة السادسة",
    "third level xoxo league": "دوريات xoxo من الدرجة الثالثة",
    "third level xoxo leagues": "دوريات xoxo من الدرجة الثالثة",
    "third tier xoxo league": "دوريات xoxo من الدرجة الثالثة",
    "third tier xoxo leagues": "دوريات xoxo من الدرجة الثالثة",
    "top level xoxo league": "دوريات xoxo من الدرجة الأولى",
    "top level xoxo leagues": "دوريات xoxo من الدرجة الأولى",
    "under-13 xoxo": "xoxo تحت 13 سنة",
    "under-13 xoxo manager history": "تاريخ مدربو فرق xoxo تحت 13 سنة",
    "under-14 xoxo": "xoxo تحت 14 سنة",
    "under-14 xoxo manager history": "تاريخ مدربو فرق xoxo تحت 14 سنة",
    "under-15 xoxo": "xoxo تحت 15 سنة",
    "under-15 xoxo manager history": "تاريخ مدربو فرق xoxo تحت 15 سنة",
    "under-16 xoxo": "xoxo تحت 16 سنة",
    "under-16 xoxo manager history": "تاريخ مدربو فرق xoxo تحت 16 سنة",
    "under-17 xoxo": "xoxo تحت 17 سنة",
    "under-17 xoxo manager history": "تاريخ مدربو فرق xoxo تحت 17 سنة",
    "under-18 xoxo": "xoxo تحت 18 سنة",
    "under-18 xoxo manager history": "تاريخ مدربو فرق xoxo تحت 18 سنة",
    "under-19 xoxo": "xoxo تحت 19 سنة",
    "under-19 xoxo manager history": "تاريخ مدربو فرق xoxo تحت 19 سنة",
    "under-20 xoxo": "xoxo تحت 20 سنة",
    "under-20 xoxo manager history": "تاريخ مدربو فرق xoxo تحت 20 سنة",
    "under-21 xoxo": "xoxo تحت 21 سنة",
    "under-21 xoxo manager history": "تاريخ مدربو فرق xoxo تحت 21 سنة",
    "under-23 xoxo": "xoxo تحت 23 سنة",
    "under-23 xoxo manager history": "تاريخ مدربو فرق xoxo تحت 23 سنة",
    "under-24 xoxo": "xoxo تحت 24 سنة",
    "under-24 xoxo manager history": "تاريخ مدربو فرق xoxo تحت 24 سنة",
    "women's international xoxo": "xoxo دولية للسيدات",
    "women's international xoxo players": "لاعبات xoxo دوليات",
    "women's international xoxo playerss": "لاعبات xoxo دوليات",
    "women's xoxo": "xoxo نسائية",
    "women's xoxo teams": "فرق xoxo نسائية",
    "xoxo chairmen and investors": "رؤساء ومسيرو xoxo",
    "xoxo clubs": "أندية xoxo",
    "xoxo coaches": "مدربو xoxo",
    "xoxo competitions": "منافسات xoxo",
    "xoxo cup competitions": "منافسات كؤوس xoxo",
    "xoxo cups": "كؤوس xoxo",
    "xoxo league competitions": "منافسات دوري xoxo",
    "xoxo league teams": "فرق دوري xoxo",
    "xoxo leagues": "دوريات xoxo",
    "xoxo olympic bronze medalists": "ميداليات xoxo برونزية أولمبية",
    "xoxo olympic gold medalists": "ميداليات xoxo ذهبية أولمبية",
    "xoxo olympic silver medalists": "ميداليات xoxo فضية أولمبية",
    "xoxo races": "سباقات xoxo",
    "xoxo super leagues": "دوريات سوبر xoxo",
    "youth international xoxo": "xoxo دولية شبابية",
    "youth xoxo": "xoxo شبابية",
    "youth xoxo competitions": "منافسات xoxo شبابية"
}

New_team_xo_labels = {
    "xoxo": "xoxo",
    "xoxo league": "دوري xoxo",
    "xoxo finals": "نهائيات xoxo",
    "xoxo champions": "أبطال xoxo",
    "olympics xoxo": "xoxo في الألعاب الأولمبية",
    "summer olympics xoxo": "xoxo في الألعاب الأولمبية الصيفية",
    "winter olympics xoxo": "xoxo في الألعاب الأولمبية الشتوية",
}


def _build_new_team_xo_team_labels() -> dict[str, str]:
    data = {}
    # ---
    # data["asian xoxo tour"] =  "بطولة آسيا xoxo"
    # data["women's asian xoxo tour"] =  "بطولة آسيا xoxo للسيدات"
    # data["ladies asian xoxo tour"] =  "بطولة آسيا xoxo للسيدات"
    # ---tournaments
    data["world champion national xoxo teams"] = "أبطال بطولة العالم xoxo"
    for ioi in ["championships", "championship"]:
        data[f"world xoxo {ioi} competitors"] = "منافسو بطولة العالم xoxo"
        data[f"world xoxo {ioi} medalists"] = "فائزون بميداليات بطولة العالم xoxo"
        # outdoor
        data[f"world wheelchair xoxo {ioi}"] = "بطولة العالم xoxo على الكراسي المتحركة"
        data[f"world xoxo {ioi}"] = "بطولة العالم xoxo"

        data[f"xoxo world {ioi}"] = "بطولة العالم xoxo"

        data[f"world junior xoxo {ioi}"] = "بطولة العالم xoxo للناشئين"
        data[f"world xoxo junior {ioi}"] = "بطولة العالم xoxo للناشئين"
        data[f"xoxo world junior {ioi}"] = "بطولة العالم xoxo للناشئين"
        data[f"xoxo junior world {ioi}"] = "بطولة العالم xoxo للناشئين"

        data[f"world outdoor xoxo {ioi}"] = "بطولة العالم xoxo في الهواء الطلق"
        data[f"outdoor world xoxo {ioi}"] = "بطولة العالم xoxo في الهواء الطلق"

        data[f"world amateur xoxo {ioi}"] = "بطولة العالم xoxo للهواة"
        data[f"world xoxo amateur {ioi}"] = "بطولة العالم xoxo للهواة"
        data[f"xoxo world amateur {ioi}"] = "بطولة العالم xoxo للهواة"
        data[f"xoxo amateur world {ioi}"] = "بطولة العالم xoxo للهواة"

        data[f"world youth xoxo {ioi}"] = "بطولة العالم xoxo للشباب"
        data[f"world xoxo youth {ioi}"] = "بطولة العالم xoxo للشباب"
        data[f"xoxo world youth {ioi}"] = "بطولة العالم xoxo للشباب"
        data[f"xoxo youth world {ioi}"] = "بطولة العالم xoxo للشباب"

        data[f"men's xoxo {ioi}"] = "بطولة xoxo للرجال"
        data[f"women's xoxo {ioi}"] = "بطولة xoxo للسيدات"

        data[f"men's xoxo world {ioi}"] = "بطولة العالم xoxo للرجال"
        data[f"women's xoxo world {ioi}"] = "بطولة العالم xoxo للسيدات"
        data[f"women's world xoxo {ioi}"] = "بطولة العالم xoxo للسيدات"

    # ---World champion national
    data["international xoxo council"] = "المجلس الدولي xoxo"
    data["xoxo world cup"] = "كأس العالم xoxo"
    data["xoxo world cup tournaments"] = "بطولات كأس العالم xoxo"

    # 'Wheelchair Rugby League World Cup': 'كأس العالم لدوري الرجبي على الكراسي المتحركة'
    # data["xoxo league"] = "دوري xoxo"
    # data["xoxo league world cup"] = "كأس العالم لدوري xoxo"
    # data["xoxo league finals"] = "نهائيات دوري xoxo"

    # 'football league': 'دوري لكرة القدم',
    # data["xoxo league"] = "دوري xoxo"

    # 'Wheelchair Rugby League World Cup': 'كأس العالم لدوري الرجبي على الكراسي المتحركة'
    data["xoxo world cup"] = "كأس العالم xoxo"

    data["amateur xoxo world cup"] = "كأس العالم xoxo للهواة"
    data["youth xoxo world cup"] = "كأس العالم xoxo للشباب"
    data["men's xoxo world cup"] = "كأس العالم xoxo للرجال"

    data["women's xoxo world cup"] = "كأس العالم xoxo للسيدات"
    data["women's xoxo world cup tournaments"] = "بطولات كأس العالم xoxo للسيدات"

    return data


New_team_xo_team_labels = _build_new_team_xo_team_labels()
labels_bot = FormatData(New_team_xo_labels, SPORTS_KEYS_FOR_LABEL, key_placeholder="xoxo", value_placeholder="xoxo")
teams_bot = FormatData(New_team_xo_team_labels, SPORTS_KEYS_FOR_TEAM, key_placeholder="xoxo", value_placeholder="xoxo")

new_team_jobs = dict(new_team_xo_jobs)

new_team_jobs.update({
    # Category:Multi-national women's basketball leagues in Europe
    "multi-national women's xoxo leagues": "دوريات xoxo نسائية متعددة الجنسيات",
    # Category:National junior women's goalball teams
    "national junior women's xoxo teams": "منتخبات xoxo للناشئات",
})

new_team_jobs.update({
    # Category:Multi-national women's basketball leagues in Europe
    "multi-national women's xoxo leagues": "دوريات xoxo نسائية متعددة الجنسيات",
    # Category:National junior women's goalball teams
    "national junior women's xoxo teams": "منتخبات xoxo للناشئات",
    "xoxo teams rivalries": "دربيات فرق xoxo",
})

jobs_bot = FormatData(new_team_jobs, SPORTS_KEYS_FOR_JOBS, key_placeholder="xoxo", value_placeholder="xoxo")


@functools.lru_cache(maxsize=None)
def find_labels_bot(category: str, default: str = "") -> str:
    """Search for a generic sports label, returning ``default`` when missing."""
    return labels_bot.search(category) or default


@functools.lru_cache(maxsize=None)
def find_teams_bot(category: str, default: str = "") -> str:
    """Search for a team-related label, returning ``default`` when missing."""
    return teams_bot.search(category) or default


@functools.lru_cache(maxsize=None)
def find_jobs_bot(category: str, default: str = "") -> str:
    """Search for a job-related sports label, returning ``default`` when missing."""
    return jobs_bot.search(category) or default


@functools.lru_cache(maxsize=None)
def wrap_team_xo_normal_2025(team: str) -> str:
    """Normalize a team string and resolve it via the available sports bots."""
    team = team.lower().replace("category:", "")
    result = find_labels_bot(team) or find_teams_bot(team) or find_jobs_bot(team) or ""
    return result.strip()


__all__ = [
    "wrap_team_xo_normal_2025",
    "find_labels_bot",
    "find_teams_bot",
    "find_jobs_bot",
]
