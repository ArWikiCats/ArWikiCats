"""
Data module for legacy bots.
Contains centralized dictionaries and mapping tables.
"""

from __future__ import annotations

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
    "pp_ends_with_pase",
    "pp_ends_with",
    "combined_suffix_mappings",
    "pp_start_with",
    "typeTable_7",
]
