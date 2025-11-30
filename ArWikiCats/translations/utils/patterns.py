import re
from typing import LiteralString


def load_keys_to_pattern(data_List) -> LiteralString:
    """
    Build a regex pattern matching any entry from ``data_List`` case-insensitively.
    """
    data_List_sorted = sorted(data_List, key=lambda x: -x.count(" "))
    alternation = "|".join(map(re.escape, [n.lower() for n in data_List_sorted]))

    # TODO: Use data_pattern_new to avoid matching partial words.
    # data_pattern_new = fr"(?<!\w)({alternation})(?!\w)"
    data_pattern = r"\b(" + alternation + r")\b"

    return data_pattern


def load_keys_to_pattern_new(data_List: list[str], by: str = "|", sort_keys: bool = True) -> str:
    """Join escaped keys into a pattern string, optionally sorting by token count."""
    # return by.join(x.strip() for x in data_List)
    data_List_sorted = sorted(data_List, key=lambda x: -x.count(" ")) if sort_keys else data_List
    data_pattern = by.join(map(re.escape, [n.lower() for n in data_List_sorted]))
    return data_pattern
