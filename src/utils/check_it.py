
from typing import List, Dict, Set


def check_key_in_tables(key: str, tables: List[Dict[str, str] | List[str] | Set[str]]) -> bool:
    for table in tables:
        if key in table:
            return True
    return False


def check_key_in_tables_return_tuple(key: str, tables: Dict[str, Dict[str, str] | Set[str]]) -> bool:
    for name, table in tables.items():
        if key in table:
            return True, name
    return False, ""


def get_value_from_any_table(key: str, tables: List[Dict[str, str]]) -> str:
    for table in tables:
        if key in table:
            return table[key]
    return ""
