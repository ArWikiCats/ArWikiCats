"""
"""
import functools
from typing import Dict
from ...helps import len_print
from ...translations_formats import FormatData, format_multi_data, MultiDataFormatterBase
from ...helps.log import logger
from ...helps.jsonl_dump import dump_data
from ...translations import (
    contries_from_nat,
)

main_data = {
    "{en} amateur international footballers": "لاعبو منتخب {ar} لكرة القدم للهواة",
    "{en} amateur international soccer players": "لاعبو منتخب {ar} لكرة القدم للهواة",
    "{en} amateur international soccer playerss": "لاعبو منتخب {ar} لكرة القدم للهواة",
    "{en} international footballers": "لاعبو منتخب {ar} لكرة القدم ",
    "{en} international rally": "رالي {ar} الدولي",
    "{en} international rules football team": "منتخب {} لكرة القدم الدولية",
    "{en} international soccer players": "لاعبو منتخب {ar} لكرة القدم ",
    "{en} international soccer playerss": "لاعبو منتخب {ar} لكرة القدم ",
    "{en} men's a' international footballers": "لاعبو منتخب {ar} لكرة القدم للرجال للمحليين",
    "{en} men's a' international soccer players": "لاعبو منتخب {ar} لكرة القدم للرجال للمحليين",
    "{en} men's a' international soccer playerss": "لاعبو منتخب {ar} لكرة القدم للرجال للمحليين",
    "{en} men's b international footballers": "لاعبو منتخب {ar} لكرة القدم الرديف للرجال",
    "{en} men's b international soccer players": "لاعبو منتخب {ar} لكرة القدم الرديف للرجال",
    "{en} men's b international soccer playerss": "لاعبو منتخب {ar} لكرة القدم الرديف للرجال",
    "{en} men's international footballers": "لاعبو منتخب {ar} لكرة القدم للرجال",
    "{en} men's international soccer players": "لاعبو منتخب {ar} لكرة القدم للرجال",
    "{en} men's international soccer playerss": "لاعبو منتخب {ar} لكرة القدم للرجال",
    "{en} men's youth international footballers": "لاعبو منتخب {ar} لكرة القدم للشباب",
    "{en} men's youth international soccer players": "لاعبو منتخب {ar} لكرة القدم للشباب",
    "{en} men's youth international soccer playerss": "لاعبو منتخب {ar} لكرة القدم للشباب",
    "{en} national football team managers": "مدربو منتخب {ar} لكرة القدم",
    "{en} national team": "منتخبات {ar} الوطنية",
    "{en} national teams": "منتخبات {ar} الوطنية",
    "{en} rally championship": "بطولة {ar} للراليات",
    "{en} sports templates": "قوالب {ar} الرياضية",
    "{en} women's international footballers": "لاعبات منتخب {ar} لكرة القدم للسيدات",
    "{en} women's international soccer players": "لاعبات منتخب {ar} لكرة القدم للسيدات",
    "{en} women's international soccer playerss": "لاعبات منتخب {ar} لكرة القدم للسيدات",
    "{en} women's youth international footballers": "لاعبات منتخب {ar} لكرة القدم للشابات",
    "{en} women's youth international soccer players": "لاعبات منتخب {ar} لكرة القدم للشابات",
    "{en} women's youth international soccer playerss": "لاعبات منتخب {ar} لكرة القدم للشابات",
    "{en} youth international footballers": "لاعبو منتخب {ar} لكرة القدم للشباب",
    "{en} youth international soccer players": "لاعبو منتخب {ar} لكرة القدم للشباب",
    "{en} youth international soccer playerss": "لاعبو منتخب {ar} لكرة القدم للشباب",
}

# TODO: USE format_multi_data
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
    "{en} {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} لكرة القدم ",
    "{en} {under_en} international managers": "مدربون {under_ar} دوليون من {ar}",
    "{en} {under_en} international soccer players": "لاعبو منتخب {ar} {under_ar} لكرة القدم ",
    "{en} {under_en} international soccer playerss": "لاعبو منتخب {ar} {under_ar} لكرة القدم "
}

KEY_AR_PLACEHOLDER = "{ar}"
KEY_EN_PLACEHOLDER = "{en}"

sport_starts = {
    "": "",
    "men's a'": "للرجال للمحليين",
    "men's b": "الرديف للرجال",
    "men's": "للرجال",
    "women's": "للسيدات",
    "men's youth": "للشباب",
    "women's youth": "للشابات",
    "amateur": "للهواة",
    "youth": "للشباب",
}


@functools.lru_cache(maxsize=1)
def _build_en_ar_is_p17() -> Dict[str, str]:
    """
    English country-name → Arabic country-name.
    This is the biggest dictionary (footballers, under-18, etc.).
    SPORT_FORMTS_EN_AR_IS_P17 len: 364 (34 base + 330 with_years)
    """
    YEARS_LIST = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]
    label_index: Dict[str, str] = dict(main_data)

    # Under-year managers/players
    for year in YEARS_LIST:
        label_index[f"{KEY_EN_PLACEHOLDER} under-{year} international managers"] = (
            f"مدربون تحت {year} سنة دوليون من {KEY_AR_PLACEHOLDER}"
        )
        label_index[f"{KEY_EN_PLACEHOLDER} under-{year} international players"] = (
            f"لاعبون تحت {year} سنة دوليون من {KEY_AR_PLACEHOLDER}"
        )
        label_index[f"{KEY_EN_PLACEHOLDER} under-{year} international playerss"] = (
            f"لاعبون تحت {year} سنة دوليون من {KEY_AR_PLACEHOLDER}"
        )

    # Footballers base groups
    for modifier, mod_label in sport_starts.items():

        start_word = "لاعبات منتخب" if "women's" in modifier else "لاعبو منتخب"

        place_holder_and_modifier = f"{KEY_EN_PLACEHOLDER} {modifier}" if modifier.strip() else KEY_EN_PLACEHOLDER

        for year in YEARS_LIST:
            youth = f"{start_word} {KEY_AR_PLACEHOLDER} تحت {year} سنة لكرة القدم {mod_label}"
            label_index[f"{place_holder_and_modifier} under-{year} international footballers"] = youth
            label_index[f"{place_holder_and_modifier} under-{year} international soccer players"] = youth
            label_index[f"{place_holder_and_modifier} under-{year} international soccer playerss"] = youth

    logger.debug(f"Lazy load SPORT_FORMTS_EN_AR_IS_P17, len: {len(label_index):,}.")

    return label_index


def get_con_3_lab_sports(suffix, country_start="", category="") -> str:

    formatted_data = _build_en_ar_is_p17()

    suffix_label = formatted_data.get(suffix, "").strip()

    return suffix_label


@functools.lru_cache(maxsize=1)
def _load_bot() -> FormatData:
    formatted_data = _build_en_ar_is_p17()
    return FormatData(
        formatted_data,
        contries_from_nat,
        key_placeholder=KEY_EN_PLACEHOLDER,
        value_placeholder=KEY_AR_PLACEHOLDER,
    )


@functools.lru_cache(maxsize=1)
def _load_multi_bot() -> MultiDataFormatterBase:
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
    }
    data = main_data | main_data_under

    return format_multi_data(
        formatted_data=data,
        data_list=under_data,
        key_placeholder="{under_en}",
        value_placeholder="{under_ar}",
        data_list2=contries_from_nat,
        key2_placeholder=KEY_EN_PLACEHOLDER,
        value2_placeholder=KEY_AR_PLACEHOLDER,
    )


@functools.lru_cache(maxsize=1000)
def get_en_ar_is_p17_label_multi(category: str) -> str:
    nat_bot = _load_multi_bot()
    return nat_bot.search_all(category)


# @dump_data(enable=1)
@functools.lru_cache(maxsize=1000)
def get_en_ar_is_p17_label(category: str) -> str:
    nat_bot = _load_bot()
    return nat_bot.search_all(category).strip()


SPORT_FORMTS_EN_AR_IS_P17 = _build_en_ar_is_p17()

len_print.data_len("p17_sport_to_move.py", {
    "SPORT_FORMTS_EN_AR_IS_P17": SPORT_FORMTS_EN_AR_IS_P17
})

__all__ = [
    "get_en_ar_is_p17_label",
    "get_en_ar_is_p17_label_multi",
    "get_con_3_lab_sports",
]
