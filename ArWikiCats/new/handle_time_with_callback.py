#!/usr/bin/python3
"""
"""
import functools
import re
from typing import Callable, Optional

from ..helps import logger
from ..time_resolvers.time_to_arabic import convert_time_to_arabic, match_time_en_first


def fix_keys(category: str) -> str:
    category = category.lower().replace("category:", "").replace("'", "")
    category = category.replace("-language ", " language ")
    return category


@functools.lru_cache(maxsize=10000)
def handle_year_at_first(
    category: str,
    callback: Optional[Callable] = None,
    result_format: str = "{sub_result} في {arabic_time}",
) -> str:
    logger.debug(f"<<yellow>> start handle_year_at_first: {category=}")
    if not callback:
        return ""

    time_str = match_time_en_first(category)

    if not time_str:
        return callback(category)

    arabic_time = convert_time_to_arabic(time_str)

    if not arabic_time:
        return ""

    category_without_time = re.sub(re.escape(time_str), "", category).strip()
    sub_result = callback(category_without_time)

    if not sub_result:
        return ""

    # result = f"{sub_result} في {arabic_time}"
    result = result_format.format(sub_result=sub_result, arabic_time=arabic_time)

    logger.info_if_or_debug(f"<<yellow>> end handle_year_at_first: {category=}, {result=}", result)
    return result


__all__ = [
    "handle_year_at_first",
]
