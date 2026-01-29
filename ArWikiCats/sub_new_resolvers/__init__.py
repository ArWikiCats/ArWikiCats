""" """

import functools

from ..helps import getLogger

logger = getLogger(__name__)
from . import peoples_resolver


@functools.lru_cache(maxsize=10000)
def main_other_resolvers(category: str) -> str:
    """
    Determine the resolved label for a category.

    Parameters:
        category (str): Category identifier to resolve.

    Returns:
        resolved_label (str): The label resolved for the given category.
    """
    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> Trying main_other_resolvers for: {category=}")

    resolved_label = peoples_resolver.work_peoples(category)

    logger.info_if_or_debug(f"<<yellow>> end main_other_resolvers: {category=}, {resolved_label=}", resolved_label)
    return resolved_label
