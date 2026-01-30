"""

English country-name → Arabic country-name.

"""

import functools

import logging
from ...translations import SPORTS_KEYS_FOR_JOBS, countries_from_nat
from ...translations_formats import MultiDataFormatterBase, format_multi_data

logger = logging.getLogger(__name__)

# TODO: This all wrong arabic values need to be fixed later
under_data_to_check = {
    "{en} {en_sport} teams": "فرق {sport_jobs} {female}",
    "{en} {en_sport} national teams": "فرق {sport_jobs} {female}",
    "{en} {en_sport} national amateur teams": "فرق {sport_jobs} {female}",
    "{en} {en_sport} national junior mens teams": "فرق {sport_jobs} {female}",
    "{en} {en_sport} national mens teams": "فرق {sport_jobs} {female}",
    "{en} {en_sport} national womens teams": "فرق {sport_jobs} {female}",
    "{en} {en_sport} national youth teams": "فرق {sport_jobs} {female}",
    "{en} {en_sport} national youth womens teams": "فرق {sport_jobs} {female}",
    "{en} {en_sport} national junior womens teams": "فرق {sport_jobs} {female}",
    "{en} {under_en} teams": "فرق {female} {under_ar}",
    "{en} {en_sport} {under_en} teams": "فرق {sport_jobs} {female} {under_ar}",
    "{en} {en_sport} national amateur {under_en} teams": "فرق {sport_jobs} {female}",
    "{en} {en_sport} national junior mens {under_en} teams": "فرق {sport_jobs} {female}",
    "{en} {en_sport} national junior womens {under_en} teams": "فرق {sport_jobs} {female}",
    "{en} {en_sport} national mens {under_en} teams": "فرق {sport_jobs} {female}",
    "{en} {en_sport} national {under_en} teams": "فرق {sport_jobs} {female}",
    "{en} {en_sport} national womens {under_en} teams": "فرق {sport_jobs} {female}",
    "{en} {en_sport} national youth {under_en} teams": "فرق {sport_jobs} {female}",
    "{en} {en_sport} youth womens {under_en} teams": "فرق {sport_jobs} {female} {under_ar} للشابات",
    # ["softball national youth womens under-24 teams"] = "منتخبات كرة لينة تحت 24 سنة للشابات"
    "{en} {en_sport} national youth womens {under_en} teams": "منتخبات {sport_jobs} {under_ar} للشابات",
}

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

# TODO: support nats keys
sports_data_under = {
    "{en_sport} national youth womens {under_en} teams": "منتخبات {sport_jobs} {under_ar} للشابات",
    "national mens {under_en} {en_sport} teams": "منتخبات {sport_jobs} {under_ar} للرجال",
    "mens {under_en} national {en_sport} teams": "منتخبات {sport_jobs} {under_ar} للرجال",
    # [multi-national womens under-19 football teams] = "منتخبات كرة قدم تحت 19 سنة متعددة الجنسيات للسيدات"
    "multi-national womens {under_en} {en_sport} teams": "منتخبات {sport_jobs} {under_ar} متعددة الجنسيات للسيدات",
    "national amateur {under_en} {en_sport} teams": "منتخبات {sport_jobs} {under_ar} للهواة",
    "national junior mens {under_en} {en_sport} teams": "منتخبات {sport_jobs} {under_ar} للناشئين",
    "national junior womens {under_en} {en_sport} teams": "منتخبات {sport_jobs} {under_ar} للناشئات",
    "national womens {under_en} {en_sport} teams": "منتخبات {sport_jobs} {under_ar} للسيدات",
    "national youth womens {under_en} {en_sport} teams": "منتخبات {sport_jobs} {under_ar} للشابات",
    "national youth {under_en} {en_sport} teams": "منتخبات {sport_jobs} {under_ar} للشباب",
    "national {under_en} {en_sport} teams": "منتخبات {sport_jobs} {under_ar}",
}

main_data_under = {
    "{en} {under_en} international players": "لاعبون {under_ar} دوليون من {ar}",
    "{en} {under_en} international playerss": "لاعبون {under_ar} دوليون من {ar}",
    "{en} amateur {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} لكرة القدم للهواة",
    "{en} amateur {under_en} international soccer players": "لاعبو منتخب {ar} {under_ar} لكرة القدم للهواة",
    "{en} amateur {under_en} international soccer playerss": "لاعبو منتخب {ar} {under_ar} لكرة القدم للهواة",
    "{en} mens a {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} لكرة القدم للرجال للمحليين",
    "{en} mens a {under_en} international soccer players": "لاعبو منتخب {ar} {under_ar} لكرة القدم للرجال للمحليين",
    "{en} mens a {under_en} international soccer playerss": "لاعبو منتخب {ar} {under_ar} لكرة القدم للرجال للمحليين",
    "{en} mens b {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} لكرة القدم الرديف للرجال",
    "{en} mens b {under_en} international soccer players": "لاعبو منتخب {ar} {under_ar} لكرة القدم الرديف للرجال",
    "{en} mens b {under_en} international soccer playerss": "لاعبو منتخب {ar} {under_ar} لكرة القدم الرديف للرجال",
    "{en} mens youth {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} لكرة القدم للشباب",
    "{en} mens youth {under_en} international soccer players": "لاعبو منتخب {ar} {under_ar} لكرة القدم للشباب",
    "{en} mens youth {under_en} international soccer playerss": "لاعبو منتخب {ar} {under_ar} لكرة القدم للشباب",
    "{en} mens {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} لكرة القدم للرجال",
    "{en} mens {under_en} international soccer players": "لاعبو منتخب {ar} {under_ar} لكرة القدم للرجال",
    "{en} mens {under_en} international soccer playerss": "لاعبو منتخب {ar} {under_ar} لكرة القدم للرجال",
    "{en} womens youth {under_en} international footballers": "لاعبات منتخب {ar} {under_ar} لكرة القدم للشابات",
    "{en} womens youth {under_en} international soccer players": "لاعبات منتخب {ar} {under_ar} لكرة القدم للشابات",
    "{en} womens youth {under_en} international soccer playerss": "لاعبات منتخب {ar} {under_ar} لكرة القدم للشابات",
    "{en} womens {under_en} international footballers": "لاعبات منتخب {ar} {under_ar} لكرة القدم للسيدات",
    "{en} womens {under_en} international soccer players": "لاعبات منتخب {ar} {under_ar} لكرة القدم للسيدات",
    "{en} womens {under_en} international soccer playerss": "لاعبات منتخب {ar} {under_ar} لكرة القدم للسيدات",
    "{en} youth {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} لكرة القدم للشباب",
    "{en} youth {under_en} international soccer players": "لاعبو منتخب {ar} {under_ar} لكرة القدم للشباب",
    "{en} youth {under_en} international soccer playerss": "لاعبو منتخب {ar} {under_ar} لكرة القدم للشباب",
    "{en} {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} لكرة القدم",
    "{en} {under_en} international managers": "مدربون {under_ar} دوليون من {ar}",
    "{en} {under_en} international soccer players": "لاعبو منتخب {ar} {under_ar} لكرة القدم",
    "{en} {under_en} international soccer playerss": "لاعبو منتخب {ar} {under_ar} لكرة القدم ",
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


@functools.lru_cache(maxsize=10000)
def fix_keys(category: str) -> str:
    category = category.replace("'", "").lower().replace("category:", "")

    replacements = {}

    for old, new in replacements.items():
        category = category.replace(old, new)

    return category.strip()


@functools.lru_cache(maxsize=1000)
def resolve_sport_under_labels(category: str) -> str:
    category = fix_keys(category)
    logger.debug(f"<<yellow>> start resolve_sport_under_labels: {category=}")

    result = _load_under_bot().search(category) or _load_bot_with_sports_keys().search(category) or ""

    logger.info(f"<<yellow>> end resolve_sport_under_labels: {category=}, {result=}")
    return result


__all__ = [
    "resolve_sport_under_labels",
]
