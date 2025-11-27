#!/usr/bin/python3
"""
TODO: refactor the code
"""

import functools
import re

from ...helps.log import logger
from ...translations import (
    All_Nat,
    Multi_sport_for_Jobs,
    Nat_mens,
    jobs_mens_data,
    short_womens_jobs,
)
from ..countries_formats.for_me import Work_for_me
from ..countries_formats.t4_2018_jobs import te4_2018_Jobs
from ..media_bots.film_keys_bot import Films
from ..o_bots import ethnic_bot
from .get_helps import get_suffix_with_keys
from .priffix_bot import Women_s_priffix_work, priffix_Mens_work

COUNTRY_TEMPLATES = {
    r"^anti\-(\w+) sentiment$": "مشاعر معادية لل%s",
}

_Multi_sport_for_Jobs: dict[str, str] = {
    "afc asian cup": "كأس آسيا",
    "afc cup": "كأس الاتحاد الآسيوي",
    "fifa futsal world cup": "كأس العالم لكرة الصالات",
}


def nat_match(category: str) -> str:
    """Match a category string to a localized sentiment label.

    Args:
        category (str): The category string to be matched.

    Returns:
        str: The localized sentiment label corresponding to the input category,
            or an empty string if no match is found.

    Example:
        category: anti-haitian sentiment, result: "مشاعر معادية للهايتيون"
    """
    category_lower = category.lower().replace("category:", "")
    matched_country_key = ""
    country_label_template = ""

    logger.debug(f'<<lightblue>> bot_te_4: nat_match normalized_category :: "{category_lower}" ')

    for pattern, template in COUNTRY_TEMPLATES.items():
        match = re.match(pattern, category_lower)
        if match:
            matched_country_key = match.group(1)
            country_label_template = template
            break

    if matched_country_key:
        logger.debug(f'<<lightblue>> bot_te_4: nat_match country_key :: "{matched_country_key}" ')

    country_label_key = Nat_mens.get(matched_country_key, "")
    country_label = ""

    if country_label_template and country_label_key:
        country_label = country_label_template % country_label_key

    if country_label:
        logger.debug(f'<<lightblue>> bot_te_4: nat_match country_label :: "{country_label}" ')

    return country_label


@functools.lru_cache(maxsize=None)
def te_2018_with_nat(category: str) -> str:
    """
    Return a localized job label for 2018 categories with nationality hints.
    TODO: use FormatData method

    Example:
        category: zimbabwean musical groups, result: "مجموعات موسيقية زيمبابوية"
    """
    logger.debug(f"<<lightyellow>>>> te_2018_with_nat >> category:({category})")

    normalized_category = category.lower().replace("_", " ").replace("-", " ")

    # Try direct lookups first
    country_label = short_womens_jobs.get(normalized_category) or jobs_mens_data.get(normalized_category)

    if not country_label:
        suffix, nat = get_suffix_with_keys(normalized_category, All_Nat, "nat")

        if suffix:
            # Try various strategies if we have a country code
            strategies = [
                lambda: Work_for_me(normalized_category, nat, suffix),
                lambda: Films(normalized_category, nat, suffix),
                lambda: ethnic_bot.ethnic_label(normalized_category, nat, suffix),
                lambda: nat_match(normalized_category),
            ]

            for strategy in strategies:
                country_label = strategy()
                if country_label:
                    break

        # Fallback strategies if still no label
        if not country_label:
            country_label = priffix_Mens_work(normalized_category) or Women_s_priffix_work(normalized_category)

        # Special case for Films if everything else failed and no country code
        if not country_label and not suffix:
            country_label = Films(normalized_category, "", "")

    logger.debug(f'<<lightblue>> bot_te_4: te_2018_with_nat :: "{country_label}" ')
    return country_label or ""


@functools.lru_cache(maxsize=None)
def Jobs_in_Multi_Sports(category: str) -> str:
    """Retrieve job information related to multiple sports based on the category.

    Args:
        category (str): The category string representing the sport or job type.

    Returns:
        str: A formatted string representing the job information related to the
            specified category.
    Example:
        category: african games competitors, result: "منافسون في الألعاب الإفريقية"
    """
    logger.debug(f"<<lightyellow>>>> Jobs_in_Multi_Sports >> category:({category}) ")

    category_clean = category.replace("_", " ")
    category_lower = category_clean.lower()

    job_key = ""
    game_label = ""

    for sport_prefix, label in Multi_sport_for_Jobs.items():
        game_prefix = f"{sport_prefix} ".lower()
        if category_lower.startswith(game_prefix):
            job_key = category_lower[len(game_prefix) :]
            game_label = label
            logger.debug(f'Jobs_in_Multi_Sports match: prefix="{game_prefix}", label="{game_label}", job="{job_key}"')
            break

    primary_label = ""
    if job_key:
        job_label = te4_2018_Jobs(job_key)
        if job_label and game_label:
            primary_label = f"{job_label} في {game_label}"

    logger.info(f'end Jobs_in_Multi_Sports "{category_clean}" , primary_label:"{primary_label}"')
    return primary_label
