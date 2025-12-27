#!/usr/bin/python3
"""
TODO: planed to be replaced by translations_resolvers_v2
"""

import functools
from typing import Tuple

from ...helps.log import logger
from ...translations import (
    All_Nat,
    Nat_men,
    Nat_women,
    People_key,
    change_male_to_female,
    en_is_nat_ar_is_man,
    en_is_nat_ar_is_women,
    jobs_mens_data,
    short_womens_jobs,
)
from ..jobs_bots.get_helps import get_suffix_with_keys
from ..jobs_bots.jobs_mainbot import jobs_with_nat_prefix, jobs_with_nat_prefix_label
from ..jobs_bots.prefix_bot import womens_prefixes_work, mens_prefixes_work
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
Main_prefix = dict(sorted(
    Main_prefix.items(),
    key=lambda k: (-k[0].count(" "), -len(k[0])),
))


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

    logger.debug(
        f'<<lightblue>> te4_2018_Jobs Main_prefix cate.startswith( {me2=}) cate:"{category}", {main_lab=}. '
    )

    # Fictional Check
    if main_ss.strip() == "fictional" and category.strip().startswith("female"):
        main_lab = "{} خياليات"
        logger.info("{} خياليات")

    return category, main_ss, main_lab


def _get_direct_lookup(category: str) -> str:
    """Try direct dictionary lookups for the category."""
    if category == "people":
        return "أشخاص"

    return (
        People_key.get(category, "")
        or short_womens_jobs.get(category, "")
        or resolve_languages_labels(category)
        or Lang_work(category)
        or jobs_mens_data.get(category, "")
    )


def _handle_nationality_logic(
    category: str,
    main_ss: str,
    category_suffix: str,
    country_prefix: str,
) -> Tuple[str, str, str]:
    """
    Handle nationality extraction and related job label logic.

    Returns:
        tuple: (country_lab, country_prefix, category_suffix, job_example_lab, updated_main_lab)
    """
    job_example_lab = ""
    updated_main_lab = ""
    country_lab = ""

    category_suffix, country_prefix = get_suffix_with_keys(category, All_Nat, "nat")

    if category_suffix and (main_ss in prefix_lab_for_2018) and not country_lab:

        # en_is_nat_ar_is_women
        job_example_lab = en_is_nat_ar_is_women.get(category_suffix.strip(), "")
        if job_example_lab:
            country_lab = job_example_lab.format(Nat_women[country_prefix])
            logger.debug(f'<<lightblue>> bot_te_4, new {country_lab=} ')
            updated_main_lab = prefix_lab_for_2018[main_ss]["female"]

        # en_is_nat_ar_is_man
        if not country_lab:
            job_example_lab = en_is_nat_ar_is_man.get(category_suffix.strip(), "")
            if job_example_lab:
                country_lab = job_example_lab.format(Nat_men[country_prefix])
                logger.debug(f'<<lightblue>> bot_te_4, new {country_lab=} ')
                updated_main_lab = prefix_lab_for_2018[main_ss]["male"]

    return country_lab, job_example_lab, updated_main_lab


@functools.lru_cache(maxsize=None)
def te4_2018_Jobs(cate: str) -> str:
    """Retrieve job-related information based on the specified category.

    This function processes the input category to determine the appropriate
    job-related label and returns it. It utilizes various mappings and
    conditions to derive the correct label based on prefixes, gender
    considerations, and other contextual information. The function also
    caches results for efficiency, avoiding redundant computations for
    previously queried categories.

    Args:
        cate (str): The category of jobs to retrieve information for.

    Returns:
        str: The job-related label corresponding to the input category.

    TODO: use FormatData method
    """
    cate = cate.replace("_", " ")
    logger.debug(f"<<lightyellow>>>> te4_2018_Jobs >> cate:({cate}) ")

    cate_original = cate
    cate_lower_original = cate.lower()

    country_lab = (
        new_religions_jobs_with_suffix(cate_lower_original) or
        jobs_with_nat_prefix_label(cate_lower_original) or
        ""
    )
    if country_lab:
        return country_lab

    # 1. Handle Prefix
    cate, main_ss, main_lab = handle_main_prefix(cate, cate_original)

    if cate.lower() != cate_lower_original:
        logger.debug(f'<<lightblue>> te4_2018_Jobs {cate=}, {cate_lower_original=}, {main_ss=}. ')

    cate_lower = cate.lower()

    # 3. Direct Lookups
    country_lab = _get_direct_lookup(cate_lower)

    category_suffix, country_prefix = get_suffix_with_keys(cate_lower, All_Nat, "nat")

    if not country_lab:
        # 4. Nationality Logic
        country_lab, job_example_lab, updated_main_lab = _handle_nationality_logic(
            cate_lower, main_ss, category_suffix, country_prefix
        )

        if category_suffix and not country_lab:
            country_lab = jobs_with_nat_prefix(cate_lower, country_prefix, category_suffix)

        if updated_main_lab:
            main_lab = updated_main_lab

        # 5. Fallback Prefixes
        if not country_lab:
            country_lab = womens_prefixes_work(cate_lower) or mens_prefixes_work(cate_lower)

    # 6. Final Formatting
    if main_ss and main_lab and country_lab:
        country_lab = main_lab.format(country_lab)
        if main_ss in Main_prefix_to and job_example_lab:
            job_example_lab = job_example_lab.format("").strip()
            country_lab = Main_prefix_to[main_ss].format(nat=Nat_women[country_prefix], t=job_example_lab)

    if not country_lab:
        country_lab = new_religions_jobs_with_suffix(cate_lower)

    logger.debug(f'end te4_2018_Jobs "{cate}" , {country_lab=}, cate2:{cate_lower_original}')

    return country_lab


__all__ = [
    "te4_2018_Jobs",
    "handle_main_prefix",
]
