"""
Centralized regex patterns for legacy bots.

This module contains all pre-compiled regex patterns extracted from various
modules to provide a single source of truth for pattern matching.

All patterns are pre-compiled for performance.
"""

from __future__ import annotations

import re

# ============================================================================
# YEAR PATTERNS (from legacy_utils/reg_lines.py)
# ============================================================================

# Match categories starting with year (e.g., "1900 in sports")
RE1_compile = re.compile(r"^(\d+\-\d+|\d+\–\d+|\d+\−\d+|\d\d\d\d).*", re.I)

# Match categories ending with year (e.g., "events in 1900")
RE2_compile = re.compile(r"^.*?\s*(\d+\-\d+|\d+\–\d+|\d+\−\d+|\d\d\d\d)$", re.I)

# Match categories with year in parentheses at end (e.g., "events (1900)")
RE3_compile = re.compile(r"^.*?\s*\((\d+\-\d+|\d+\–\d+|\d+\–present|\d+\−\d+|\d\d\d\d)\)$", re.I)

# Match year at start with space after (e.g., "1900 season")
re_sub_year = r"^(\d+\-\d+|\d+\–\d+|\d+\−\d+|\d\d\d\d)\s.*$"

# Match categories with year in parentheses (e.g., "American Soccer League (1933–83)")
RE33_compile = re.compile(r"^.*?\s*(\((?:\d\d\d\d|\d+\-\d+|\d+\–\d+|\d+\–present|\d+\−\d+)\))$", re.I)


# ============================================================================
# GENERAL PATTERNS (from make_bots/reg_result.py)
# ============================================================================

# Match millennium or century suffixes
REGEX_SUB_MILLENNIUM_CENTURY = re.compile(r"[−–\-](millennium|century)", re.I)

# Match category prefix (case-insensitive)
REGEX_SUB_CATEGORY_LOWERCASE = re.compile(r"category:", re.IGNORECASE)


# ============================================================================
# WITH_YEARS_BOT PATTERNS (from legacy_resolvers_bots/with_years_bot.py)
# ============================================================================

# Compiled version of re_sub_year pattern
REGEX_SUB_YEAR = re.compile(re_sub_year, re.IGNORECASE)


# ============================================================================
# BYS PATTERNS (from legacy_resolvers_bots/bys.py)
# ============================================================================

# Match "by X and Y" patterns
DUAL_BY_PATTERN = re.compile(r"^by (.*?) and (.*?)$", flags=re.IGNORECASE)

# Match "X by Y" patterns
BY_MATCH_PATTERN = re.compile(r"^(.*?) (by .*)$", flags=re.IGNORECASE)

# Match "X and Y" patterns
AND_PATTERN = re.compile(r"^(.*?) and (.*)$", flags=re.IGNORECASE)


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
