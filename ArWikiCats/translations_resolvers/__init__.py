
from ..translations_resolvers_v2 import countries_names_sport_multi_v2
from .nats_women import nats_women_label
from . import countries_names, nats_sports_males


def resolved_sports_formats_labels(normalized_category) -> str:

    resolved_label = countries_names.resolve_by_countries_names(normalized_category)

    if not resolved_label:
        resolved_label = nats_sports_males.resolve_federation_label(normalized_category)

    if not resolved_label:
        resolved_label = nats_women_label(normalized_category)

    if not resolved_label:
        resolved_label = countries_names_sport_multi_v2.resolve_countries_names_sport(normalized_category)

    return resolved_label


__all__ = [
    "nats_women_label",
    "resolved_sports_formats_labels",
]
