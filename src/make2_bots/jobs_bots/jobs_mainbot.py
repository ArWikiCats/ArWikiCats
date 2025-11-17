#!/usr/bin/python3
"""
!
"""
import functools
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


@functools.lru_cache(maxsize=None)
def Jobs(cate: str, country_prefix: str, category_suffix: str, mens: str="", womens: str="") -> str:
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
    logger.debug(f'<<lightblue>> bot_te_4.py Jobs: cate: "{cate}", country_prefix: "{country_prefix}", category_suffix: "{category_suffix}" ')
    country = country_prefix
    country_lab = ""
    # ---
    con_3_lab = jobs_mens_data.get(category_suffix, "")
    # ---
    con_4 = category_suffix
    if category_suffix.startswith("people "):
        con_4 = category_suffix[len("people ") :]
    # ---
    pkjn = [" مغتربون", " مغتربات"]
    # ---
    # mens Jobs
    mens_nat_lab = mens or Nat_mens.get(country, "")
    # ---
    if mens_nat_lab:
        # ---
        if category_suffix.strip() == "people":
            country_lab = mens_nat_lab
        # ---
        if not country_lab:
            con_3_lab = priffix_Mens_work(category_suffix)
        # ---
        if con_3_lab:
            # ---
            country_lab = f"{con_3_lab} {mens_nat_lab}"
            if con_3_lab.startswith("حسب"):
                country_lab = f"{mens_nat_lab} {con_3_lab}"
            # ---
            if category_suffix.strip() in NAT_BEFORE_OCC or con_4.strip() in NAT_BEFORE_OCC:
                country_lab = f"{mens_nat_lab} {con_3_lab}"
            # ---
            TAJO = MEN_WOMENS_WITH_NATO.get(category_suffix, {})
            if TAJO and "{nato}" in TAJO.get("mens", ""):
                country_lab = TAJO["mens"].format(nato=mens_nat_lab)
                logger.debug('<<lightblue>> TAJO["mens"]: has {nato} "%s"' % TAJO["mens"])
            # ---
            for kjn in pkjn:
                if con_3_lab.endswith(kjn):
                    country_lab = f"{con_3_lab[:-len(kjn)]} {mens_nat_lab}{kjn}"
                    break
            # ---
            logger.debug(f'\t<<lightblue>> category_suffix: "{category_suffix}" ')
            logger.debug(f'\t<<lightblue>> test mens Jobs: new lab: "{country_lab}" ')
    # ---
    # Womens Jobs
    # ---
    if not country_lab:
        women_nat_lab = womens or Nat_Womens.get(country, "")
        if women_nat_lab:
            # ---
            if category_suffix.strip() in ["women", "female", "women's"]:
                country_lab = women_nat_lab
            # ---
            if not country_lab:
                f_lab = short_womens_jobs.get(category_suffix, "")
                # ---
                if not f_lab:
                    f_lab = Women_s_priffix_work(category_suffix)
                # ---
                if f_lab:
                    # logger.debug('<<lightblue>> cate.startswith("%s"), category_suffix:"%s"' % (cate , category_suffix))
                    country_lab = f"{f_lab} {women_nat_lab}"
                    # ---
                    if "{nato}" in f_lab:
                        country_lab = f_lab.format(nato=women_nat_lab)
                        logger.debug('<<lightblue>> TAJO["womens"]: has {nato} "%s"' % f_lab)
                # ---
                for kjn in pkjn:
                    if f_lab.endswith(kjn):
                        country_lab = f"{f_lab[:-len(kjn)]} {women_nat_lab}{kjn}"
                        break
        # ---
        logger.debug(f'\t<<lightblue>> test Womens Jobs: new lab: "{country_lab}" ')
    # ---
    return country_lab
