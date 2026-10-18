"""
Utilities module for legacy bots.
Contains shared utility functions and regex patterns.
"""

from __future__ import annotations

from .regex_hub import (
    AND_PATTERN,
    BY_MATCH_PATTERN,
    DUAL_BY_PATTERN,
    REGEX_SUB_CATEGORY_LOWERCASE,
    REGEX_SUB_MILLENNIUM_CENTURY,
    REGEX_SUB_YEAR,
    RE1_compile,
    RE2_compile,
    RE3_compile,
    RE33_compile,
    re_sub_year,
)

__all__ = [
    # Year patterns
    "RE1_compile",
    "RE2_compile",
    "RE3_compile",
    "re_sub_year",
    "RE33_compile",
    # General patterns
    "REGEX_SUB_MILLENNIUM_CENTURY",
    "REGEX_SUB_CATEGORY_LOWERCASE",
    # With years patterns
    "REGEX_SUB_YEAR",
    # Bys patterns
    "DUAL_BY_PATTERN",
    "BY_MATCH_PATTERN",
    "AND_PATTERN",
]
