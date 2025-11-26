"""
This module processes categories that start with an English country name and maps their suffixes to Arabic labels.
It checks the suffix against the following tables:

* category_relation_mapping
* SPORT_FORMTS_EN_AR_IS_P17
* en_is_P17_ar_is_P17
* pop_format

If no match is found, it falls back to Get_Sport_Format_xo_en_ar_is_P17().

"""

from ...helps.log import logger
from ...helps.jsonl_dump import dump_data
from ...translations import (
    SPORT_FORMTS_EN_AR_IS_P17,
    Get_Sport_Format_xo_en_ar_is_P17,
    contries_from_nat,
    en_is_P17_ar_is_P17,
)
from ..format_bots import category_relation_mapping, pop_format
from ..jobs_bots.get_helps import get_suffix_with_keys


@dump_data(enable=1)
def from_category_relation_mapping(suffix) -> str:
    suffix_label = ""
    codd = category_relation_mapping.get(suffix, "")

    if codd.startswith("لل"):
        suffix_label = "{} " + codd

    logger.debug(f'from_category_relation_mapping {suffix=}, {suffix_label}"')

    return suffix_label

@dump_data(enable=1)
def get_con_3_lab_pop_format(suffix, country_start="", category="") -> str:

    suffix_label = ""

    key = suffix.strip()
    suffix_label = pop_format.get(key, "")
    logger.debug(f'<<lightblue>>>>>> <<lightgreen>>pop_format<<lightblue>> {category=}, {country_start=}, suffix:"{suffix}"')

    return suffix_label


def get_con_3_lab(suffix, country_start="", category="") -> tuple[str, str]:
    sources = [
        (SPORT_FORMTS_EN_AR_IS_P17, True, "SPORT_FORMTS_EN_AR_IS_P17"),
        (en_is_P17_ar_is_P17, True, "en_is_P17_ar_is_P17"),
        # (pop_format, False, "pop_format"),
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

    return suffix_label, name


def Get_P17(category: str) -> str:  # الإنجليزي جنسية والعربي اسم البلد
    """
    Category input in english is nationality, return arabic as country name.

    Resolve categories that start with nationality adjectives into country labels.

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

    suffix_label = from_category_relation_mapping(suffix)

    if not suffix_label:
        suffix_label, _ = get_con_3_lab(suffix, country_start, category)

    if not suffix_label:
        suffix_label = get_con_3_lab_pop_format(suffix, country_start, category)

    if not suffix_label:
        suffix_label = Get_Sport_Format_xo_en_ar_is_P17(suffix.strip())

    if not suffix_label:
        logger.debug(f'<<lightred>>>>>> {suffix_label=}, resolved_label == ""')
        return ""

    if "{nat}" in suffix_label:
        resolved_label = suffix_label.format(nat=country_start_lab)
    else:
        resolved_label = suffix_label.format(country_start_lab)

    logger.debug(f'<<lightblue>>>>>> Get_P17: test_60: new cnt_la "{resolved_label}" ')

    return resolved_label


__all__ = [
    "Get_P17",
]
