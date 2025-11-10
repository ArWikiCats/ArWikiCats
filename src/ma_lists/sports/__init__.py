# -*- coding: utf-8 -*-

from .tennis import tennis_keys
from .nat_p17 import sport_formts_for_p17, nat_p17_oioi
from .teams_new_data import Teams_new
from .games_labs import summer_winter_games
from .skeys import (
    sport_formts_en_ar_is_p17,
    sport_formts_en_p17_ar_nat,
    sport_formts_enar_p17_team,
    sport_formts_new_kkk,
    sport_formts_male_nat,
    sport_formts_female_nat,
)

from .Sport_key import fanco_line, Sports_Keys_For_Team, Sports_Keys_For_Label, Sports_Keys_For_Jobs
from .olympics_data import olympics

__all__ = [
    "tennis_keys",
    "Teams_new",
    "sport_formts_en_ar_is_p17",
    "sport_formts_en_p17_ar_nat",
    "sport_formts_enar_p17_team",
    "sport_formts_new_kkk",
    "sport_formts_male_nat",
    "sport_formts_female_nat",
    "sport_formts_for_p17",
    "nat_p17_oioi",
    "summer_winter_games",
    "fanco_line",
    "Sports_Keys_For_Team",
    "Sports_Keys_For_Label",
    "Sports_Keys_For_Jobs",
    "olympics",
]
