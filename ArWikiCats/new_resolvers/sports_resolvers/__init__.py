"""
Package for resolving sports-related categories.
This package provides resolvers for sports teams, athletes, and competitions,
often combined with geographic or nationality elements.
"""

import functools
import logging

from . import (
    countries_names_and_sports,
    jobs_multi_sports_reslover,
    nationalities_and_sports,
    raw_sports,
    raw_sports_with_suffixes,
    sport_lab_nat,
)

logger = logging.getLogger(__name__)


@functools.lru_cache(maxsize=10000)
def main_sports_resolvers(category) -> str:
    """
    Resolve a normalized category string into a sports-related label.

    Parameters:
        category (str): Category text (may include a leading "Category:"); this input will be trimmed and lowercased before resolution.

    Returns:
        str: Resolved sports category label, or an empty string if no resolver produced a match.
    """
    category = category.strip().lower().replace("category:", "")

    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> {category=}")

    result = (
        countries_names_and_sports.resolve_countries_names_sport_with_ends(category)
        or nationalities_and_sports.resolve_nats_sport_multi_v2(category)
        or jobs_multi_sports_reslover.jobs_in_multi_sports(category)
        or sport_lab_nat.sport_lab_nat_load_new(category)
        or raw_sports_with_suffixes.wrap_team_xo_normal_2025_with_ends(category)
        or raw_sports.resolve_sport_label_unified(category)
        or ""
    )

    logger.log(20 if result else 10, f"<<yellow>> end {category=}, {result=}")
    return result


__all__ = [
    "main_sports_resolvers",
]
