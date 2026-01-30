#!/usr/bin/python3
"""
Separator-Based Resolver Module

This module provides functionality to translate English category names
into Arabic labels by applying separator-based resolution strategies.

It is extracted from the legacy circular_dependency package to break the import cycle.
This module imports from arabic_label_builder, which in turn imports from country_resolver.
This creates a proper DAG of imports with no cycles.
"""

from __future__ import annotations

import functools
import re

from ...format_bots.relation_mapping import translation_category_relations
import logging
from ...utils import get_relation_word
from .arabic_label_builder import find_ar_label

logger = logging.getLogger(__name__)

en_literes = "[a-z]"


@functools.lru_cache(maxsize=10000)
def work_separator_names(
    category: str,
) -> str:
    """Process categories that contain relational words (separator).

    This function extracts relational words from categories and uses them
    to find appropriate Arabic labels.

    Args:
        category: The category string to process

    Returns:
        The associated Arabic label if found, otherwise an empty string.
    """
    separator, separator_name = get_relation_word(category, translation_category_relations)

    if not separator:
        return ""

    logger.info(f'<<lightblue>>>>>> work_separator_names: separator:"{separator_name}":"{separator}" in category ')
    arlabel = find_ar_label(category, separator, cate_test=category)

    if not arlabel:
        return ""

    # Check if the result contains Arabic characters
    if re.sub(en_literes, "", arlabel, flags=re.IGNORECASE) != arlabel:
        arlabel = ""

    logger.info(f">>>> <<lightyellow>> {arlabel=}")

    return arlabel


__all__ = [
    "work_separator_names",
]
