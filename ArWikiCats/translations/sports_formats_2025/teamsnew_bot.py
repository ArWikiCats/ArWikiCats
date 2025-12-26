#!/usr/bin/python3
"""
Usage:
"""

import functools
from typing import Dict
from ..jobs.jobs_players_list import FOOTBALL_KEYS_PLAYERS
from ..sports.Sport_key import SPORTS_KEYS_FOR_JOBS


after_keys: dict[str, str] = {
    "squads": "تشكيلات",
    "finals": "نهائيات",
    "positions": "مراكز",
    "tournaments": "بطولات",
    "films": "أفلام",
    "teams": "فرق",
    "venues": "ملاعب",
    "clubs": "أندية",
    "organizations": "منظمات",
    "non-profit organizations": "منظمات غير ربحية",
    "non-profit publishers": "ناشرون غير ربحيون",
    "organisations": "منظمات",
    "events": "أحداث",
    "umpires": "حكام",
    "trainers": "مدربو",
    "scouts": "كشافة",
    # "people" : "أعلام",
    "coaches": "مدربو",
    "leagues": "دوريات",
    "managers": "مدربو",
    # "managers" : "مدراء",
    # "captains" : "مدربو",
    "playerss": "لاعبو",
    "players": "لاعبو",
    "results": "نتائج",
    "matches": "مباريات",
    "navigational boxes": "صناديق تصفح",
    "lists": "قوائم",
    "home stadiums": "ملاعب",
    "templates": "قوالب",
    "rivalries": "دربيات",
    "champions": "أبطال",
    "competitions": "منافسات",
    "statistics": "إحصائيات",
    "records": "سجلات",
    "records and statistics": "سجلات وإحصائيات",
    "manager history": "تاريخ مدربو",
}


@functools.lru_cache(maxsize=1)
def load_teams_new() -> Dict[str, str]:
    """
    lazy load TEAMS_NEW

    # result length: "count": 325907, "size": "7.3 MiB" ( SPORT_KEY_RECORDS*1425  (223*1425))
    """

    PPP_Keys = {
        "": "",
        "men's": "رجالية",
        "women's": "نسائية",
        "youth": "شبابية",
        "men's youth": "للشباب",
        "women's youth": "للشابات",
        "amateur": "للهواة",
    }

    data = {}
    # 526 item per SPORTS_KEYS_FOR_JOBS items
    for sport, sport_label in SPORTS_KEYS_FOR_JOBS.items():
        data.update(
            {
                f"{sport}": f"{sport_label}",
                # f"{sport} managers": f"مدراء {sport_label}",
                f"{sport} managers": f"مدربو {sport_label}",
                f"{sport} coaches": f"مدربو {sport_label}",
                f"{sport} people": f"أعلام {sport_label}",
                f"{sport} playerss": f"لاعبو {sport_label}",
                f"{sport} players": f"لاعبو {sport_label}",
                f"{sport} referees": f"حكام {sport_label}",
            }
        )
        for PP in PPP_Keys:
            key2 = f"{PP} {sport}".strip()
            value2 = f"{sport_label} {PPP_Keys[PP]}".strip()
            data[key2] = value2
            for after, after_label in after_keys.items():
                data[f"{key2} {after}"] = f"{after_label} {value2}"
            for after in FOOTBALL_KEYS_PLAYERS:
                PP_o = f"{key2} {after}"
                llab = FOOTBALL_KEYS_PLAYERS[after]["males"]
                if "women's" in PP_o:
                    llab = FOOTBALL_KEYS_PLAYERS[after]["females"]
                data[PP_o] = f"{llab} {value2}"
    return data


@functools.lru_cache(maxsize=None)
def teams_new_founder(key: str, default: str = "") -> str:
    """Look up a team label from the cached 2025 dataset."""
    data = load_teams_new()
    return data.get(key, default)


__all__ = [
    "teams_new_founder",
]
