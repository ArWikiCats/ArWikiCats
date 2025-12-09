#!/usr/bin/python3
""" """

import functools

# from ...helps.jsonl_dump import dump_data
from ...translations_formats import FormatData
from ..sports.Sport_key import (
    SPORTS_KEYS_FOR_JOBS,
    SPORTS_KEYS_FOR_LABEL,
    SPORTS_KEYS_FOR_TEAM,
)
from .te3 import New_team_xo_team_labels
from .team_job import New_team_xo_jobs, New_team_xo_labels, new_team_xo_jobs_additional

labels_bot = FormatData(New_team_xo_labels, SPORTS_KEYS_FOR_LABEL, key_placeholder="xoxo", value_placeholder="xoxo")
teams_bot = FormatData(New_team_xo_team_labels, SPORTS_KEYS_FOR_TEAM, key_placeholder="xoxo", value_placeholder="xoxo")

# new_team_jobs = new_team_xo_jobs_additional | New_team_xo_jobs
new_team_jobs = New_team_xo_jobs
jobs_bot = FormatData(new_team_jobs, SPORTS_KEYS_FOR_JOBS, key_placeholder="xoxo", value_placeholder="xoxo")


@functools.lru_cache(maxsize=None)
def find_labels_bot(category: str, default: str = "") -> str:
    """Search for a generic sports label, returning ``default`` when missing."""
    return labels_bot.search(category) or default


@functools.lru_cache(maxsize=None)
def find_teams_bot(category: str, default: str = "") -> str:
    """Search for a team-related label, returning ``default`` when missing."""
    return teams_bot.search(category) or default


@functools.lru_cache(maxsize=None)
def find_jobs_bot(category: str, default: str = "") -> str:
    """Search for a job-related sports label, returning ``default`` when missing."""
    return jobs_bot.search(category) or default


@functools.lru_cache(maxsize=None)
def wrap_team_xo_normal_2025(team: str) -> str:
    """Normalize a team string and resolve it via the available sports bots."""
    team = team.lower().replace("category:", "")
    result = find_labels_bot(team) or find_teams_bot(team) or find_jobs_bot(team) or ""
    return result.strip()


__all__ = [
    "wrap_team_xo_normal_2025",
    "find_labels_bot",
    "find_teams_bot",
    "find_jobs_bot",
]
