#!/usr/bin/python3
"""

"""
from typing import Dict
from ..sports.sports_lists import AFTER_KEYS
from ..jobs.jobs_players_list import FOOTBALL_KEYS_PLAYERS
from ..sports.Sport_key import SPORTS_KEYS_FOR_JOBS
# from ...helps import len_print

PPP_Keys = {
    "": "",
    "men's": "رجالية",
    "women's": "نسائية",
    "youth": "شبابية",
    "men's youth": "للشباب",
    "women's youth": "للشابات",
    "amateur": "للهواة",
}


def load_teams_new() -> Dict[str, str]:
    """
    lazy load TEAMS_NEW

    # result length: "count": 325907, "size": "7.3 MiB" ( SPORT_KEY_RECORDS*1425  (223*1425))
    """
    data = {}
    # 526 item per SPORTS_KEYS_FOR_JOBS items
    for sport, sport_label in SPORTS_KEYS_FOR_JOBS.items():
        data.update({
            f"{sport}" : f"{sport_label}",
            f"{sport} managers" : f"مدراء {sport_label}",
            f"{sport} coaches" : f"مدربو {sport_label}",
            f"{sport} people" : f"أعلام {sport_label}",
            f"{sport} playerss" : f"لاعبو {sport_label}",
            f"{sport} players" : f"لاعبو {sport_label}",
            f"{sport} referees" : f"حكام {sport_label}",
        })
        for PP in PPP_Keys:
            key2 = f"{PP} {sport}".strip()
            value2 = f"{sport_label} {PPP_Keys[PP]}".strip()
            data[key2] = value2
            for after, after_label in AFTER_KEYS.items():
                data[f"{key2} {after}"] = f"{after_label} {value2}"
            for after in FOOTBALL_KEYS_PLAYERS:
                PP_o = f"{key2} {after}"
                llab = FOOTBALL_KEYS_PLAYERS[after]["mens"]
                if "women's" in PP_o:
                    llab = FOOTBALL_KEYS_PLAYERS[after]["womens"]
                data[PP_o] = f"{llab} {value2}"
    return data


__all__ = [
    "load_teams_new",
]
