"""
Utility functions for gender-related category resolution.
This module provides functions to normalize and standardize gender-specific
terms in category keys before they are matched by resolvers.
"""

import functools
import re

REGEX_WOMENS = re.compile(r"\b(womens|women)\b", re.I)  # replaced by female
REGEX_MENS = re.compile(r"\b(mens|men)\b", re.I)  # replaced by male


@functools.lru_cache(maxsize=10000)
def fix_keys(category: str) -> str:
    category = category.lower().replace("category:", "")
    category = category.replace("'", "")

    replacements = {
        "expatriates": "expatriate",
        "canadian football": "canadian-football",
        "american football": "american-football",
    }

    for old, new in replacements.items():
        category = category.replace(old, new)

    category = REGEX_WOMENS.sub("female", category)
    category = REGEX_MENS.sub("male", category)

    return category.strip()
