"""
Core module for legacy bots.
Contains shared resolver functions and base logic.
"""

from __future__ import annotations

from .base_resolver import Get_country2, find_lab, get_KAKO, get_lab_for_country2

__all__ = [
    "Get_country2",
    "get_KAKO",
    "find_lab",
    "get_lab_for_country2",
]
