
from typing import List, Dict


def check_key_in_tables(key: str, tables: List[Dict[str, str] | List[str]]) -> bool:
    for table in tables:
        if key in table:
            return True
    return False


def get_value_from_any_table(key: str, tables: List[Dict[str, str]]) -> str:
    for table in tables:
        if key in table:
            table[key]
    return ""
