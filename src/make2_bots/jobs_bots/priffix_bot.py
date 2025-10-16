#!/usr/bin/python3
"""
from ..make2_bots.jobs_bots.priffix_bot import Women_s_priffix_work, priffix_Mens_work
"""
from typing import Dict
from ..ma_lists import Nat_mens
from ..ma_lists import (
    Jobs_key_mens,
    Jobs_key_womens,
    womens_Jobs_2017,
    Female_Jobs,
)
from ..ma_lists import By_table
from ..ma_lists import replace_labels_2022, change_male_to_female, Mens_suffix, Mens_priffix, Women_s_priffix

from ..make2_bots.matables_bots.bot_2018 import pop_All_2018
from ..helps.print_bot import output_test4

priffix_Mens_work_cash: Dict[str, str] = {}
priffix_woMens_work_cash: Dict[str, str] = {}


def priffix_Mens_work(con_33: str) -> str:
    """Process and retrieve the appropriate label for a given input string.

    This function takes an input string, processes it to determine if it
    matches any predefined prefixes or suffixes associated with male job
    categories. It first normalizes the input by converting it to lowercase
    and stripping whitespace. The function checks various dictionaries to
    find a corresponding label based on the input. If a match is found, it
    formats the label accordingly and caches the result for future use. The
    function also handles specific cases where the input may end with
    "people" and adjusts the label based on additional mappings.

    Args:
        con_33 (str): The input string representing a job title or category.

    Returns:
        str: The formatted label corresponding to the input string.
    """

    # ---
    cash_key = con_33.lower().strip()
    # ---
    if cash_key in priffix_Mens_work_cash:
        return priffix_Mens_work_cash[cash_key]
    # ---
    output_test4(f'<<lightblue>> --- start: priffix_Mens_work :"{con_33}"')
    con_33_lab = ""
    # ---
    if not con_33_lab:
        con_33_lab = By_table.get(con_33, "")
        if con_33_lab:
            priffix_Mens_work_cash[cash_key] = con_33_lab
            # ---
            return con_33_lab
    # ---
    if not con_33_lab:
        con_33_lab = Jobs_key_mens.get(con_33, "")
        if con_33_lab:
            output_test4(f'<<lightblue>> Jobs_key_mens: con_33_lab:"{con_33_lab}"')
    # ---
    for priff, priff_lab in Mens_priffix.items():
        if con_33_lab:
            break
        # ---
        pri = f"{priff} "

        if not con_33.startswith(pri):
            continue
        # ---
        con_8 = con_33[len(pri) :]
        con_88 = con_8
        # ---
        if con_8.endswith(" people"):
            con_nat = con_8[: -len(" people")]
            if Nat_mens.get(con_nat):
                con_88 = con_nat
        con_88 = con_88.strip()
        # ---
        output_test4(f'<<lightblue>> con_8:{con_8}, con_88:"{con_88}"')
        # ---
        output_test4(f'<<lightblue>> con_33.startswith pri ("{pri}"), con_88:"{con_88}"')
        # ---
        con_8_lab = Jobs_key_mens.get(con_88, "")
        if not con_8_lab:
            con_8_lab = Nat_mens.get(con_88, "")
        # ---
        if con_88 in Female_Jobs and priff_lab in change_male_to_female:
            priff_lab = change_male_to_female[priff_lab]
        # ---
        if con_8_lab:
            output_test4(f'<<lightblue>> priffix_Mens_work: pri("{pri}"), con_88:{con_88}, con_8_lab:"{con_8_lab}"')
            con_33_lab = priff_lab.format(con_8_lab)
            # ---
            if con_33_lab in replace_labels_2022:
                con_33_lab = replace_labels_2022[con_33_lab]
                output_test4(f'<<lightgreen>> change con_33_lab to "{con_33_lab}" replace_labels_2022.')
            # ---
            output_test4(f'<<lightblue>> con_33_lab: "{con_33_lab}"')
    # ---
    for suffix, suf_lab in Mens_suffix.items():
        if con_33_lab:
            break
        # ---
        suffix2 = f" {suffix}"
        if not con_33.endswith(suffix2):
            continue
        # ---
        con_8 = con_33[: -len(suffix2)]
        con_88 = con_8
        # ---
        if con_8.endswith(" people"):
            con_nat = con_8[: -len(" people")]
            if Nat_mens.get(con_nat):
                con_88 = con_nat
        con_88 = con_88.strip()
        # ---
        output_test4(f'<<lightblue>> con_33.endswith suffix2("{suffix2}"), con 88:"{con_88}"')
        # ---
        con_88_lab = Nat_mens.get(con_88, "")
        # ---
        if not con_88_lab:
            con_88_lab = pop_All_2018.get(con_88) or pop_All_2018.get(con_8) or ""
        # ---
        if con_88_lab:
            output_test4(f'<<lightblue>> con_33.startswith_suffix2("{suffix2}"), con_88_lab:"{con_88_lab}"')
            con_33_lab = suf_lab.format(con_88_lab)
            # ---
            output_test4(f'<<lightblue>> con_33_lab "{con_33_lab}"')
    # ---
    output_test4(f'<<lightblue>> ----- end: priffix_Mens_work :con_33_lab:"{con_33_lab}",con_33:"{con_33}"..')
    # ---
    priffix_Mens_work_cash[cash_key] = con_33_lab
    # ---
    return con_33_lab


def Women_s_priffix_work(con_3: str) -> str:
    """Retrieve the women's prefix work label based on the input string.

    This function processes the input string to determine if it matches any
    predefined women's job prefixes. It first checks if the lowercase and
    stripped version of the input exists in a cache. If not found, it
    attempts to derive the job label from a mapping of women's jobs. The
    function also handles specific cases where the input string ends with "
    women" and checks against various prefixes to find a match. The result
    is cached for future reference.

    Args:
        con_3 (str): The input string representing a job or title related to women.

    Returns:
        str: The corresponding job label or an empty string if no match is found.
    """

    # ---
    cash_key = con_3.lower().strip()
    # ---
    if cash_key in priffix_woMens_work_cash:
        return priffix_woMens_work_cash[cash_key]
    # ---
    f_lab = ""
    # ---
    if not f_lab:
        f_lab = Jobs_key_womens.get(con_3, "")
    # ---
    con_33 = con_3
    if con_3.endswith(" women"):
        con_33 = con_3[: -len(" women")]
    # ---
    for wriff, wrifflab in Women_s_priffix.items():
        if f_lab:
            break
        Wriff2 = f"{wriff} "
        if wriff == "women's":
            Wriff2 = "women's-"
        if con_33.startswith(Wriff2):
            con_4 = con_33[len(Wriff2) :]
            con_8_Wb = womens_Jobs_2017.get(con_4, "")
            output_test4(f'<<lightblue>> con_33.startswith_Wriff2("{Wriff2}"),con_4:"{con_4}", con_8_Wb:"{con_8_Wb}"')
            if con_8_Wb:
                f_lab = wrifflab.format(con_8_Wb)
    # ---
    priffix_woMens_work_cash[cash_key] = f_lab
    # ---
    return f_lab
