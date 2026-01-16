"""
This module processes categories that start with an English country name and maps their suffixes to Arabic labels.
It checks the suffix against the following tables:

* category_relation_mapping
* pop_format


"""

import functools

from ...helps import dump_data, logger
from ...translations import (
    countries_from_nat,
)
from ..format_bots import pop_format
from ..format_bots.relation_mapping import translation_category_relations
from ..jobs_bots.get_helps import get_suffix_with_keys

countries_from_nat_sorted = dict(
    sorted(
        countries_from_nat.items(),
        key=lambda k: (-k[0].count(" "), -len(k[0])),
    )
)


@dump_data(1)
def from_category_relation_mapping(suffix) -> str:
    suffix_label = ""
    codd = translation_category_relations.get(suffix, "")

    if codd.startswith("لل"):
        suffix_label = "{} " + codd

    logger.debug(f'from_category_relation_mapping {suffix=}, {suffix_label}"')

    return suffix_label


@dump_data(1)
def get_con_3_lab_pop_format(suffix, country_start="", category="") -> str:
    suffix_label = ""

    key = suffix.strip()
    suffix_label = pop_format.get(key, "")
    logger.debug(f"<<lightblue>>>>>> <<lightgreen>>pop_format<<lightblue>> {category=}, {country_start=}, {suffix=}")

    return suffix_label


@functools.lru_cache(maxsize=10000)
@dump_data(1)
def get_p17_main(category: str) -> str:  # الإنجليزي جنسية والعربي اسم البلد
    """
    Category input in english is nationality, return arabic as country name.

    Resolve categories that start with nationality adjectives into country labels.

    """
    resolved_label = ""
    category = category.lower()

    suffix, country_start = get_suffix_with_keys(category, countries_from_nat_sorted)
    country_start_lab = countries_from_nat.get(country_start, "")

    if not suffix or not country_start:
        logger.info(f'<<lightred>>>>>> {suffix=} or {country_start=} == ""')
        return ""

    logger.debug(f"<<lightblue>> {country_start=}, {suffix=}")
    logger.debug(f"<<lightpurple>>>>>> {country_start_lab=}")

    suffix_label = (
        from_category_relation_mapping(suffix) or get_con_3_lab_pop_format(suffix, country_start, category) or ""
    )

    if not suffix_label:
        logger.debug(f'<<lightred>>>>>> {suffix_label=}, resolved_label == ""')
        return ""

    if "{nat}" in suffix_label:
        resolved_label = suffix_label.format(nat=country_start_lab)
    else:
        resolved_label = suffix_label.format(country_start_lab)

    logger.debug(f'<<lightblue>>>>>> get_p17: test_60: new cnt_la "{resolved_label}" ')

    return resolved_label


__all__ = [
    "get_p17_main",
]
