
from . import womens, mens


def new_jobs_resolver_label(normalized_category) -> str:

    resolved_label = (
        mens.mens_resolver_labels(normalized_category) or
        womens.womens_resolver_labels(normalized_category) or
        ""
    )

    return resolved_label


__all__ = [
    "resolved_translations_resolvers",
]
