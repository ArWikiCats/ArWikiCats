#!/usr/bin/python3
"""
!
"""
import sys
import json
from typing import Any, List, Union, Mapping
from humanize import naturalsize

all_len = {}


def format_size(key: str, value: int | float, lens: List[Union[str, Any]]) -> str:
    if key in lens:
        return value
    return naturalsize(value, binary=True)


def data_len(
    bot: str,
    tab: Mapping[str, int | float],
) -> None:
    data = {
        x: {
            "count": len(v) if not isinstance(v, int) else v,
            "size": format_size(x, sys.getsizeof(v), {})
        }
        for x, v in tab.items()
    }

    if not data:
        return

    all_len.setdefault(bot, {})
    all_len[bot].update(data)


def dump_all_len(file):
    # sort all_len by keys ignore case
    all_len_save = {
        "by_count": {},
        "all": dict(sorted(all_len.items(), key=lambda item: item[0].lower())),
    }
    for x, v in all_len.items():
        for var, tab in v.items():
            all_len_save["by_count"].setdefault(var, tab["count"])

    all_len_save["by_count"] = dict(sorted(all_len_save["by_count"].items(), key=lambda item: item[1], reverse=True))

    with open(file, "w", encoding="utf-8") as f:
        json.dump(all_len_save, f, ensure_ascii=False, indent=4)
