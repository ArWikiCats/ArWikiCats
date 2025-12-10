
from . import countries_names, nats_women


def resolved_translations_resolvers(normalized_category) -> str:

    resolved_label = countries_names.resolve_by_countries_names(normalized_category)

    if not resolved_label:
        resolved_label = nats_women.nats_women_label(normalized_category)

    return resolved_label


__all__ = [
    "nats_women_label",
    "resolved_translations_resolvers",
]
