import functools

from ...helps import logger
from .film_keys_bot import get_Films_key_CAO, resolve_films
from .resolve_films_labels import get_films_key_tyty_new
from .resolve_films_labels_and_time import get_films_key_tyty_new_and_time


@functools.lru_cache(maxsize=None)
def resolve_nationalities_main(normalized_category) -> str:
    normalized_category = normalized_category.strip().lower().replace("category:", "")

    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> Trying nationalities_resolvers resolvers for: {normalized_category=}")

    resolved_label = (
        get_films_key_tyty_new_and_time(normalized_category)
        or get_Films_key_CAO(normalized_category)
        or get_films_key_tyty_new(normalized_category)
        or resolve_films(normalized_category)
        or ""
    )

    logger.debug(f"<<green>> end nationalities_resolvers: {normalized_category=}, {resolved_label=}")
    return resolved_label


__all__ = [
    "resolve_nationalities_main",
    "get_films_key_tyty_new",
    "get_films_key_tyty_new_and_time",
]
