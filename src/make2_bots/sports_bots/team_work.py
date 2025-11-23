#!/usr/bin/python3
"""
Sports team and club category processing.
"""

import functools

from ...helps.jsonl_dump import dump_data
from ...helps.log import logger
from ...translations import INTER_FEDS_LOWER, Clubs_key_2, pop_of_football_lower
from ..jobs_bots import bot_te_4
from ..o_bots.utils import resolve_suffix_template

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
    "governing bodies": "هيئات تنظيم {}",
    "bodies": "هيئات {}",
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

# sorted by len of " " in key
Teams_new_end_keys = dict(sorted(Teams_new_end_keys.items(), key=lambda x: x[0].count(" "), reverse=True))


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

# @dump_data()


@functools.lru_cache(maxsize=None)
def Get_team_work_Club(category: str) -> str:
    """Return the Arabic label for ``category`` using known suffixes.

    Args:
        category: The category name to resolve.

    Returns:
        The resolved Arabic label or an empty string if the suffix is unknown.
    """

    normalized = category.strip()
    logger.info(f'get_parties_lab category:"{category}"')

    category_label = resolve_suffix_template(normalized, Teams_new_end_keys, _resolve_club_label)

    if category_label:
        logger.info(f'get_parties_lab category:"{category}", category_label:"{category_label}"')

    return category_label


__all__ = [
    "Teams_new_end_keys",
    "Get_team_work_Club",
]
