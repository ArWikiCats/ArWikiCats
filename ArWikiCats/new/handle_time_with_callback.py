"""
Utility for handling time components in categories using callbacks.
This module provides functions to extract time components (like years)
from the beginning of a category string and process the remainder
using a provided callback function.
"""

import functools
import re
from typing import Callable, Optional

from ..helps import getLogger
from ..time_formats.time_to_arabic import convert_time_to_arabic, match_time_en_first

logger = getLogger(__name__)


def fix_keys(category: str) -> str:
    """
    Normalize a category key for language processing.

    Parameters:
        category (str): Raw category string that may include the prefix "category:", single quotes, or the substring "-language ".

    Returns:
        str: Normalized category string in lowercase with the "category:" prefix and single quotes removed, and "-language " replaced by " language ".
    """
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
