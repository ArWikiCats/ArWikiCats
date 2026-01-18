#!/usr/bin/python3
"""Bot for checking keys in player and job mapping tables.

This module provides functions to check if keys exist in various player and job
mapping tables, and to add new key-value pairs to these tables.

from ..matables_bots.check_bot import check_key_new_players
check_key_new_players(key)
"""

from ...helps import logger
from ...translations import Jobs_new, jobs_mens_data
from ...utils import check_key_in_tables
from .bot import players_new_keys

set_tables = [players_new_keys, Jobs_new, jobs_mens_data]


def check_key_new_players_n(key: str) -> bool:
    """Return True if the key exists in any player or job mapping table.

    Args:
        key: The key to check in the mapping tables

    Returns:
        True if the key exists in any table, False otherwise
    """
    return check_key_in_tables(key, set_tables) or check_key_in_tables(key.lower(), set_tables)


def check_key_new_players(key: str) -> bool:
    """Return True if the key exists in any player or job mapping table.

    Args:
        key: The key to check in the mapping tables

    Returns:
        True if the key exists in any table, False otherwise
    """
    key_lower = key.lower()
    result = any(key in table or key_lower in table for table in set_tables)
    logger.info(f"check_key_new_players [{key}] == {result}")
    return result


def add_key_new_players(key: str, value: str, file: str) -> None:
    """Add a new key-value pair to the players mapping table.

    Args:
        key: The key to add
        value: The value to associate with the key
        file: The file where the addition is happening (for logging)
    """
    players_new_keys[key.lower()] = value
    logger.info(f"add to New_players[{key}] = {value} in {file}")
