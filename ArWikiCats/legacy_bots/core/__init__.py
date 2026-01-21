"""
Core module for base resolver functions.

This module provides foundational functions for resolving category labels
that don't depend on other resolver bots, helping to break circular imports.
"""

from .base_resolver import fix_minor, get_cats
from .shared_resolvers import wrap_event2

__all__ = [
    "fix_minor",
    "get_cats",
    "wrap_event2",
]
