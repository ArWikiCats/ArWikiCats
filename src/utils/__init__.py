#
from .match_relation_word import get_relation_word
from .check_it import (
    check_key_in_tables,
    check_key_in_tables_return_tuple,
    get_value_from_any_table,
)

__all__ = [
    "check_key_in_tables",
    "get_value_from_any_table",
    "check_key_in_tables_return_tuple",
    "get_relation_word",
]
