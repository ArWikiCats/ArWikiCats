#!/usr/bin/python3
"""


"""
import functools
from .team_job import New_team_xo_jobs, New_team_xo_labels
from .te3 import New_team_xo_team_labels
from ..sports.Sport_key import SPORTS_KEYS_FOR_LABEL, SPORTS_KEYS_FOR_TEAM, SPORTS_KEYS_FOR_JOBS
from ...ma_lists_formats.format_data import FormatData


labels_bot = FormatData(New_team_xo_labels, SPORTS_KEYS_FOR_LABEL, key_placeholder="xoxo", value_placeholder="xoxo")
teams_bot = FormatData(New_team_xo_team_labels, SPORTS_KEYS_FOR_TEAM, key_placeholder="xoxo", value_placeholder="xoxo")
jobs_bot = FormatData(New_team_xo_jobs, SPORTS_KEYS_FOR_JOBS, key_placeholder="xoxo", value_placeholder="xoxo")


@functools.lru_cache(maxsize=None)
def find_labels_bot(category: str, default: str="") -> str:
    return labels_bot.search(category) or default


@functools.lru_cache(maxsize=None)
def find_teams_bot(category: str, default: str="") -> str:
    return teams_bot.search(category) or default


@functools.lru_cache(maxsize=None)
def find_jobs_bot(category: str, default: str="") -> str:
    return jobs_bot.search(category) or default


@functools.lru_cache(maxsize=None)
def wrap_team_xo_normal_2025(team: str):
    # ---
    team = team.lower().replace("category:", "")
    # ---
    result = find_labels_bot(team) or find_teams_bot(team) or find_jobs_bot(team) or ""
    # ---
    return result


__all__ = [
    "wrap_team_xo_normal_2025",
]
