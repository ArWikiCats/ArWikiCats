"""Normalization helpers for Arabic category labels."""

from __future__ import annotations

from .fixtitle import add_fee, fix_it, fixlab
from .mv_years import move_3, move_by_in, move_years, move_years_first

__all__ = [
    "add_fee",
    "fix_it",
    "fixlab",
    "move_3",
    "move_by_in",
    "move_years",
    "move_years_first",
]
