#!/usr/bin/python3
"""


"""

import re
# ---
from .te2 import New_For_nat_female_xo_team
from ..sports.Sport_key import SPORTS_KEYS_FOR_JOBS
from ...helps.log import logger
from ..utils.match_sport_keys import match_sport_key


def Get_sport_formts_female_nat(con_77: str) -> str:  # New_For_nat_female_xo_team
    # قبل تطبيق الوظيفة
    # sports.py: len:"SPORT_FORMTS_FEMALE_NAT":  549000
    # بعد تطبيق الوظيفة
    # sports.py: len:"New_For_nat_female_xo_team":  1528  , len:"SPORT_FORMTS_FEMALE_NAT":  0
    label = ""
    sport_key = match_sport_key(con_77)
    if sport_key:
        sport_arabic_label = ""
        template_label = ""
        normalized_team_key = con_77.replace(sport_key, "xzxz")
        normalized_team_key = re.sub(sport_key, "xzxz", normalized_team_key, flags=re.IGNORECASE)
        logger.info(
            f'Get_Sport_Formats_For_nat female con_77:"{con_77}", sport_key:"{sport_key}", team_xz:"{normalized_team_key}"'
        )
        if normalized_team_key in New_For_nat_female_xo_team:
            sport_arabic_label = SPORTS_KEYS_FOR_JOBS.get(sport_key, "")
            if not sport_arabic_label:
                logger.info(f' sport_key:"{sport_key}" not in SPORTS_KEYS_FOR_JOBS ')
            template_label = New_For_nat_female_xo_team[normalized_team_key]
            if template_label and sport_arabic_label:
                resolved_label = template_label.replace("xzxz", sport_arabic_label)
                if "xzxz" not in resolved_label:
                    label = resolved_label
                    logger.info(f'Get_Sport_Formats_For_nat female bbvb:"{label}"')
        else:
            logger.info(
                f'Get_Sport_Formats_For_nat female team_xz:"{normalized_team_key}" not in New_For_nat_female_xo_team'
            )
    if label:
        logger.info(f'Get_Sport_Formats_For_nat female con_77:"{con_77}", label:"{label}"')
    return label
