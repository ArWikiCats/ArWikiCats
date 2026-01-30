#!/usr/bin/python3
""" """

import functools

from ...helps import getLogger
from ...new.handle_suffixes import (
    resolve_sport_category_suffix_with_mapping,
    resolve_suffix_with_mapping_genders,
)
from .pre_defined import pre_defined_results
from .raw_sports import resolve_sport_label_unified

logger = getLogger(__name__)

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
    "chairmen and investors": "رؤساء ومسيرو",
    "cups": "كؤوس",
}

FOOTBALL_KEYS_PLAYERS = {
    "centers": {"males": "لاعبو وسط", "females": "لاعبات وسط"},
    "central defenders": {"males": "قلوب دفاع", "females": "مدافعات مركزيات"},
    "centres": {"males": "لاعبو وسط", "females": "لاعبات وسط"},
    "defencemen": {"males": "مدافعو", "females": "مدافعات"},
    "defenders": {"males": "مدافعو", "females": "مدافعات"},
    "defensive backs": {"males": "مدافعون خلفيون", "females": "مدافعات خلفيات"},
    "defensive linemen": {"males": "مدافعو خط", "females": "مدافعات خط"},
    "drop kickers": {"males": "مسددو ركلات", "females": "مسددات ركلات"},
    "forwards": {"males": "مهاجمو", "females": "مهاجمات"},
    "fullbacks": {"males": "مدافعو", "females": "مدافعات"},
    "goalkeepers": {"males": "حراس مرمى", "females": "حارسات مرمى"},
    "goaltenders": {"males": "حراس مرمى", "females": "حارسات مرمى"},
    "guards": {"males": "حراس", "females": "حارسات"},
    "halfbacks": {"males": "أظهرة مساعدون", "females": "ظهيرات مساعدات"},
    "inside forwards": {"males": "مهاجمون داخليون", "females": "مهاجمات داخليات"},
    "journalists": {"males": "صحفيو", "females": "صحفيات"},
    "kickers": {"males": "راكلو", "females": "راكلات"},
    "left wingers": {"males": "أجنحة يسار", "females": "جناحات يسار"},
    "linebackers": {"males": "أظهرة", "females": "ظهيرات"},
    "midfielders": {"males": "لاعبو وسط", "females": "لاعبات وسط"},
    "offensive linemen": {"males": "مهاجمو خط", "females": "مهاجمات خط"},
    "outside forwards": {"males": "مهاجمون خارجيون", "females": "مهاجمات خارجيات"},
    "peoplee": {"males": "أعلام", "females": "أعلام"},
    "placekickers": {"males": "مسددو", "females": "مسددات"},
    "players": {"males": "لاعبو", "females": "لاعبات"},
    "point guards": {"males": "لاعبو هجوم خلفي", "females": "لاعبات هجوم خلفي"},
    "power forwards": {"males": "مهاجمون أقوياء الجسم", "females": "مهاجمات قويات الجسم"},
    "quarterbacks": {"males": "أظهرة رباعيون", "females": "ظهيرات رباعيات"},
    "receivers": {"males": "مستقبلو", "females": "مستقبلات"},
    "right wingers": {"males": "أجنحة يمين", "females": "جناحات يمين"},
    "running backs": {"males": "راكضون للخلف", "females": "راكضات للخلف"},
    "scouts": {"males": "كشافة", "females": "كشافة"},
    "shooting guards": {"males": "مدافعون مسددون", "females": "مدافعات مسددات"},
    "small forwards": {"males": "مهاجمون صغيرو الجسم", "females": "مهاجمات صغيرات الجسم"},
    "sports-people": {"males": "رياضيو", "females": "رياضيات"},
    "tackles": {"males": "مصطدمو", "females": "مصطدمات"},
    "utility players": {"males": "لاعبو مراكز متعددة", "females": "لاعبات مراكز متعددة"},
    "wide receivers": {"males": "مستقبلون واسعون", "females": "مستقبلات واسعات"},
    "wing halves": {"males": "أنصاف أجنحة", "females": "جناحات نصفيات"},
    "wingers": {"males": "أجنحة", "females": "جناحات"},
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


def fix_result_callable(result: str, category: str, key: str, value: str) -> str:
    if result.startswith("لاعبو ") and "للسيدات" in result:
        result = result.replace("لاعبو ", "لاعبات ")

    if key == "teams" and "national" in category:
        result = result.replace("فرق ", "منتخبات ")

    return result


@functools.lru_cache(maxsize=10000)
def fix_keys(category: str) -> str:
    category = category.lower().replace("category:", "")
    category = category.replace("'", "")
    category = category.replace("playerss", "players")

    return category.strip()


def wrap_team_xo_normal_2025_with_ends(category) -> str:
    category = fix_keys(category)
    logger.debug(f"<<yellow>> start wrap_team_xo_normal_2025_with_ends: {category=}")

    result = pre_defined_results.get(category) or resolve_sport_label_unified(category)

    if not result:
        result = resolve_sport_category_suffix_with_mapping(
            category=category,
            data=mappings_data,
            callback=resolve_sport_label_unified,
            fix_result_callable=fix_result_callable,
        )

    if not result:
        result = resolve_suffix_with_mapping_genders(
            category=category,
            data=football_keys_players,
            callback=resolve_sport_label_unified,
            fix_result_callable=fix_result_callable,
        )

    logger.info_if_or_debug(f"<<yellow>> end wrap_team_xo_normal_2025_with_ends: {category=}, {result=}", result)
    return result


__all__ = [
    "wrap_team_xo_normal_2025_with_ends",
]
