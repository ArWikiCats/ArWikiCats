# -*- coding: utf-8 -*-

from .games_labs import SUMMER_WINTER_GAMES
from .olympics_data import olympics
from .skeys import (
    SPORT_FORMTS_FEMALE_NAT,
    SPORT_FORMTS_MALE_NAT,
)
from .Sport_key import SPORTS_KEYS_FOR_JOBS, SPORTS_KEYS_FOR_LABEL, SPORTS_KEYS_FOR_TEAM
from .tennis import TENNIS_KEYS

__all__ = [
    "TENNIS_KEYS",
    "SPORT_FORMTS_MALE_NAT",
    "SPORT_FORMTS_FEMALE_NAT",
    "SUMMER_WINTER_GAMES",
    "SPORTS_KEYS_FOR_TEAM",
    "SPORTS_KEYS_FOR_LABEL",
    "SPORTS_KEYS_FOR_JOBS",
    "olympics",
]
