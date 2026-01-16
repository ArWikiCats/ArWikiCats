"""
Public interface for the :mod:`make_bots.o_bots` package.

"""

from __future__ import annotations

from .parties_bot import get_parties_lab
from .peoples_resolver import make_people_lab, work_peoples
from .univer import te_universities

__all__ = [
    "get_by_label",
    "get_parties_lab",
    "make_by_label",
    "make_people_lab",
    "te_universities",
    "work_peoples",
]
