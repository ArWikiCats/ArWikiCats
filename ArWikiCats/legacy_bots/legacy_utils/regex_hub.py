"""
Centralized regex patterns for the legacy_bots module.

This module provides a single source of truth for all compiled regular expressions
used throughout the legacy_bots module, improving maintainability and avoiding
circular imports.
"""

import re

# =============================================================================
# Year-related patterns (from legacy_utils/reg_lines.py)
# =============================================================================

YEARS_REGEX_AR = r"\d+[−–\-]\d+" r"|(?:عقد|القرن|الألفية)*\s*\d+\s*(ق[\s\.]م|قبل الميلاد)*"

# Match year at start of string (e.g., "1900-2000 ..." or "1900...")
RE1_YEAR_AT_START = re.compile(r"^(\d+\-\d+|\d+\–\d+|\d+\−\d+|\d\d\d\d).*", re.I)

# Match year at end of string (e.g., "... 1900" or "... 1900-2000")
RE2_YEAR_AT_END = re.compile(r"^.*?\s*(\d+\-\d+|\d+\–\d+|\d+\−\d+|\d\d\d\d)$", re.I)

# Match year range in parentheses at end (e.g., "... (1900-2000)" or "... (1900)")
RE3_YEAR_IN_PARENS = re.compile(r"^.*?\s*\((\d+\-\d+|\d+\–\d+|\d+\–present|\d+\−\d+|\d\d\d\d)\)$", re.I)

# Match year range in parentheses including the parentheses themselves
RE33_YEAR_RANGE_IN_PARENS = re.compile(r"^.*?\s*(\((?:\d\d\d\d|\d+\-\d+|\d+\–\d+|\d+\–present|\d+\−\d+)\))$", re.I)

# Pattern for substituting year at start
RE_SUB_YEAR_PATTERN = r"^(\d+\-\d+|\d+\–\d+|\d+\−\d+|\d\d\d\d)\s.*$"
REGEX_SUB_YEAR = re.compile(RE_SUB_YEAR_PATTERN, re.IGNORECASE)

# =============================================================================
# "By" patterns (from legacy_resolvers_bots/bys.py)
# =============================================================================

# Match "by X and Y" patterns (e.g., "by country and year")
DUAL_BY_PATTERN = re.compile(r"^by (.*?) and (.*?)$", flags=re.IGNORECASE)

# Match "X by Y" patterns (e.g., "athletes by sport")
BY_MATCH_PATTERN = re.compile(r"^(.*?) (by .*)$", flags=re.IGNORECASE)

# Match "X and Y" patterns
AND_PATTERN = re.compile(r"^(.*?) and (.*)$", flags=re.IGNORECASE)

# =============================================================================
# Make bots patterns (from make_bots/reg_result.py)
# =============================================================================

# Substitute millennium/century with normalized dash
REGEX_SUB_MILLENNIUM_CENTURY = re.compile(r"[−–\-](millennium|century)", re.I)

# Case-insensitive match for "category:" prefix
REGEX_SUB_CATEGORY_LOWERCASE = re.compile(r"category:", re.IGNORECASE)

# =============================================================================
# Aliases for backward compatibility with original names
# =============================================================================

# These aliases maintain compatibility with existing imports
RE1_compile = RE1_YEAR_AT_START
RE2_compile = RE2_YEAR_AT_END
RE3_compile = RE3_YEAR_IN_PARENS
RE33_compile = RE33_YEAR_RANGE_IN_PARENS
re_sub_year = RE_SUB_YEAR_PATTERN


__all__ = [
    # New descriptive names
    "YEARS_REGEX_AR",
    "RE1_YEAR_AT_START",
    "RE2_YEAR_AT_END",
    "RE3_YEAR_IN_PARENS",
    "RE33_YEAR_RANGE_IN_PARENS",
    "RE_SUB_YEAR_PATTERN",
    "REGEX_SUB_YEAR",
    "DUAL_BY_PATTERN",
    "BY_MATCH_PATTERN",
    "AND_PATTERN",
    "REGEX_SUB_MILLENNIUM_CENTURY",
    "REGEX_SUB_CATEGORY_LOWERCASE",
    # Backward compatibility aliases
    "RE1_compile",
    "RE2_compile",
    "RE3_compile",
    "RE33_compile",
    "re_sub_year",
]
