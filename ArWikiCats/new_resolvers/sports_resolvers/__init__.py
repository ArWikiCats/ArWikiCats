import functools

from ...helps import logger
from . import (
    countries_names_and_sports,
    jobs_multi_sports_reslover,
    match_labs,
    nationalities_and_sports,
    raw_sports,
    sport_lab_nat,
)


@functools.lru_cache(maxsize=None)
def main_sports_resolvers(normalized_category) -> str:
    """Main entry point for sports resolvers.

    Args:
        normalized_category (str): The normalized category string.

    Returns:
        str: The resolved sports category label.
    """
    normalized_category = normalized_category.strip().lower().replace("category:", "")

    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> Trying sports_resolvers resolvers for: {normalized_category=}")

    resolved_label = (
        # raw_sports.wrap_team_xo_normal_2025_with_ends(normalized_category) or               #
        countries_names_and_sports.resolve_countries_names_sport_with_ends(normalized_category)
        or nationalities_and_sports.resolve_nats_sport_multi_v2(normalized_category)
        or jobs_multi_sports_reslover.jobs_in_multi_sports(normalized_category)
        # or match_labs.find_teams_2025(normalized_category)
        # or sport_lab_nat.sport_lab_nat_load_new(normalized_category)
        or ""
    )

    logger.info_if_or_debug(
        f"<<yellow>> end main_sports_resolvers: {normalized_category=}, {resolved_label=}", resolved_label
    )
    return resolved_label


__all__ = [
    "main_sports_resolvers",
]
