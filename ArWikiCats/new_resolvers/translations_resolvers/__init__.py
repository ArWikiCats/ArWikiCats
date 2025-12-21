
from . import countries_names, us_states, countries_names_medalists
from ...helps import logger


def resolved_translations_resolvers(normalized_category) -> str:
    normalized_category = normalized_category.strip().lower().replace("category:", "")
    logger.debug("--"*20)
    logger.debug(f"<><><><><><> <<green>> Trying v1 resolvers for: {normalized_category=}")

    resolved_label = (
        countries_names.resolve_by_countries_names(normalized_category) or
        countries_names_medalists.resolve_countries_names_medalists(normalized_category) or
        us_states.resolve_us_states(normalized_category) or
        ""
    )

    logger.debug(f"<<green>> end resolved_translations_resolvers: {normalized_category=}, {resolved_label=}")
    return resolved_label


__all__ = [
    "resolved_translations_resolvers",
]
