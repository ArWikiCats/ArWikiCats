import functools

from ...helps import logger
from . import (
    year_job_origin_resolver,
    year_job_resolver,
)


@functools.lru_cache(maxsize=None)
def time_and_jobs_resolvers_main(normalized_category) -> str:
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
