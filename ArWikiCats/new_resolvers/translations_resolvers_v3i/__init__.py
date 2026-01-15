import functools

from ...helps import logger
from . import (
    resolve_v3i,
    resolve_v3ii,
)


@functools.lru_cache(maxsize=None)
def resolve_v3i_main(normalized_category) -> str:
    normalized_category = normalized_category.strip().lower().replace("category:", "")
    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> Trying v3i resolvers for: {normalized_category=}")

    resolved_label = (
        resolve_v3i.resolve_year_job_from_countries(normalized_category)
        or resolve_v3ii.resolve_year_job_countries(normalized_category)
        or ""
    )

    logger.info_if_or_debug(
        f"<<yellow>> end resolve_v3i_main: {normalized_category=}, {resolved_label=}", resolved_label
    )
    return resolved_label


__all__ = [
    "resolve_v3i_main",
]
