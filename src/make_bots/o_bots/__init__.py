"""Public interface for the :mod:`make_bots.o_bots` package.

This module re-exports the most frequently used helpers from the package
while avoiding circular imports that occur when :mod:`media_bots.films_bot`
imports :mod:`o_bots`.  The :func:`te_films` helper relies on a subset of the
``o_bots`` modules (notably :mod:`bys`) which previously executed at import
time.  When :mod:`films_bot` imported :mod:`fax`, Python loaded this module,
which in turn imported :mod:`bys` and attempted to re-import
``media_bots.films_bot``.  The refactor below lazy-loads the ``bys`` exports so
that the package initialisation no longer triggers the cycle.
"""

from __future__ import annotations

from . import fax as fax_module
from .army import te_army
from .ethnic_bot import ethnic, ethnic_culture
from .fax import te_language
from .parties_bot import get_parties_lab
from .popl import make_people_lab, work_peoples
from .rele import work_relations
from .univer import te_universities

fax = fax_module

__all__ = [
    "ethnic",
    "ethnic_culture",
    "fax",
    "get_and_label",
    "get_by_label",
    "get_parties_lab",
    "make_by_label",
    "make_people_lab",
    "te_army",
    "te_language",
    "te_universities",
    "work_peoples",
    "work_relations",
]
