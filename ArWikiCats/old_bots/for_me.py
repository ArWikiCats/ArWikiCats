#!/usr/bin/python3
"""
TODO: planed to be replaced by ArWikiCats.new_resolvers.nationalities_resolvers
"""

import functools

from ..helps import logger
from ..translations import (
    all_nat_sorted,
    Nat_the_female,
    Nat_women,
    religious_entries,
    New_female_keys,
)
from ..translations.mixed.bot_te_4_list import (
    en_is_nat_ar_is_women,
)
from ..make_bots.jobs_bots.get_helps import get_suffix_with_keys
from ..make_bots.o_bots import ethnic_bot


def _get_female_no_def_label(suffix: str, women_nat_lab: str) -> str | None:
    """Attempt to get female label without definite article."""
    con_3_lab = en_is_nat_ar_is_women.get(suffix.strip(), "")
    if not con_3_lab:
        con_3_lab = New_female_keys.get(suffix.strip(), "") or religious_entries.get(suffix.strip(), "")
        if con_3_lab:
            con_3_lab += " {}"

    if not con_3_lab:
        return None

    country_lab = con_3_lab.format(women_nat_lab)
    logger.debug(f"<<lightblue>> test44:en_is_nat_ar_is_women new {country_lab=} ")
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

    logger.debug(f"<<lightblue>>>> Work_for_me >> {cate} .nat:({nat}), {suffix=}, nat_lab={women_nat_lab}")

    # 2. نسائية بدون ألف ولام التعريف (Ethnic)
    res = ethnic_bot.ethnic_label(cate, nat, suffix)
    if res:
        return res

    # 3. نسائية بدون ألف ولام التعريف
    res = _get_female_no_def_label(suffix, women_nat_lab)
    if res is not None:
        return res

    return ""


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
    suffix, nationality_key = get_suffix_with_keys(normalized_category, all_nat_sorted, "nat")

    if suffix:
        result = Work_for_me(normalized_category, nationality_key, suffix)

    logger.debug(f'<<lightblue>> for_me: Work_for_me_main :: "{result}"')
    return result
