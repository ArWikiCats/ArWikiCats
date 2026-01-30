"""
Package for resolving job titles and occupations in category names.
This package provides specialized resolvers for male and female job titles,
as well as religious occupations.
"""

import functools

import logging
from . import mens, relegin_jobs_new, womens

logger = logging.getLogger(__name__)


@functools.lru_cache(maxsize=10000)
def main_jobs_resolvers(normalized_category) -> str:
    """
    Resolve a job category name to a standardized jobs label.

    Parameters:
        normalized_category (str): Category name to resolve. Leading "category:" prefix, surrounding whitespace, and letter case are ignored.

    Returns:
        str: The resolved jobs category label, or an empty string if no resolver matched.
    """
    normalized_category = normalized_category.strip().lower().replace("category:", "")
    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> {normalized_category=}")

    resolved_label = (
        mens.mens_resolver_labels(normalized_category)
        or womens.womens_resolver_labels(normalized_category)
        or relegin_jobs_new.new_religions_jobs_with_suffix(normalized_category)
        or ""
    )

    logger.info(f"<<yellow>> end {normalized_category=}, {resolved_label=}")
    return resolved_label


__all__ = [
    "main_jobs_resolvers",
]
