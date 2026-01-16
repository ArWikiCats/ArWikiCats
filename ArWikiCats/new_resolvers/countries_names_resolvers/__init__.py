import functools

from ...helps import logger
from . import (  # countries_names_double_v2,
    countries_names,
    countries_names_v2,
    geo_names_formats,
    medalists_resolvers,
    us_states,
)


@functools.lru_cache(maxsize=None)
def resolve_countries_names_main(normalized_category) -> str:
    normalized_category = normalized_category.strip().lower().replace("category:", "")
    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> Trying countries_names_resolvers for: {normalized_category=}")

    resolved_label = (
        # NOTE: order matters here
        # resolve_by_countries_names_v2 must be before resolve_by_countries_names, to avoid mis-resolving like:
        # incorrect:    [Category:Zimbabwe political leader] : "تصنيف:قادة زيمبابوي السياسيون",
        # correct:      [Category:Zimbabwe political leader] : "تصنيف:قادة سياسيون زيمبابويون",
        countries_names_v2.resolve_by_countries_names_v2(normalized_category)
        or countries_names.resolve_by_countries_names(normalized_category)
        or medalists_resolvers.resolve_countries_names_medalists(normalized_category)
        or us_states.resolve_us_states(normalized_category)
        or geo_names_formats.resolve_by_geo_names(normalized_category)
        # or countries_names_double_v2.resolve_countries_names_double(normalized_category)
        or ""
    )

    logger.info_if_or_debug(
        f"<<yellow>> end countries_names_resolvers: {normalized_category=}, {resolved_label=}", resolved_label
    )
    return resolved_label


__all__ = [
    "resolve_countries_names_main",
]
