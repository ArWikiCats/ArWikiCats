
from . import (
    countries_names_sport_multi_v2,
    countries_names_v2,
    nats_sport_multi_v2,
    nats_v2,
    nats_time_v2,
    army2,
)


def resolved_translations_resolvers_v2(normalized_category) -> str:

    resolved_label = (
        countries_names_sport_multi_v2.resolve_countries_names_sport(normalized_category) or
        countries_names_v2.resolve_by_countries_names_v2(normalized_category) or
        nats_sport_multi_v2.resolve_nats_sport_multi_v2(normalized_category) or
        nats_v2.resolve_by_nats(normalized_category) or
        nats_time_v2.resolve_nats_time_v2(normalized_category) or
        army2.resolve_secretaries_labels(normalized_category) or
        ""
    )

    return resolved_label


__all__ = [
    "resolved_translations_resolvers_v2",
]
