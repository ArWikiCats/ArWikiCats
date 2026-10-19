"""Make bots module for Arabic Wikipedia categories processing.

This package contains various utilities for processing and transforming
Wikipedia category names from English to Arabic.
"""

from .bot import Films_O_TT, add_to_films_o_tt, players_new_keys
from .check_bot import check_key_new_players
from .reg_result import get_cats, get_reg_result
from .table1_bot import get_kako

__all__ = [
    "check_key_new_players",
    "get_kako",
    "Films_O_TT",
    "players_new_keys",
    "add_to_films_o_tt",
    "get_cats",
    "get_reg_result",
]
