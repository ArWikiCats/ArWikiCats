""" """

import functools
import logging

from . import peoples_resolver

logger = logging.getLogger(__name__)


@functools.lru_cache(maxsize=10000)
def main_other_resolvers(category: str) -> str:
    """
    Determine the resolved label for a category.

    Parameters:
        category (str): Category identifier to resolve.

    Returns:
        result (str): The label resolved for the given category.
    """
    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> {category=}")

    result = peoples_resolver.work_peoples(category)

    logger.log(20 if result else 10, f"<<yellow>> end {category=}, {result=}")
    return result
