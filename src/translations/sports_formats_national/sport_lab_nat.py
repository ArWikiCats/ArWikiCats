#!/usr/bin/python3
""" """

import re

from ...helps.jsonl_dump import dump_data
from ...helps.log import logger
from ..sports.Sport_key import SPORTS_KEYS_FOR_JOBS
from ..utils.match_sport_keys import match_sport_key
from .te2 import New_For_nat_female_xo_team


@dump_data(enable=True)
def Get_sport_formts_female_nat(con_77: str) -> str:  # New_For_nat_female_xo_team
    """
    Resolve female national sport formats into Arabic labels.
    TODO: use FormatData method
    """
    sport_key = match_sport_key(con_77)

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
