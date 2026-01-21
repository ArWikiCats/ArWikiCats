"""Year prefix patterns and typo handling (Legacy Wrapper)."""

from __future__ import annotations

def get_country_label(country_lower: str, country_not_lower: str, cate3: str, compare_lab: str) -> str:
    from .. import _resolver
    return _resolver._get_country_label_for_typo(country_lower, country_not_lower, cate3, compare_lab)

def label_for_startwith_year_or_typeo(category_r: str) -> str:
    from .. import _resolver
    return _resolver._resolve_year_or_typo(category_r)
