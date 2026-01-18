"""
Time-related translation utilities for the ArWikiCats project.
This package provides functions for converting English time expressions
(years, decades, centuries) into their Arabic equivalents.
"""

from .time_to_arabic import (
    convert_time_to_arabic,
    match_time_en_first,
)
from .utils_time import standardize_time_phrases

__all__ = [
    "convert_time_to_arabic",
    "match_time_en_first",
    "standardize_time_phrases",
]
