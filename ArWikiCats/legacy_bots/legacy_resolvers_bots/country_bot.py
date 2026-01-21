"""
Country Label Bot Module (Legacy Wrapper)
"""

from __future__ import annotations

def Get_country2(country: str) -> str:
    from .. import _resolver
    return _resolver._get_country_2_logic(country)

def get_country(country: str, start_get_country2: bool = True) -> str:
    from .. import _resolver
    return _resolver._get_country_label(country, start_get_country2=start_get_country2)

def fetch_country_term_label(
    term_lower: str, separator: str, lab_type: str = "", start_get_country2: bool = True
) -> str:
    from .. import _resolver
    return _resolver._get_term_label_logic(term_lower, separator, lab_type, start_get_country2)

def event2_d2(category_r) -> str:
    from .. import _resolver
    return _resolver._resolve_country_event(category_r)

def check_historical_prefixes(country: str) -> str:
    from .. import _resolver
    return _resolver._check_historical_prefixes(country)

__all__ = [
    "fetch_country_term_label",
    "get_country",
]
