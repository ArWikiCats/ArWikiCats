#!/usr/bin/python3
"""


"""
import functools
from .team_job import New_team_xo_jobs, New_team_xo_labels
from .te3 import New_team_xo_team_labels
from ..sports.Sport_key import Sports_Keys_For_Label, Sports_Keys_For_Team, Sports_Keys_For_Jobs
from ...ma_lists_formats.format_data import FormatData


labels_bot = FormatData(New_team_xo_labels, Sports_Keys_For_Label, key_placeholder="xoxo", value_placeholder="xoxo")
teams_bot = FormatData(New_team_xo_team_labels, Sports_Keys_For_Team, key_placeholder="xoxo", value_placeholder="xoxo")
jobs_bot = FormatData(New_team_xo_jobs, Sports_Keys_For_Jobs, key_placeholder="xoxo", value_placeholder="xoxo")


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
