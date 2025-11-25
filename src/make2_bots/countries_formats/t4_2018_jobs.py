#!/usr/bin/python3
"""
!
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
from ..jobs_bots.jobs_mainbot import jobs_with_nat_prefix
from ..jobs_bots.priffix_bot import Women_s_priffix_work, priffix_Mens_work
from ..jobs_bots.relegin_jobs import try_relegins_jobs_with_suffix
from ..languages_bot.langs_w import Lang_work

# TODO: fix typo to prefix_lab_for_2018
priffix_lab_for_2018: dict[str, dict[str, str]] = {
    "fictional": {"men": "{} خيالي", "women": "{} خيالية"},
    "native": {"men": "{} أصلي", "women": "{} أصلية"},
    "contemporary": {"men": "{} معاصر", "women": "{} معاصرة"},
    "ancient": {"men": "{} قديم", "women": "{} قديمة"},
}

Main_priffix_to: dict[str, str] = {
    "non": "{t} غير {nat}",
}


Main_priffix: dict[str, str] = {
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
Main_priffix = dict(sorted(Main_priffix.items(), key=lambda x: x[0].count(" "), reverse=True))


def handle_main_prefix(category: str, category_original: str = "") -> Tuple[str, str, str]:
    """
    Handle Main_priffix logic to strip prefixes and determine main label.

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

    for me, melab in Main_priffix.items():
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
        f'<<lightblue>> te4_2018_Jobs Main_priffix cate.startswith(me2: "{me2}") cate:"{category}",Main_lab:"{main_lab}". '
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

    if category_suffix and (main_ss in priffix_lab_for_2018) and not country_lab:

        # en_is_nat_ar_is_women
        job_example_lab = en_is_nat_ar_is_women.get(category_suffix.strip(), "")
        if job_example_lab:
            country_lab = job_example_lab.format(Nat_women[country_prefix])
            logger.debug(f'<<lightblue>> bot_te_4, new country_lab "{country_lab}" ')
            updated_main_lab = priffix_lab_for_2018[main_ss]["women"]

        # en_is_nat_ar_is_man
        if not country_lab:
            job_example_lab = en_is_nat_ar_is_man.get(category_suffix.strip(), "")
            if job_example_lab:
                country_lab = job_example_lab.format(Nat_men[country_prefix])
                logger.debug(f'<<lightblue>> bot_te_4, new country_lab "{country_lab}" ')
                updated_main_lab = priffix_lab_for_2018[main_ss]["men"]

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

    # 1. Handle Prefix
    cate, main_ss, main_lab = handle_main_prefix(cate, cate_original)

    if cate.lower() != cate_lower_original:
        logger.debug(f'<<lightblue>> te4_2018_Jobs cate:"{cate}",cate2:"{cate_lower_original}",Main_Ss:"{main_ss}". ')

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
            country_lab = Women_s_priffix_work(cate_lower) or priffix_Mens_work(cate_lower)

    # 6. Final Formatting
    if main_ss and main_lab and country_lab:
        country_lab = main_lab.format(country_lab)
        if main_ss in Main_priffix_to and job_example_lab:
            job_example_lab = job_example_lab.format("").strip()
            country_lab = Main_priffix_to[main_ss].format(nat=Nat_women[country_prefix], t=job_example_lab)

    if not country_lab:
        country_lab = try_relegins_jobs_with_suffix(cate_lower)

    logger.debug(f'end te4_2018_Jobs "{cate}" , country_lab:"{country_lab}", cate2:{cate_lower_original}')

    return country_lab


__all__ = [
    "te4_2018_Jobs",
    "handle_main_prefix",
]
