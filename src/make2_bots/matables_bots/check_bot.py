#!/usr/bin/python3
"""

from ..matables_bots.check_bot import check_key_new_players
check_key_new_players(key)
"""

from ...translations import Jobs_new, jobs_mens_data
from ...utils import check_key_in_tables
from .bot import players_new_keys

set_tables = [players_new_keys, Jobs_new, jobs_mens_data]


def check_key_new_players_n(key: str) -> bool:
    """Return True if the key exists in any player or job mapping table."""
    return check_key_in_tables(key, set_tables) or check_key_in_tables(key.lower(), set_tables)


def check_key_new_players(key: str) -> bool:
    """Return True if the key exists in any player or job mapping table."""
    return any(key in table for table in set_tables) or any(key.lower() in table for table in set_tables)
