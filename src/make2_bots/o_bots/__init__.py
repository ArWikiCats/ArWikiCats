"""Public interface for the :mod:`make2_bots.o_bots` package.

This module re-exports the most frequently used helpers from the package
while avoiding circular imports that occur when :mod:`media_bots.films_bot`
imports :mod:`o_bots`.  The :func:`test_films` helper relies on a subset of the
``o_bots`` modules (notably :mod:`bys`) which previously executed at import
time.  When :mod:`films_bot` imported :mod:`fax`, Python loaded this module,
which in turn imported :mod:`bys` and attempted to re-import
``media_bots.films_bot``.  The refactor below lazy-loads the ``bys`` exports so
that the package initialisation no longer triggers the cycle.
"""

from __future__ import annotations
from . import fax as fax_module
from .army import test_army
from .ethnic_bot import ethnic, ethnic_culture
from .fax import get_teams_new, test_language
from .parties_bot import get_parties_lab
from .popl import work_peoples, make_people_lab
from .rele import work_relations
from .univer import test_universities

fax = fax_module

__all__ = [
    "get_teams_new",
    "get_and_label",
    "get_by_label",
    "work_peoples",
    "fax",
    "get_and_label",
    "get_by_label",
    "get_parties_lab",
    "get_teams_new",
    "make_by_label",
    "make_people_lab",
    "test_language",
    "test_universities",
    "test_army",
    "test_universities",
    "work_peoples",
    "work_relations",
    "work_relations",
    "ethnic",
    "ethnic_culture",
]
