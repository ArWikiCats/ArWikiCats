import functools

from ...helps import logger
from .countries_names_double_v2 import resolve_countries_names_double
from .nationalities_double_v2 import resolve_by_nats_double_v2


@functools.lru_cache(maxsize=None)
def main_relations_resolvers(category: str) -> str:
    """Main entry point for relation resolvers.

    Orchestrates the resolution of relationship-based category names by attempting
    to match against nationality and country name resolvers in sequence.

    Args:
        category (str): The category string to be resolved.

    Returns:
        str: The resolved Arabic category label, or an empty string if no match is found.
    """
    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> Trying main_relations_resolvers for: {category=}")

    resolved_label = resolve_by_nats_double_v2(category) or resolve_countries_names_double(category)

    logger.info_if_or_debug(f"<<yellow>> end main_relations_resolvers: {category=}, {resolved_label=}", resolved_label)
    return resolved_label
