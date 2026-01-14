#!/usr/bin/python3
"""
Bot for translating job-related and nationality-based categories.

This module provides functionality for matching and translating categories
related to jobs, nationalities, and multi-sports topics from English to Arabic.

TODO: planed to be replaced by ArWikiCats.new_resolvers.nationalities_resolvers
"""

import functools
from ..new_resolvers.jobs_resolvers import resolve_jobs_main
from ..new_resolvers.countries_names_resolvers.medalists_resolvers import medalists_data

from ..helps import logger


def _find_sport_prefix_match(category_lower: str) -> tuple[str, str]:
    """Find a matching sport prefix in the category.

    Args:
        category_lower: The lowercase category string.

    Returns:
        A tuple of (job_suffix, sport_label) or ("", "") if no match.
    """
    for sport_prefix, sport_label in medalists_data.items():
        prefix_pattern = f"{sport_prefix} ".lower()
        if category_lower.startswith(prefix_pattern):
            job_suffix = category_lower[len(prefix_pattern) :]
            logger.debug(
                f'jobs_in_multi_sports match: prefix="{prefix_pattern}", ' f'label="{sport_label}", job="{job_suffix}"'
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

    category = category.replace("_", " ").lower()
    category = category.replace("olympics", "olympic")

    job_suffix, sport_label = _find_sport_prefix_match(category)

    if not job_suffix or not sport_label:
        return ""

    job_label = resolve_jobs_main(job_suffix)

    if not job_label:
        return ""

    result = f"{job_label} في {sport_label}"
    logger.info(f'end jobs_in_multi_sports "{category}", {result=}')
    return result


__all__ = [
    "jobs_in_multi_sports",
]
