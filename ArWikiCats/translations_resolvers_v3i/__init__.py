
import functools

from ..helps import logger
from . import (
    resolve_v3i,
)


@functools.lru_cache(maxsize=None)
def resolved_translations_resolvers_v3i(normalized_category) -> str:
    normalized_category = normalized_category.strip().lower().replace("category:", "")
    logger.debug("--"*20)
    logger.debug(f"<><><><><><> <<green>> Trying v3i resolvers for: {normalized_category=}")

    resolved_label = (
        resolve_v3i.resolve_year_job_from_countries(normalized_category) or
        ""
    )

    logger.debug(f"<<green>> end resolved_translations_resolvers_v3i: {normalized_category=}, {resolved_label=}")
    return resolved_label


__all__ = [
    "resolved_translations_resolvers_v3i",
]
