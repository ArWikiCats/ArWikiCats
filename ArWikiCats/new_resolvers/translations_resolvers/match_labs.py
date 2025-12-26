#!/usr/bin/python3
""" """

import functools
from typing import Dict

from ...helps import len_print
from ...new.handle_suffixes import resolve_sport_category_suffix_with_mapping, resolve_suffix_with_mapping_genders
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
    "mens": "رجالية",
    "womens": "نسائية",
    "youth": "شبابية",
    "mens youth": "للشباب",
    "womens youth": "للشابات",
    "amateur": "للهواة",
}


mappings_data: dict[str, str] = {
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
    "coaches": "مدربو",
    "leagues": "دوريات",
    "managers": "مدربو",
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

mappings_data = dict(
    sorted(
        mappings_data.items(),
        key=lambda k: (-k[0].count(" "), -len(k[0])),
    )
)

football_keys_players = dict(
    sorted(
        FOOTBALL_KEYS_PLAYERS.items(),
        key=lambda k: (-k[0].count(" "), -len(k[0])),
    )
)


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

        # for after, after_label in mappings_data.items(): data[f"{key2} {after}"] = f"{after_label} {value2}"

        for after in FOOTBALL_KEYS_PLAYERS:
            PP_o = f"{key2} {after}"
            llab = FOOTBALL_KEYS_PLAYERS[after]["males"]
            if "womens" in PP_o:
                llab = FOOTBALL_KEYS_PLAYERS[after]["females"]

            data[PP_o] = f"{llab} {value2}"

    return data


@functools.lru_cache(maxsize=1)
def load_class() -> FormatData:
    """Load and cache the formatter used for 2025 team categories."""
    teams_2025 = load_data()

    bot = FormatData(teams_2025, SPORTS_KEYS_FOR_JOBS, key_placeholder="{sport}", value_placeholder="{sport_label}")

    return bot


def fix_result_callable(result, category, key, value):
    if result.startswith("لاعبو ") and "للسيدات" in result:
        result = result.replace("لاعبو ", "لاعبات ")

    if key == "teams" and "national" in category:
        result = result.replace("فرق ", "منتخبات ")

    return result


@functools.lru_cache(maxsize=None)
def _find_teams_2025(category: str, default: str = "") -> str:
    """Search for a 2025 team label, falling back to ``default`` when absent."""
    bot = load_class()
    return bot.search(category) or default


@functools.lru_cache(maxsize=10000)
def fix_keys(category: str) -> str:
    category = category.replace("'", "").lower().replace("category:", "")

    return category.strip()


def find_teams_2025(category) -> str:
    category = fix_keys(category)

    label2 = _find_teams_2025(category)

    if not label2:
        label2 = resolve_sport_category_suffix_with_mapping(
            category=category,
            data=mappings_data,
            callback=_find_teams_2025,
            fix_result_callable=fix_result_callable,
        )

    if not label2:
        label2 = resolve_suffix_with_mapping_genders(
            category=category,
            data=mappings_data,
            callback=_find_teams_2025,
            fix_result_callable=fix_result_callable,
        )

    return label2


len_print.data_len("sports/teams_new_data_2025.py", {"teams_2025": load_data()})  # teams_2025: 526 <> "TEAMS_NEW": "352,946",

__all__ = [
    "find_teams_2025",
    "load_data",
]
