"""

English country-name → Arabic country-name.

"""
import functools

from ...helps import logger
from ...translations_formats import format_multi_data, MultiDataFormatterBase
from ...translations import countries_from_nat, SPORTS_KEYS_FOR_JOBS

under_data = {
    "under-13": "تحت 13 سنة",
    "under-14": "تحت 14 سنة",
    "under-15": "تحت 15 سنة",
    "under-16": "تحت 16 سنة",
    "under-17": "تحت 17 سنة",
    "under-18": "تحت 18 سنة",
    "under-19": "تحت 19 سنة",
    "under-20": "تحت 20 سنة",
    "under-21": "تحت 21 سنة",
    "under-23": "تحت 23 سنة",
    "under-24": "تحت 24 سنة",
    "u23": "تحت 23 سنة",
}

# TODO: support sports keys
sports_data_under = {
    "national men's {under_en} {en_sport} teams": "منتخبات {sport_jobs} {under_ar} للرجال",
    "men's {under_en} national {en_sport} teams": "منتخبات {sport_team} {under_ar} للرجال",
    "multi-national women's {under_en} {en_sport} teams": "منتخبات {sport_team} {under_ar} متعددة الجنسيات للسيدات",
    "national amateur {under_en} {en_sport} teams": "منتخبات {sport_team} {under_ar} للهواة",
    "national junior men's {under_en} {en_sport} teams": "منتخبات {sport_team} {under_ar} للناشئين",
    "national junior women's {under_en} {en_sport} teams": "منتخبات {sport_team} {under_ar} للناشئات",
    "national women's {under_en} {en_sport} teams": "منتخبات {sport_team} {under_ar} للسيدات",
    "national youth women's {under_en} {en_sport} teams": "منتخبات {sport_team} {under_ar} للشابات",
    "national youth {under_en} {en_sport} teams": "منتخبات {sport_team} {under_ar} للشباب",
    "national {under_en} {en_sport} teams": "منتخبات {sport_team} {under_ar}",
}

main_data_under = {
    "{en} {under_en} international players": "لاعبون {under_ar} دوليون من {ar}",
    "{en} {under_en} international playerss": "لاعبون {under_ar} دوليون من {ar}",

    "{en} amateur {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} لكرة القدم للهواة",
    "{en} amateur {under_en} international soccer players": "لاعبو منتخب {ar} {under_ar} لكرة القدم للهواة",
    "{en} amateur {under_en} international soccer playerss": "لاعبو منتخب {ar} {under_ar} لكرة القدم للهواة",
    "{en} men's a' {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} لكرة القدم للرجال للمحليين",
    "{en} men's a' {under_en} international soccer players": "لاعبو منتخب {ar} {under_ar} لكرة القدم للرجال للمحليين",
    "{en} men's a' {under_en} international soccer playerss": "لاعبو منتخب {ar} {under_ar} لكرة القدم للرجال للمحليين",
    "{en} men's b {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} لكرة القدم الرديف للرجال",
    "{en} men's b {under_en} international soccer players": "لاعبو منتخب {ar} {under_ar} لكرة القدم الرديف للرجال",
    "{en} men's b {under_en} international soccer playerss": "لاعبو منتخب {ar} {under_ar} لكرة القدم الرديف للرجال",
    "{en} men's youth {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} لكرة القدم للشباب",
    "{en} men's youth {under_en} international soccer players": "لاعبو منتخب {ar} {under_ar} لكرة القدم للشباب",
    "{en} men's youth {under_en} international soccer playerss": "لاعبو منتخب {ar} {under_ar} لكرة القدم للشباب",
    "{en} men's {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} لكرة القدم للرجال",
    "{en} men's {under_en} international soccer players": "لاعبو منتخب {ar} {under_ar} لكرة القدم للرجال",
    "{en} men's {under_en} international soccer playerss": "لاعبو منتخب {ar} {under_ar} لكرة القدم للرجال",
    "{en} women's youth {under_en} international footballers": "لاعبات منتخب {ar} {under_ar} لكرة القدم للشابات",
    "{en} women's youth {under_en} international soccer players": "لاعبات منتخب {ar} {under_ar} لكرة القدم للشابات",
    "{en} women's youth {under_en} international soccer playerss": "لاعبات منتخب {ar} {under_ar} لكرة القدم للشابات",
    "{en} women's {under_en} international footballers": "لاعبات منتخب {ar} {under_ar} لكرة القدم للسيدات",
    "{en} women's {under_en} international soccer players": "لاعبات منتخب {ar} {under_ar} لكرة القدم للسيدات",
    "{en} women's {under_en} international soccer playerss": "لاعبات منتخب {ar} {under_ar} لكرة القدم للسيدات",
    "{en} youth {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} لكرة القدم للشباب",
    "{en} youth {under_en} international soccer players": "لاعبو منتخب {ar} {under_ar} لكرة القدم للشباب",
    "{en} youth {under_en} international soccer playerss": "لاعبو منتخب {ar} {under_ar} لكرة القدم للشباب",
    "{en} {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} لكرة القدم",
    "{en} {under_en} international managers": "مدربون {under_ar} دوليون من {ar}",
    "{en} {under_en} international soccer players": "لاعبو منتخب {ar} {under_ar} لكرة القدم",
    "{en} {under_en} international soccer playerss": "لاعبو منتخب {ar} {under_ar} لكرة القدم "
}


@functools.lru_cache(maxsize=1)
def _load_bot_with_sports_keys() -> MultiDataFormatterBase:

    return format_multi_data(
        formatted_data=sports_data_under,
        data_list=under_data,
        key_placeholder="{under_en}",
        value_placeholder="{under_ar}",
        data_list2=SPORTS_KEYS_FOR_JOBS,
        key2_placeholder="{en_sport}",
        value2_placeholder="{sport_jobs}",
    )


@functools.lru_cache(maxsize=1)
def _load_under_bot() -> MultiDataFormatterBase:

    return format_multi_data(
        formatted_data=main_data_under,
        data_list=under_data,
        key_placeholder="{under_en}",
        value_placeholder="{under_ar}",
        data_list2=countries_from_nat,
        key2_placeholder="{en}",
        value2_placeholder="{ar}",
    )


@functools.lru_cache(maxsize=1000)
def resolve_sport_under_labels(category: str) -> str:
    logger.debug(f"<<yellow>> start resolve_sport_under_labels: {category=}")
    result = (
        _load_under_bot().search(category) or
        _load_bot_with_sports_keys().search(category) or
        ""
    )
    logger.debug(f"<<yellow>> end resolve_sport_under_labels: {category=}, {result=}")
    return result


__all__ = [
    "resolve_sport_under_labels",
]
