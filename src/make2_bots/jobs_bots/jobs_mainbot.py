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
    MEN_WOMENS_WITH_NATO,
)
from ...helps.log import logger
from ..jobs_bots.priffix_bot import Women_s_priffix_work, priffix_Mens_work
from ...helps.jsonl_dump import save


@functools.lru_cache(maxsize=None)
def Jobs(cate: str, country_prefix: str, category_suffix: str, mens: str="", womens: str="", save_result=True) -> str:
    """Retrieve job labels based on category and country.

    This function generates job labels for both men and women based on the
    provided category, starting country, and additional context. It uses
    @functools.lru_cache for performance optimization and utilizes various mappings to
    determine the appropriate labels. The function handles different cases
    for men's and women's jobs, including specific prefixes and country-
    specific labels.

    Args:
        cate (str): The category of the job.
        country_prefix (str): The starting country for the job label.
        category_suffix (str): Additional context for the job label.

    Returns:
        str: The generated job label based on the input parameters.
    """
    # ---
    category_suffix = category_suffix.strip().lower()
    # ---
    logger.debug(f'<<lightblue>> bot_te_4.py Jobs: cate: "{cate}", country_prefix: "{country_prefix}", category_suffix: "{category_suffix}" ')
    country = country_prefix
    country_lab = ""
    # ---
    category_suffix = category_suffix[len("people ") :] if category_suffix.startswith("people ") else category_suffix
    # ---
    pkjn = [" مغتربون", " مغتربات"]
    # ---
    # mens Jobs
    mens_nat_lab: str = mens or Nat_mens.get(country, "")
    # ---
    if mens_nat_lab:
        # ---
        if category_suffix == "people":
            country_lab = mens_nat_lab
        # ---
        con_lab = ""
        # ---
        if not country_lab:
            con_lab = jobs_mens_data.get(category_suffix, "") or priffix_Mens_work(category_suffix)
        # ---
        if con_lab:
            # ---
            country_lab = f"{con_lab} {mens_nat_lab}"
            if con_lab.startswith("حسب"):
                country_lab = f"{mens_nat_lab} {con_lab}"
            # ---
            if category_suffix in NAT_BEFORE_OCC:
                country_lab = f"{mens_nat_lab} {con_lab}"
            # ---
            TAJO = MEN_WOMENS_WITH_NATO.get(category_suffix, {})
            if TAJO and "{nato}" in TAJO.get("mens", ""):
                country_lab = TAJO["mens"].format(nato=mens_nat_lab)
                logger.debug('<<lightblue>> TAJO["mens"]: has {nato} "%s"' % TAJO["mens"])
            # ---
            for kjn in pkjn:
                if con_lab.endswith(kjn):
                    country_lab = f"{con_lab[:-len(kjn)]} {mens_nat_lab}{kjn}"
                    break
            # ---
            logger.debug(f'\t<<lightblue>> category_suffix: "{category_suffix}" ')
            logger.debug(f'\t<<lightblue>> test mens Jobs: new lab: "{country_lab}" ')
    # ---
    # Womens Jobs
    # ---
    women_nat_lab: str = womens or Nat_Womens.get(country, "")
    # ---
    if not country_lab and women_nat_lab:
        # ---
        if category_suffix in ["women", "female", "women's"]:
            country_lab = women_nat_lab
        # ---
        if not country_lab:
            con_lab = short_womens_jobs.get(category_suffix, "") or Women_s_priffix_work(category_suffix)
            # ---
            if not con_lab:
                # TODO: NEW TO CHECK
                # Check for {nato} in women's path as well, assuming con_lab can come from MEN_WOMENS_WITH_NATO
                TAJO = MEN_WOMENS_WITH_NATO.get(category_suffix, {})
                if TAJO and "{nato}" in TAJO.get("womens", ""):
                    country_lab = TAJO["womens"].format(nato=women_nat_lab)
                    logger.debug('<<lightblue>> TAJO["womens"]: has {nato} "%s"' % TAJO["womens"])
            # ---
            if con_lab:
                country_lab = f"{con_lab} {women_nat_lab}"
                # ---
                if "{nato}" in con_lab:
                    country_lab = con_lab.format(nato=women_nat_lab)
                    logger.debug('<<lightblue>> TAJO["womens"]: has {nato} "%s"' % con_lab)
            # ---
            for kjn in pkjn:
                if con_lab.endswith(kjn):
                    country_lab = f"{con_lab[:-len(kjn)]} {women_nat_lab}{kjn}"
                    break
        # ---
        logger.debug(f'\t<<lightblue>> test Womens Jobs: new lab: "{country_lab}" ')
    # ---
    if country_lab and save_result:
        save(Path(__file__).parent / "jobs_mainbot.jsonl", [{"cate": cate, "country_prefix": country_prefix, "category_suffix": category_suffix, "mens": mens, "womens": womens, "country_lab": country_lab}])
    # ---
    return country_lab
