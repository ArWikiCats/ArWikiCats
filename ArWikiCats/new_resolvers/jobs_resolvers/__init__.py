
from . import womens, mens


def resolve_jobs_main(normalized_category) -> str:

    normalized_category = normalized_category.lower().replace("category:", "")
    resolved_label = (
        mens.mens_resolver_labels(normalized_category) or
        womens.womens_resolver_labels(normalized_category) or
        ""
    )

    return resolved_label


__all__ = [
    "resolve_jobs_main",
]
