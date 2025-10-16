#!/usr/bin/python3
"""

from ..jobs_bots.jobs_mainbot import Jobs#, Jobs2

"""
from typing import Dict, Optional, Any
from ..ma_lists_bots import Nat_mens, Nat_Womens

from ..ma_lists_bots import (
    Jobs_key_mens,
    Jobs_key_womens,
    Nat_Before_Occ,
    Men_Womens_with_nato,
)
from ..helps.print_bot import output_test4
from ..jobs_bots.priffix_bot import Women_s_priffix_work, priffix_Mens_work

Jobs_cash: Dict[str, str] = {}


def Jobs2(cate: str, Start: str, con_3: str) -> str:
    # ---
    contry: str = Start
    contry_lab: str = ""
    # ---
    con_3_lab = Jobs_key_mens.get(con_3, "")
    if con_3_lab:
        if Nat_mens.get(contry, "") != "":
            # output_test4('<<lightblue>> cate.startswith("%s"), con_3:"%s"' % (cate , con_3))
            contry_lab = f"{con_3_lab} {Nat_mens.get(contry, '')}"
            output_test4(f'<<lightblue>> test Jobs: new contry_lab  "{contry_lab}" ')
    # ---
    return contry_lab


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
    contry = Start
    contry_lab = ""
    # ---
    con_3_lab = Jobs_key_mens.get(con_3, "")
    # ---
    con_4 = con_3
    if con_3.startswith("people "):
        con_4 = con_3[len("people ") :]
    # ---
    pkjn = [" مغتربون", " مغتربات"]
    # ---
    # mens Jobs
    mens_nat_lab = tab.get("mens") or Nat_mens.get(contry, "")
    # ---
    if mens_nat_lab:
        # ---
        if con_3.strip() == "people":
            contry_lab = mens_nat_lab
        # ---
        if not contry_lab:
            con_3_lab = priffix_Mens_work(con_3)
        # ---
        if con_3_lab:
            # ---
            contry_lab = f"{con_3_lab} {mens_nat_lab}"
            if con_3_lab.startswith("حسب"):
                contry_lab = f"{mens_nat_lab} {con_3_lab}"

            # ---
            if con_3.strip() in Nat_Before_Occ or con_4.strip() in Nat_Before_Occ:
                contry_lab = f"{mens_nat_lab} {con_3_lab}"
            # ---
            TAJO = Men_Womens_with_nato.get(con_3, {})
            if TAJO and TAJO.get("mens", "").find("{nato}") != -1:
                contry_lab = TAJO["mens"].format(nato=mens_nat_lab)
                output_test4('<<lightblue>> TAJO["mens"]: has {nato} "%s"' % TAJO["mens"])
            # ---
            for kjn in pkjn:
                if con_3_lab.endswith(kjn):
                    contry_lab = f"{con_3_lab[:-len(kjn)]} {mens_nat_lab}{kjn}"
                    break
            # ---
            output_test4(f'\t<<lightblue>> con_3: "{con_3}" ')
            output_test4(f'\t<<lightblue>> test mens Jobs: new lab: "{contry_lab}" ')
    # ---#
    # Womens Jobs
    # ---
    if not contry_lab:
        women_nat_lab = tab.get("womens") or Nat_Womens.get(contry, "")
        if women_nat_lab:
            # ---
            if con_3.strip() in ["women", "female", "women's"]:
                contry_lab = women_nat_lab
            # ---
            if not contry_lab:
                f_lab = Jobs_key_womens.get(con_3, "")
                # ---
                if not f_lab:
                    f_lab = Women_s_priffix_work(con_3)
                # ---
                if f_lab:
                    # output_test4('<<lightblue>> cate.startswith("%s"), con_3:"%s"' % (cate , con_3))
                    contry_lab = f"{f_lab} {women_nat_lab}"
                    # ---
                    if "{nato}" in f_lab:
                        contry_lab = f_lab.format(nato=women_nat_lab)
                        output_test4('<<lightblue>> TAJO["womens"]: has {nato} "%s"' % f_lab)
                # ---
                for kjn in pkjn:
                    if f_lab.endswith(kjn):
                        contry_lab = f"{f_lab[:-len(kjn)]} {women_nat_lab}{kjn}"
                        break
        # ---
        output_test4(f'\t<<lightblue>> test Womens Jobs: new lab: "{contry_lab}" ')
    # ---
    Jobs_cash[cash_key] = contry_lab
    # ---
    return contry_lab
