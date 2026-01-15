import functools

from ...helps import logger
from .film_keys_bot import Films, get_Films_key_CAO
from .resolve_films_labels import get_films_key_tyty_new
from .resolve_films_labels_and_time import get_films_key_tyty_new_and_time


@functools.lru_cache(maxsize=None)
def resolve_nationalities_main(normalized_category) -> str:
    """
    Resolve a film nationalities label from a category string.

    Normalizes the input by trimming whitespace, converting to lowercase, and removing a leading "category:" prefix, then queries a sequence of film-label resolvers and returns the first non-empty result.

    Parameters:
        normalized_category (str): Category text to resolve; may include a leading "category:" prefix.

    Returns:
        str: The resolved label if any resolver finds a match, otherwise an empty string.
    """
    normalized_category = normalized_category.strip().lower().replace("category:", "")

    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> Trying nationalities_resolvers resolvers for: {normalized_category=}")

    resolved_label = (
        get_films_key_tyty_new_and_time(normalized_category)
        or get_Films_key_CAO(normalized_category)
        or get_films_key_tyty_new(normalized_category)
        or Films(normalized_category)
        or ""
    )

    logger.info_if_or_debug(
        f"<<yellow>> end nationalities_resolvers: {normalized_category=}, {resolved_label=}", resolved_label
    )
    return resolved_label


__all__ = [
    "resolve_nationalities_main",
    "get_films_key_tyty_new",
    "get_films_key_tyty_new_and_time",
]
