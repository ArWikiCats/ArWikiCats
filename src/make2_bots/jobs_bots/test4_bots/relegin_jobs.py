#!/usr/bin/python3
"""
from .test4_bots.relegin_jobs import try_relegins_jobs

"""
from typing import Dict
from ..jobs_mainbot import Jobs
from ....ma_lists import RELIGIOUS_KEYS_PP
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
    job_example, nat = get_con_3(cate, list(RELIGIOUS_KEYS_PP.keys()), "religions")
    # ---
    Tab = RELIGIOUS_KEYS_PP.get(nat, {})
    # ---
    if job_example:
        country_lab = Jobs(cate, nat, job_example, Type="rel", tab=Tab)
    # ---
    output_test4(f"\t xx end: <<lightred>>try_relegins_jobs <<lightpurple>> cate:{cate}, country_lab:{country_lab} ")
    # ---

    # ---
    return country_lab
