"""
Year-based category label processing (Legacy Wrapper).
"""

from __future__ import annotations

def Try_With_Years(category: str) -> str:
    from .. import _resolver
    return _resolver._try_with_years_logic(category)

def wrap_try_with_years(category_r) -> str:
    from .. import _resolver
    return _resolver._resolve_with_years(category_r)

def handle_political_terms(category_text: str) -> str:
    from .. import _resolver
    return _resolver._handle_political_terms(category_text)
