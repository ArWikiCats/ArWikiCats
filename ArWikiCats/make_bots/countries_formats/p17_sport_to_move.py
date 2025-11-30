"""
"""
import functools
from typing import Dict
from ...helps import len_print
from ...translations_formats import FormatData
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
    "{en} amateur {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} سنة لكرة القدم للهواة",
    "{en} amateur {under_en} international soccer players": "لاعبو منتخب {ar} {under_ar} سنة لكرة القدم للهواة",
    "{en} amateur {under_en} international soccer playerss": "لاعبو منتخب {ar} {under_ar} سنة لكرة القدم للهواة",
    "{en} men's a' {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} سنة لكرة القدم للرجال للمحليين",
    "{en} men's a' {under_en} international soccer players": "لاعبو منتخب {ar} {under_ar} سنة لكرة القدم للرجال للمحليين",
    "{en} men's a' {under_en} international soccer playerss": "لاعبو منتخب {ar} {under_ar} سنة لكرة القدم للرجال للمحليين",
    "{en} men's b {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} سنة لكرة القدم الرديف للرجال",
    "{en} men's b {under_en} international soccer players": "لاعبو منتخب {ar} {under_ar} سنة لكرة القدم الرديف للرجال",
    "{en} men's b {under_en} international soccer playerss": "لاعبو منتخب {ar} {under_ar} سنة لكرة القدم الرديف للرجال",
    "{en} men's youth {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} سنة لكرة القدم للشباب",
    "{en} men's youth {under_en} international soccer players": "لاعبو منتخب {ar} {under_ar} سنة لكرة القدم للشباب",
    "{en} men's youth {under_en} international soccer playerss": "لاعبو منتخب {ar} {under_ar} سنة لكرة القدم للشباب",
    "{en} men's {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} سنة لكرة القدم للرجال",
    "{en} men's {under_en} international soccer players": "لاعبو منتخب {ar} {under_ar} سنة لكرة القدم للرجال",
    "{en} men's {under_en} international soccer playerss": "لاعبو منتخب {ar} {under_ar} سنة لكرة القدم للرجال",
    "{en} women's youth {under_en} international footballers": "لاعبات منتخب {ar} {under_ar} سنة لكرة القدم للشابات",
    "{en} women's youth {under_en} international soccer players": "لاعبات منتخب {ar} {under_ar} سنة لكرة القدم للشابات",
    "{en} women's youth {under_en} international soccer playerss": "لاعبات منتخب {ar} {under_ar} سنة لكرة القدم للشابات",
    "{en} women's {under_en} international footballers": "لاعبات منتخب {ar} {under_ar} سنة لكرة القدم للسيدات",
    "{en} women's {under_en} international soccer players": "لاعبات منتخب {ar} {under_ar} سنة لكرة القدم للسيدات",
    "{en} women's {under_en} international soccer playerss": "لاعبات منتخب {ar} {under_ar} سنة لكرة القدم للسيدات",
    "{en} youth {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} سنة لكرة القدم للشباب",
    "{en} youth {under_en} international soccer players": "لاعبو منتخب {ar} {under_ar} سنة لكرة القدم للشباب",
    "{en} youth {under_en} international soccer playerss": "لاعبو منتخب {ar} {under_ar} سنة لكرة القدم للشباب",
    "{en} {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} سنة لكرة القدم ",
    "{en} {under_en} international managers": "مدربو {under_ar} سنة دوليون من {ar}",
    "{en} {under_en} international soccer players": "لاعبو منتخب {ar} {under_ar} سنة لكرة القدم ",
    "{en} {under_en} international soccer playerss": "لاعبو منتخب {ar} {under_ar} سنة لكرة القدم "
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
            f"مدربو تحت {year} سنة دوليون من {KEY_AR_PLACEHOLDER}"
        )
        label_index[f"{KEY_EN_PLACEHOLDER} under-{year} international players"] = (
            f"لاعبو تحت {year} سنة دوليون من {KEY_AR_PLACEHOLDER}"
        )
        label_index[f"{KEY_EN_PLACEHOLDER} under-{year} international playerss"] = (
            f"لاعبو تحت {year} سنة دوليون من {KEY_AR_PLACEHOLDER}"
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
def _load_bot() -> str:
    formatted_data = _build_en_ar_is_p17()
    return FormatData(
        formatted_data,
        contries_from_nat,
        key_placeholder=KEY_EN_PLACEHOLDER,
        value_placeholder=KEY_AR_PLACEHOLDER,
    )


# @dump_data(enable=1)
@functools.lru_cache(maxsize=1000)
def sport_formts_en_ar_is_p17_label(category: str) -> str:
    nat_bot = _load_bot()
    return nat_bot.search(category).strip()


SPORT_FORMTS_EN_AR_IS_P17 = _build_en_ar_is_p17()

len_print.data_len("p17_sport_to_move.py", {
    "SPORT_FORMTS_EN_AR_IS_P17": SPORT_FORMTS_EN_AR_IS_P17
})

__all__ = [
    "sport_formts_en_ar_is_p17_label",
    "get_con_3_lab_sports",
]
