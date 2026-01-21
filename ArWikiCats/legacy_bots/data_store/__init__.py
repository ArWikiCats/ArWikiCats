"""
Data store module for centralized static mappings and dictionaries.

This module provides a single source of truth for all static data mappings
used in the legacy_bots module, helping to avoid circular imports and
improve maintainability.
"""

from .mappings import (
    change_numb,
    change_numb_to_word,
    combined_suffix_mappings,
    pp_ends_with,
    pp_ends_with_pase,
    pp_start_with,
    typeTable_7,
)

__all__ = [
    "change_numb",
    "change_numb_to_word",
    "combined_suffix_mappings",
    "pp_ends_with",
    "pp_ends_with_pase",
    "pp_start_with",
    "typeTable_7",
]
