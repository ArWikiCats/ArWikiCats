"""

This module goal is to collect all `male` resolvers so it can replaced later by genders_resolvers.

"""

import functools
import logging

from .mens import males_resolver_labels
from .relegins import new_religions_jobs_for_males
from .relegins_nats import resolve_nats_jobs_for_males

logger = logging.getLogger(__name__)


@functools.lru_cache(maxsize=10000)
def main_jobs_resolvers_for_males(normalized_category) -> str:
    """
    """
    normalized_category = normalized_category.strip().lower().replace("category:", "")
    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> {normalized_category=}")

    resolved_label = (
        males_resolver_labels(normalized_category)
        or new_religions_jobs_for_males(normalized_category)
        or resolve_nats_jobs_for_males(normalized_category)
        or ""
    )

    logger.info(f"<<yellow>> end {normalized_category=}, {resolved_label=}")
    return resolved_label


__all__ = [
    "males_resolver_labels",
    "new_religions_jobs_for_males",
    "resolve_nats_jobs_for_males",
    "main_jobs_resolvers_for_males",
]
