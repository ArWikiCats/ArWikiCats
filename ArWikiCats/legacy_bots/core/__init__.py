"""
Core module for base resolver functions.

This module provides foundational functions for resolving category labels
that don't depend on other resolver bots, helping to break circular imports.

Note: shared_resolvers is NOT imported here to avoid circular imports.
Import it directly: from ..core.shared_resolvers import translate_general_category
"""

from .base_resolver import get_cats

__all__ = [
    "get_cats",
]
