"""
"""

from ...helps.log import logger
from ...helps.jsonl_dump import dump_data
from ...translations import (
    Get_Sport_Format_xo_en_ar_is_P17,
    SPORT_FORMTS_EN_AR_IS_P17,
    contries_from_nat,
)
from ..jobs_bots.get_helps import get_suffix_with_keys

en_is_P17_ar_is_P17_SPORTS: dict[str, str] = {
    "afc women's asian cup squad": "تشكيلات {} في كأس آسيا للسيدات",
    "afc asian cup squad": "تشكيلات {} في كأس آسيا",
    "fifa world cup squad": "تشكيلات {} في كأس العالم",
    "fifa futsal world cup squad": "تشكيلات {} في كأس العالم لكرة الصالات",
    "summer olympics squad": "تشكيلات {} في الألعاب الأولمبية الصيفية",
    "winter olympics squad": "تشكيلات {} في الألعاب الأولمبية الشتوية",
    "olympics squad": "تشكيلات {} في الألعاب الأولمبية",
    "summer olympics": " {} في الألعاب الأولمبية الصيفية",
    "winter olympics": " {} في الألعاب الأولمبية الشتوية",
}


@dump_data(enable=1)
def wrap_get_Sport_Format_xo_en_ar_is_P17(suffix) -> str:
    return Get_Sport_Format_xo_en_ar_is_P17(suffix)


def get_con_3_lab_sports(suffix, country_start="", category="") -> tuple[str, str]:
    sources = [
        (SPORT_FORMTS_EN_AR_IS_P17, True, "SPORT_FORMTS_EN_AR_IS_P17"),
        (en_is_P17_ar_is_P17_SPORTS, True, "en_is_P17_ar_is_P17_SPORTS"),
    ]

    suffix_label = ""
    name = ""
    for source, do_strip, name in sources:
        key = suffix.strip() if do_strip else suffix
        suffix_label = source.get(key, "")
        if suffix_label:
            break

    name = name if suffix_label else ""
    logger.debug(f'<<lightblue>>>>>> <<lightgreen>>{name}<<lightblue>> suffix:"{suffix}"')

    return suffix_label


def Get_P17_with_sport(category: str) -> str:
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

    suffix_label = wrap_get_Sport_Format_xo_en_ar_is_P17(suffix.strip())

    if not suffix_label:
        suffix_label = get_con_3_lab_sports(suffix.strip())

    if not suffix_label:
        logger.debug(f'<<lightred>>>>>> {suffix_label=}, resolved_label == ""')
        return ""

    if "{nat}" in suffix_label:
        resolved_label = suffix_label.format(nat=country_start_lab)
    else:
        resolved_label = suffix_label.format(country_start_lab)

    logger.debug(f'<<lightblue>>>>>> Get_P17_with_p17_sport: test_60: new cnt_la "{resolved_label}" ')

    return resolved_label


__all__ = [
    "Get_P17_with_sport",
    "get_con_3_lab_sports",
]
