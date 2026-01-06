#!/usr/bin/python3
"""
TODO: planed to be replaced by ArWikiCats.new_resolvers.nationalities_resolvers
"""

import functools
from typing import Tuple

from ...helps import logger
from ...new_resolvers.jobs_resolvers import resolve_jobs_main
from ...translations import (
    all_nat_sorted,
    People_key,
    change_male_to_female,
    jobs_mens_data,
    short_womens_jobs,
)
from ..jobs_bots.get_helps import get_suffix_with_keys
from ..jobs_bots.jobs_mainbot import jobs_with_nat_prefix, jobs_with_nat_prefix_label
from ..jobs_bots.prefix_bot import mens_prefixes_work, womens_prefixes_work
from ..jobs_bots.relegin_jobs_new import new_religions_jobs_with_suffix
from ..languages_bot.langs_w import Lang_work
from ..languages_bot.resolve_languages_new import resolve_languages_labels

# TODO: fix typo to prefix_lab_for_2018
prefix_lab_for_2018: dict[str, dict[str, str]] = {
    "fictional": {"male": "{} خيالي", "female": "{} خيالية"},
    "native": {"male": "{} أصلي", "female": "{} أصلية"},
    "contemporary": {"male": "{} معاصر", "female": "{} معاصرة"},
    "ancient": {"male": "{} قديم", "female": "{} قديمة"},
}

Main_prefix_to: dict[str, str] = {
    "non": "{t} غير {nat}",
}


Main_prefix: dict[str, str] = {
    "assassinatedz": "{} مغتالون",  # TEST
    "assassinated": "{} مغتالون",
    "fictional": "{} خياليون",
    "native": "{} أصليون",
    "murdered": "{} قتلوا",
    "killed": "{} قتلوا",
    "contemporary": "{} معاصرون",
    "ancient": "{} قدماء",
    "cultural depictions of": "تصوير ثقافي عن {}",
    "fictional depictions of": "تصوير خيالي عن {}",
    "depictions of": "تصوير عن {}",
    # "medieval" : "{} من العصور الوسطى",
    "non": "{} غير",
    # "non" : "غير {}",
}

# sorted by len of " " in key
Main_prefix = dict(
    sorted(
        Main_prefix.items(),
        key=lambda k: (-k[0].count(" "), -len(k[0])),
    )
)


def handle_main_prefix(category: str, category_original: str = "") -> Tuple[str, str, str]:
    """
    Handle Main_prefix logic to strip prefixes and determine main label.

    Args:
        category: The current category string (potentially modified).
        category_original: The original category string (used for slicing).

    Returns:
        tuple: (modified_category, main_ss, main_lab)
    """
    main_ss = ""
    main_lab = ""
    if not category_original:
        category_original = category

    for me, melab in Main_prefix.items():
        me2 = f"{me} "
        if category.lower().startswith(me2.lower()):
            main_ss = me
            # Note: This logic seems to assume only one prefix or resets to original slice
            category = category_original[len(me2) :]
            main_lab = melab

            break

    if category.lower().endswith("women") or category.lower().endswith("women's"):
        if main_lab in change_male_to_female:
            main_lab = change_male_to_female[main_lab]

    logger.debug(f'<<lightblue>> te4_2018_Jobs Main_prefix cate.startswith( {me2=}) cate:"{category}", {main_lab=}. ')

    # Fictional Check
    if main_ss.strip() == "fictional" and category.strip().startswith("female"):
        main_lab = "{} خياليات"
        logger.info("{} خياليات")

    return category, main_ss, main_lab


def _get_direct_lookup(category: str) -> str:
    """
    Return a localized Arabic label for the given category when available.

    Returns:
        str: Arabic label for the category, or an empty string if no matching label is found.
    """
    if category == "people":
        return "أشخاص"

    return (
        People_key.get(category, "")
        or short_womens_jobs.get(category, "")
        or resolve_languages_labels(category)
        or Lang_work(category)
        or jobs_mens_data.get(category, "")
    )


@functools.lru_cache(maxsize=None)
def te4_2018_Jobs(cate: str) -> str:
    """
    Determine the localized label for a job- or nationality-related category.

    Parameters:
        cate (str): Category name or phrase (underscores are treated as spaces).

    Returns:
        str: The localized label corresponding to the category, or an empty string if no label can be resolved.

    TODO: use FormatData method
    """
    cate = cate.replace("_", " ")
    logger.debug(f"<<lightyellow>>>> te4_2018_Jobs >> cate:({cate}) ")

    cate_original = cate
    cate_lower_original = cate.lower()

    country_lab = (
        resolve_jobs_main(cate_lower_original)
        or new_religions_jobs_with_suffix(cate_lower_original)
        or jobs_with_nat_prefix_label(cate_lower_original)
        or ""
    )
    if country_lab:
        return country_lab

    # 1. Handle Prefix
    cate, main_ss, main_lab = handle_main_prefix(cate, cate_original)

    if cate.lower() != cate_lower_original:
        logger.debug(f"<<lightblue>> te4_2018_Jobs {cate=}, {cate_lower_original=}, {main_ss=}. ")

    cate_lower = cate.lower()

    # 3. Direct Lookups
    country_lab = _get_direct_lookup(cate_lower)

    category_suffix, country_prefix = get_suffix_with_keys(cate_lower, all_nat_sorted, "nat")

    if not country_lab:
        if category_suffix and not country_lab:
            country_lab = jobs_with_nat_prefix(cate_lower, country_prefix, category_suffix)

        # 5. Fallback Prefixes
        if not country_lab:
            country_lab = womens_prefixes_work(cate_lower) or mens_prefixes_work(cate_lower)

    # 6. Final Formatting
    if main_ss and main_lab and country_lab:
        country_lab = main_lab.format(country_lab)
    if not country_lab:
        country_lab = new_religions_jobs_with_suffix(cate_lower)

    logger.debug(f'end te4_2018_Jobs "{cate}" , {country_lab=}, cate2:{cate_lower_original}')

    return country_lab


__all__ = [
    "te4_2018_Jobs",
    "handle_main_prefix",
]
