#!/usr/bin/python3
"""
!
"""

import functools

from ...helps.log import logger
from ...translations import RELIGIOUS_KEYS_PP
from .get_helps import get_suffix_with_keys
from .jobs_mainbot import jobs_with_nat_prefix


@functools.lru_cache(maxsize=None)
def try_relegins_jobs_with_suffix(cate: str) -> str:
    """
    Try to generate religion job labels using nationality-style suffix logic.

    TODO: replaced by new_relegins_jobs_with_suffix
    """

    logger.debug(f"\t xx start: <<lightred>>try_relegins_jobs_with_suffix >> <<lightpurple>> {cate=}")

    category_suffix, country_prefix = get_suffix_with_keys(cate, list(RELIGIOUS_KEYS_PP.keys()), "religions")

    country_lab = ""

    if category_suffix:

        Tab = RELIGIOUS_KEYS_PP.get(country_prefix, {})

        mens = Tab.get("mens")
        womens = Tab.get("females")
        country_lab = jobs_with_nat_prefix(cate, country_prefix, category_suffix, mens=mens, womens=womens, find_nats=False)

    logger.debug(f"\t xx end: <<lightred>>try_relegins_jobs_with_suffix <<lightpurple>> {cate=}, {country_lab=} ")

    return country_lab
