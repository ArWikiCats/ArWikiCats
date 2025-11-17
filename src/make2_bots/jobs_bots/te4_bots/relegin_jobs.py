#!/usr/bin/python3
"""
!
"""
from ..jobs_mainbot import Jobs
from ....translations import RELIGIOUS_KEYS_PP
from ....helps.print_bot import output_test4
from ..get_helps import get_con_3
import functools


@functools.lru_cache(maxsize=None)
def try_relegins_jobs(cate: str) -> str:
    # ---
    output_test4(f"\t xx start: <<lightred>>try_relegins_jobs >> <<lightpurple>> cate:{cate}")
    # ---
    country_lab = ""
    # ---
    category_suffix, country_prefix = get_con_3(cate, "religions")
    # ---
    Tab = RELIGIOUS_KEYS_PP.get(country_prefix, {})
    # ---
    if category_suffix:
        country_lab = Jobs(
            cate,
            country_prefix,
            category_suffix,
            mens=Tab.get("mens"),
            womens=Tab.get("womens")
        )
    # ---
    output_test4(f"\t xx end: <<lightred>>try_relegins_jobs <<lightpurple>> cate:{cate}, country_lab:{country_lab} ")
    # ---
    return country_lab
