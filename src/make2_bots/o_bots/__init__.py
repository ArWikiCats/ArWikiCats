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

from importlib import import_module
from typing import Any, Dict

from . import fax as fax_module
from .army import test_Army, test_army
from .ethnic_bot import Ethnic, Ethnic_culture, ethnic, ethnic_culture
from .fax import Get_Teams_new, get_teams_new, test_Lang, test_language
from .parties_bot import get_parties_lab
from .popl import Work_peoples, make_people_lab, work_peoples
from .rele import Work_relations, work_relations
from .univer import test_Universities, test_universities

fax = fax_module

__all__ = [
    "Ethnic",
    "Ethnic_culture",
    "Get_Teams_new",
    "Get_and_label",
    "Get_by_label",
    "Make_By_lab",
    "make_By_lab",
    "Work_peoples",
    "fax",
    "get_and_label",
    "get_by_label",
    "get_parties_lab",
    "get_teams_new",
    "make_by_label",
    "make_people_lab",
    "test_Lang",
    "test_Universities",
    "test_army",
    "test_language",
    "test_universities",
    "test_Army",
    "work_peoples",
    "work_relations",
    "Work_relations",
    "ethnic",
    "ethnic_culture",
]

_BYS_EXPORTS: Dict[str, str] = {
    "Get_and_label": "Get_and_label",
    "Get_by_label": "Get_by_label",
    "Make_By_lab": "Make_By_lab",
    "get_and_label": "get_and_label",
    "get_by_label": "get_by_label",
    "make_by_label": "make_by_label",
    "make_By_lab": "make_By_lab",
}


def __getattr__(name: str) -> Any:
    """Dynamically import ``bys`` helpers on first access.

    Args:
        name: The attribute requested from the package.

    Returns:
        The resolved attribute from :mod:`make2_bots.o_bots.bys`.

    Raises:
        AttributeError: If ``name`` is not a recognised export.
    """

    if name in _BYS_EXPORTS:
        module = import_module(f"{__name__}.bys")
        attribute = getattr(module, _BYS_EXPORTS[name])
        globals()[name] = attribute
        return attribute

    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
