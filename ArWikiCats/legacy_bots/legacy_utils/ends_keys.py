"""Suffix mappings for category label generation.

This module now re-exports from the centralized data_store for backward compatibility.
The actual data is defined in legacy_bots/data_store/mappings.py.
"""

from ..data_store import combined_suffix_mappings, pp_ends_with, pp_ends_with_pase

__all__ = [
    "combined_suffix_mappings",
    "pp_ends_with",
    "pp_ends_with_pase",
]
