#!/usr/bin/python3
""" """

import functools
from typing import Dict

from ...helps import len_print
from ...translations_formats import FormatData
from ...translations.jobs.jobs_players_list import FOOTBALL_KEYS_PLAYERS
from ...translations.sports.Sport_key import SPORTS_KEYS_FOR_JOBS

teams_2025_sample = {
    # "{sport}": "{sport_label}",
    # "{sport} managers": "مدراء {sport_label}",
    "{sport} managers": "مدربو {sport_label}",
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
def load_data() -> Dict[str, str]:
    """
    lazy load TEAMS_NEW

    # result length: "count": 325907, "size": "7.3 MiB" ( SPORT_KEY_RECORDS*1425  (223*1425))
    """
    data = {}
    # 526 item per SPORTS_KEYS_FOR_JOBS items
    sport = "{sport}"
    sport_label = "{sport_label}"
    data = {
        # f"{sport}": f"{sport_label}",
        # f"{sport} managers": f"مدراء {sport_label}",
        f"{sport} managers": f"مدربو {sport_label}",
        f"{sport} coaches": f"مدربو {sport_label}",
        f"{sport} people": f"أعلام {sport_label}",
        f"{sport} playerss": f"لاعبو {sport_label}",
        f"{sport} players": f"لاعبو {sport_label}",
        f"{sport} referees": f"حكام {sport_label}",
    }

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


@functools.lru_cache(maxsize=1)
def load_class() -> FormatData:
    """Load and cache the formatter used for 2025 team categories."""
    teams_2025 = load_data()

    bot = FormatData(teams_2025, SPORTS_KEYS_FOR_JOBS, key_placeholder="{sport}", value_placeholder="{sport_label}")

    return bot


@functools.lru_cache(maxsize=None)
def find_teams_2025(category: str, default: str = "") -> str:
    """Search for a 2025 team label, falling back to ``default`` when absent."""
    bot = load_class()
    return bot.search(category) or default


len_print.data_len("sports/teams_new_data_2025.py", {"teams_2025": load_data()})  # teams_2025: 526 <> "TEAMS_NEW": "352,946",

__all__ = [
    "find_teams_2025",
    "load_data",
]
