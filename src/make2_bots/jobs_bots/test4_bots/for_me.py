"""Helpers for deriving job labels that contain nationality information."""

from __future__ import annotations

import re

from ....ma_lists import All_contry_with_nat_ar, Nat_men, Nat_women, New_female_keys, New_male_keys, NN_table, en_is_nat_ar_is_al_mens, en_is_nat_ar_is_al_women, en_is_nat_ar_is_man, en_is_nat_ar_is_P17, en_is_nat_ar_is_women
from ...o_bots import ethnic_bot
from ..utils import cached_lookup, log_debug, normalize_cache_key

MEN_KEYS_CACHE: dict[str, str] = {}
WORK_FOR_ME_CACHE: dict[str, str] = {}

__all__ = ["Work_for_New_2018_men_Keys_with_all", "Work_for_me"]


def Work_for_New_2018_men_Keys_with_all(cate: str, nat: str, con_3: str) -> str:  # noqa: N802
    """Retrieve country label for men based on category, nationality, and key."""

    cache_key = normalize_cache_key(cate, nat, con_3)
    return cached_lookup(
        MEN_KEYS_CACHE,
        (cache_key,),
        lambda: _resolve_men_keys(cate, nat, con_3),
    )


def Work_for_me(cate: str, nat: str, con_3: str) -> str:  # noqa: N802
    """Retrieve a country label based on category, nationality, and context."""

    cache_key = normalize_cache_key(cate, nat, con_3)
    return cached_lookup(
        WORK_FOR_ME_CACHE,
        (cache_key,),
        lambda: _resolve_work_for_me(cate, nat, con_3),
    )


def _resolve_men_keys(cate: str, nat: str, con_3: str) -> str:
    """Compute the label for :func:`Work_for_New_2018_men_Keys_with_all`."""

    men_nat_lab = Nat_men.get(nat, "")
    contry_lab = ""

    template = en_is_nat_ar_is_al_mens.get(con_3.strip(), "")
    if template:
        if nat in NN_table:
            men_nat_lab = NN_table[nat]["men"]
        men_nat_lab = add_all(men_nat_lab)
        contry_lab = template.format(men_nat_lab)
        log_debug(
            '<<lightblue>> test_4:en_is_nat_ar_is_al_mens new contry_lab  "%s" ',
            contry_lab,
        )

    return contry_lab


def _resolve_work_for_me(cate: str, nat: str, con_3: str) -> str:
    """Compute the heavy lifting for :func:`Work_for_me`."""

    women_nat_lab = Nat_women.get(nat, "")
    men_nat_lab = Nat_men.get(nat, "")
    nat_lab = Nat_women.get(nat, "")

    log_debug(
        '<<lightblue>>>> Work_for_me >> %s .nat:(%s), con_3:"%s", nat_lab:"%s"',
        cate,
        nat,
        con_3,
        nat_lab,
    )
    contry_lab = ""
    con_3_lab = ""

    # الإنجليزي جنسية والعربي اسم البلد
    if not con_3_lab and not contry_lab:
        con_3_lab = en_is_nat_ar_is_P17.get(con_3.strip(), "")
        cco_lab = All_contry_with_nat_ar.get(nat.strip(), {}).get("ar", "")
        if con_3_lab and cco_lab:
            contry_lab = con_3_lab.format(cco_lab)
            log_debug(
                '<<lightblue>> test_4:en_is_nat_ar_is_women new contry_lab   "%s" ',
                contry_lab,
            )

    # نسائية بدون ألف ولام التعريف
    if not con_3_lab and not contry_lab:
        contry_lab = ethnic_bot.Ethnic(cate, nat, con_3)

    if not contry_lab:
        con_3_lab = en_is_nat_ar_is_women.get(con_3.strip(), "")
        if not con_3_lab:
            con_3_lab = New_female_keys.get(con_3.strip(), "")
            if con_3_lab:
                con_3_lab += " {}"
        if con_3_lab:
            contry_lab = con_3_lab.format(women_nat_lab)
            log_debug(
                '<<lightblue>> test44:en_is_nat_ar_is_women new contry_lab   "%s" ',
                contry_lab,
            )

    if not contry_lab:
        con_3_lab = en_is_nat_ar_is_al_women.get(con_3.strip(), "")
        if con_3_lab:
            women_label = add_all(NN_table.get(nat, {}).get("women", women_nat_lab) or women_nat_lab)
            if "{nat}" in con_3_lab:
                contry_lab = con_3_lab.format(nat=women_label)
            else:
                contry_lab = con_3_lab.format(women_label)
            log_debug(
                '<<lightblue>> test_4:en_is_nat_ar_is_al_women new contry_lab  "%s" ',
                contry_lab,
            )

    if not contry_lab:
        con_3_lab = en_is_nat_ar_is_man.get(con_3.strip(), "")
        if not con_3_lab:
            con_3_lab = New_male_keys.get(con_3.strip(), "")
            if con_3_lab:
                con_3_lab += " {}"
        if con_3_lab:
            contry_lab = con_3_lab.format(men_nat_lab)
            log_debug(
                '<<lightblue>> test_4:en_is_nat_ar_is_man new contry_lab    "%s" ',
                contry_lab,
            )

    if not contry_lab:
        contry_lab = Work_for_New_2018_men_Keys_with_all(cate, nat, con_3)

    return contry_lab


def add_all(lab: str) -> str:
    """Prefix a label with the Arabic definite article."""

    lab_no_al = re.sub(r" ", " ال", lab)
    return f"ال{lab_no_al}"
