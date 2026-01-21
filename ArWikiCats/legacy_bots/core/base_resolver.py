"""
Core shared resolver functions for legacy bots.

This module provides a centralized import point for frequently used resolver
functions that are shared across multiple legacy bot modules. By importing
from this central location instead of directly from individual modules, we
reduce coupling and prevent potential circular import issues.

Functions re-exported here:
- Get_country2: Resolves Arabic labels for country names (from shared_resolvers)
- get_KAKO: Looks up Arabic labels using multiple mapping tables
- find_lab: Finds labels for categories using multiple data sources
- get_lab_for_country2: Retrieves Arabic labels for countries from various resolvers
"""

from __future__ import annotations

# Import from their original locations
from ..common_resolver_chain import get_lab_for_country2
from ..legacy_resolvers_bots.general_resolver import find_lab
from ..make_bots.table1_bot import get_KAKO
from .shared_resolvers import Get_country2

__all__ = [
    "Get_country2",
    "get_KAKO",
    "find_lab",
    "get_lab_for_country2",
]
