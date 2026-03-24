"""
Package for resolving job titles and occupations in category names.
This package provides specialized resolvers for male and female job titles,
as well as religious occupations.
"""

import functools
import logging

from ..worker import run_resolvers
from . import mens, relegin_jobs_new, womens

logger = logging.getLogger(__name__)


@functools.lru_cache(maxsize=10000)
def main_jobs_resolvers(category) -> str:
    """
    Resolve a job category name to a standardized jobs label.

    Parameters:
        category (str): Category name to resolve. Leading "category:" prefix, surrounding whitespace, and letter case are ignored.

    Returns:
        str: The resolved jobs category label, or an empty string if no resolver matched.
    """
    category = category.strip().lower().replace("category:", "")
    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> {category=}")

    result = run_resolvers(category, [
        mens.mens_resolver_labels,
        # males_resolver_labels,  # male resolvers
        womens.womens_resolver_labels,
        relegin_jobs_new.new_religions_jobs_with_suffix,
        # new_religions_jobs_for_males,  # male resolvers
    ])

    logger.log(20 if result else 10, f"<<yellow>> end {category=}, {result=}")
    return result


__all__ = [
    "main_jobs_resolvers",
]
