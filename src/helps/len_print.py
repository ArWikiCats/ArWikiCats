#!/usr/bin/python3
"""
!
"""
import sys
import json
from typing import Any, List, Union, Mapping
from humanize import naturalsize
from pathlib import Path

all_len = {}


def format_size(key: str, value: int | float, lens: List[Union[str, Any]]) -> str:
    if key in lens:
        return value
    return naturalsize(value, binary=True)


def save_data(bot, tab):
    bot_path = Path("D:/categories_bot/len_data") / bot
    bot_path.mkdir(parents=True, exist_ok=True)

    for name, data in tab.items():
        if isinstance(data, dict) or isinstance(data, list):
            # sort data by key
            # ---
            # if isinstance(data, dict):
            #     data = dict(sorted(data.items(), key=lambda item: item[0].lower()))
            # elif isinstance(data, list):
            #     data = sorted(data)
            # ---
            with open(bot_path / f"{name}.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)


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

    save_data(bot, tab)

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
    for _, v in all_len.items():
        for var, tab in v.items():
            all_len_save["by_count"].setdefault(var, tab["count"])

    sorted_items = sorted(all_len_save["by_count"].items(), key=lambda item: item[1], reverse=True)
    all_len_save["by_count"] = {k: f"{v:,}" for k, v in sorted_items}

    with open(file, "w", encoding="utf-8") as f:
        json.dump(all_len_save, f, ensure_ascii=False, indent=4)
