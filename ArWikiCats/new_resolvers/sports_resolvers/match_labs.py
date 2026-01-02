#!/usr/bin/python3
"""
TODO: merge with sports_resolvers/raw_sports.py
"""

import functools

from ...helps import dump_data, logger
from ...new.handle_suffixes import resolve_sport_category_suffix_with_mapping, resolve_suffix_with_mapping_genders
from ...translations.sports.Sport_key import SPORT_KEY_RECORDS
from ...translations_formats import FormatDataV2

teams_2025_sample = {
    "{sport} people": "أعلام {sport_jobs}",
    "{sport} squads": "تشكيلات {sport_jobs}",
    "{sport} finals": "نهائيات {sport_jobs}",
    "{sport} positions": "مراكز {sport_jobs}",
    "{sport} tournaments": "بطولات {sport_jobs}",
    "{sport} films": "أفلام {sport_jobs}",
    "{sport} teams": "فرق {sport_jobs}",
    "{sport} venues": "ملاعب {sport_jobs}",
    "{sport} clubs": "أندية {sport_jobs}",
    "{sport} organizations": "منظمات {sport_jobs}",
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
    "clubs and teams": "أندية وفرق",
    "organizations": "منظمات",
    "non-profit organizations": "منظمات غير ربحية",
    "non-profit publishers": "ناشرون غير ربحيون",
    "organisations": "منظمات",
    "events": "أحداث",
    "scouts": "كشافة",
    "leagues": "دوريات",
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
    "trainers": "مدربو",
    "coaches": "مدربو",
    "managers": "مدربو",
    "people": "أعلام",
    "umpires": "حكام",
    "referees": "حكام",
    "directors": "مدراء",
}

teams_2025 = {
    "{sport}": "{sport_jobs}",
    # "{sport}": "{sport_label}",
    "amateur {sport}": "{sport_jobs} للهواة",
    "mens youth {sport}": "{sport_jobs} للشباب",
    "mens {sport}": "{sport_jobs} رجالية",
    "womens youth {sport}": "{sport_jobs} للشابات",
    "womens {sport}": "{sport_jobs} نسائية",
    "youth {sport}": "{sport_jobs} شبابية",
}

FOOTBALL_KEYS_PLAYERS = {
    "journalists": {"males": "صحفيو", "females": "صحفيات"},
    "players": {"males": "لاعبو", "females": "لاعبات"},
    "placekickers": {"males": "مسددو", "females": "مسددات"},
    "kickers": {"males": "راكلو", "females": "راكلات"},
    "defenders": {"males": "مدافعو", "females": "مدافعات"},
    "forwards": {"males": "مهاجمو", "females": "مهاجمات"},
    "fullbacks": {"males": "مدافعو", "females": "مدافعات"},
    "defencemen": {"males": "مدافعو", "females": "مدافعات"},
    "receivers": {"males": "مستقبلو", "females": "مستقبلات"},
    "tackles": {"males": "مصطدمو", "females": "مصطدمات"},
    "sports-people": {"males": "رياضيو", "females": "رياضيات"},
    "utility players": {"males": "لاعبو مراكز متعددة", "females": "لاعبات مراكز متعددة"},
    "wide receivers": {"males": "مستقبلون واسعون", "females": "مستقبلات واسعات"},
    "peoplee": {"males": "أعلام", "females": "أعلام"},
    "scouts": {"males": "كشافة", "females": "كشافة"},
    "halfbacks": {"males": "أظهرة مساعدون", "females": "ظهيرات مساعدات"},
    "quarterbacks": {"males": "أظهرة رباعيون", "females": "ظهيرات رباعيات"},
    "centers": {"males": "لاعبو وسط", "females": "لاعبات وسط"},
    "centres": {"males": "لاعبو وسط", "females": "لاعبات وسط"},
    "midfielders": {"males": "لاعبو وسط", "females": "لاعبات وسط"},
    "drop kickers": {"males": "مسددو ركلات", "females": "مسددات ركلات"},
    "central defenders": {"males": "قلوب دفاع", "females": "مدافعات مركزيات"},
    "inside forwards": {"males": "مهاجمون داخليون", "females": "مهاجمات داخليات"},
    "outside forwards": {"males": "مهاجمون خارجيون", "females": "مهاجمات خارجيات"},
    "small forwards": {"males": "مهاجمون صغيرو الجسم", "females": "مهاجمات صغيرات الجسم"},
    "power forwards": {"males": "مهاجمون أقوياء الجسم", "females": "مهاجمات قويات الجسم"},
    "defensive backs": {"males": "مدافعون خلفيون", "females": "مدافعات خلفيات"},
    "running backs": {"males": "راكضون للخلف", "females": "راكضات للخلف"},
    "linebackers": {"males": "أظهرة", "females": "ظهيرات"},
    "goalkeepers": {"males": "حراس مرمى", "females": "حارسات مرمى"},
    "goaltenders": {"males": "حراس مرمى", "females": "حارسات مرمى"},
    "guards": {"males": "حراس", "females": "حارسات"},
    "shooting guards": {"males": "مدافعون مسددون", "females": "مدافعات مسددات"},
    "point guards": {"males": "لاعبو هجوم خلفي", "females": "لاعبات هجوم خلفي"},
    "offensive linemen": {"males": "مهاجمو خط", "females": "مهاجمات خط"},
    "defensive linemen": {"males": "مدافعو خط", "females": "مدافعات خط"},
    "left wingers": {"males": "أجنحة يسار", "females": "جناحات يسار"},
    "right wingers": {"males": "أجنحة يمين", "females": "جناحات يمين"},
    "wingers": {"males": "أجنحة", "females": "جناحات"},
    "wing halves": {"males": "أنصاف أجنحة", "females": "جناحات نصفيات"},
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

PPP_Keys = {
    "": "",
    "mens": "رجالية",
    "womens": "نسائية",
    "youth": "شبابية",
    "mens youth": "للشباب",
    "womens youth": "للشابات",
    "amateur": "للهواة",
}


@functools.lru_cache(maxsize=1)
def load_v2() -> FormatDataV2:
    """Load and cache the formatter used for 2025 team categories."""

    sports_data = {
        x: {
            "sport_label": v.get("label", ""),
            "sport_team": v.get("team", ""),
            "sport_jobs": v.get("jobs", ""),
        }
        for x, v in SPORT_KEY_RECORDS.items()
        if v.get("jobs")
    }
    sports_data.pop("sports", None)
    bot = FormatDataV2(
        formatted_data=teams_2025,
        data_list=sports_data,
        key_placeholder="{sport}",
    )

    return bot


def fix_result_callable(result: str, category: str, key: str, value: str) -> str:
    if result.startswith("لاعبو ") and "للسيدات" in result:
        result = result.replace("لاعبو ", "لاعبات ")

    if key == "teams" and "national" in category:
        result = result.replace("فرق ", "منتخبات ")

    return result


@functools.lru_cache(maxsize=None)
def _find_teams_2025(category: str, default: str = "") -> str:
    """Search for a 2025 team label, falling back to ``default`` when absent."""
    bot = load_v2()
    return bot.search_all_category(category) or default


@functools.lru_cache(maxsize=10000)
def fix_keys(category: str) -> str:
    category = category.lower().replace("category:", "")
    category = category.replace("'", "")
    category = category.replace("playerss", "players")

    return category.strip()


# @dump_data(1)
def find_teams_2025(category) -> str:
    category = fix_keys(category)

    logger.debug(f"<<yellow>> start find_teams_2025: {category=}")

    if SPORT_KEY_RECORDS.get(category):
        return SPORT_KEY_RECORDS[category].get("label", "")

    result = _find_teams_2025(category)

    if not result:
        result = resolve_sport_category_suffix_with_mapping(
            category=category,
            data=mappings_data,
            callback=_find_teams_2025,
            fix_result_callable=fix_result_callable,
        )

    if not result:
        result = resolve_suffix_with_mapping_genders(
            category=category,
            data=football_keys_players,
            callback=_find_teams_2025,
            fix_result_callable=fix_result_callable,
        )

    logger.info_if_or_debug(f"<<yellow>> end find_teams_2025: {category=}, {result=}", result)
    return result


__all__ = [
    "find_teams_2025",
]
