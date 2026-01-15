import functools

from ...helps import logger
from .countries_names_double_v2 import resolve_countries_names_double
from .nationalities_double_v2 import resolve_by_nats_double_v2


@functools.lru_cache(maxsize=None)
def new_relations_resolvers(category: str) -> str:
    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> Trying new_relations_resolvers for: {category=}")

    resolved_label = resolve_by_nats_double_v2(category) or resolve_countries_names_double(category)

    logger.info_if_or_debug(f"<<yellow>> end new_relations_resolvers: {category=}, {resolved_label=}", resolved_label)
    return resolved_label
