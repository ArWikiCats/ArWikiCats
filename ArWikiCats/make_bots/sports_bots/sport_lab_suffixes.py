"""Helpers for resolving sports teams and language categories."""

from __future__ import annotations

import functools

from ...helps.log import logger
from ...translations import SPORTS_KEYS_FOR_JOBS
from ..o_bots.utils import resolve_suffix_template
from ...translations_resolvers.nats_new import nats_new_create_label
from ...translations.sports_formats_teams.sport_lab2 import wrap_team_xo_normal_2025
from . import team_work


@functools.lru_cache(maxsize=10000)
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
    logger.info(f'start get_teams_new team:"{normalized_team}"')
    logger.debug(f"get_teams_new: Resolving team label, team: {normalized_team}")

    team_label = wrap_team_xo_normal_2025(normalized_team) or nats_new_create_label(normalized_team)

    if not team_label:
        team_label = resolve_suffix_template(
            normalized_team,
            team_work.Teams_new_end_keys,
            lambda prefix: SPORTS_KEYS_FOR_JOBS.get(prefix, ""),
        )
    if team_label:
        logger.info(f'get_teams_new: team_label:"{team_label}" for normalized_team: ({normalized_team})')

    return team_label


__all__ = [
    "get_teams_new",
]
