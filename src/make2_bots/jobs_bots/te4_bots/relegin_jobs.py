#!/usr/bin/python3
"""
!
"""
import functools
from pathlib import Path

from ..jobs_mainbot import jobs_with_nat_prefix
from ....translations import RELIGIOUS_KEYS_PP
from ....helps.print_bot import output_test4
from ..get_helps import get_con_3
from ....helps.jsonl_dump import save


@functools.lru_cache(maxsize=None)
def try_relegins_jobs(cate: str) -> str:
    # ---
    output_test4(f"\t xx start: <<lightred>>try_relegins_jobs >> <<lightpurple>> cate:{cate}")
    # ---
    country_lab = ""
    # ---
    category_suffix, country_prefix = get_con_3(cate, "religions")
    # ---
    if not category_suffix:
        return ""
    # ---
    Tab = RELIGIOUS_KEYS_PP.get(country_prefix, {})
    # ---
    mens = Tab.get("mens")
    womens = Tab.get("womens")
    # ---
    country_lab = jobs_with_nat_prefix(
        cate,
        country_prefix,
        category_suffix,
        mens=mens,
        womens=womens
    )
    # ---
    output_test4(f"\t xx end: <<lightred>>try_relegins_jobs <<lightpurple>> cate:{cate}, country_lab:{country_lab} ")
    # ---
    if country_lab:
        save(Path(__file__).parent / "relegin_jobs.jsonl", [{"cate": cate, "country_prefix": country_prefix, "category_suffix": category_suffix, "mens": mens, "womens": womens, "country_lab": country_lab}])
    # ---
    return country_lab
