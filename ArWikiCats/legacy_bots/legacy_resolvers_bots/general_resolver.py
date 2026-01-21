#!/usr/bin/python3
"""
Arabic label translation for general categories.

This module provides functionality to translate English category names
into Arabic labels by applying various resolution strategies.

NOTE: The actual implementation has been moved to core/shared_resolvers.py
to break circular imports. This module re-exports for backward compatibility.
"""

from ..core.shared_resolvers import (
    find_lab,
    translate_general_category,
    work_separator_names,
)

__all__ = [
    "find_lab",
    "translate_general_category",
    "work_separator_names",
]
