"""
Utility functions for the ArWikiCats project.
This package contains helper functions for fixing text, checking table entries,
and matching relationship words.
"""

#
from .check_it import (
    check_key_in_tables,
    check_key_in_tables_return_tuple,
    get_value_from_any_table,
)
from .match_relation_word import get_relation_word

__all__ = [
    "check_key_in_tables",
    "get_value_from_any_table",
    "check_key_in_tables_return_tuple",
    "get_relation_word",
]
