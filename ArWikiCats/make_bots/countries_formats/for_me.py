#!/usr/bin/python3
"""
TODO: planed to be replaced by ArWikiCats.new_resolvers.nationalities_resolvers
"""

import functools
import re

from ...helps import logger
from ...translations import (
    Nat_men,
    All_Nat,
    Nat_the_female,
    Nat_the_male,
    Nat_women,
    New_female_keys,
    all_country_with_nat_ar,
    en_is_nat_ar_is_al_mens,
    en_is_nat_ar_is_al_women,
    en_is_nat_ar_is_P17,
    en_is_nat_ar_is_women,
)
from ...make_bots.jobs_bots.get_helps import get_suffix_with_keys
from ..o_bots import ethnic_bot


@functools.lru_cache(maxsize=None)
def Work_for_New_2018_men_Keys_with_all(cate: str, nat: str, suffix: str) -> str:
    """Retrieve country label for men based on category, nationality, and a
    specific key.

    This function attempts to derive a country label based on the
    nationality and the provided key. The function utilizes various mappings
    to format the country label appropriately.

    Args:
        cate (str): The category of the work.
        nat (str): The nationality to be used for label generation.
        suffix (str): A specific key used to retrieve additional information.

    Returns:
        str: The formatted country label for men based on the inputs.
    """

    men_nat_lab = Nat_the_male.get(nat, "")

    if not men_nat_lab:
        return ""

    # رجالية بألف ولام التعريف
    suffix_label = en_is_nat_ar_is_al_mens.get(suffix.strip(), "")

    if not suffix_label:
        return ""

    country_lab = suffix_label.format(men_nat_lab)
    logger.info(f"Work_for_New_2018_men_Keys_with_all: {suffix=}, {suffix_label=} ")
    logger.info(f"Work_for_New_2018_men_Keys_with_all: {nat=}, {men_nat_lab=}, {country_lab=} ")

    return country_lab


def _get_p17_label(nat: str, suffix: str) -> str | None:
    """Attempt to get label from P17 mappings."""
    con_3_lab = en_is_nat_ar_is_P17.get(suffix.strip(), "")
    if not con_3_lab:
        return None

    cco_lab = ""
    if nat.strip() in all_country_with_nat_ar:
        cco_lab = all_country_with_nat_ar[nat.strip()].get("ar", "")

    if cco_lab:
        logger.debug(f"<<lightblue>> Work_for_me: {con_3_lab=} ")
        country_lab = con_3_lab.format(cco_lab)
        logger.debug(f"<<lightblue>> bot_te_4:all_country_with_nat_ar new {country_lab=} ")
        return country_lab

    return ""


def _get_female_no_def_label(suffix: str, women_nat_lab: str) -> str | None:
    """Attempt to get female label without definite article."""
    con_3_lab = en_is_nat_ar_is_women.get(suffix.strip(), "")
    if not con_3_lab:
        con_3_lab = New_female_keys.get(suffix.strip(), "")
        if con_3_lab:
            con_3_lab += " {}"

    if not con_3_lab:
        return None

    country_lab = con_3_lab.format(women_nat_lab)
    logger.debug(f"<<lightblue>> test44:en_is_nat_ar_is_women new {country_lab=} ")
    return country_lab


def _get_female_def_label(suffix: str, the_female_nat_lab: str) -> str | None:
    """
    Return a female country label that includes the definite article for the given suffix and female nationality label.

    Parameters:
        suffix (str): Suffix key used to look up a definite-article template.
        the_female_nat_lab (str): Female nationality label to insert into the template.

    Returns:
        str | None: Formatted country label when a template is found for the suffix, `None` if no template exists.
    """
    con_3_lab = en_is_nat_ar_is_al_women.get(suffix.strip(), "")
    if not con_3_lab:
        return None

    if "{nat}" in con_3_lab:
        country_lab = con_3_lab.format(nat=the_female_nat_lab)
    else:
        country_lab = con_3_lab.format(the_female_nat_lab)
    logger.debug(f"<<lightblue>> bot_te_4:en_is_nat_ar_is_al_women new {country_lab=} ")
    return country_lab


@functools.lru_cache(maxsize=None)
def Work_for_me(cate: str, nat: str, suffix: str) -> str:
    """
    Resolve a localized country label for a given category, nationality key, and suffix.

    Parameters:
        cate (str): Category name used to select an appropriate label variant.
        nat (str): Nationality key looked up in nationality mapping dictionaries.
        suffix (str): Suffix key that determines the label variant to use.

    Returns:
        str: The resolved country label (may be an Arabic or mixed label). Returns an empty string when no suitable mapping is found.
    """
    women_nat_lab = Nat_women.get(nat, "")
    the_female_nat_lab = Nat_the_female.get(nat, "")
    men_nat_lab = Nat_men.get(nat, "")

    logger.debug(f"<<lightblue>>>> Work_for_me >> {cate} .nat:({nat}), {suffix=}, nat_lab={women_nat_lab}")

    # 1. الإنجليزي جنسية والعربي اسم البلد
    res = _get_p17_label(nat, suffix)
    if res is not None:
        return res

    # 2. نسائية بدون ألف ولام التعريف (Ethnic)
    res = ethnic_bot.ethnic_label(cate, nat, suffix)
    if res:
        return res

    # 3. نسائية بدون ألف ولام التعريف
    res = _get_female_no_def_label(suffix, women_nat_lab)
    if res is not None:
        return res

    # 4. نسائية بألف ولام التعريف
    res = _get_female_def_label(suffix, the_female_nat_lab)
    if res is not None:
        return res

    # 5. رجالية بدون ألف ولام التعريف
    # res = _get_male_no_def_label(suffix, men_nat_lab) if res is not None: return res

    # 6. رجالية بألف ولام التعريف (Fallback)
    return Work_for_New_2018_men_Keys_with_all(cate, nat, suffix)


@functools.lru_cache(maxsize=None)
def Work_for_me_main(category: str) -> str:
    """
    Normalize an input category and resolve the corresponding country label using a derived suffix and nationality key.

    Parameters:
        category (str): Category name (e.g., a Wikipedia category) used to derive a suffix and nationality key.

    Returns:
        str: The resolved country label, or an empty string if no label could be determined.
    """
    logger.debug(f"<<lightyellow>>>> Work_for_me_main >> category:({category})")

    normalized_category = category.lower().replace("_", " ").replace("-", " ")
    result = ""
    suffix, nationality_key = get_suffix_with_keys(normalized_category, All_Nat, "nat")

    if suffix:
        result = Work_for_me(normalized_category, nationality_key, suffix)

    logger.debug(f'<<lightblue>> bot_te_4: Work_for_me_main :: "{result}"')
    return result
