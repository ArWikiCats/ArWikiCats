"""
Package for resolving sports-related categories.
This package provides resolvers for sports teams, athletes, and competitions,
often combined with geographic or nationality elements.
"""

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


def main_sports_resolvers(normalized_category) -> str:
    """
    Resolve a normalized category string into a sports-related label.

    Parameters:
        normalized_category (str): Category text (may include a leading "Category:"); this input will be trimmed and lowercased before resolution.

    Returns:
        str: Resolved sports category label, or an empty string if no resolver produced a match.
    """
    normalized_category = normalized_category.strip().lower().replace("category:", "")

    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> {normalized_category=}")

    resolved_label = (
        countries_names_and_sports.resolve_countries_names_sport_with_ends(normalized_category)
        or nationalities_and_sports.resolve_nats_sport_multi_v2(normalized_category)
        or jobs_multi_sports_reslover.jobs_in_multi_sports(normalized_category)
        or sport_lab_nat.sport_lab_nat_load_new(normalized_category)
        or raw_sports_with_suffixes.wrap_team_xo_normal_2025_with_ends(normalized_category)
        or raw_sports.resolve_sport_label_unified(normalized_category)
        or ""
    )

    logger.info(f"<<yellow>> end {normalized_category=}, {resolved_label=}")
    return resolved_label


__all__ = [
    "main_sports_resolvers",
]
