"""
This module processes categories that start with an English country name and maps their suffixes to Arabic labels.
It checks the suffix against the following tables:

* category_relation_mapping
* pop_format


"""

from ...helps.log import logger
from ...helps.jsonl_dump import dump_data
from ...translations import (
    contries_from_nat,
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


def get_con_3_lab_pop_format(suffix, country_start="", category="") -> str:

    suffix_label = ""

    key = suffix.strip()
    suffix_label = pop_format.get(key, "")
    logger.debug(f'<<lightblue>>>>>> <<lightgreen>>pop_format<<lightblue>> {category=}, {country_start=}, suffix:"{suffix}"')

    return suffix_label


def Get_P17_main(category: str) -> str:  # الإنجليزي جنسية والعربي اسم البلد
    """
    Category input in english is nationality, return arabic as country name.

    Resolve categories that start with nationality adjectives into country labels.

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
        suffix_label = get_con_3_lab_pop_format(suffix, country_start, category)

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
    "Get_P17_main",
]
