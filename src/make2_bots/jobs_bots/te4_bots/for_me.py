#!/usr/bin/python3
"""
!
"""

import functools
import re

from ....helps.log import logger
from ....translations import (
    Nat_men,
    Nat_women,
    New_female_keys,
    New_male_keys,
    NN_table2 as NN_table,
    all_country_with_nat_ar,
    en_is_nat_ar_is_al_mens,
    en_is_nat_ar_is_al_women,
    en_is_nat_ar_is_man,
    en_is_nat_ar_is_P17,
    en_is_nat_ar_is_women,
)
from ...o_bots import ethnic_bot


def add_all(lab: str) -> str:
    """Insert the definite article into every word of the given label."""
    lab_no_al = re.sub(r" ", " ال", lab)
    new_lab = f"ال{lab_no_al}"
    return new_lab


@functools.lru_cache(maxsize=None)
def Work_for_New_2018_men_Keys_with_all(cate: str, nat: str, con_3: str) -> str:
    """Retrieve country label for men based on category, nationality, and a
    specific key.

    This function constructs a cash key from the provided category,
    nationality, and a third parameter. It checks if this key exists in the
    `wo_2018_cash` dictionary. If it does, it returns the corresponding
    value. If not, it attempts to derive a country label based on the
    nationality and the provided key. The function utilizes various mappings
    to format the country label appropriately.

    Args:
        cate (str): The category of the work.
        nat (str): The nationality to be used for label generation.
        con_3 (str): A specific key used to retrieve additional information.

    Returns:
        str: The formatted country label for men based on the inputs.
    """

    men_nat_lab = Nat_men.get(nat, "")
    country_lab = ""
    con_3_lab = ""

    # رجالية بألف ولام التعريف
    if not con_3_lab and not country_lab:
        con_3_lab = en_is_nat_ar_is_al_mens.get(con_3.strip(), "")
        if con_3_lab:
            if nat in NN_table:
                men_nat_lab = NN_table[nat]["men"]
            men_nat_lab_no_al = re.sub(r" ", " ال", men_nat_lab)
            men_nat_lab = f"ال{men_nat_lab_no_al}"
            country_lab = con_3_lab.format(men_nat_lab)
            logger.debug(f'<<lightblue>> bot_te_4:en_is_nat_ar_is_al_mens new country_lab  "{country_lab}" ')

    return country_lab


@functools.lru_cache(maxsize=None)
def Work_for_me(cate: str, nat: str, con_3: str) -> str:
    """Retrieve a country label based on category, nationality, and a third
    parameter.
    """
    women_nat_lab = Nat_women.get(nat, "")
    men_nat_lab = Nat_men.get(nat, "")
    nat_lab = Nat_women[nat]
    logger.debug(f'<<lightblue>>>> Work_for_me >> {cate} .nat:({nat}), con_3:"{con_3}", nat_lab:"{nat_lab}"')
    country_lab = ""
    con_3_lab = ""
    cco_lab = ""

    # الإنجليزي جنسية والعربي اسم البلد
    if not con_3_lab and not country_lab:
        con_3_lab = en_is_nat_ar_is_P17.get(con_3.strip(), "")
        if nat.strip() in all_country_with_nat_ar:
            cco_lab = all_country_with_nat_ar[nat.strip()].get("ar", "")
        if con_3_lab:
            logger.debug(f'<<lightblue>> Work_for_me:con_3_lab: "{con_3_lab}" ')
            if cco_lab:
                country_lab = con_3_lab.format(cco_lab)
                logger.debug(f'<<lightblue>> bot_te_4:en_is_nat_ar_is_women new country_lab   "{country_lab}" ')

    # نسائية بدون ألف ولام التعريف
    if con_3_lab == "" and country_lab == "":
        country_lab = ethnic_bot.ethnic(cate, nat, con_3)

    # نسائية بدون ألف ولام التعريف
    if con_3_lab == "" and country_lab == "":
        con_3_lab = en_is_nat_ar_is_women.get(con_3.strip(), "")
        if not con_3_lab:
            con_3_lab = New_female_keys.get(con_3.strip(), "")
            if con_3_lab:
                con_3_lab += " {}"
        if con_3_lab:
            country_lab = con_3_lab.format(women_nat_lab)
            logger.debug(f'<<lightblue>> test44:en_is_nat_ar_is_women new country_lab   "{country_lab}" ')

    # نسائية بألف ولام التعريف
    if con_3_lab == "" and country_lab == "":
        con_3_lab = en_is_nat_ar_is_al_women.get(con_3.strip(), "")
        if con_3_lab:
            if nat in NN_table:
                women_nat_lab = NN_table[nat]["women"]
            women_nat_lab = add_all(women_nat_lab)
            if "{nat}" in con_3_lab:
                country_lab = con_3_lab.format(nat=women_nat_lab)
            else:
                country_lab = con_3_lab.format(women_nat_lab)
            logger.debug(f'<<lightblue>> bot_te_4:en_is_nat_ar_is_al_women new country_lab  "{country_lab}" ')

    # رجالية بدون ألف ولام التعريف
    if con_3_lab == "" and country_lab == "":
        con_3_lab = en_is_nat_ar_is_man.get(con_3.strip(), "")
        if not con_3_lab:
            con_3_lab = New_male_keys.get(con_3.strip(), "")
            if con_3_lab:
                con_3_lab += " {}"
        if con_3_lab:
            country_lab = con_3_lab.format(men_nat_lab)
            logger.debug(f'<<lightblue>> bot_te_4:en_is_nat_ar_is_man new country_lab    "{country_lab}" ')

    # رجالية بألف ولام التعريف
    if con_3_lab == "" and country_lab == "":
        country_lab = Work_for_New_2018_men_Keys_with_all(cate, nat, con_3)

    return country_lab
