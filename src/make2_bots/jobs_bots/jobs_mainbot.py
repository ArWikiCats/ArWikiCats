#!/usr/bin/python3
"""

from ..jobs_bots.jobs_mainbot import Jobs#, Jobs2

"""
from typing import Dict, Optional

from ...ma_lists import (
    Nat_mens,
    Nat_Womens,
    jobs_mens_data,
    short_womens_jobs,
    NAT_BEFORE_OCC,
    MEN_WOMENS_WITH_NATO,
)
from ...helps.print_bot import output_test4
from ..jobs_bots.priffix_bot import Women_s_priffix_work, priffix_Mens_work

Jobs_cash: Dict[str, str] = {}


def Jobs2(cate: str, Start: str, con_3: str) -> str:
    # ---
    country: str = Start
    country_lab: str = ""
    # ---
    con_3_lab = jobs_mens_data.get(con_3, "")
    if con_3_lab:
        if Nat_mens.get(country, "") != "":
            # output_test4('<<lightblue>> cate.startswith("%s"), con_3:"%s"' % (cate , con_3))
            country_lab = f"{con_3_lab} {Nat_mens.get(country, '')}"
            output_test4(f'<<lightblue>> test Jobs: new country_lab  "{country_lab}" ')
    # ---
    return country_lab


def Jobs(cate: str, Start: str, con_3: str, Type: str = "", tab: Optional[Dict[str, str]] = None) -> str:
    """Retrieve job labels based on category and country.

    This function generates job labels for both men and women based on the
    provided category, starting country, and additional context. It checks
    cached results to improve performance and utilizes various mappings to
    determine the appropriate labels. The function handles different cases
    for men's and women's jobs, including specific prefixes and country-
    specific labels.

    Args:
        cate (str): The category of the job.
        Start (str): The starting country for the job label.
        con_3 (str): Additional context for the job label.
        Type (str?): An optional type parameter. Defaults to an empty string.
        tab (dict?): A dictionary containing additional labels for men and women.
            Defaults to None.

    Returns:
        str: The generated job label based on the input parameters.
    """

    # ---
    if not tab:
        tab = {}
    # ---
    cash_key = f"{cate}, {Start}, {Type}, {con_3}".lower().strip()
    # ---
    if cash_key in Jobs_cash:
        return Jobs_cash[cash_key]
    # ---
    output_test4(f'<<lightblue>> test_4.py Jobs: cate: "{cate}", Start: "{Start}", con_3: "{con_3}" ')
    country = Start
    country_lab = ""
    # ---
    con_3_lab = jobs_mens_data.get(con_3, "")
    # ---
    con_4 = con_3
    if con_3.startswith("people "):
        con_4 = con_3[len("people ") :]
    # ---
    pkjn = [" مغتربون", " مغتربات"]
    # ---
    # mens Jobs
    mens_nat_lab = tab.get("mens") or Nat_mens.get(country, "")
    # ---
    if mens_nat_lab:
        # ---
        if con_3.strip() == "people":
            country_lab = mens_nat_lab
        # ---
        if not country_lab:
            con_3_lab = priffix_Mens_work(con_3)
        # ---
        if con_3_lab:
            # ---
            country_lab = f"{con_3_lab} {mens_nat_lab}"
            if con_3_lab.startswith("حسب"):
                country_lab = f"{mens_nat_lab} {con_3_lab}"

            # ---
            if con_3.strip() in NAT_BEFORE_OCC or con_4.strip() in NAT_BEFORE_OCC:
                country_lab = f"{mens_nat_lab} {con_3_lab}"
            # ---
            TAJO = MEN_WOMENS_WITH_NATO.get(con_3, {})
            if TAJO and "{nato}" in TAJO.get("mens", ""):
                country_lab = TAJO["mens"].format(nato=mens_nat_lab)
                output_test4('<<lightblue>> TAJO["mens"]: has {nato} "%s"' % TAJO["mens"])
            # ---
            for kjn in pkjn:
                if con_3_lab.endswith(kjn):
                    country_lab = f"{con_3_lab[:-len(kjn)]} {mens_nat_lab}{kjn}"
                    break
            # ---
            output_test4(f'\t<<lightblue>> con_3: "{con_3}" ')
            output_test4(f'\t<<lightblue>> test mens Jobs: new lab: "{country_lab}" ')
    # ---#
    # Womens Jobs
    # ---
    if not country_lab:
        women_nat_lab = tab.get("womens") or Nat_Womens.get(country, "")
        if women_nat_lab:
            # ---
            if con_3.strip() in ["women", "female", "women's"]:
                country_lab = women_nat_lab
            # ---
            if not country_lab:
                f_lab = short_womens_jobs.get(con_3, "")
                # ---
                if not f_lab:
                    f_lab = Women_s_priffix_work(con_3)
                # ---
                if f_lab:
                    # output_test4('<<lightblue>> cate.startswith("%s"), con_3:"%s"' % (cate , con_3))
                    country_lab = f"{f_lab} {women_nat_lab}"
                    # ---
                    if "{nato}" in f_lab:
                        country_lab = f_lab.format(nato=women_nat_lab)
                        output_test4('<<lightblue>> TAJO["womens"]: has {nato} "%s"' % f_lab)
                # ---
                for kjn in pkjn:
                    if f_lab.endswith(kjn):
                        country_lab = f"{f_lab[:-len(kjn)]} {women_nat_lab}{kjn}"
                        break
        # ---
        output_test4(f'\t<<lightblue>> test Womens Jobs: new lab: "{country_lab}" ')
    # ---
    Jobs_cash[cash_key] = country_lab
    # ---
    return country_lab
