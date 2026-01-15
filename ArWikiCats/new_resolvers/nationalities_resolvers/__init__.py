import functools

from ...helps import logger
from . import (
    ministers_resolver,
    nationalities_time_v2,
    nationalities_v2,
)


@functools.lru_cache(maxsize=None)
def resolve_nationalities_main(normalized_category) -> str:
    normalized_category = normalized_category.strip().lower().replace("category:", "")

    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> Trying nationalities_resolvers resolvers for: {normalized_category=}")

    resolved_label = (
        nationalities_v2.resolve_by_nats(normalized_category)
        or nationalities_time_v2.resolve_nats_time_v2(normalized_category)
        or ministers_resolver.resolve_secretaries_labels(normalized_category)
        or ""
    )

    logger.info_if_or_debug(
        f"<<yellow>> end nationalities_resolvers: {normalized_category=}, {resolved_label=}", resolved_label
    )
    return resolved_label


__all__ = [
    "resolve_nationalities_main",
]
