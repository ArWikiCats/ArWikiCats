#!/usr/bin/python3
"""Bot for checking keys in player and job mapping tables.

This module provides functions to check if keys exist in various player and job
mapping tables, and to add new key-value pairs to these tables.

from ..matables_bots.check_bot import check_key_new_players
check_key_new_players(key)
"""

import logging
from typing import Dict, List, Set

from ...translations import Jobs_new, jobs_mens_data
from .bot import players_new_keys

logger = logging.getLogger(__name__)

set_tables = [players_new_keys, Jobs_new, jobs_mens_data]


def check_key_in_tables(key: str, tables: List[Dict[str, str] | List[str] | Set[str]]) -> bool:
    """Return True if ``key`` exists in any container within ``tables``."""
    for table in tables:
        if key in table or key.lower() in table:
            return True
    return False


def check_key_new_players_n(key: str) -> bool:
    """Return True if the key exists in any player or job mapping table.

    Args:
        key: The key to check in the mapping tables

    Returns:
        True if the key exists in any table, False otherwise
    """
    return check_key_in_tables(key, set_tables) or check_key_in_tables(key.lower(), set_tables)


def check_key_new_players(key: str) -> bool:
    """
    Check whether a key exists in any player or job mapping table.

    Parameters:
        key (str): The key to look up; lookup is case-insensitive (the key is checked as provided and in lowercase).

    Returns:
        bool: True if the key is present in any table, False otherwise.
    """
    key_lower = key.lower()
    result = any(key in table or key_lower in table for table in set_tables)
    logger.info(f"check_key_new_players [{key}] == {result}")
    return result


def add_key_new_players(key: str, value: str, file: str) -> None:
    """
    Add a mapping from key to value in the players_new_keys table, storing the key in lowercase.

    Parameters:
        key (str): Key to add; will be normalized to lowercase before storage.
        value (str): Value to associate with the key.
        file (str): Context file name included in the informational log entry.
    """
    players_new_keys[key.lower()] = value
    logger.info(f"add to New_players[{key}] = {value} in {file}")
