"""
TODO: merge with translations_resolvers OR translations_resolvers_v2 or (Recommended: p17_sport_to_move_under.py)
"""
import functools
import re
from ...helps import dump_data, logger
from ...translations_formats import format_multi_data_v2, MultiDataFormatterBaseV2
from ...translations import (
    countries_from_nat,
    SPORT_KEY_RECORDS,
)

from ..handle_suffixes import resolve_sport_category_suffix_with_mapping

label_mappings_ends = {
    "champions": "أبطال",
    "clubs": "أندية",
    "coaches": "مدربو",
    "competitions": "منافسات",
    "events": "أحداث",
    "films": "أفلام",
    "finals": "نهائيات",
    "home stadiums": "ملاعب",
    "leagues": "دوريات",
    "lists": "قوائم",
    "manager history": "تاريخ مدربو",
    "managers": "مدربو",
    "matches": "مباريات",
    "navigational boxes": "صناديق تصفح",
    "non-profit organizations": "منظمات غير ربحية",
    "non-profit publishers": "ناشرون غير ربحيون",
    "organisations": "منظمات",
    "organizations": "منظمات",
    "players": "لاعبو",
    "positions": "مراكز",
    "records": "سجلات",
    "records and statistics": "سجلات وإحصائيات",
    "results": "نتائج",
    "rivalries": "دربيات",
    "scouts": "كشافة",
    "squads": "تشكيلات",
    "statistics": "إحصائيات",
    "teams": "فرق",
    "templates": "قوالب",
    "tournaments": "بطولات",
    "trainers": "مدربو",
    "umpires": "حكام",
    "venues": "ملاعب"
}

label_mappings_ends = dict(sorted(
    label_mappings_ends.items(),
    key=lambda k: (-k[0].count(" "), -len(k[0])),
))


# NOTE: plan to use it later
TEAM_DATA_NEW = {
    "men's {under_en} national xoxo team": "منتخب {} xoxo {under_ar} للرجال",
    "multi-national women's {under_en} xoxo team": "منتخب {} xoxo {under_ar} متعددة الجنسيات للسيدات",
    "national amateur {under_en} xoxo team": "منتخب {} xoxo {under_ar} للهواة",
    "national junior men's {under_en} xoxo team": "منتخب {} xoxo {under_ar} للناشئين",
    "national junior women's {under_en} xoxo team": "منتخب {} xoxo {under_ar} للناشئات",
    "national men's {under_en} xoxo team": "منتخب {} xoxo {under_ar} للرجال",
    "national {under_en} xoxo team": "منتخب {} xoxo {under_ar}",
    "national women's {under_en} xoxo team": "منتخب {} xoxo {under_ar} للسيدات",
    "national youth {under_en} xoxo team": "منتخب {} xoxo {under_ar} للشباب",
    "national youth women's {under_en} xoxo team": "منتخب {} xoxo {under_ar} للشابات",
}

SPORT_FORMATS_ENAR_P17_TEAM = {
    "{en} {en_sport} league": "دوري {ar} {sport_team}",
    "{en} professional {en_sport} league": "دوري {ar} {sport_team} للمحترفين",
    "{en} amateur {en_sport} cup": "كأس {ar} {sport_team} للهواة",
    "{en} youth {en_sport} cup": "كأس {ar} {sport_team} للشباب",
    "{en} men's {en_sport} cup": "كأس {ar} {sport_team} للرجال",
    "{en} women's {en_sport} cup": "كأس {ar} {sport_team} للسيدات",
    "{en} amateur {en_sport} championships": "بطولة {ar} {sport_team} للهواة",
    "{en} youth {en_sport} championships": "بطولة {ar} {sport_team} للشباب",
    "{en} men's {en_sport} championships": "بطولة {ar} {sport_team} للرجال",
    "{en} women's {en_sport} championships": "بطولة {ar} {sport_team} للسيدات",
    "{en} amateur {en_sport} championship": "بطولة {ar} {sport_team} للهواة",
    "{en} youth {en_sport} championship": "بطولة {ar} {sport_team} للشباب",
    "{en} men's {en_sport} championship": "بطولة {ar} {sport_team} للرجال",
    "{en} women's {en_sport} championship": "بطولة {ar} {sport_team} للسيدات",
    "{en} {en_sport} cup": "كأس {ar} {sport_team}",
    # ---national youth handball team
    "{en} {en_sport} national team": "منتخب {ar} {sport_team}",
    "{en} national {en_sport} team": "منتخب {ar} {sport_team}",

    # Category:Denmark national football team staff
    "{en} {en_sport} national team staff": "طاقم منتخب {ar} {sport_team}",

    # Category:Denmark national football team non-playing staff
    "{en} {en_sport} national team non-playing staff": "طاقم منتخب {ar} {sport_team} غير اللاعبين",

    # Polish men's volleyball national team national junior men's
    "{en} national junior men's {en_sport} team": "منتخب {ar} {sport_team} للناشئين",
    "{en} national junior {en_sport} team": "منتخب {ar} {sport_team} للناشئين",
    "{en} national women's {en_sport} team": "منتخب {ar} {sport_team} للسيدات",
    "{en} mennnn's national {en_sport} team": "منتخب {ar} {sport_team} للرجال",
    "{en} men's {en_sport} national team": "منتخب {ar} {sport_team} للرجال",
    "{en} national men's {en_sport} team": "منتخب {ar} {sport_team} للرجال",

    # Australian men's U23 national road cycling team
    "{en} men's u23 national {en_sport} team": "منتخب {ar} {sport_team} تحت 23 سنة للرجال",
    "{en} national youth {en_sport} team": "منتخب {ar} {sport_team} للشباب",

    "{en} national women's {en_sport} team managers": "مدربو منتخب {ar} {sport_team} للسيدات",
    "{en} national {en_sport} team managers": "مدربو منتخب {ar} {sport_team}",

    "{en} national women's {en_sport} team coaches": "مدربو منتخب {ar} {sport_team} للسيدات",
    "{en} national {en_sport} team coaches": "مدربو منتخب {ar} {sport_team}",

    "{en} national women's {en_sport} team trainers": "مدربو منتخب {ar} {sport_team} للسيدات",
    "{en} national {en_sport} team trainers": "مدربو منتخب {ar} {sport_team}",

    "{en} national youth women's {en_sport} team": "منتخب {ar} {sport_team} للشابات",
    "{en} national junior women's {en_sport} team": "منتخب {ar} {sport_team} للناشئات",
    "{en} national amateur {en_sport} team": "منتخب {ar} {sport_team} للهواة",
    "{en} multi-national women's {en_sport} team": "منتخب {ar} {sport_team} متعددة الجنسيات للسيدات",

    "{en} men's under-23 national {en_sport} team": "منتخب {ar} {sport_team} تحت 23 سنة للرجال",
    "{en} multi-national women's under-13 {en_sport} team": "منتخب {ar} {sport_team} تحت 13 سنة متعددة الجنسيات للسيدات",
    "{en} multi-national women's under-14 {en_sport} team": "منتخب {ar} {sport_team} تحت 14 سنة متعددة الجنسيات للسيدات",
    "{en} multi-national women's under-15 {en_sport} team": "منتخب {ar} {sport_team} تحت 15 سنة متعددة الجنسيات للسيدات",
    "{en} multi-national women's under-16 {en_sport} team": "منتخب {ar} {sport_team} تحت 16 سنة متعددة الجنسيات للسيدات",
    "{en} multi-national women's under-17 {en_sport} team": "منتخب {ar} {sport_team} تحت 17 سنة متعددة الجنسيات للسيدات",
    "{en} multi-national women's under-18 {en_sport} team": "منتخب {ar} {sport_team} تحت 18 سنة متعددة الجنسيات للسيدات",
    "{en} multi-national women's under-19 {en_sport} team": "منتخب {ar} {sport_team} تحت 19 سنة متعددة الجنسيات للسيدات",
    "{en} multi-national women's under-20 {en_sport} team": "منتخب {ar} {sport_team} تحت 20 سنة متعددة الجنسيات للسيدات",
    "{en} multi-national women's under-21 {en_sport} team": "منتخب {ar} {sport_team} تحت 21 سنة متعددة الجنسيات للسيدات",
    "{en} multi-national women's under-23 {en_sport} team": "منتخب {ar} {sport_team} تحت 23 سنة متعددة الجنسيات للسيدات",
    "{en} multi-national women's under-24 {en_sport} team": "منتخب {ar} {sport_team} تحت 24 سنة متعددة الجنسيات للسيدات",
    "{en} national amateur under-13 {en_sport} team": "منتخب {ar} {sport_team} تحت 13 سنة للهواة",
    "{en} national amateur under-14 {en_sport} team": "منتخب {ar} {sport_team} تحت 14 سنة للهواة",
    "{en} national amateur under-15 {en_sport} team": "منتخب {ar} {sport_team} تحت 15 سنة للهواة",
    "{en} national amateur under-16 {en_sport} team": "منتخب {ar} {sport_team} تحت 16 سنة للهواة",
    "{en} national amateur under-17 {en_sport} team": "منتخب {ar} {sport_team} تحت 17 سنة للهواة",
    "{en} national amateur under-18 {en_sport} team": "منتخب {ar} {sport_team} تحت 18 سنة للهواة",
    "{en} national amateur under-19 {en_sport} team": "منتخب {ar} {sport_team} تحت 19 سنة للهواة",
    "{en} national amateur under-20 {en_sport} team": "منتخب {ar} {sport_team} تحت 20 سنة للهواة",
    "{en} national amateur under-21 {en_sport} team": "منتخب {ar} {sport_team} تحت 21 سنة للهواة",
    "{en} national amateur under-23 {en_sport} team": "منتخب {ar} {sport_team} تحت 23 سنة للهواة",
    "{en} national amateur under-24 {en_sport} team": "منتخب {ar} {sport_team} تحت 24 سنة للهواة",
    "{en} national junior men's under-13 {en_sport} team": "منتخب {ar} {sport_team} تحت 13 سنة للناشئين",
    "{en} national junior men's under-14 {en_sport} team": "منتخب {ar} {sport_team} تحت 14 سنة للناشئين",
    "{en} national junior men's under-15 {en_sport} team": "منتخب {ar} {sport_team} تحت 15 سنة للناشئين",
    "{en} national junior men's under-16 {en_sport} team": "منتخب {ar} {sport_team} تحت 16 سنة للناشئين",
    "{en} national junior men's under-17 {en_sport} team": "منتخب {ar} {sport_team} تحت 17 سنة للناشئين",
    "{en} national junior men's under-18 {en_sport} team": "منتخب {ar} {sport_team} تحت 18 سنة للناشئين",
    "{en} national junior men's under-19 {en_sport} team": "منتخب {ar} {sport_team} تحت 19 سنة للناشئين",
    "{en} national junior men's under-20 {en_sport} team": "منتخب {ar} {sport_team} تحت 20 سنة للناشئين",
    "{en} national junior men's under-21 {en_sport} team": "منتخب {ar} {sport_team} تحت 21 سنة للناشئين",
    "{en} national junior men's under-23 {en_sport} team": "منتخب {ar} {sport_team} تحت 23 سنة للناشئين",
    "{en} national junior men's under-24 {en_sport} team": "منتخب {ar} {sport_team} تحت 24 سنة للناشئين",
    "{en} national junior women's under-13 {en_sport} team": "منتخب {ar} {sport_team} تحت 13 سنة للناشئات",
    "{en} national junior women's under-14 {en_sport} team": "منتخب {ar} {sport_team} تحت 14 سنة للناشئات",
    "{en} national junior women's under-15 {en_sport} team": "منتخب {ar} {sport_team} تحت 15 سنة للناشئات",
    "{en} national junior women's under-16 {en_sport} team": "منتخب {ar} {sport_team} تحت 16 سنة للناشئات",
    "{en} national junior women's under-17 {en_sport} team": "منتخب {ar} {sport_team} تحت 17 سنة للناشئات",
    "{en} national junior women's under-18 {en_sport} team": "منتخب {ar} {sport_team} تحت 18 سنة للناشئات",
    "{en} national junior women's under-19 {en_sport} team": "منتخب {ar} {sport_team} تحت 19 سنة للناشئات",
    "{en} national junior women's under-20 {en_sport} team": "منتخب {ar} {sport_team} تحت 20 سنة للناشئات",
    "{en} national junior women's under-21 {en_sport} team": "منتخب {ar} {sport_team} تحت 21 سنة للناشئات",
    "{en} national junior women's under-23 {en_sport} team": "منتخب {ar} {sport_team} تحت 23 سنة للناشئات",
    "{en} national junior women's under-24 {en_sport} team": "منتخب {ar} {sport_team} تحت 24 سنة للناشئات",
    "{en} national men's under-13 {en_sport} team": "منتخب {ar} {sport_team} تحت 13 سنة للرجال",
    "{en} national men's under-14 {en_sport} team": "منتخب {ar} {sport_team} تحت 14 سنة للرجال",
    "{en} national men's under-15 {en_sport} team": "منتخب {ar} {sport_team} تحت 15 سنة للرجال",
    "{en} national men's under-16 {en_sport} team": "منتخب {ar} {sport_team} تحت 16 سنة للرجال",
    "{en} national men's under-17 {en_sport} team": "منتخب {ar} {sport_team} تحت 17 سنة للرجال",
    "{en} national men's under-18 {en_sport} team": "منتخب {ar} {sport_team} تحت 18 سنة للرجال",
    "{en} national men's under-19 {en_sport} team": "منتخب {ar} {sport_team} تحت 19 سنة للرجال",
    "{en} national men's under-20 {en_sport} team": "منتخب {ar} {sport_team} تحت 20 سنة للرجال",
    "{en} national men's under-21 {en_sport} team": "منتخب {ar} {sport_team} تحت 21 سنة للرجال",
    "{en} national men's under-23 {en_sport} team": "منتخب {ar} {sport_team} تحت 23 سنة للرجال",
    "{en} national men's under-24 {en_sport} team": "منتخب {ar} {sport_team} تحت 24 سنة للرجال",
    "{en} national under-13 {en_sport} team": "منتخب {ar} {sport_team} تحت 13 سنة",
    "{en} national under-14 {en_sport} team": "منتخب {ar} {sport_team} تحت 14 سنة",
    "{en} national under-15 {en_sport} team": "منتخب {ar} {sport_team} تحت 15 سنة",
    "{en} national under-16 {en_sport} team": "منتخب {ar} {sport_team} تحت 16 سنة",
    "{en} national under-17 {en_sport} team": "منتخب {ar} {sport_team} تحت 17 سنة",
    "{en} national under-18 {en_sport} team": "منتخب {ar} {sport_team} تحت 18 سنة",
    "{en} national under-19 {en_sport} team": "منتخب {ar} {sport_team} تحت 19 سنة",
    "{en} national under-20 {en_sport} team": "منتخب {ar} {sport_team} تحت 20 سنة",
    "{en} national under-21 {en_sport} team": "منتخب {ar} {sport_team} تحت 21 سنة",
    "{en} national under-23 {en_sport} team": "منتخب {ar} {sport_team} تحت 23 سنة",
    "{en} national under-24 {en_sport} team": "منتخب {ar} {sport_team} تحت 24 سنة",
    "{en} national women's under-13 {en_sport} team": "منتخب {ar} {sport_team} تحت 13 سنة للسيدات",
    "{en} national women's under-14 {en_sport} team": "منتخب {ar} {sport_team} تحت 14 سنة للسيدات",
    "{en} national women's under-15 {en_sport} team": "منتخب {ar} {sport_team} تحت 15 سنة للسيدات",
    "{en} national women's under-16 {en_sport} team": "منتخب {ar} {sport_team} تحت 16 سنة للسيدات",
    "{en} national women's under-17 {en_sport} team": "منتخب {ar} {sport_team} تحت 17 سنة للسيدات",
    "{en} national women's under-18 {en_sport} team": "منتخب {ar} {sport_team} تحت 18 سنة للسيدات",
    "{en} national women's under-19 {en_sport} team": "منتخب {ar} {sport_team} تحت 19 سنة للسيدات",
    "{en} national women's under-20 {en_sport} team": "منتخب {ar} {sport_team} تحت 20 سنة للسيدات",
    "{en} national women's under-21 {en_sport} team": "منتخب {ar} {sport_team} تحت 21 سنة للسيدات",
    "{en} national women's under-23 {en_sport} team": "منتخب {ar} {sport_team} تحت 23 سنة للسيدات",
    "{en} national women's under-24 {en_sport} team": "منتخب {ar} {sport_team} تحت 24 سنة للسيدات",
    "{en} national youth under-13 {en_sport} team": "منتخب {ar} {sport_team} تحت 13 سنة للشباب",
    "{en} national youth under-14 {en_sport} team": "منتخب {ar} {sport_team} تحت 14 سنة للشباب",
    "{en} national youth under-15 {en_sport} team": "منتخب {ar} {sport_team} تحت 15 سنة للشباب",
    "{en} national youth under-16 {en_sport} team": "منتخب {ar} {sport_team} تحت 16 سنة للشباب",
    "{en} national youth under-17 {en_sport} team": "منتخب {ar} {sport_team} تحت 17 سنة للشباب",
    "{en} national youth under-18 {en_sport} team": "منتخب {ar} {sport_team} تحت 18 سنة للشباب",
    "{en} national youth under-19 {en_sport} team": "منتخب {ar} {sport_team} تحت 19 سنة للشباب",
    "{en} national youth under-20 {en_sport} team": "منتخب {ar} {sport_team} تحت 20 سنة للشباب",
    "{en} national youth under-21 {en_sport} team": "منتخب {ar} {sport_team} تحت 21 سنة للشباب",
    "{en} national youth under-23 {en_sport} team": "منتخب {ar} {sport_team} تحت 23 سنة للشباب",
    "{en} national youth under-24 {en_sport} team": "منتخب {ar} {sport_team} تحت 24 سنة للشباب",
    "{en} national youth women's under-13 {en_sport} team": "منتخب {ar} {sport_team} تحت 13 سنة للشابات",
    "{en} national youth women's under-14 {en_sport} team": "منتخب {ar} {sport_team} تحت 14 سنة للشابات",
    "{en} national youth women's under-15 {en_sport} team": "منتخب {ar} {sport_team} تحت 15 سنة للشابات",
    "{en} national youth women's under-16 {en_sport} team": "منتخب {ar} {sport_team} تحت 16 سنة للشابات",
    "{en} national youth women's under-17 {en_sport} team": "منتخب {ar} {sport_team} تحت 17 سنة للشابات",
    "{en} national youth women's under-18 {en_sport} team": "منتخب {ar} {sport_team} تحت 18 سنة للشابات",
    "{en} national youth women's under-19 {en_sport} team": "منتخب {ar} {sport_team} تحت 19 سنة للشابات",
    "{en} national youth women's under-20 {en_sport} team": "منتخب {ar} {sport_team} تحت 20 سنة للشابات",
    "{en} national youth women's under-21 {en_sport} team": "منتخب {ar} {sport_team} تحت 21 سنة للشابات",
    "{en} national youth women's under-23 {en_sport} team": "منتخب {ar} {sport_team} تحت 23 سنة للشابات",
    "{en} national youth women's under-24 {en_sport} team": "منتخب {ar} {sport_team} تحت 24 سنة للشابات"
}


def remove_the(text: str) -> str:
    if text.lower().startswith("the "):
        return text[4:]
    return text


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBaseV2:
    nats_data = {
        x: {"ar": v}
        for x, v in countries_from_nat.items()
    }

    sports_data = {
        x: {
            "sport_ar": v["label"],
            "sport_team": v["team"],
            "sport_jobs": v["jobs"],
        }
        for x, v in SPORT_KEY_RECORDS.items()
        if v.get("label")
    }

    both_bot = format_multi_data_v2(
        formatted_data=SPORT_FORMATS_ENAR_P17_TEAM,
        data_list=nats_data,
        key_placeholder="{en}",
        data_list2=sports_data,
        key2_placeholder="{en_sport}",
        text_after="",
        text_before="the ",
        search_first_part=True,
        use_other_formatted_data=True,
    )
    return both_bot


@functools.lru_cache(maxsize=10000)
def _get_p17_with_sport(category: str) -> str:
    logger.debug(f"<<yellow>> start _get_p17_with_sport: {category=}")

    both_bot = _load_bot()
    result = both_bot.search_all_category(category)

    logger.debug(f"<<yellow>> end _get_p17_with_sport: {category=}, {result=}")
    return result


@functools.lru_cache(maxsize=10000)
@dump_data()
def get_p17_with_sport_new(category: str) -> str:
    logger.debug(f"<<yellow>> start get_p17_with_sport_new: {category=}")

    result = resolve_sport_category_suffix_with_mapping(category, label_mappings_ends, _get_p17_with_sport)

    if result.startswith("لاعبو ") and "للسيدات" in result:
        result = result.replace("لاعبو ", "لاعبات ")

    logger.debug(f"<<yellow>> end get_p17_with_sport_new: {category=}, {result=}")
    return result


__all__ = [
    "get_p17_with_sport_new",
]
