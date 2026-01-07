#!/usr/bin/python3
"""
Bot for translating job-related and nationality-based categories.

This module provides functionality for matching and translating categories
related to jobs, nationalities, and multi-sports topics from English to Arabic.

TODO: planed to be replaced by ArWikiCats.new_resolvers.nationalities_resolvers
"""

import functools
import re
from typing import Optional

from ..new_resolvers.jobs_resolvers import resolve_jobs_main
from ..make_bots.languages_bot.langs_w import Lang_work

from ..helps import logger
from ..translations import (
    all_nat_sorted,
    Multi_sport_for_Jobs,
    Nat_mens,
    jobs_mens_data,
    short_womens_jobs,
)
from ..make_bots.languages_bot.resolve_languages_new import resolve_languages_labels
from ..make_bots.countries_formats.for_me import Work_for_me_main
from .t4_2018_jobs import te4_2018_Jobs
from ..make_bots.o_bots import ethnic_bot
from ..make_bots.jobs_bots.get_helps import get_suffix_with_keys
from .prefix_bot import mens_prefixes_work, womens_prefixes_work

# Template patterns for anti-sentiment categories
ANTI_SENTIMENT_PATTERNS: dict[str, str] = {
    r"^anti\-(\w+) sentiment$": "مشاعر معادية لل%s",
}


def _normalize_category(category: str) -> str:
    """Normalize a category string for matching.

    Args:
        category: The raw category string.

    Returns:
        Lowercase category with 'category:' prefix removed.
    """
    return category.lower().replace("category:", "")


def _match_anti_sentiment_pattern(normalized_category: str) -> tuple[str, str]:
    """Match a category against anti-sentiment patterns.

    Args:
        normalized_category: The normalized category string.

    Returns:
        A tuple of (matched_country_key, template) or ("", "") if no match.
    """
    for pattern, template in ANTI_SENTIMENT_PATTERNS.items():
        match = re.match(pattern, normalized_category)
        if match:
            return match.group(1), template
    return "", ""


@functools.lru_cache(maxsize=10000)
def nat_match(category: str) -> str:
    """Match a category string to a localized anti-sentiment label.

    Processes categories like "anti-haitian sentiment" and returns the
    Arabic equivalent "مشاعر معادية للهايتيون".

    Args:
        category: The category string to be matched.

    Returns:
        The localized sentiment label, or empty string if no match.

    Example:
        >>> nat_match("anti-haitian sentiment")
        "مشاعر معادية للهايتيون"
    """
    normalized_category = _normalize_category(category)
    logger.debug(f'<<lightblue>> bot_te_4: nat_match normalized_category :: "{normalized_category}"')

    matched_country_key, template = _match_anti_sentiment_pattern(normalized_category)

    if not matched_country_key:
        return ""

    logger.debug(f'<<lightblue>> bot_te_4: nat_match country_key :: "{matched_country_key}"')

    nationality_label = Nat_mens.get(matched_country_key, "")
    if not nationality_label:
        return ""

    result = template % nationality_label
    logger.debug(f"<<lightblue>> bot_te_4: nat_match {result=}")
    return result


def _try_direct_job_lookup(normalized_category: str) -> Optional[str]:
    """Try direct dictionary lookups for job categories.

    Args:
        normalized_category: The normalized category string.

    Returns:
        The job label if found, None otherwise.
    """
    return short_womens_jobs.get(normalized_category) or jobs_mens_data.get(normalized_category)


def _try_nationality_based_strategies(
    normalized_category: str,
    nationality_key: str,
    suffix: str,
) -> Optional[str]:
    """
    Attempt nationality-aware translation strategies for a normalized category.

    Tries each configured nationality-based strategy in order and returns the first non-empty translation.

    Parameters:
        normalized_category: The normalized category string (lowercased and cleaned).
        nationality_key: The detected nationality key used by nationality-aware strategies.
        suffix: The remaining suffix of the category after nationality extraction.

    Returns:
        The translated label if a strategy produced one, None otherwise.
    """
    strategies = [
        ("ethnic_bot.ethnic_label", lambda: ethnic_bot.ethnic_label(normalized_category, nationality_key, suffix)),
        ("nat_match", lambda: nat_match(normalized_category)),
    ]

    for strategy_name, strategy_func in strategies:
        result = strategy_func()
        if result:
            logger.debug(f"<<lightblue>> te_2018_with_nat: def {strategy_name}() {result=}")
            return result

    return None


def _try_prefix_based_work(normalized_category: str) -> str:
    """Try prefix-based job label extraction.

    Args:
        normalized_category: The normalized category string.

    Returns:
        The job label if found, empty string otherwise.
    """
    return mens_prefixes_work(normalized_category) or womens_prefixes_work(normalized_category) or ""


@functools.lru_cache(maxsize=None)
def te_2018_with_nat(category: str) -> str:
    """Return a localized job label for 2018 categories with nationality hints.

    This function processes job-related categories that include nationality
    information and returns the appropriate Arabic translation.

    Args:
        category: The category string to translate.

    Returns:
        The localized job label, or empty string if no match.

    Example:
        >>> te_2018_with_nat("zimbabwean musical groups")
        "مجموعات موسيقية زيمبابوية"

    TODO: Consider using FormatData method for consistency.
    """
    logger.debug(f"<<lightyellow>>>> te_2018_with_nat >> category:({category})")

    normalized_category = category.lower().replace("_", " ").replace("-", " ")

    # Strategy 1: Direct dictionary lookup
    direct_result = _try_direct_job_lookup(normalized_category) or Work_for_me_main(normalized_category)
    if direct_result:
        logger.debug(f'<<lightblue>> bot_te_4: te_2018_with_nat :: "{direct_result}"')
        return direct_result

    # Strategy 2: Nationality-based extraction
    suffix, nationality_key = get_suffix_with_keys(normalized_category, all_nat_sorted, "nat")

    if suffix:
        nationality_result = _try_nationality_based_strategies(normalized_category, nationality_key, suffix)
        if nationality_result:
            return nationality_result

    # Strategy 3: Prefix-based fallback
    # fallback_result = _try_prefix_based_work(normalized_category)
    fallback_result = ""
    logger.debug(f'<<lightblue>> bot_te_4: te_2018_with_nat :: "{fallback_result}"')
    return fallback_result


def _find_sport_prefix_match(category_lower: str) -> tuple[str, str]:
    """Find a matching sport prefix in the category.

    Args:
        category_lower: The lowercase category string.

    Returns:
        A tuple of (job_suffix, sport_label) or ("", "") if no match.
    """
    for sport_prefix, sport_label in Multi_sport_for_Jobs.items():
        prefix_pattern = f"{sport_prefix} ".lower()
        if category_lower.startswith(prefix_pattern):
            job_suffix = category_lower[len(prefix_pattern) :]
            logger.debug(
                f'Jobs_in_Multi_Sports match: prefix="{prefix_pattern}", ' f'label="{sport_label}", job="{job_suffix}"'
            )
            return job_suffix, sport_label
    return "", ""


@functools.lru_cache(maxsize=None)
def jobs_in_multi_sports(category: str) -> str:
    """Retrieve job information related to multiple sports based on the category.

    Processes categories that combine sports events with job roles and
    returns the Arabic translation.

    Args:
        category: The category string representing the sport or job type.

    Returns:
        A formatted string with the job in the context of the sport event.

    Example:
        >>> jobs_in_multi_sports("african games competitors")
        "منافسون في الألعاب الإفريقية"
    """
    logger.debug(f"<<lightyellow>>>> jobs_in_multi_sports >> category:({category})")

    category_clean = category.replace("_", " ")
    category_lower = category_clean.lower()

    data_find_in_it = {
        # medalists
        "olympic medalists": "فائزون بميداليات أولمبية",
        "olympic gold medalists": "فائزون بميداليات ذهبية أولمبية",
        "olympic silver medalists": "فائزون بميداليات فضية أولمبية",
        "olympic bronze medalists": "فائزون بميداليات برونزية أولمبية",
        "winter olympic medalists": "فائزون بميداليات أولمبية شتوية",
        "summer olympic medalists": "فائزون بميداليات أولمبية صيفية",
        # competitors
        "olympic competitors": "منافسون أولمبيون",
        "winter olympic competitors": "منافسون أولمبيون شتويون",
        "summer olympic competitors": "منافسون أولمبيون صيفيون",
    }
    category_lower_fixed = category_lower.replace("olympics", "olympic")
    if category_lower_fixed in data_find_in_it:
        logger.info(f'end jobs_in_multi_sports "{category_lower_fixed}", direct found')
        return data_find_in_it[category_lower_fixed]

    job_suffix, sport_label = _find_sport_prefix_match(category_lower)

    if not job_suffix or not sport_label:
        return ""

    job_label = (
        resolve_languages_labels(job_suffix) or
        te4_2018_Jobs(job_suffix) or
        Lang_work(job_suffix) or
        resolve_jobs_main(job_suffix) or
        ""
    )
    if not job_label:
        return ""

    result = f"{job_label} في {sport_label}"
    logger.info(f'end jobs_in_multi_sports "{category_clean}", {result=}')
    return result


# Backward compatibility alias
Jobs_in_Multi_Sports = jobs_in_multi_sports


__all__ = [
    "nat_match",
    "te_2018_with_nat",
    "jobs_in_multi_sports",
    "Jobs_in_Multi_Sports",  # Backward compatibility
]
