
import re


def load_keys_to_pattern(data_List, by="|", sort_keys=True):
    # return by.join(x.strip() for x in data_List)
    # ---
    data_List_sorted = sorted(data_List, key=lambda x: -x.count(" ")) if sort_keys else data_List
    # ---
    data_pattern = by.join(map(re.escape, [n.lower() for n in data_List_sorted]))
    # ---
    return data_pattern
