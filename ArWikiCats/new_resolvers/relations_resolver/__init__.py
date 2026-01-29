"""
Package for resolving categories with complex relational structures.
This package provides resolvers for categories that involve multiple
nationalities or country names in complex relationships.
"""

import functools

from ...helps import getLogger

logger = getLogger(__name__)
from .countries_names_double_v2 import resolve_countries_names_double
from .nationalities_double_v2 import resolve_by_nats_double_v2
from .nationalities_not_double import two_nationalities_but_not_double_resolver


@functools.lru_cache(maxsize=10000)
def main_relations_resolvers(category: str) -> str:
    """
    Resolve a relation-based category string to its Arabic label by trying nationality then country-name resolvers.

    Attempts nationality-based resolution first; if that yields no result, attempts country-name resolution.

    Parameters:
        category (str): Category text to resolve.

    Returns:
        str: The resolved Arabic category label if a match is found, otherwise an empty string.
    """
    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> Trying main_relations_resolvers for: {category=}")

    resolved_label = (
        ""
        or resolve_by_nats_double_v2(category)
        or resolve_countries_names_double(category)
        or two_nationalities_but_not_double_resolver(category)
    )

    logger.info_if_or_debug(f"<<yellow>> end main_relations_resolvers: {category=}, {resolved_label=}", resolved_label)
    return resolved_label
