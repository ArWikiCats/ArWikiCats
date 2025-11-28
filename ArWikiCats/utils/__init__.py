#
from .check_it import (
    check_key_in_tables,
    check_key_in_tables_return_tuple,
    get_value_from_any_table,
)
from .fixing import fix_minor
from .match_relation_word import get_relation_word

__all__ = [
    "fix_minor",
    "check_key_in_tables",
    "get_value_from_any_table",
    "check_key_in_tables_return_tuple",
    "get_relation_word",
]
