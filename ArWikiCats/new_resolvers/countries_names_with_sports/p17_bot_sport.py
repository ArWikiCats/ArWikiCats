"""

TODO: merge with countries_names_sport_multi_v2.py

"""

import functools
import logging

from ...new.handle_suffixes import resolve_sport_category_suffix_with_mapping
from ...translations import (
    SPORTS_KEYS_FOR_TEAM,
    countries_from_nat,
)
from ...translations_formats import MultiDataFormatterBaseV2, format_multi_data_v2
from ..teams_mappings_ends import teams_label_mappings_ends

logger = logging.getLogger(__name__)

SPORT_FORMATS_ENAR_P17_TEAM = {
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
    "{en} national youth women's under-24 {en_sport} team": "منتخب {ar} {sport_team} تحت 24 سنة للشابات",
}


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBaseV2:
    nats_data = {x: {"ar": v} for x, v in countries_from_nat.items()}

    sports_data = {
        x: {
            "sport_team": v,
        }
        for x, v in SPORTS_KEYS_FOR_TEAM.items()
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
    if countries_from_nat.get(category):
        return ""

    logger.debug(f"<<yellow>> start {category=}")

    both_bot = _load_bot()
    result = both_bot.search_all_category(category)

    logger.info(f"<<yellow>> end {category=}, {result=}")
    return result


@functools.lru_cache(maxsize=10000)
def fix_keys(category: str) -> str:
    category = category.lower().replace("category:", "")
    # category = category.replace("'", "")

    replacements = {}

    for old, new in replacements.items():
        category = category.replace(old, new)

    return category.strip()


def fix_result_callable(result: str, category: str, key: str, value: str) -> str:
    if result.startswith("لاعبو ") and "للسيدات" in result:
        result = result.replace("لاعبو ", "لاعبات ")

    if key == "teams" and "national" in category:
        result = result.replace("فرق ", "منتخبات ")

    return result


@functools.lru_cache(maxsize=10000)
# @dump_data()
def get_p17_with_sport_new(category: str) -> str:
    category = fix_keys(category)

    logger.debug(f"<<yellow>> start {category=}")

    result = resolve_sport_category_suffix_with_mapping(
        category=category,
        data=teams_label_mappings_ends,
        callback=_get_p17_with_sport,
        fix_result_callable=fix_result_callable,
    )

    logger.info(f"<<yellow>> end {category=}, {result=}")
    return result


__all__ = [
    "get_p17_with_sport_new",
]
