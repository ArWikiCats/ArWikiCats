"""Suffix mappings for category label generation.

This module contains dictionaries for mapping English category suffixes
to Arabic equivalents for various types of categories.

DEPRECATED: This module re-exports from ..data.mappings for backward compatibility.
New code should import directly from ArWikiCats.legacy_bots.data.mappings.
"""

# Re-export from centralized data module
from ..data.mappings import combined_suffix_mappings, pp_ends_with, pp_ends_with_pase

__all__ = [
    "combined_suffix_mappings",
    "pp_ends_with",
    "pp_ends_with_pase",
]
