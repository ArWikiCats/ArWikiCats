"""
Category filtering logic for English Wikipedia categories.
This module defines blacklists and prefixes to identify categories that should
not be processed or translated.
"""

import logging
import re

logger = logging.getLogger(__name__)

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


def is_category_allowed(category_name: str) -> bool:
    """Return ``True`` when the English category is allowed for processing."""
    normalized_category = category_name.lower()
    for blocked_fragment in CATEGORY_BLACKLIST:
        if blocked_fragment.lower() in normalized_category:
            logger.info(f"<<lightred>> find ({blocked_fragment}) in category_name")
            return False

    normalized_category = normalized_category.replace("category:", "")
    for blocked_prefix in CATEGORY_PREFIX_BLACKLIST:
        if normalized_category.startswith(blocked_prefix.lower()):
            logger.info(f"<<lightred>> category_name.startswith({blocked_prefix})")
            return False

    for month_name in MONTH_NAMES:
        # match the end of category_name like month \d+
        matt = rf"^.*? from {month_name.lower()} \d+$"
        if re.match(matt, normalized_category):
            logger.info(f"<<lightred>> category_name.match({matt})")
            return False

    return True
