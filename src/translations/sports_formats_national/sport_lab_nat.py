#!/usr/bin/python3
"""

TODO: Replaced by sport_lab_nat_new_2026.py

"""

import re
import functools
from ...helps.log import logger
from ..sports.Sport_key import SPORTS_KEYS_FOR_JOBS
from ..utils.match_sport_keys import match_sport_key
from .te2 import New_For_nat_female_xo_team

from ...translations import (
    Nat_women,
)
from ...make2_bots.jobs_bots.get_helps import get_con_3


@functools.lru_cache(maxsize=None)
def Get_sport_formts_female_nat(con_77: str) -> str:  # New_For_nat_female_xo_team
    """
    Resolve female national sport formats into Arabic labels.
    Example:
        con_77: "under-13 baseball teams", result: "فرق كرة قاعدة {nat} تحت 13 سنة"
    """
    sport_key = match_sport_key(con_77)
    print(f"Get_sport_formts_female_nat {con_77=} sport_key:{sport_key=}")

    if not sport_key:
        return ""

    result = ""

    normalized_team_key = con_77.replace(sport_key, "xzxz")
    normalized_team_key = re.sub(sport_key, "xzxz", normalized_team_key, flags=re.IGNORECASE)

    logger.info(f'Get_sport_formts_female_nat female con_77:"{con_77}", sport_key:"{sport_key}", team_xz:"{normalized_team_key}"')

    template_label = New_For_nat_female_xo_team.get(normalized_team_key, "")

    if not template_label:
        logger.info(f'Get_sport_formts_female_nat female team_xz:"{normalized_team_key}" not in New_For_nat_female_xo_team')
        return ""

    sport_arabic_label = SPORTS_KEYS_FOR_JOBS.get(sport_key, "")
    if not sport_arabic_label:
        logger.info(f' sport_key:"{sport_key}" not in SPORTS_KEYS_FOR_JOBS ')

    if not template_label or not sport_arabic_label:
        return ""

    resolved_label = template_label.replace("xzxz", sport_arabic_label)

    if "xzxz" in resolved_label:
        return ""

    result = resolved_label
    logger.info(f'Get_sport_formts_female_nat female con_77:"{con_77}", result:"{result}"')

    return result


@functools.lru_cache(maxsize=None)
def sport_lab_nat_load(category: str, check_the: bool=False) -> str:
    """
    Example:
        category:Yemeni under-13 baseball teams", result: "فرق كرة قاعدة يمنية تحت 13 سنة"
    """
    normalized_category = category.lower()

    sport_format_key, country_start = get_con_3(normalized_category, "nat", check_the=check_the)

    print(f"sport_lab_nat_load {normalized_category=}: {sport_format_key=} {country_start=}")

    if not country_start or not sport_format_key:
        return ""

    nat_lab = Nat_women.get(country_start, "")

    if not nat_lab:
        return ""

    sport_format_label = Get_sport_formts_female_nat(sport_format_key)
    if not sport_format_label:
        return ""

    category_label = sport_format_label.format(nat=nat_lab)
    logger.debug(f'<<lightblue>>xxx sport_lab_nat_load: new category_label  "{category_label}"')

    return category_label


__all__ = [
    "Get_sport_formts_female_nat",
    "sport_lab_nat_load",
]
