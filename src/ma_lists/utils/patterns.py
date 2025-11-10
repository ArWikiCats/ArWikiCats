
import re


def load_keys_to_pattern(data_List):
    data_List_sorted = sorted(data_List, key=lambda x: -x.count(" "))
    # ---
    # data_pattern = r'\b(' + '|'.join([n.lower() for n in data_List_sorted]) + r')\b'
    data_pattern = r'\b(' + '|'.join(map(re.escape, [n.lower() for n in data_List_sorted])) + r')\b'
    # ---
    data_pattern = data_pattern.replace(r"\ ", " ").replace(r"\\ ", " ")
    return data_pattern
