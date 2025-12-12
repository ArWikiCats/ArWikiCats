
from . import womens, mens


def new_jobs_resolver_label(normalized_category) -> str:

    resolved_label = (
        womens.womens_resolver_label(normalized_category) or
        mens.mens_resolver_label(normalized_category) or
        ""
    )

    return resolved_label


__all__ = [
    "resolved_translations_resolvers",
]
