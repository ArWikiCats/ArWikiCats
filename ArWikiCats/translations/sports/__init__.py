# -*- coding: utf-8 -*-

from .games_labs import SUMMER_WINTER_GAMES
from .olympics_data import olympic_event_translations
from .Sport_key import SPORTS_KEYS_FOR_JOBS, SPORTS_KEYS_FOR_LABEL, SPORTS_KEYS_FOR_TEAM
from .tennis import TENNIS_KEYS

__all__ = [
    "TENNIS_KEYS",
    "SUMMER_WINTER_GAMES",
    "SPORTS_KEYS_FOR_TEAM",
    "SPORTS_KEYS_FOR_LABEL",
    "SPORTS_KEYS_FOR_JOBS",
    "olympic_event_translations",
]
