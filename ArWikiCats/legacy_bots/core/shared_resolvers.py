"""
Shared resolver functions to break circular imports.

This module contains resolver functions that were causing circular imports
between country_bot.py, ar_lab_bot.py, and general_resolver.py.
By centralizing them here, the circular import chain is broken.

The circular import chain was:
- ar_lab_bot -> country_bot -> general_resolver -> ar_lab_bot

Now the dependency is:
- shared_resolvers uses deferred imports for ar_lab_bot.find_ar_label (only at call time)
- country_bot -> shared_resolvers (no cycle)
- general_resolver -> re-exports from shared_resolvers (backward compat)
"""

from __future__ import annotations

import functools
import re

from ...fix import fixtitle
from ...format_bots.relation_mapping import translation_category_relations
from ...helps import logger
from ...sub_new_resolvers import university_resolver
from ...time_formats import time_to_arabic
from ...translations import Jobs_new, jobs_mens_data
from ...utils import get_relation_word, get_value_from_any_table
from ..legacy_resolvers_bots.bot_2018 import get_pop_All_18
from ..make_bots import Films_O_TT, players_new_keys

# ==============================================================================
# Functions moved from general_resolver.py
# ==============================================================================

en_literes = "[abcdefghijklmnopqrstuvwxyz]"


@functools.lru_cache(maxsize=10000)
def find_lab(category: str, category_r: str) -> str:
    """Find a label for the given category using multiple data sources.

    Args:
        category: The normalized category string to look up
        category_r: The original category string for logging

    Returns:
        The found Arabic label or empty string if not found
    """
    cate_low = category.lower()

    _lab = (
        ""
        or Films_O_TT.get(cate_low, "")
        or get_pop_All_18(cate_low, "")
        or get_value_from_any_table(cate_low, [players_new_keys, jobs_mens_data, Jobs_new])
        or time_to_arabic.convert_time_to_arabic(cate_low)
    )
    if _lab:
        logger.info(f'>>>> <<lightyellow>>test: cat "{category_r}", {_lab=}')
        logger.info(f'>>>> <<lightyellow>> cat:"{category_r}", {_lab=}')

    return _lab


@functools.lru_cache(maxsize=10000)
def work_separator_names(
    category: str,
    cate_test: str = "",
    start_get_country2: bool = False,
) -> str:
    """Process categories that contain relational words (separator).

    This function extracts relational words from categories and uses them
    to find appropriate Arabic labels.

    Args:
        category: The category string to process
        cate_test: Optional test category string
        start_get_country2: Whether to start country lookup

    Returns:
        The associated Arabic label if found, otherwise an empty string.
    """
    # Deferred import to break circular dependency at module load time
    # This is the correct pattern: find_ar_label is only needed at call time
    from ..legacy_resolvers_bots.ar_lab_bot import find_ar_label

    separator, separator_name = get_relation_word(category, translation_category_relations)

    if not separator:
        return ""

    logger.info(f'<<lightblue>>>>>> work_separator_names: separator:"{separator_name}":"{separator}" in category ')
    arlabel = find_ar_label(category, separator, cate_test=cate_test, start_get_country2=start_get_country2)

    if not arlabel:
        return ""

    # Check if the result contains Arabic characters
    if re.sub(en_literes, "", arlabel, flags=re.IGNORECASE) != arlabel:
        arlabel = ""

    logger.info(f">>>> <<lightyellow>> {arlabel=}")

    return arlabel


def _translate_general_category(category_r: str, category: str, start_get_country2: bool = True) -> str:
    """Translate an English category to Arabic label.

    This function processes a category string by normalizing the format
    and applying various strategies to find an appropriate Arabic label.

    Args:
        category_r: The input category string that needs to be processed
        start_get_country2: A flag indicating whether to retrieve country-related data.
            Defaults to True.

    Returns:
        The processed Arabic label associated with the input category.
    """
    cate_test = category.lower()

    arlabel = get_pop_All_18(category, "")

    if not arlabel:
        arlabel = find_lab(category, category_r)

    if not arlabel:
        arlabel = work_separator_names(category, cate_test, start_get_country2=start_get_country2)

    return arlabel


@functools.lru_cache(maxsize=10000)
def translate_general_category(category_r: str, start_get_country2: bool = True, fix_title: bool = True) -> str:
    """
    "Category:20th-century musicians by instrument from Northern Ireland": "تصنيف:موسيقيون في القرن 20 حسب الآلة من أيرلندا الشمالية",
    "Category:21st-century musicians by instrument from Northern Ireland": "تصنيف:موسيقيون في القرن 21 حسب الآلة من أيرلندا الشمالية",
    """
    category = category_r.replace("_", " ")
    category = re.sub(r"category:", "", category, flags=re.IGNORECASE)

    logger.info(f"<<lightyellow>>>> ^^^^^^^^^ translate_general_category start ^^^^^^^^^ ({category}) ")
    logger.debug(f"<<lightyellow>>>>>> {category_r=}, {start_get_country2=}, {fix_title=}")

    arlabel = _translate_general_category(category_r, category, start_get_country2)

    if arlabel and fix_title:
        arlabel = fixtitle.fixlabel(arlabel, en=category_r)
        logger.info(f'>>>>>> <<green>>test: cat "{category_r}", {arlabel=}')

    if arlabel:
        logger.debug(f"<<lightyellow>>>> translate_general_category {arlabel=}  ")

    logger.debug("<<lightyellow>>>> ^^^^^^^^^ translate_general_category end ^^^^^^^^^ ")

    return arlabel


# ==============================================================================
# Functions moved from ar_lab_bot.py
# ==============================================================================


@functools.lru_cache(maxsize=10000)
def wrap_event2(category: str, separator: str = "") -> str:
    """
    Attempt to resolve a category label by trying several resolver functions in order.

    This function was moved from ar_lab_bot.py to break circular imports.

    Parameters:
        category (str): The input category string to resolve.
        separator (str): Unused; kept for API compatibility.

    Returns:
        str: The first non-empty label returned by the resolvers, or an empty string if none match.
    """
    from ..legacy_resolvers_bots import country_bot, with_years_bot
    from ..legacy_resolvers_bots.year_or_typeo import label_for_startwith_year_or_typeo

    result = (
        university_resolver.resolve_university_category(category)
        or country_bot.event2_d2(category)
        or with_years_bot.wrap_try_with_years(category)
        or label_for_startwith_year_or_typeo(category)
        or ""
    )
    return result


__all__ = [
    "wrap_event2",
    "translate_general_category",
    "find_lab",
    "work_separator_names",
]
