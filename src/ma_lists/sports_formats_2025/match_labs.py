#!/usr/bin/python3
"""

"""
import functools
from typing import Dict
from ..sports.Sport_key import Sports_Keys_For_Jobs
from ..sports.sports_lists import AFTER_KEYS
from ..jobs.jobs_players_list import FOOTBALL_KEYS_PLAYERS
from ...ma_lists_formats.format_data import FormatData
from ...helps import len_print


teams_2025_sample = {
    "{sport}": "{sport_label}",
    "{sport} managers": "مدراء {sport_label}",
    "{sport} coaches": "مدربو {sport_label}",
    "{sport} people": "أعلام {sport_label}",
    "{sport} playerss": "لاعبو {sport_label}",
    "{sport} players": "لاعبو {sport_label}",
    "{sport} referees": "حكام {sport_label}",
    "{sport} squads": "تشكيلات {sport_label}",
    "{sport} finals": "نهائيات {sport_label}",
    "{sport} positions": "مراكز {sport_label}",
    "{sport} tournaments": "بطولات {sport_label}",
    "{sport} films": "أفلام {sport_label}",
    "{sport} teams": "فرق {sport_label}",
    "{sport} venues": "ملاعب {sport_label}",
    "{sport} clubs": "أندية {sport_label}",
    "{sport} organizations": "منظمات {sport_label}",
}

PPP_Keys = {
    "": "",
    "men's": "رجالية",
    "women's": "نسائية",
    "youth": "شبابية",
    "men's youth": "للشباب",
    "women's youth": "للشابات",
    "amateur": "للهواة",
}


@functools.lru_cache(maxsize=1)
def load_data() -> Dict[str, str]:
    """
    lazy load Teams_new

    # result length: "count": 325907, "size": "7.3 MiB" ( Sports_Keys_New*1425  (223*1425))
    """
    # ---
    data = {}
    # ---
    # 526 item per Sports_Keys_For_Jobs items
    # ---
    sport = "{sport}"
    sport_label = "{sport_label}"
    # ---
    data = {
        f"{sport}" : f"{sport_label}",
        f"{sport} managers" : f"مدراء {sport_label}",
        f"{sport} coaches" : f"مدربو {sport_label}",
        f"{sport} people" : f"أعلام {sport_label}",
        f"{sport} playerss" : f"لاعبو {sport_label}",
        f"{sport} players" : f"لاعبو {sport_label}",
        f"{sport} referees" : f"حكام {sport_label}",
    }

    for PP in PPP_Keys:
        key2 = f"{PP} {sport}".strip()
        value2 = f"{sport_label} {PPP_Keys[PP]}".strip()
        # ---
        data[key2] = value2
        # ---
        for after, after_label in AFTER_KEYS.items():
            data[f"{key2} {after}"] = f"{after_label} {value2}"
        # ---
        for after in FOOTBALL_KEYS_PLAYERS:
            PP_o = f"{key2} {after}"
            # ---
            llab = FOOTBALL_KEYS_PLAYERS[after]["mens"]
            if "women's" in PP_o:
                llab = FOOTBALL_KEYS_PLAYERS[after]["womens"]
            # ---
            data[PP_o] = f"{llab} {value2}"

    return data


@functools.lru_cache(maxsize=1)
def load_class() -> FormatData:
    teams_2025 = load_data()

    bot = FormatData(teams_2025, Sports_Keys_For_Jobs, key_placeholder="{sport}", value_placeholder="{sport_label}")

    return bot


@functools.lru_cache(maxsize=None)
def find_teams_2025(category: str, default: str="") -> str:
    bot = load_class()
    return bot.search(category) or default


len_print.data_len("sports/teams_new_data_2025.py", {
    "teams_2025" : 533  # teams_2025: 533 <> "Teams_new": "352,946",
})

__all__ = [
    "find_teams_2025",
    "load_data",
]
