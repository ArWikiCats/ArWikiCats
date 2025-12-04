#!/usr/bin/python3
"""
!
"""

import functools

from ...helps.jsonl_dump import dump_data
from ...helps.log import logger
from ...translations import RELIGIOUS_KEYS_PP

# from ....helps.jsonl_dump import save
from .get_helps import get_suffix_with_keys
from .jobs_mainbot import jobs_with_nat_prefix


@functools.lru_cache(maxsize=None)
@dump_data(1)
def relegins_jobs(cate: str) -> str:
    """
    Resolve religion-based job labels without country context.
    TODO: replaced by new_relegins_jobs_with_suffix
    """
    logger.debug(f"\t xx start: <<lightred>>relegins_jobs >> <<lightpurple>> {cate=}")
    cate_lower = cate.lower().strip()
    data = RELIGIOUS_KEYS_PP.get(cate_lower, {})
    if data:
        return data.get("mens")
    for x in ["female ", "womens ", "women's "]:
        if cate_lower.startswith(x):
            cate_lower_2 = cate_lower[len(x) :]
            data = RELIGIOUS_KEYS_PP.get(cate_lower_2, {})
            if data:
                return data.get("womens")
    return ""


@functools.lru_cache(maxsize=None)
def get_suffix_prefix(cate: str) -> str:
    category_suffix, country_prefix = get_suffix_with_keys(cate, list(RELIGIOUS_KEYS_PP.keys()), "religions")
    return category_suffix, country_prefix


@functools.lru_cache(maxsize=None)
def try_relegins_jobs_with_suffix(cate: str) -> str:
    """
    Try to generate religion job labels using nationality-style suffix logic.

    TODO: replaced by new_relegins_jobs_with_suffix
    """

    logger.debug(f"\t xx start: <<lightred>>try_relegins_jobs_with_suffix >> <<lightpurple>> {cate=}")

    category_suffix, country_prefix = get_suffix_prefix(cate)

    country_lab = ""

    if category_suffix:

        Tab = RELIGIOUS_KEYS_PP.get(country_prefix, {})

        mens = Tab.get("mens")
        womens = Tab.get("womens")
        country_lab = jobs_with_nat_prefix(cate, country_prefix, category_suffix, mens=mens, womens=womens, find_nats=False)

    logger.debug(f"\t xx end: <<lightred>>try_relegins_jobs_with_suffix <<lightpurple>> {cate=}, {country_lab=} ")

    return country_lab
