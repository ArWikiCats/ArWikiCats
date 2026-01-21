#!/usr/bin/python3


"""
Number translations for the ArWikiCats project.
This module provides mappings for translating numeric values and ordinal numbers
into their Arabic word equivalents, including support for hundreds.

DEPRECATED: This module re-exports from ..data.mappings for backward compatibility.
New code should import directly from ArWikiCats.legacy_bots.data.mappings.
"""

# Re-export from centralized data module
from ..data.mappings import change_numb, change_numb_to_word

__all__ = ["change_numb", "change_numb_to_word"]
