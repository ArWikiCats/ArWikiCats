"""
"""
import functools
from typing import Dict
from ...translations_formats import FormatData
from ...helps.log import logger
from ...helps.jsonl_dump import dump_data
from ...translations import (
    contries_from_nat,
)


KEY_AR_PLACEHOLDER = "{ar}"
KEY_EN_PLACEHOLDER = "{en}"

sport_starts = {
    "": "",
    "men's a' ": "للرجال للمحليين",
    "men's b ": "الرديف للرجال",
    "men's ": "للرجال",
    "women's ": "للسيدات",
    "men's youth ": "للشباب",
    "women's youth ": "للشابات",
    "amateur ": "للهواة",
    "youth ": "للشباب",
}


@functools.lru_cache(maxsize=1)
def _build_en_ar_is_p17() -> Dict[str, str]:
    """
    English country-name → Arabic country-name.
    This is the biggest dictionary (footballers, under-18, etc.).
    SPORT_FORMTS_EN_AR_IS_P17 len: 364
    """
    YEARS_LIST = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]
    # years make 330 key

    label_index: Dict[str, str] = {
        f"{KEY_EN_PLACEHOLDER} international rules football team": "منتخب {} لكرة القدم الدولية",
        f"{KEY_EN_PLACEHOLDER} rally championship": f"بطولة {KEY_AR_PLACEHOLDER} للراليات",
        f"{KEY_EN_PLACEHOLDER} sports templates": f"قوالب {KEY_AR_PLACEHOLDER} الرياضية",
        f"{KEY_EN_PLACEHOLDER} national team": f"منتخبات {KEY_AR_PLACEHOLDER} الوطنية",
        f"{KEY_EN_PLACEHOLDER} national teams": f"منتخبات {KEY_AR_PLACEHOLDER} الوطنية",
        f"{KEY_EN_PLACEHOLDER} national football team managers": f"مدربو منتخب {KEY_AR_PLACEHOLDER} لكرة القدم",
        f"{KEY_EN_PLACEHOLDER} international rally": f"رالي {KEY_AR_PLACEHOLDER} الدولي",
    }

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

        base = f"{start_word} {KEY_AR_PLACEHOLDER} لكرة القدم {mod_label}"

        label_index[f"{KEY_EN_PLACEHOLDER} {modifier}international footballers"] = base
        label_index[f"{KEY_EN_PLACEHOLDER} {modifier}international soccer players"] = base
        label_index[f"{KEY_EN_PLACEHOLDER} {modifier}international soccer playerss"] = base

        for year in YEARS_LIST:
            youth = f"{start_word} {KEY_AR_PLACEHOLDER} تحت {year} سنة لكرة القدم {mod_label}"
            label_index[f"{KEY_EN_PLACEHOLDER} {modifier}under-{year} international footballers"] = youth
            label_index[f"{KEY_EN_PLACEHOLDER} {modifier}under-{year} international soccer players"] = youth
            label_index[f"{KEY_EN_PLACEHOLDER} {modifier}under-{year} international soccer playerss"] = youth

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


__all__ = [
    "sport_formts_en_ar_is_p17_label",
    "get_con_3_lab_sports",
]
