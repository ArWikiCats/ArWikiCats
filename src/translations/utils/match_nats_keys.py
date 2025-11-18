#!/usr/bin/python3
"""

"""
import re
from .patterns import load_keys_to_pattern
from ..nats.Nationality import all_country_with_nat_ar

pp = [[len(xy.split(" ")), xy] for xy in all_country_with_nat_ar]
pp.sort(reverse=True)
texts_new = "|".join([xy for _, xy in pp])
# ---
All_nat_to_ar = texts_new.replace("(", r"\(").replace(")", r"\)")
# ---
nat_reg_line = rf"\b({All_nat_to_ar})\b"
# ---
new_pattern = load_keys_to_pattern(all_country_with_nat_ar)

RE_KEYS_NEW = re.compile(new_pattern, re.I)
RE_KEYS_OLD = re.compile(nat_reg_line, re.I)


from pathlib import Path
from ...helps.jsonl_dump import save_data

# @functools.lru_cache(maxsize=None)


@save_data(Path(__file__).parent / "match_nat_key.jsonl", ["category"])
def match_nat_key(category: str):
    # ---
    match = RE_KEYS_NEW.search(f" {category} ")
    # ---
    if match:
        return match.group(1)
    # ---
    return ""


__all__ = [
    "match_nat_key",
]
