"""
TODO: merge with translations_resolvers OR translations_resolvers_v2 or (Recommended: p17_sport_to_move_under.py)
"""
import functools
import re
from ...helps import dump_data, logger, len_print
from ...translations import (
    countries_from_nat,
    SPORTS_KEYS_FOR_TEAM,
    match_sport_key,
    apply_pattern_replacements,
)

from ..jobs_bots.get_helps import get_suffix_with_keys
from .p17_bot_sport_wrap import resolve_p17_bot_sport_suffixes


SPORT_FORMATS_ENAR_P17_TEAM = {
    "xoxo league": "دوري {} xoxo",
    "professional xoxo league": "دوري {} xoxo للمحترفين",
    "amateur xoxo cup": "كأس {} xoxo للهواة",
    "youth xoxo cup": "كأس {} xoxo للشباب",
    "men's xoxo cup": "كأس {} xoxo للرجال",
    "women's xoxo cup": "كأس {} xoxo للسيدات",
    "amateur xoxo championships": "بطولة {} xoxo للهواة",
    "youth xoxo championships": "بطولة {} xoxo للشباب",
    "men's xoxo championships": "بطولة {} xoxo للرجال",
    "women's xoxo championships": "بطولة {} xoxo للسيدات",
    "amateur xoxo championship": "بطولة {} xoxo للهواة",
    "youth xoxo championship": "بطولة {} xoxo للشباب",
    "men's xoxo championship": "بطولة {} xoxo للرجال",
    "women's xoxo championship": "بطولة {} xoxo للسيدات",
    "xoxo cup": "كأس {} xoxo",
    # ---national youth handball team
    "xoxo national team": "منتخب {} xoxo",
    "national xoxo team": "منتخب {} xoxo",

    # Category:Denmark national football team staff
    "xoxo national team staff": "طاقم منتخب {} xoxo",

    # Category:Denmark national football team non-playing staff
    "xoxo national team non-playing staff": "طاقم منتخب {} xoxo غير اللاعبين",

    # Polish men's volleyball national team national junior men's
    "national junior men's xoxo team": "منتخب {} xoxo للناشئين",
    "national junior xoxo team": "منتخب {} xoxo للناشئين",
    "national women's xoxo team": "منتخب {} xoxo للسيدات",
    "mennnn's national xoxo team": "منتخب {} xoxo للرجال",
    "men's xoxo national team": "منتخب {} xoxo للرجال",
    "national men's xoxo team": "منتخب {} xoxo للرجال",

    # Australian men's U23 national road cycling team
    "men's u23 national xoxo team": "منتخب {} xoxo تحت 23 سنة للرجال",
    "national youth xoxo team": "منتخب {} xoxo للشباب",

    "national women's xoxo team managers": "مدربو منتخب {} xoxo للسيدات",
    "national xoxo team managers": "مدربو منتخب {} xoxo",

    "national women's xoxo team coaches": "مدربو منتخب {} xoxo للسيدات",
    "national xoxo team coaches": "مدربو منتخب {} xoxo",

    "national women's xoxo team trainers": "مدربو منتخب {} xoxo للسيدات",
    "national xoxo team trainers": "مدربو منتخب {} xoxo",

    "national youth women's xoxo team": "منتخب {} xoxo للشابات",
    "national junior women's xoxo team": "منتخب {} xoxo للناشئات",
    "national amateur xoxo team": "منتخب {} xoxo للهواة",
    "multi-national women's xoxo team": "منتخب {} xoxo متعددة الجنسيات للسيدات",

    "men's under-23 national xoxo team": "منتخب {} xoxo تحت 23 سنة للرجال",
    "multi-national women's under-13 xoxo team": "منتخب {} xoxo تحت 13 سنة متعددة الجنسيات للسيدات",
    "multi-national women's under-14 xoxo team": "منتخب {} xoxo تحت 14 سنة متعددة الجنسيات للسيدات",
    "multi-national women's under-15 xoxo team": "منتخب {} xoxo تحت 15 سنة متعددة الجنسيات للسيدات",
    "multi-national women's under-16 xoxo team": "منتخب {} xoxo تحت 16 سنة متعددة الجنسيات للسيدات",
    "multi-national women's under-17 xoxo team": "منتخب {} xoxo تحت 17 سنة متعددة الجنسيات للسيدات",
    "multi-national women's under-18 xoxo team": "منتخب {} xoxo تحت 18 سنة متعددة الجنسيات للسيدات",
    "multi-national women's under-19 xoxo team": "منتخب {} xoxo تحت 19 سنة متعددة الجنسيات للسيدات",
    "multi-national women's under-20 xoxo team": "منتخب {} xoxo تحت 20 سنة متعددة الجنسيات للسيدات",
    "multi-national women's under-21 xoxo team": "منتخب {} xoxo تحت 21 سنة متعددة الجنسيات للسيدات",
    "multi-national women's under-23 xoxo team": "منتخب {} xoxo تحت 23 سنة متعددة الجنسيات للسيدات",
    "multi-national women's under-24 xoxo team": "منتخب {} xoxo تحت 24 سنة متعددة الجنسيات للسيدات",
    "national amateur under-13 xoxo team": "منتخب {} xoxo تحت 13 سنة للهواة",
    "national amateur under-14 xoxo team": "منتخب {} xoxo تحت 14 سنة للهواة",
    "national amateur under-15 xoxo team": "منتخب {} xoxo تحت 15 سنة للهواة",
    "national amateur under-16 xoxo team": "منتخب {} xoxo تحت 16 سنة للهواة",
    "national amateur under-17 xoxo team": "منتخب {} xoxo تحت 17 سنة للهواة",
    "national amateur under-18 xoxo team": "منتخب {} xoxo تحت 18 سنة للهواة",
    "national amateur under-19 xoxo team": "منتخب {} xoxo تحت 19 سنة للهواة",
    "national amateur under-20 xoxo team": "منتخب {} xoxo تحت 20 سنة للهواة",
    "national amateur under-21 xoxo team": "منتخب {} xoxo تحت 21 سنة للهواة",
    "national amateur under-23 xoxo team": "منتخب {} xoxo تحت 23 سنة للهواة",
    "national amateur under-24 xoxo team": "منتخب {} xoxo تحت 24 سنة للهواة",
    "national junior men's under-13 xoxo team": "منتخب {} xoxo تحت 13 سنة للناشئين",
    "national junior men's under-14 xoxo team": "منتخب {} xoxo تحت 14 سنة للناشئين",
    "national junior men's under-15 xoxo team": "منتخب {} xoxo تحت 15 سنة للناشئين",
    "national junior men's under-16 xoxo team": "منتخب {} xoxo تحت 16 سنة للناشئين",
    "national junior men's under-17 xoxo team": "منتخب {} xoxo تحت 17 سنة للناشئين",
    "national junior men's under-18 xoxo team": "منتخب {} xoxo تحت 18 سنة للناشئين",
    "national junior men's under-19 xoxo team": "منتخب {} xoxo تحت 19 سنة للناشئين",
    "national junior men's under-20 xoxo team": "منتخب {} xoxo تحت 20 سنة للناشئين",
    "national junior men's under-21 xoxo team": "منتخب {} xoxo تحت 21 سنة للناشئين",
    "national junior men's under-23 xoxo team": "منتخب {} xoxo تحت 23 سنة للناشئين",
    "national junior men's under-24 xoxo team": "منتخب {} xoxo تحت 24 سنة للناشئين",
    "national junior women's under-13 xoxo team": "منتخب {} xoxo تحت 13 سنة للناشئات",
    "national junior women's under-14 xoxo team": "منتخب {} xoxo تحت 14 سنة للناشئات",
    "national junior women's under-15 xoxo team": "منتخب {} xoxo تحت 15 سنة للناشئات",
    "national junior women's under-16 xoxo team": "منتخب {} xoxo تحت 16 سنة للناشئات",
    "national junior women's under-17 xoxo team": "منتخب {} xoxo تحت 17 سنة للناشئات",
    "national junior women's under-18 xoxo team": "منتخب {} xoxo تحت 18 سنة للناشئات",
    "national junior women's under-19 xoxo team": "منتخب {} xoxo تحت 19 سنة للناشئات",
    "national junior women's under-20 xoxo team": "منتخب {} xoxo تحت 20 سنة للناشئات",
    "national junior women's under-21 xoxo team": "منتخب {} xoxo تحت 21 سنة للناشئات",
    "national junior women's under-23 xoxo team": "منتخب {} xoxo تحت 23 سنة للناشئات",
    "national junior women's under-24 xoxo team": "منتخب {} xoxo تحت 24 سنة للناشئات",
    "national men's under-13 xoxo team": "منتخب {} xoxo تحت 13 سنة للرجال",
    "national men's under-14 xoxo team": "منتخب {} xoxo تحت 14 سنة للرجال",
    "national men's under-15 xoxo team": "منتخب {} xoxo تحت 15 سنة للرجال",
    "national men's under-16 xoxo team": "منتخب {} xoxo تحت 16 سنة للرجال",
    "national men's under-17 xoxo team": "منتخب {} xoxo تحت 17 سنة للرجال",
    "national men's under-18 xoxo team": "منتخب {} xoxo تحت 18 سنة للرجال",
    "national men's under-19 xoxo team": "منتخب {} xoxo تحت 19 سنة للرجال",
    "national men's under-20 xoxo team": "منتخب {} xoxo تحت 20 سنة للرجال",
    "national men's under-21 xoxo team": "منتخب {} xoxo تحت 21 سنة للرجال",
    "national men's under-23 xoxo team": "منتخب {} xoxo تحت 23 سنة للرجال",
    "national men's under-24 xoxo team": "منتخب {} xoxo تحت 24 سنة للرجال",
    "national under-13 xoxo team": "منتخب {} xoxo تحت 13 سنة",
    "national under-14 xoxo team": "منتخب {} xoxo تحت 14 سنة",
    "national under-15 xoxo team": "منتخب {} xoxo تحت 15 سنة",
    "national under-16 xoxo team": "منتخب {} xoxo تحت 16 سنة",
    "national under-17 xoxo team": "منتخب {} xoxo تحت 17 سنة",
    "national under-18 xoxo team": "منتخب {} xoxo تحت 18 سنة",
    "national under-19 xoxo team": "منتخب {} xoxo تحت 19 سنة",
    "national under-20 xoxo team": "منتخب {} xoxo تحت 20 سنة",
    "national under-21 xoxo team": "منتخب {} xoxo تحت 21 سنة",
    "national under-23 xoxo team": "منتخب {} xoxo تحت 23 سنة",
    "national under-24 xoxo team": "منتخب {} xoxo تحت 24 سنة",
    "national women's under-13 xoxo team": "منتخب {} xoxo تحت 13 سنة للسيدات",
    "national women's under-14 xoxo team": "منتخب {} xoxo تحت 14 سنة للسيدات",
    "national women's under-15 xoxo team": "منتخب {} xoxo تحت 15 سنة للسيدات",
    "national women's under-16 xoxo team": "منتخب {} xoxo تحت 16 سنة للسيدات",
    "national women's under-17 xoxo team": "منتخب {} xoxo تحت 17 سنة للسيدات",
    "national women's under-18 xoxo team": "منتخب {} xoxo تحت 18 سنة للسيدات",
    "national women's under-19 xoxo team": "منتخب {} xoxo تحت 19 سنة للسيدات",
    "national women's under-20 xoxo team": "منتخب {} xoxo تحت 20 سنة للسيدات",
    "national women's under-21 xoxo team": "منتخب {} xoxo تحت 21 سنة للسيدات",
    "national women's under-23 xoxo team": "منتخب {} xoxo تحت 23 سنة للسيدات",
    "national women's under-24 xoxo team": "منتخب {} xoxo تحت 24 سنة للسيدات",
    "national youth under-13 xoxo team": "منتخب {} xoxo تحت 13 سنة للشباب",
    "national youth under-14 xoxo team": "منتخب {} xoxo تحت 14 سنة للشباب",
    "national youth under-15 xoxo team": "منتخب {} xoxo تحت 15 سنة للشباب",
    "national youth under-16 xoxo team": "منتخب {} xoxo تحت 16 سنة للشباب",
    "national youth under-17 xoxo team": "منتخب {} xoxo تحت 17 سنة للشباب",
    "national youth under-18 xoxo team": "منتخب {} xoxo تحت 18 سنة للشباب",
    "national youth under-19 xoxo team": "منتخب {} xoxo تحت 19 سنة للشباب",
    "national youth under-20 xoxo team": "منتخب {} xoxo تحت 20 سنة للشباب",
    "national youth under-21 xoxo team": "منتخب {} xoxo تحت 21 سنة للشباب",
    "national youth under-23 xoxo team": "منتخب {} xoxo تحت 23 سنة للشباب",
    "national youth under-24 xoxo team": "منتخب {} xoxo تحت 24 سنة للشباب",
    "national youth women's under-13 xoxo team": "منتخب {} xoxo تحت 13 سنة للشابات",
    "national youth women's under-14 xoxo team": "منتخب {} xoxo تحت 14 سنة للشابات",
    "national youth women's under-15 xoxo team": "منتخب {} xoxo تحت 15 سنة للشابات",
    "national youth women's under-16 xoxo team": "منتخب {} xoxo تحت 16 سنة للشابات",
    "national youth women's under-17 xoxo team": "منتخب {} xoxo تحت 17 سنة للشابات",
    "national youth women's under-18 xoxo team": "منتخب {} xoxo تحت 18 سنة للشابات",
    "national youth women's under-19 xoxo team": "منتخب {} xoxo تحت 19 سنة للشابات",
    "national youth women's under-20 xoxo team": "منتخب {} xoxo تحت 20 سنة للشابات",
    "national youth women's under-21 xoxo team": "منتخب {} xoxo تحت 21 سنة للشابات",
    "national youth women's under-23 xoxo team": "منتخب {} xoxo تحت 23 سنة للشابات",
    "national youth women's under-24 xoxo team": "منتخب {} xoxo تحت 24 سنة للشابات"
}


def Get_Sport_Format_xo_en_ar_is_P17(suffix: str) -> str:
    """
    Return a sport label that merges templates with Arabic sport names.

    Example:
        suffix: "winter olympics softball", return: "كرة لينة {} في الألعاب الأولمبية الشتوية"
    """
    sport_key = match_sport_key(suffix)
    if not sport_key:
        return ""

    sport_label = SPORTS_KEYS_FOR_TEAM.get(sport_key, "")

    if not sport_label:
        return ""

    normalized_key = re.sub(re.escape(sport_key), "xoxo", suffix, flags=re.IGNORECASE)

    logger.info(f'Get_SFxo_en_ar_is P17: {suffix=}, {sport_key=}, team_xoxo:"{normalized_key}"')

    template_label = SPORT_FORMATS_ENAR_P17_TEAM.get(normalized_key, "")

    if not template_label:
        logger.info(f'Get_SFxo_en_ar_is P17 team_xoxo:"{normalized_key}" not in SPORT_FORMATS_ENAR_P17_TEAM')
        return ""

    con_3_label = apply_pattern_replacements(template_label, sport_label, "xoxo")

    logger.info(f'Get_SFxo_en_ar_is P17 {suffix=}, {con_3_label=}')

    return con_3_label


@functools.lru_cache(maxsize=10000)
@dump_data()
def _get_p17_with_sport(category: str) -> str:
    """
    """
    resolved_label = ""
    category = category.lower()

    suffix, country_start = get_suffix_with_keys(category, countries_from_nat)
    country_start_lab = countries_from_nat.get(country_start, "")

    if not suffix or not country_start:
        logger.info(f'<<lightred>>>>>> {suffix=} or {country_start=} == ""')
        return ""

    logger.debug(f'<<lightblue>> {country_start=}, {suffix=}')
    logger.debug(f'<<lightpurple>>>>>> {country_start_lab=}')

    suffix_label = Get_Sport_Format_xo_en_ar_is_P17(suffix.strip())

    if not suffix_label:
        logger.debug(f'<<lightred>>>>>> {suffix_label=}, resolved_label == ""')
        return ""

    if "{nat}" in suffix_label:
        resolved_label = suffix_label.format(nat=country_start_lab)
    else:
        resolved_label = suffix_label.format(country_start_lab)

    logger.debug(f'<<lightblue>>>>>> Get_P17_with_p17_sport: test_60: new cnt_la "{resolved_label}" ')

    return resolved_label


@functools.lru_cache(maxsize=10000)
@dump_data()
def get_p17_with_sport(category: str) -> str:
    logger.debug(f"<<yellow>> start get_p17_with_sport: {category=}")
    result = (
        resolve_p17_bot_sport_suffixes(category, _get_p17_with_sport) or
        _get_p17_with_sport(category) or
        ""
    )
    if result.startswith("لاعبو ") and "للسيدات" in result:
        result = result.replace("لاعبو ", "لاعبات ")

    logger.debug(f"<<yellow>> end get_p17_with_sport: {category=}, {result=}")
    return result


len_print.data_len(
    "p17_bot_sport.py",
    {
        "SPORT_FORMATS_ENAR_P17_TEAM": SPORT_FORMATS_ENAR_P17_TEAM,
    },
)

__all__ = [
    "get_p17_with_sport",
]
