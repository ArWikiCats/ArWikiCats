
import functools

from ..helps import logger
from . import (
    countries_names_sport_multi_v2,
    countries_names_v2,
    ministers_resolver,
    nats_sport_multi_v2,
    nats_v2,
    nats_time_v2,
)


@functools.lru_cache(maxsize=None)
def resolved_translations_resolvers_v2(normalized_category) -> str:
    logger.debug(f"Trying v2 resolvers for: {normalized_category=}")

    resolved_label = (
        countries_names_sport_multi_v2.resolve_countries_names_sport(normalized_category) or
        countries_names_v2.resolve_by_countries_names_v2(normalized_category) or
        nats_sport_multi_v2.resolve_nats_sport_multi_v2(normalized_category) or
        nats_v2.resolve_by_nats(normalized_category) or
        nats_time_v2.resolve_nats_time_v2(normalized_category) or
        ministers_resolver.resolve_secretaries_labels(normalized_category) or
        ""
    )

    return resolved_label


__all__ = [
    "resolved_translations_resolvers_v2",
]
