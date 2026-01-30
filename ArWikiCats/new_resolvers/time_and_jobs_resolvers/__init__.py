"""
Package for resolving categories that combine time periods with jobs.
This package provides specialized resolvers for categories like
"14th-century writers" or "21st-century politicians from Yemen".
"""

import functools

import logging
from . import (
    year_job_origin_resolver,
    year_job_resolver,
)

logger = logging.getLogger(__name__)


@functools.lru_cache(maxsize=10000)
def time_and_jobs_resolvers_main(normalized_category) -> str:
    """
    Resolve a combined time-period-and-job category string to its Arabic label.

    Attempts multiple internal resolvers in sequence and returns the first non-empty match.

    Parameters:
        normalized_category (str): Category string to resolve; may include a leading 'Category:' prefix.

    Returns:
        str: The resolved Arabic category label if found, otherwise an empty string.
    """
    normalized_category = normalized_category.strip().lower().replace("category:", "")
    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> {normalized_category=}")

    resolved_label = (
        year_job_origin_resolver.resolve_year_job_from_countries(normalized_category)
        or year_job_resolver.resolve_year_job_countries(normalized_category)
        or ""
    )

    logger.info(f"<<yellow>> end {normalized_category=}, {resolved_label=}")
    return resolved_label


__all__ = [
    "time_and_jobs_resolvers_main",
]
