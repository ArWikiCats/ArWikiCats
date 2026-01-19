"""
Public interface for the :mod:`make_bots.o_bots` package.

"""

from __future__ import annotations

from ...sub_new_resolvers.peoples_resolver import work_peoples
from .parties_resolver import get_parties_lab
from .university_resolver import resolve_university_category

__all__ = [
    "get_by_label",
    "get_parties_lab",
    "make_by_label",
    "resolve_university_category",
    "work_peoples",
]
