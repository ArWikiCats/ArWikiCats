"""
Utility for checking keys in various data tables.
This module provides functions to verify if a key exists in one or more
lookup tables and retrieve its associated value.
"""


def check_key_in_tables(key: str, tables: list[dict[str, str] | list[str] | set[str]]) -> bool:
    """Return True if ``key`` exists in any container within ``tables``."""
    for table in tables:
        if key in table or key.lower() in table:
            return True
    return False


def check_key_in_tables_return_tuple(key: str, tables: dict[str, dict[str, str] | set[str]]) -> tuple[bool, str]:
    """Return presence flag and table name when ``key`` is found."""
    for name, table in tables.items():
        if key in table or key.lower() in table:
            return True, name
    return False, ""


def get_value_from_any_table(key: str, tables: list[dict[str, str]]) -> str:
    """Return the value for ``key`` from the first mapping that contains it."""
    for table in tables:
        if key in table or key.lower() in table:
            return table[key]
    return ""


__all__ = [
    "check_key_in_tables",
    "check_key_in_tables_return_tuple",
    "get_value_from_any_table",
]
