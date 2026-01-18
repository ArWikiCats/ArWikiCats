"""
Helpers for resolving sports teams and language categories.

TODO: compare this file with ArWikiCats/new/handle_suffixes.py
"""

from __future__ import annotations

from ..translations import SPORTS_KEYS_FOR_JOBS
from . import team_work
from .o_bots.utils import resolve_suffix_template


def resolve_team_suffix(normalized_team) -> str:
    """Resolve team suffix for sports categories.

    Args:
        normalized_team (str): The normalized team name.

    Returns:
        str: The resolved team suffix.
    """
    return resolve_suffix_template(
        normalized_team,
        team_work.Teams_new_end_keys,
        lambda prefix: SPORTS_KEYS_FOR_JOBS.get(prefix, ""),
    )


__all__ = [
    "resolve_team_suffix",
]
