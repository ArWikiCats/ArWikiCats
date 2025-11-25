#!/usr/bin/python3
"""
Usage:
"""

import functools
from typing import Dict

from ...helps import len_print
from .teams_new_data import load_teams_new


@functools.lru_cache(maxsize=1)
def lazy_load() -> Dict[str, str]:
    """Load and cache the 2025 teams dataset."""
    return load_teams_new()


@functools.lru_cache(maxsize=None)
def teams_new_founder(key: str, default: str = "") -> str:
    """Look up a team label from the cached 2025 dataset."""
    data = lazy_load()
    return data.get(key, default)


__all__ = ["teams_new_founder"]
