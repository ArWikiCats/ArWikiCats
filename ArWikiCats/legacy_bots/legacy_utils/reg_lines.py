"""

Group of regex expressions used in the bot for later improvements

DEPRECATED: This module re-exports from ..utils.regex_hub for backward compatibility.
New code should import directly from ArWikiCats.legacy_bots.utils.regex_hub.
"""

# Re-export from centralized regex module
from ..utils.regex_hub import (
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
