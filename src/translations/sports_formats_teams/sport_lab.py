#!/usr/bin/python3
""" """

import re

from ...helps.log import logger
from ..sports.Sport_key import SPORTS_KEYS_FOR_JOBS, SPORTS_KEYS_FOR_TEAM
from ..sports_formats_nats.new import create_label
from ..sports_formats_teams.te3 import SPORT_FORMTS_ENAR_P17_TEAM
from ..utils import apply_pattern_replacement
from ..utils.match_sport_keys import match_sport_key
from .sport_lab2 import wrap_team_xo_normal_2025
from .team_job import sport_formts_enar_p17_jobs


def Get_Sport_Format_xo_en_ar_is_P17(suffix: str) -> str:  # sport_formts_enar_p17_jobs
    """
    Return a sport label that merges templates with Arabic sport names.

    Example:
        suffix: "winter olympics softball", return: "كرة لينة {} في الألعاب الأولمبية الشتوية"
    """
    con_3_label = ""

    sport_key = match_sport_key(suffix)
    if not sport_key:
        return ""

    sport_label = ""

    template_label = ""
    normalized_key = suffix.replace(sport_key, "xoxo")
    normalized_key = re.sub(sport_key, "xoxo", normalized_key, flags=re.IGNORECASE)

    logger.info(f'Get_SFxo_en_ar_is P17: suffix:"{suffix}", sport_key:"{sport_key}", team_xoxo:"{normalized_key}"')

    if normalized_key in sport_formts_enar_p17_jobs:
        sport_label = SPORTS_KEYS_FOR_JOBS[sport_key]
        template_label = sport_formts_enar_p17_jobs.get(normalized_key, "")

    elif normalized_key in SPORT_FORMTS_ENAR_P17_TEAM:
        sport_label = SPORTS_KEYS_FOR_TEAM[sport_key]
        template_label = SPORT_FORMTS_ENAR_P17_TEAM.get(normalized_key, "")

    else:
        logger.info(
            f'Get_SFxo_en_ar_is P17 team_xoxo:"{normalized_key}" not in sport_formts_enar_p17_jobs or SPORT_FORMTS_ENAR_P17_TEAM'
        )

    if template_label and sport_label:
        con_3_label = apply_pattern_replacement(template_label, sport_label, "xoxo")
        logger.info(f'Get_SFxo_en_ar_is P17 blab:"{con_3_label}"')
    else:
        logger.info(f'Get_SFxo_en_ar_is P17 team_xoxo:"{normalized_key}" not in sport_formts_enar_p17_jobs')

    if con_3_label:
        logger.info(f'Get_SFxo_en_ar_is P17 suffix:"{suffix}", con_3_label:"{con_3_label}"')

    return con_3_label


def get_new_team_xo(team: str) -> str:
    """Resolve team labels with 2026-format templates and fallbacks."""
    team_lab = wrap_team_xo_normal_2025(team)
    if not team_lab:
        team_lab = create_label(team)
    return team_lab


__all__ = [
    "Get_Sport_Format_xo_en_ar_is_P17",
    "get_new_team_xo",
]
