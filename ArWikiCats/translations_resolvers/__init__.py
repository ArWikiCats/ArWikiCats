
from . import countries_names, us_states
from ..helps import logger


def resolved_translations_resolvers(normalized_category) -> str:

    normalized_category = normalized_category.lower().replace("category:", " ")
    logger.debug(f"<><><><><><> Trying v1 resolvers for: {normalized_category=}")

    resolved_label = (
        countries_names.resolve_by_countries_names(normalized_category) or
        us_states.resolve_us_states(normalized_category) or
        ""
    )

    return resolved_label


__all__ = [
    "resolved_translations_resolvers",
]
