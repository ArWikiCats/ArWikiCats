#!/usr/bin/python3
""" """

import functools

# from ...helps.jsonl_dump import dump_data
from ...translations_formats import FormatData
from ..sports.Sport_key import (
    SPORTS_KEYS_FOR_JOBS,
    SPORTS_KEYS_FOR_LABEL,
    SPORTS_KEYS_FOR_TEAM,
)
from .team_job import New_team_xo_jobs, new_team_xo_jobs_additional

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

new_team_jobs = New_team_xo_jobs
# new_team_jobs = new_team_xo_jobs_additional | New_team_xo_jobs

new_team_jobs.update({
    # Category:Multi-national women's basketball leagues in Europe
    "multi-national women's xoxo leagues": "دوريات xoxo نسائية متعددة الجنسيات",
    # Category:National junior women's goalball teams
    "national junior women's xoxo teams": "منتخبات xoxo للناشئات"
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
