"""
Helpers for resolving sports teams and language categories.

TODO: compare this file with ArWikiCats/new/handle_suffixes.py
"""

from __future__ import annotations

import functools

from ..helps import dump_data, logger
from ..new_resolvers.sports_resolvers import resolve_sports_main
from ..new_resolvers.sports_resolvers.raw_sports import wrap_team_xo_normal_2025_with_ends
from ..translations import SPORTS_KEYS_FOR_JOBS
from . import team_work
from .o_bots.utils import resolve_suffix_template


# @dump_data(1)
def resolve_team_suffix(normalized_team) -> str:
    return resolve_suffix_template(
        normalized_team,
        team_work.Teams_new_end_keys,
        lambda prefix: SPORTS_KEYS_FOR_JOBS.get(prefix, ""),
    )


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

    # _ = resolve_team_suffix(normalized_team)  # TODO: remove after tests

    team_label = (
        resolve_sports_main(normalized_team)
        or wrap_team_xo_normal_2025_with_ends(normalized_team)
        or resolve_team_suffix(normalized_team)
        or ""
    )

    logger.info(f"get_teams_new: {team_label=} for normalized_team: ({normalized_team})")

    return team_label


__all__ = [
    "get_teams_new",
]
