""" """

from ...helps.log import logger
from ...translations import (
    SPORT_FORMTS_EN_AR_IS_P17,
    Get_Sport_Format_xo_en_ar_is_P17,
    contries_from_nat,
    en_is_P17_ar_is_P17,
)
from ..format_bots import category_relation_mapping, pop_format
from ..jobs_bots.get_helps import get_suffix_with_keys


def get_con_3_lab(suffix):
    sources = [
        (SPORT_FORMTS_EN_AR_IS_P17, True, "SPORT_FORMTS_EN_AR_IS_P17"),
        (en_is_P17_ar_is_P17, True, "en_is_P17_ar_is_P17"),
        (pop_format, False, "pop_format"),
    ]

    suffix_label = ""

    for source, do_strip, name in sources:
        key = suffix.strip() if do_strip else suffix
        suffix_label = source.get(key, "")
        if suffix_label:
            logger.debug(f'<<lightblue>>>>>> <<lightgreen>>{name}<<lightblue>> suffix:"{suffix}"')
            break

    return suffix_label


def Get_P17(category: str) -> str:  # الإنجليزي جنسية والعربي اسم البلد
    """
    Category input in english is nationality, return arabic as country name.

    Resolve categories that start with nationality adjectives into country labels.

    TODO: use FormatData method
    """
    resolved_label = ""
    suffix_label = ""
    category = category.lower()

    suffix, country_start = get_suffix_with_keys(category, contries_from_nat)
    country_start_lab = contries_from_nat.get(country_start, "")

    if not suffix or not country_start:
        logger.info(f'<<lightred>>>>>> suffix: "{suffix}" or country_start :"{country_start}" == ""')
        return

    logger.debug(f'<<lightblue>> country_start:"{country_start}", suffix:"{suffix}"')
    logger.debug(f'<<lightpurple>>>>>> country_start_lab:"{country_start_lab}"')

    if suffix in category_relation_mapping:
        codd = category_relation_mapping[suffix]
        if codd.startswith("لل"):
            suffix_label = "{} " + codd
            logger.debug(f'get lab from category_relation_mapping suffix_label:"{suffix_label}"')

    if not suffix_label:
        suffix_label = get_con_3_lab(suffix)

    if not suffix_label:
        suffix_label = Get_Sport_Format_xo_en_ar_is_P17(suffix.strip())

    if not suffix_label:
        logger.debug(f'<<lightred>>>>>> {suffix_label=}, resolved_label == ""')
        return

    if "{nat}" in suffix_label:
        resolved_label = suffix_label.format(nat=country_start_lab)
    else:
        resolved_label = suffix_label.format(country_start_lab)

    logger.debug(f'<<lightblue>>>>>> Get_P17: test_60: new cnt_la "{resolved_label}" ')

    return resolved_label


__all__ = [
    "Get_P17",
]
