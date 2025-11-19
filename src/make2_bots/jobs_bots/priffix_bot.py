#!/usr/bin/python3
"""
!
"""
import functools

from ...helps.log import logger
from ...translations import (
    By_table,
    Female_Jobs,
    Mens_priffix,
    Mens_suffix,
    Nat_mens,
    Women_s_priffix,
    change_male_to_female,
    jobs_mens_data,
    jobs_womens_data,
    replace_labels_2022,
    short_womens_jobs,
)
from ..lazy_data_bots.bot_2018 import get_pop_All_18


@functools.lru_cache(maxsize=None)
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
    logger.debug(f'<<lightblue>> --- start: priffix_Mens_work :"{con_33}"')
    label = By_table.get(con_33, "")
    if label:
        return label
    label = jobs_mens_data.get(con_33, "")
    if label:
        logger.debug(f'<<lightblue>> ----- end: priffix_Mens_work :label:"{label}",con_33:"{con_33}"..')
        return label
    for priff, priff_lab in Mens_priffix.items():
        pri = f"{priff} "
        if not con_33.startswith(pri):
            continue
        con_8 = con_33[len(pri) :]
        con_88 = con_8
        if con_8.endswith(" people"):
            con_nat = con_8[: -len(" people")]
            if Nat_mens.get(con_nat):
                con_88 = con_nat
        con_88 = con_88.strip()
        logger.debug(f'<<lightblue>> con_8:{con_8}, con_88:"{con_88}"')
        logger.debug(f'<<lightblue>> con_33.startswith pri ("{pri}"), con_88:"{con_88}"')
        con_8_lab = jobs_mens_data.get(con_88, "")
        if not con_8_lab:
            con_8_lab = Nat_mens.get(con_88, "")
        if con_88 in Female_Jobs and priff_lab in change_male_to_female:
            priff_lab = change_male_to_female[priff_lab]
        if not con_8_lab:
            continue
        logger.debug(f'<<lightblue>> priffix_Mens_work: pri("{pri}"), con_88:{con_88}, con_8_lab:"{con_8_lab}"')
        label = priff_lab.format(con_8_lab)
        if label in replace_labels_2022:
            label = replace_labels_2022[label]
            logger.debug(f'<<lightgreen>> change label to "{label}" replace_labels_2022.')
        if label.strip():
            logger.debug(f'<<lightblue>> ----- end: priffix_Mens_work :label:"{label}",con_33:"{con_33}"..')
            return label
    for suffix, suf_lab in Mens_suffix.items():
        suffix2 = f" {suffix}"
        if not con_33.endswith(suffix2):
            continue
        con_8 = con_33[: -len(suffix2)]
        con_88 = con_8
        if con_8.endswith(" people"):
            con_nat = con_8[: -len(" people")]
            if Nat_mens.get(con_nat):
                con_88 = con_nat
        con_88 = con_88.strip()
        logger.debug(f'<<lightblue>> con_33.endswith suffix2("{suffix2}"), con 88:"{con_88}"')
        con_88_lab = Nat_mens.get(con_88, "")
        if not con_88_lab:
            con_88_lab = get_pop_All_18(con_88) or get_pop_All_18(con_8) or ""
        if con_88_lab:
            logger.debug(f'<<lightblue>> con_33.startswith_suffix2("{suffix2}"), con_88_lab:"{con_88_lab}"')
            label = suf_lab.format(con_88_lab)
        if label.strip():
            logger.debug(f'<<lightblue>> ----- end: priffix_Mens_work :label:"{label}",con_33:"{con_33}"..')
            return label
    return ""


@functools.lru_cache(maxsize=None)
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
    label = short_womens_jobs.get(con_3, "")
    if label:
        return label
    con_33 = con_3
    if con_3.endswith(" women"):
        con_33 = con_3[: -len(" women")]
    for wriff, wrifflab in Women_s_priffix.items():
        data = [f"{wriff} "]
        if wriff == "women's":
            data.append("women's-")
        for prefix in data:
            if not con_33.startswith(prefix):
                continue
            con_4 = con_33[len(prefix) :]
            con_8_Wb = jobs_womens_data.get(con_4, "")
            logger.debug(f'<<lightblue>> con_33.startswith_Wriff2("{prefix}"),con_4:"{con_4}", con_8_Wb:"{con_8_Wb}"')
            if con_8_Wb:
                label = wrifflab.format(con_8_Wb)
                return label
    return ""
