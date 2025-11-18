#!/usr/bin/python3
"""
!
"""
import functools
from pathlib import Path
from ...translations import (
    Nat_mens,
    Nat_Womens,
    jobs_mens_data,
    short_womens_jobs,
    NAT_BEFORE_OCC,
)
from ...helps.log import logger
from ..jobs_bots.priffix_bot import Women_s_priffix_work, priffix_Mens_work
from ...helps.jsonl_dump import save

MEN_WOMENS_WITH_NATO = {
    "eugenicists": {
        "mens": "علماء {nato} متخصصون في تحسين النسل",
        "womens": "عالمات {nato} متخصصات في تحسين النسل",
    },
    "politicians who committed suicide": {
        "mens": "سياسيون {nato} أقدموا على الانتحار",
        "womens": "سياسيات {nato} أقدمن على الانتحار",
    },
    "contemporary artists": {
        "mens": "فنانون {nato} معاصرون",
        "womens": "فنانات {nato} معاصرات",
    },
}


def fix_expatriates(country_lab, con_lab, nat_lab):
    # ---
    pkjn = ["مغتربون", "مغتربات"]
    # ---
    for kjn in pkjn:
        if con_lab.endswith(f" {kjn}"):
            striped = con_lab[:-len(kjn)].strip()
            country_lab = f"{striped} {nat_lab} {kjn}"
            break
        # ---
        if country_lab.endswith(f" {kjn}"):
            # ---
            striped = country_lab[:-len(kjn)].strip()
            country_lab = f"{striped} {kjn}"
            break
    # ---
    return country_lab


def country_lab_mens_womens(jender_key, category_suffix, nat_lab, con_lab):
    # ---
    # TODO: NEW TO CHECK
    TAJO = MEN_WOMENS_WITH_NATO.get(category_suffix, {}).get(jender_key, "")
    # ---
    if "{nato}" in TAJO:
        country_lab = TAJO.format(nato=nat_lab)
        logger.debug(f"<<lightblue>> TAJO[{jender_key}]: has {{nato}} {TAJO}")
        return country_lab
    # ---
    if not con_lab:
        return ""
    # ---
    country_lab = f"{con_lab} {nat_lab}"
    # ---
    if con_lab.startswith("حسب") or category_suffix in NAT_BEFORE_OCC:
        country_lab = f"{nat_lab} {con_lab}"
    # ---
    country_lab = fix_expatriates(country_lab, con_lab, nat_lab)
    # ---
    logger.debug(f'\t<<lightblue>> test {jender_key} Jobs: new lab: "{country_lab}" ')
    # ---
    return country_lab


@functools.lru_cache(maxsize=None)
def jobs_with_nat_prefix(cate: str, country_prefix: str, category_suffix: str, mens: str="", womens: str="",
                         save_result=True, find_nats=True) -> str:
    """
    Retrieve job labels based on category and country.
    """
    # ---
    category_suffix = category_suffix.strip().lower()
    # ---
    logger.debug(f'<<lightblue>> jobs_mainbot.py jobs_with_nat_prefix: {cate=}, {country_prefix=}, {category_suffix=}.')
    # ---
    country_lab = ""
    # ---
    category_suffix = category_suffix[len("people ") :] if category_suffix.startswith("people ") else category_suffix
    # ---
    mens_nat_lab: str = mens or (Nat_mens.get(country_prefix, "") if find_nats else "")
    # ---
    if mens_nat_lab:
        if category_suffix == "people":
            country_lab = mens_nat_lab
        else:
            con_lab = jobs_mens_data.get(category_suffix, "") or priffix_Mens_work(category_suffix) or ""
            country_lab = country_lab_mens_womens("mens", category_suffix, mens_nat_lab, con_lab)
    # ---
    women_nat_lab: str = womens or (Nat_Womens.get(country_prefix, "") if find_nats else "")
    # ---
    if not country_lab and women_nat_lab:
        if category_suffix in ["women", "female", "women's"]:
            country_lab = women_nat_lab
        else:
            con_lab = short_womens_jobs.get(category_suffix, "") or Women_s_priffix_work(category_suffix) or ""
            country_lab = country_lab_mens_womens("womens", category_suffix, women_nat_lab, con_lab)
    # ---
    if country_lab and save_result:
        save(Path(__file__).parent / "jobs_mainbot.jsonl", [{"cate": cate, "country_prefix": country_prefix, "category_suffix": category_suffix, "mens": mens, "womens": womens, "country_lab": country_lab}])
    # ---
    return country_lab
