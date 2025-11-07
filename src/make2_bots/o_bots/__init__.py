"""Public interface for the :mod:`make2_bots.o_bots` package."""

from .army import test_Army, test_army
from .bys import Get_and_label, Get_by_label, Make_By_lab, get_and_label, get_by_label, make_by_label
from .ethnic_bot import Ethnic, Ethnic_culture, ethnic, ethnic_culture
from .fax import Get_Teams_new, get_teams_new, test_Lang, test_language
from .parties_bot import get_parties_lab
from .popl import Work_peoples, make_people_lab, work_peoples
from .rele import Work_relations, work_relations
from .univer import test_Universities, test_universities

__all__ = [
    "Ethnic",
    "Ethnic_culture",
    "Get_Teams_new",
    "Get_and_label",
    "Get_by_label",
    "Make_By_lab",
    "Work_peoples",
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
