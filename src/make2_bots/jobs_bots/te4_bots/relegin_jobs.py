#!/usr/bin/python3
"""
!
"""

import functools
from pathlib import Path

from ....helps.log import logger
from ....translations import RELIGIOUS_KEYS_PP

# from ....helps.jsonl_dump import save
from ..get_helps import get_con_3
from ..jobs_mainbot import jobs_with_nat_prefix


@functools.lru_cache(maxsize=None)
def relegins_jobs(cate: str) -> str:
    logger.debug(f"\t xx start: <<lightred>>relegins_jobs >> <<lightpurple>> cate:{cate}")
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
def try_relegins_jobs_with_suffix(cate: str) -> str:
    logger.debug(f"\t xx start: <<lightred>>try_relegins_jobs_with_suffix >> <<lightpurple>> cate:{cate}")
    category_suffix, country_prefix = get_con_3(cate, "religions")
    if not category_suffix:
        return ""
    Tab = RELIGIOUS_KEYS_PP.get(country_prefix, {})
    mens = Tab.get("mens")
    womens = Tab.get("womens")
    country_lab = jobs_with_nat_prefix(cate, country_prefix, category_suffix, mens=mens, womens=womens, find_nats=False)
    logger.debug(f"\t xx end: <<lightred>>try_relegins_jobs_with_suffix <<lightpurple>> cate:{cate}, country_lab:{country_lab} ")
    # if country_lab:
    # save(Path(__file__).parent / "relegin_jobs.jsonl", [{"cate": cate, "country_prefix": country_prefix, "category_suffix": category_suffix, "mens": mens, "womens": womens, "country_lab": country_lab}])
    return country_lab
