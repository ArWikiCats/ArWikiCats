"""
Text fixing utilities for the ArWikiCats project.

This module now re-exports from the core module for backward compatibility.
The actual implementation is in legacy_bots/core/base_resolver.py.
"""

from ..core.base_resolver import fix_minor

__all__ = [
    "fix_minor",
]
