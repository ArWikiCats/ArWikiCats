"""Helpers for resolving sports teams and language categories."""

from __future__ import annotations

from typing import Dict

from ... import malists_sport_lab as sport_lab
from ...helps.log import logger
from ...helps.print_bot import print_put
from ...ma_lists import SPORTS_KEYS_FOR_JOBS
from . import team_work
from ..o_bots.utils import resolve_suffix_template

LANGUAGE_CACHE: Dict[str, str] = {}


def get_teams_new(team_name: str) -> str:
    """Return the label for ``team_name`` using multiple heuristics.

    Args:
        team_name: The English club or team name to translate.

    Returns:
        The resolved Arabic label or an empty string when no mapping exists.
    """

    # إيجاد لاحقات التسميات الرياضية

    # قبل تطبيق الوظيفة
    # sports.py: len:"Teams new":  685955
    # بعد تطبيق الوظيفة
    # sports.py: len:"Teams new":  114691

    normalized_team = team_name.strip()
    print_put(f'get_teams_new team:"{normalized_team}"')
    logger.info(f"get_teams_new: Resolving team label, team: {normalized_team}")

    team_label = sport_lab.Get_New_team_xo(normalized_team)

    if not team_label:
        team_label = resolve_suffix_template(
            normalized_team,
            team_work.Teams_new_end_keys,
            lambda prefix: SPORTS_KEYS_FOR_JOBS.get(prefix, ""),
        )
        if team_label:
            print_put(f'get_teams_new: team_label:"{team_label}" from sports suffix lookup')

    return team_label


__all__ = [
    "get_teams_new",
]
