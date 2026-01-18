"""
Package for resolving categories that combine time periods with jobs.
This package provides specialized resolvers for categories like
"14th-century writers" or "21st-century politicians from Yemen".
"""

import functools

from ...helps import logger
from . import (
    year_job_origin_resolver,
    year_job_resolver,
)


@functools.lru_cache(maxsize=None)
def time_and_jobs_resolvers_main(normalized_category) -> str:
    """Main entry point for time and jobs resolvers.

    Orchestrates the resolution of category names that combine time periods with jobs
    by attempting to match against various time-job resolvers in sequence.

    Args:
        normalized_category (str): The normalized category string to be resolved.

    Returns:
        str: The resolved Arabic category label, or an empty string if no match is found.
    """
    normalized_category = normalized_category.strip().lower().replace("category:", "")
    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> Trying time_and_jobs_resolvers_main for: {normalized_category=}")

    resolved_label = (
        year_job_origin_resolver.resolve_year_job_from_countries(normalized_category)
        or year_job_resolver.resolve_year_job_countries(normalized_category)
        or ""
    )

    logger.info_if_or_debug(
        f"<<yellow>> end time_and_jobs_resolvers_main: {normalized_category=}, {resolved_label=}", resolved_label
    )
    return resolved_label


__all__ = [
    "time_and_jobs_resolvers_main",
]
