#!/usr/bin/python3
"""
Sports team and club category processing.

This module handles translation of sports-related categories,
particularly for teams, clubs, and sports organizations.

Example usage:
    from make.bots import team_work
    team_work.Get_Club(cate, out=False)
    team_work.Teams_new_end_keys
"""

import functools
from ...helps.log import logger

from ...translations import Clubs_key_2
from ...translations import INTER_FEDS_LOWER
from ...translations import pop_of_football_lower
from ..jobs_bots import bot_te_4
from ..lazy_data_bots.bot_2018 import Add_to_pop_All_18

from ...helps.jsonl_dump import save_data

Teams_new_end_keys = {
    "fan clubs": "أندية معجبي {}",
    "broadcasters": "مذيعو {}",
    "commentators": "معلقو {}",
    "commissioners": "مفوضو {}",
    "owners and executives": "رؤساء تنفيذيون وملاك {}",
    "personnel": "أفراد {}",
    "owners": "ملاك {}",
    "executives": "مدراء {}",
    "equipment": "معدات {}",
    "culture": "ثقافة {}",
    "logos": "شعارات {}",
    "tactics and skills": "مهارات {}",
    "media": "إعلام {}",
    "people": "أعلام {}",
    "terminology": "مصطلحات {}",
    "occupations": "مهن {}",
    "variants": "أشكال {}",
    "bodies": "هيئات {}",
    "governing bodies": "هيئات تنظيم {}",
    "video games": "ألعاب فيديو {}",
    "chairmen and investors": "رؤساء ومسيرو {}",
    "comics": "قصص مصورة {}",
    "cups": "كؤوس {}",
    "records and statistics": "سجلات وإحصائيات {}",
    "leagues": "دوريات {}",
    "leagues seasons": "مواسم دوريات {}",
    "seasons": "مواسم {}",
    "competition": "منافسات {}",
    "competitions": "منافسات {}",
    "world competitions": "منافسات {} عالمية",
    "teams": "فرق {}",
    "television series": "مسلسلات تلفزيونية {}",
    "films": "أفلام {}",
    "championships": "بطولات {}",
    "music": "موسيقى {}",
    "clubs": "أندية {}",
    "referees": "حكام {}",
    "organizations": "منظمات {}",
    "non-profit organizations": "منظمات غير ربحية {}",
    "non-profit publishers": "ناشرون غير ربحيون {}",
    "stadiums": "ملاعب {}",
    "lists": "قوائم {}",
    "awards": "جوائز {}",
    "songs": "أغاني {}",
    "non-playing staff": "طاقم {} غير اللاعبين",
    "trainers": "مدربو {}",
    "umpires": "حكام {}",
    "cup playoffs": "تصفيات كأس {}",
    "cup": "كأس {}",
    "coaches": "مدربو {}",
    "managers": "مدربو {}",  # "مدراء {}"
    "manager": "مدربو {}",
    "manager history": "تاريخ مدربو {}",
    "footballers": "لاعبو {}",
    "playerss": "لاعبو {}",
    "players": "لاعبو {}",
    "results": "نتائج {}",
    "matches": "مباريات {}",
    "rivalries": "دربيات {}",
    "champions": "أبطال {}",
}


def _extract_club_key(category: str, suffix: str) -> str:
    """Extract club key from category with given suffix.

    Args:
        category: Normalized category string
        suffix: The suffix to check for

    Returns:
        Club key if found, empty string otherwise
    """
    team_suffix = f" team {suffix}"
    if category.endswith(team_suffix):
        return category[: -len(team_suffix)]

    simple_suffix = f" {suffix}"
    if category.endswith(simple_suffix):
        return category[: -len(simple_suffix)]

    return ""


def _resolve_club_label(club_key: str) -> str:
    """Resolve club label from various lookup tables.

    Args:
        club_key: The club key to look up

    Returns:
        Resolved club label or empty string
    """
    club_lab = Clubs_key_2.get(club_key) or pop_of_football_lower.get(club_key) or INTER_FEDS_LOWER.get(club_key) or ""

    if not club_lab:
        club_lab = bot_te_4.te_2018_with_nat(club_key)

    return club_lab


@save_data()
@functools.lru_cache(maxsize=None)
def Get_Club(
    category: str,
    return_tab: bool = False,
) -> str | dict[str, str | dict[str, str]]:
    """Get club/team category label.

    Args:
        category: The category string to process
        return_tab: If True, return dict with metadata; if False, return label string

    Returns:
        Either a string label or a dict with 'lab' and 'add' keys
    """
    new_entries = {}
    normalized_category = category.lower()
    category_label = ""
    result = {"lab": "", "add": {}}

    for suffix, suffix_template in Teams_new_end_keys.items():
        club_key = _extract_club_key(normalized_category, suffix)

        if not club_key:
            continue

        logger.debug(f'club_uu:"{club_key}", tat:"{suffix}" ')
        club_lab = _resolve_club_label(club_key)

        if club_lab:
            category_label = suffix_template.format(club_lab)
            break

    if category_label:
        logger.debug(f'Get_Club cate:"{normalized_category}", catelab:"{category_label}"')

    result["lab"] = category_label
    Add_to_pop_All_18(new_entries)

    return result if return_tab else category_label


def Get_team_work_Club(category: str) -> str:
    """Get team work club label (convenience wrapper).

    Args:
        category: The category string to process

    Returns:
        Club label string
    """
    label = ""

    slab = Get_Club(category, return_tab=True)

    if isinstance(slab, str):
        return slab

    label = slab.get("lab", "")

    return label
