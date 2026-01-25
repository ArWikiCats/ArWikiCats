# -*- coding: utf-8 -*-

from .cycling import BASE_CYCLING_EVENTS, CYCLING_TEMPLATES
from .games_labs import SUMMER_WINTER_GAMES, SUMMER_WINTER_TABS
from .Sport_key import (
    SPORT_KEY_RECORDS,
    SPORT_KEY_RECORDS_BASE,
    SPORTS_KEYS_FOR_JOBS,
    SPORTS_KEYS_FOR_LABEL,
    SPORTS_KEYS_FOR_TEAM,
)
from .sub_teams_keys import sub_teams_new, sub_teams_labels, sub_teams_olympics
from .tennis import TENNIS_KEYS

__all__ = [
    "TENNIS_KEYS",
    "SUMMER_WINTER_GAMES",
    "SUMMER_WINTER_TABS",
    "SPORT_KEY_RECORDS",
    "SPORTS_KEYS_FOR_TEAM",
    "SPORT_KEY_RECORDS_BASE",
    "SPORTS_KEYS_FOR_LABEL",
    "SPORTS_KEYS_FOR_JOBS",
    "sub_teams_new",
    "sub_teams_labels",
    "sub_teams_olympics",
    "BASE_CYCLING_EVENTS",
    "CYCLING_TEMPLATES",
]
