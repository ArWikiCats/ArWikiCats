"""

Regex patterns for category label processing.

This module now re-exports from the centralized regex_hub for backward compatibility.
The actual patterns are defined in legacy_bots/legacy_utils/regex_hub.py.

"""

from .regex_hub import (
    YEARS_REGEX_AR,
    RE1_compile,
    RE2_compile,
    RE3_compile,
    RE33_compile,
    re_sub_year,
)

__all__ = [
    "YEARS_REGEX_AR",
    "RE1_compile",
    "RE2_compile",
    "RE3_compile",
    "re_sub_year",
    "RE33_compile",
]
