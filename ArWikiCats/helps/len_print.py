#!/usr/bin/python3
"""
Utility for tracking and saving data size statistics.
This module provides functions to calculate the size and count of data structures
used by various bots and optionally save this data to JSON files.
"""

import functools
import json
import os
import logging
import sys
from pathlib import Path
from typing import Any, List, Mapping, Union

from humanize import naturalsize

logger = logging.getLogger(__name__)

all_len = {}


@functools.lru_cache(maxsize=1)
def get_save_path() -> str:
    save_data_path = os.getenv("SAVE_DATA_PATH", "")
    return save_data_path


def format_size(key: str, value: int | float, lens: List[Union[str, Any]]) -> str:
    """Format byte sizes unless the key should remain numeric."""
    if key in lens:
        return value
    return naturalsize(value, binary=True)


def save_data(bot: str, tab: Mapping) -> None:
    """Persist bot data to JSON files when a save path is configured."""
    save_data_path = get_save_path()
    if not save_data_path:
        return

    bot_path = Path(save_data_path) / bot
    try:
        bot_path.mkdir(parents=True, exist_ok=True)

        for name, data in tab.items():
            if not data:
                continue
            if isinstance(data, dict | list):
                # sort data by key
                if isinstance(data, dict):
                    data = dict(sorted(data.items(), key=lambda item: item[0].lower()))
                elif isinstance(data, list):
                    data = sorted(set(data))
                with open(bot_path / f"{name}.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        logger.error(f"Error saving data to {bot_path}: {e}", exc_info=True)


def data_len(
    bot: str,
    tab: Mapping[str, Any],
) -> None:
    """Collect and optionally save size statistics for the given bot data.

    Supports both raw objects (dicts, lists) and pre-calculated lengths (integers).
    - For raw objects: calculates len() and sys.getsizeof() normally
    - For pre-calculated lengths (int/float): uses the value as count, size marked as 'N/A'
    """

    save_data_path = get_save_path()
    if not save_data_path:
        return

    data = {}
    for x, v in tab.items():
        if isinstance(v, (int, float)):
            # Pre-calculated length - use value directly as count
            data[x] = {
                "count": v,
                "size": "N/A",
                "raw_size": 0,
            }
        elif isinstance(v, (dict, list)):
            # Raw object - calculate len() and getsizeof() normally
            data[x] = {
                "count": len(v),
                "size": format_size(x, sys.getsizeof(v), {}),
                "raw_size": sys.getsizeof(v),
            }
        else:
            # Other types - try to get len() if possible
            try:
                data[x] = {
                    "count": len(v),
                    "size": format_size(x, sys.getsizeof(v), {}),
                    "raw_size": sys.getsizeof(v),
                }
            except (TypeError, AttributeError):
                data[x] = {
                    "count": 1,
                    "size": format_size(x, sys.getsizeof(v), {}),
                    "raw_size": sys.getsizeof(v),
                }

    save_data(bot, tab)

    if not data:
        return

    all_len.setdefault(bot, {})
    all_len[bot].update(data)


def dump_all_len() -> dict[str, dict]:
    """Return aggregated counts and sizes for all processed bots."""
    # sort all_len by keys ignore case
    all_len_save = {
        "by_size": {},
        "by_count": {},
        "all": dict(sorted(all_len.items(), key=lambda item: item[0].lower())),
    }
    for _, v in all_len.items():
        for var, tab in v.items():
            all_len_save["by_count"].setdefault(var, tab["count"])
            all_len_save["by_size"].setdefault(var, tab["raw_size"])

    sorted_items = sorted(all_len_save["by_count"].items(), key=lambda item: item[1], reverse=True)
    all_len_save["by_count"] = {k: f"{v:,}" for k, v in sorted_items}

    all_len_save["by_size"] = dict(sorted(all_len_save["by_size"].items(), key=lambda item: item[1], reverse=True))

    return all_len_save
