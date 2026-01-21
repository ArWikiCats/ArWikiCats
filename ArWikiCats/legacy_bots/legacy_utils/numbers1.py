#!/usr/bin/python3


"""
Number translations for the ArWikiCats project.

This module now re-exports from the centralized data_store for backward compatibility.
The actual data is defined in legacy_bots/data_store/mappings.py.
"""

from ..data_store import change_numb, change_numb_to_word

__all__ = [
    "change_numb",
    "change_numb_to_word",
]
