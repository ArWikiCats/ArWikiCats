#!/usr/bin/python3
"""
from .test4_bots.relegin_jobs import try_relegins_jobs

"""
from typing import Dict
from ..jobs_mainbot import Jobs
from ....helps.print_bot import output_test4
from ..get_helps import get_con_3

try_relegins_jobs_cash: Dict[str, str] = {}


def try_relegins_jobs(cate: str) -> str:
    # ---
    cach_key = cate.lower().strip()
    # ---
    if cach_key in try_relegins_jobs_cash:
        return try_relegins_jobs_cash[cach_key]
    # ---
    output_test4(f"\t xx start: <<lightred>>try_relegins_jobs >> <<lightpurple>> cate:{cate}")
    # ---
    contry_lab = ""
    # ---
    job_example, nat = get_con_3(cate, list(religious_keys_PP.keys()), "religions")
    # ---
    Tab = religious_keys_PP.get(nat, {})
    # ---
    if job_example:
        contry_lab = Jobs(cate, nat, job_example, Type="rel", tab=Tab)
    # ---
    output_test4(f"\t xx end: <<lightred>>try_relegins_jobs <<lightpurple>> cate:{cate}, contry_lab:{contry_lab} ")
    # ---
    try_relegins_jobs_cash[cach_key] = contry_lab
    # ---
    return contry_lab
