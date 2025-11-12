#!/usr/bin/python3
"""

from ..matables_bots.check_bot import check_key_new_players
check_key_new_players(key)
"""
from ...utils import check_key_in_tables
from .bot import players_new_keys
from ...ma_lists import Jobs_new, jobs_mens_data

set_tables = [players_new_keys, Jobs_new, jobs_mens_data]


def check_key_new_players(key: str) -> bool:

    return check_key_in_tables(key, set_tables) or check_key_in_tables(key.lower(), set_tables)
