#!/usr/bin/python3
"""
Utility for tracking and saving data size statistics.
This module provides functions to calculate the size and count of data structures
used by various bots and optionally save this data to JSON files.
"""

import json
import sys
from pathlib import Path
from typing import Any, List, Mapping, Union

from humanize import naturalsize

from ..config import app_settings
from ..helps.log import getLogger

logger = getLogger(__name__)

all_len = {}


def format_size(key: str, value: int | float, lens: List[Union[str, Any]]) -> str:
    """Format byte sizes unless the key should remain numeric."""
    if key in lens:
        return value
    return naturalsize(value, binary=True)


def save_data(bot: str, tab: Mapping) -> None:
    """Persist bot data to JSON files when a save path is configured."""
    if not app_settings.save_data_path:
        return

    bot_path = Path(app_settings.save_data_path) / bot
    try:
        bot_path.mkdir(parents=True, exist_ok=True)

        for name, data in tab.items():
            if not data:
                continue
            if isinstance(data, dict) or isinstance(data, list):
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
    tab: Mapping[str, int | float],
) -> None:
    """Collect and optionally save size statistics for the given bot data."""
    data = {
        x: {
            "count": len(v) if not isinstance(v, int) else v,
            "size": format_size(x, sys.getsizeof(v), {}),
        }
        for x, v in tab.items()
    }
    if app_settings.save_data_path:
        save_data(bot, tab)

    if not data:
        return

    all_len.setdefault(bot, {})
    all_len[bot].update(data)


def dump_all_len() -> dict[str, dict]:
    """Return aggregated counts and sizes for all processed bots."""
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

    return all_len_save
