
import functools
from ...helps import logger

from ..countries_names_resolvers import countries_names_v2
from ..sports_resolvers import countries_names_and_sports, nationalities_and_sports
from . import (
    ministers_resolver,
    nationalities_time_v2,
    nationalities_v2,
)


@functools.lru_cache(maxsize=None)
def resolve_nationalities_main(normalized_category) -> str:
    normalized_category = normalized_category.strip().lower().replace("category:", "")

    logger.debug("--"*20)
    logger.debug(f"<><><><><><> <<green>> Trying nationalities_resolvers resolvers for: {normalized_category=}")

    resolved_label = (
        countries_names_and_sports.resolve_countries_names_sport_with_ends(normalized_category) or
        countries_names_v2.resolve_by_countries_names_v2(normalized_category) or
        nationalities_and_sports.resolve_nats_sport_multi_v2(normalized_category) or
        nationalities_v2.resolve_by_nats(normalized_category) or
        nationalities_time_v2.resolve_nats_time_v2(normalized_category) or
        ministers_resolver.resolve_secretaries_labels(normalized_category) or
        ""
    )

    logger.debug(f"<<green>> end nationalities_resolvers: {normalized_category=}, {resolved_label=}")
    return resolved_label


__all__ = [
    "resolve_nationalities_main",
]
