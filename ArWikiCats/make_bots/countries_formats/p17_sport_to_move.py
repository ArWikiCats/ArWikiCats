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
from ..jobs_bots.get_helps import get_suffix_with_keys


COUNTRY_PLACEHOLDER = "{}"

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
    SPORT_FORMTS_EN_AR_IS_P17
    """
    YEARS_LIST = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]
    # years make 330 key

    label_index: Dict[str, str] = {}

    # Static entries
    label_index["international rules football team"] = "منتخب {} لكرة القدم الدولية"

    # Under-year managers/players
    for year in YEARS_LIST:
        label_index[f"under-{year} international managers"] = (
            f"مدربو تحت {year} سنة دوليون من {COUNTRY_PLACEHOLDER}"
        )
        label_index[f"under-{year} international players"] = (
            f"لاعبو تحت {year} سنة دوليون من {COUNTRY_PLACEHOLDER}"
        )
        label_index[f"under-{year} international playerss"] = (
            f"لاعبو تحت {year} سنة دوليون من {COUNTRY_PLACEHOLDER}"
        )

    # Footballers base groups
    for modifier, mod_label in sport_starts.items():

        start_word = "لاعبات منتخب" if "women's" in modifier else "لاعبو منتخب"

        base = f"{start_word} {COUNTRY_PLACEHOLDER} لكرة القدم {mod_label}"

        label_index[f"{modifier}international footballers"] = base
        label_index[f"{modifier}international soccer players"] = base
        label_index[f"{modifier}international soccer playerss"] = base

        for year in YEARS_LIST:
            youth = f"{start_word} {COUNTRY_PLACEHOLDER} تحت {year} سنة لكرة القدم {mod_label}"
            label_index[f"{modifier}under-{year} international footballers"] = youth
            label_index[f"{modifier}under-{year} international soccer players"] = youth
            label_index[f"{modifier}under-{year} international soccer playerss"] = youth

    label_index["rally championship"] = f"بطولة {COUNTRY_PLACEHOLDER} للراليات"

    label_index["sports templates"] = f"قوالب {COUNTRY_PLACEHOLDER} الرياضية"
    label_index["national team"] = f"منتخبات {COUNTRY_PLACEHOLDER} الوطنية"
    label_index["national teams"] = f"منتخبات {COUNTRY_PLACEHOLDER} الوطنية"
    label_index["national football team managers"] = f"مدربو منتخب {COUNTRY_PLACEHOLDER} لكرة القدم"

    label_index["international rally"] = f"رالي {COUNTRY_PLACEHOLDER} الدولي"

    return label_index


def get_con_3_lab_sports(suffix, country_start="", category="") -> str:

    formatted_data = _build_en_ar_is_p17()

    suffix_label = formatted_data.get(suffix, "")

    return suffix_label


@functools.lru_cache(maxsize=1)
def _load_bot() -> str:
    formatted_data = _build_en_ar_is_p17()
    _data = {f"{{en}} {x}": v for x, v in formatted_data.items()}

    return FormatData(
        _data,
        contries_from_nat,
        key_placeholder="{en}",
        value_placeholder=COUNTRY_PLACEHOLDER,
    )


def sport_formts_en_ar_is_p17_label_new(category: str) -> str:
    nat_bot = _load_bot()
    return nat_bot.search(category).strip()


# @dump_data(enable=1)
def sport_formts_en_ar_is_p17_label(category: str) -> str:
    """
    TODO: use FormatData method
    """
    resolved_label = ""
    category = category.lower()

    suffix, country_start = get_suffix_with_keys(category, contries_from_nat)
    country_start_lab = contries_from_nat.get(country_start, "")

    if not suffix or not country_start:
        logger.info(f'<<lightred>>>>>> suffix: "{suffix}" or country_start :"{country_start}" == ""')
        return ""

    logger.debug(f'<<lightblue>> country_start:"{country_start}", suffix:"{suffix}"')
    logger.debug(f'<<lightpurple>>>>>> country_start_lab:"{country_start_lab}"')

    formatted_data = _build_en_ar_is_p17()

    suffix_label = formatted_data.get(suffix, "")

    logger.debug(f'<<lightblue>>>>>> <<lightgreen>>SPORT_FORMTS_EN_AR_IS_P17<<lightblue>> suffix:"{suffix}"')

    if not suffix_label:
        logger.debug(f'<<lightred>>>>>> {suffix_label=}, resolved_label == ""')
        return ""

    if "{nat}" in suffix_label:
        resolved_label = suffix_label.format(nat=country_start_lab)
    else:
        resolved_label = suffix_label.format(country_start_lab)

    logger.debug(f'<<lightblue>>>>>> Get_P17_with_p17_sport: test_60: new cnt_la "{resolved_label}" ')

    return resolved_label.strip()


__all__ = [
    "sport_formts_en_ar_is_p17_label",
    "sport_formts_en_ar_is_p17_label_new",
    "get_con_3_lab_sports",
]
