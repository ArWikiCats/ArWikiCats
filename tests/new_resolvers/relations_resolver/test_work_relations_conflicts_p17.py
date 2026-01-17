from __future__ import annotations

import pytest

from ArWikiCats.new_resolvers.relations_resolver import main_relations_resolvers


@pytest.mark.unit
def test_basic_conflict_uses_p17_prefixes_with_countries_from_all_country_ar() -> None:
    """Plain 'conflict' using all_country_ar and P17_PREFIXES."""
    value = "east germany-west germany conflict"
    result = main_relations_resolvers(value)
    # ألمانيا الشرقية + ألمانيا الغربية
    # assert result == "صراع ألمانيا الشرقية وألمانيا الغربية"
    assert result == "الصراع الألماني الشرقي الألماني الغربي"


@pytest.mark.unit
def test_proxy_conflict_uses_p17_proxy_pattern() -> None:
    """'proxy conflict' formatting with two countries."""
    value = "afghanistan-africa proxy conflict"
    result = main_relations_resolvers(value)
    # أفغانستان + إفريقيا
    assert result == "صراع أفغانستان وإفريقيا بالوكالة"


@pytest.mark.unit
def test_conflict_with_en_dash_separator() -> None:
    """Conflict branch with en dash instead of hyphen."""
    value = "east germany–west germany conflict"
    result = main_relations_resolvers(value)
    # assert result == "صراع ألمانيا الشرقية وألمانيا الغربية"
    assert result == "الصراع الألماني الشرقي الألماني الغربي"


@pytest.mark.unit
def test_conflict_with_minus_sign_separator() -> None:
    """Conflict branch with minus sign instead of hyphen."""
    value = "east germany−west germany conflict"
    result = main_relations_resolvers(value)
    # assert result == "صراع ألمانيا الشرقية وألمانيا الغربية"
    assert result == "الصراع الألماني الشرقي الألماني الغربي"


@pytest.mark.unit
def test_p17_prefix_not_matched_returns_empty() -> None:
    """Non-matching suffix should not be handled by P17_PREFIXES."""
    value = "east germany-west germany relationship"
    result = main_relations_resolvers(value)
    assert result == ""


@pytest.mark.unit
def test_p17_with_unknown_country_returns_empty() -> None:
    """Unknown country key in all_country_ar should result in empty label."""
    value = "unknownland-west germany conflict"
    result = main_relations_resolvers(value)
    assert result == ""
