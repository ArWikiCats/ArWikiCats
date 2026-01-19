""" """

import functools

from ..helps import logger
from . import peoples_resolver


@functools.lru_cache(maxsize=None)
def main_other_resolvers(category: str) -> str:
    """ """
    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> Trying main_other_resolvers for: {category=}")

    resolved_label = peoples_resolver.work_peoples(category)

    logger.info_if_or_debug(f"<<yellow>> end main_other_resolvers: {category=}, {resolved_label=}", resolved_label)
    return resolved_label
