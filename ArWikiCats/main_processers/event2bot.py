#!/usr/bin/python3
"""
!
"""

import functools
import re
from ..helps.log import logger

from ..time_resolvers import with_years_bot
from ..ma_bots.country_bot import get_country

from ..ma_bots2.year_or_typeo.bot_lab import label_for_startwith_year_or_typeo
from ..make_bots.o_bots import univer

en_literes = "[abcdefghijklmnopqrstuvwxyz]"


def event2_d2(category_r) -> str:
    """
    Determine the category label based on the input string.
    """
    cat3 = category_r.lower()

    logger.info(f'<<lightred>>>>>> category33:"{cat3}" ')

    # TODO: THIS NEED REVIEW
    # Reject strings that contain common English prepositions
    blocked = ("in", "of", "from", "by", "at")
    if any(f" {word} " in cat3.lower() for word in blocked):
        return ""

    category_lab = ""
    if re.sub(r"^\d", "", cat3) == cat3:
        category_lab = get_country(cat3)
    else:
        category_lab = with_years_bot.Try_With_Years(cat3)
        if category_lab:
            category_lab = f"تصنيف:{category_lab}"

    return category_lab


@functools.lru_cache(maxsize=None)
def event2_new(category_r: str) -> str:
    """Process a category string and return a corresponding label.

    This function takes a category string as input, processes it to extract
    relevant information, and attempts to generate a label based on
    predefined patterns and rules. It utilizes regular expressions to
    identify various time periods, such as centuries and millennia, and
    uses @functools.lru_cache for performance optimization. If no label can be generated,
    it defaults to a fallback mechanism.

    Args:
        category_r (str): The category string to be processed.

    Returns:
        str: The generated label corresponding to the input category string, or an
            empty string if no label could be determined.
    """

    logger.info("<<lightblue>>>> vvvvvvvvvvvv event2 start vvvvvvvvvvvv ")
    logger.info(f'<<lightyellow>>>>>> event2_new :"{category_r}"')
    category_r = re.sub(r"category:", "", category_r, flags=re.IGNORECASE)

    ar_label = (
        univer.te_universities(category_r)
        or event2_d2(category_r)
        or label_for_startwith_year_or_typeo(category_r)
        or ""
    )
    if ar_label.startswith("تصنيف:"):
        ar_label = ar_label[len("تصنيف:") :]

    logger.info("<<lightblue>>>> ^^^^^^^^^ event2_new end 3 ^^^^^^^^^ ")

    return ar_label
