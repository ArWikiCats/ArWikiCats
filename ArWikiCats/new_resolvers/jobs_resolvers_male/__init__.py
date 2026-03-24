"""

This module goal is to collect all `male` resolvers so it can replaced later by genders_resolvers.

"""

import functools
import logging

from ..worker import run_resolvers
from .mens import males_resolver_labels
from .relegins import new_religions_jobs_for_males
from .relegins_nats import resolve_nats_jobs_for_males

logger = logging.getLogger(__name__)


@functools.lru_cache(maxsize=10000)
def main_jobs_resolvers_for_males(category) -> str:
    """
    Resolve job categories for males using male-specific resolvers.
    """
    category = category.strip().lower().replace("category:", "")
    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> {category=}")

    result = run_resolvers(category, [
        males_resolver_labels,
        new_religions_jobs_for_males,
        resolve_nats_jobs_for_males,
    ])

    logger.log(20 if result else 10, f"<<yellow>> end {category=}, {result=}")
    return result


__all__ = [
    "males_resolver_labels",
    "new_religions_jobs_for_males",
    "resolve_nats_jobs_for_males",
    "main_jobs_resolvers_for_males",
]
