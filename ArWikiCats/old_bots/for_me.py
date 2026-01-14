#!/usr/bin/python3
"""
TODO: planed to be replaced by ArWikiCats.new_resolvers.nationalities_resolvers
"""

import functools

from ..helps.jsonl_dump import dump_data

from ..helps import logger
from ..translations import (
    all_nat_sorted,
    Nat_women,
    religious_entries,
    New_female_keys,
)
from ..translations.mixed.bot_te_4_list import (
    en_is_nat_ar_is_women,
)
from ..make_bots.jobs_bots.get_helps import get_suffix_with_keys
from ..make_bots.o_bots.ethnic_bot import ethnic_label_main


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
@dump_data(1)
def _work_for_me_main(normalized_category: str) -> str:
    """
    """
    logger.debug(f"<<lightyellow>>>> Work_for_me_main >> category:({normalized_category})")

    suffix, nationality_key = get_suffix_with_keys(normalized_category, all_nat_sorted, "nat")
    result = ""
    if suffix:
        women_nat_lab = Nat_women.get(nationality_key, "")
        result = _get_female_no_def_label(suffix, women_nat_lab)

    logger.debug(f'<<lightblue>> for_me: Work_for_me_main :: "{result}"')
    return result


@functools.lru_cache(maxsize=None)
def Work_for_me_main(category: str) -> str:
    """
    """
    logger.debug(f"<<lightyellow>>>> Work_for_me_main >> category:({category})")

    normalized_category = category.lower().replace("_", " ").replace("-", " ")

    result = ethnic_label_main(normalized_category) or _work_for_me_main(normalized_category)

    return result
