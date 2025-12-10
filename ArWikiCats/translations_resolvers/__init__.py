
from . import countries_names


def resolved_translations_resolvers(normalized_category) -> str:

    resolved_label = countries_names.resolve_by_countries_names(normalized_category)

    return resolved_label


__all__ = [
    "resolved_translations_resolvers",
]
