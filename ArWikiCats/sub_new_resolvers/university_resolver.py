"""University labelling helpers (legacy wrapper)."""

from __future__ import annotations

def resolve_university_category(category: str) -> str:
    """
    Resolve a university-related category using the unified LegacyBotsResolver.
    """
    from ..legacy_bots import _resolver
    return _resolver._resolve_university(category)

__all__ = [
    "resolve_university_category",
]
