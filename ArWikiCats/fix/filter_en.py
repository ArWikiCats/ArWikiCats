"""
Category filtering logic for English Wikipedia categories.
This module defines blacklists and prefixes to identify categories that should
not be processed or translated.
"""

import re

from ..helps import getLogger

logger = getLogger(__name__)

CATEGORY_BLACKLIST: list[str] = [
    "Disambiguation",
    "wikiproject",
    "sockpuppets",
    "without a source",
    "images for deletion",
]
# ---
CATEGORY_PREFIX_BLACKLIST: list[str] = [
    "Clean-up",
    "Cleanup",
    "Uncategorized",
    "Unreferenced",
    "Unverifiable",
    "Unverified",
    "Wikipedia",
    "Wikipedia articles",
    "Articles about",
    "Articles containing",
    "Articles covered",
    "Articles lacking",
    "Articles needing",
    "Articles prone",
    "Articles requiring",
    "Articles slanted",
    "Articles sourced",
    "Articles tagged",
    "Articles that",
    "Articles to",
    "Articles with",
    "use ",
    "User pages",
    "Userspace",
]

MONTH_NAMES = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def filter_cat(cat: str) -> bool:
    """Return ``True`` when the English category is allowed for processing."""
    normalized_category = cat.lower()
    for blocked_fragment in CATEGORY_BLACKLIST:
        if blocked_fragment in normalized_category:
            logger.info(f"<<lightred>> find ({blocked_fragment}) in cat")
            return False

    normalized_category = normalized_category.replace("category:", "")
    for blocked_prefix in CATEGORY_PREFIX_BLACKLIST:
        if normalized_category.startswith(blocked_prefix.lower()):
            logger.info(f"<<lightred>> cat.startswith({blocked_prefix})")
            return False

    for month_name in MONTH_NAMES:
        # match the end of cat like month \d+
        matt = rf"^.*? from {month_name.lower()} \d+$"
        if re.match(matt, normalized_category):
            logger.info(f"<<lightred>> cat.match({matt})")
            return False

    return True
