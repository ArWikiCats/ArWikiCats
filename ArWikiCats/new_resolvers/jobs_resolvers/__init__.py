import functools

from ...helps import logger
from . import mens, relegin_jobs_new, womens


@functools.lru_cache(maxsize=None)
def resolve_jobs_main(normalized_category) -> str:
    normalized_category = normalized_category.strip().lower().replace("category:", "")
    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> Trying jobs_resolvers for: {normalized_category=}")

    resolved_label = (
        mens.mens_resolver_labels(normalized_category)
        or womens.womens_resolver_labels(normalized_category)
        or relegin_jobs_new.new_religions_jobs_with_suffix(normalized_category)
        or ""
    )

    logger.info_if_or_debug(f"<<yellow>> end jobs_resolvers: {normalized_category=}, {resolved_label=}", resolved_label)
    return resolved_label


__all__ = [
    "resolve_jobs_main",
]
