import re


def load_keys_to_pattern_new(data_List: list[str], by: str = "|", sort_keys: bool = True) -> str:
    """Join escaped keys into a pattern string, optionally sorting by token count."""
    # return by.join(x.strip() for x in data_List)

    data_List_sorted = sorted(
        data_List,
        # key=lambda x: -x.count(" ")
        key=lambda k: (-k[0].count(" "), -len(k[0])),
    ) if sort_keys else data_List

    data_pattern = by.join(map(re.escape, [n.lower() for n in data_List_sorted]))
    return data_pattern
