# tests/relations/test_work_relations_conflicts_p17.py
from __future__ import annotations

import pytest

# Adjust this import according to your package layout
from ArWikiCats.make_bots.o_bots.rele import work_relations


def _norm(text: str) -> str:
    """Normalize whitespace for robust assertions."""
    return " ".join(text.strip().split())


@pytest.mark.unit
def test_basic_conflict_uses_p17_prefixes_with_countries_from_all_country_ar():
    """Plain 'conflict' using all_country_ar and P17_PREFIXES."""
    value = "east germany-west germany conflict"
    result = work_relations(value)
    # ألمانيا الشرقية + ألمانيا الغربية
    # assert _norm(result) == "صراع ألمانيا الشرقية وألمانيا الغربية"
    assert _norm(result) == "الصراع الألماني الشرقي الألماني الغربي"


@pytest.mark.unit
def test_proxy_conflict_uses_p17_proxy_pattern():
    """'proxy conflict' formatting with two countries."""
    value = "afghanistan-africa proxy conflict"
    result = work_relations(value)
    # أفغانستان + إفريقيا
    assert _norm(result) == "صراع أفغانستان وإفريقيا بالوكالة"


@pytest.mark.unit
def test_conflict_with_en_dash_separator():
    """Conflict branch with en dash instead of hyphen."""
    value = "east germany–west germany conflict"
    result = work_relations(value)
    # assert _norm(result) == "صراع ألمانيا الشرقية وألمانيا الغربية"
    assert _norm(result) == "الصراع الألماني الشرقي الألماني الغربي"


@pytest.mark.unit
def test_conflict_with_minus_sign_separator():
    """Conflict branch with minus sign instead of hyphen."""
    value = "east germany−west germany conflict"
    result = work_relations(value)
    # assert _norm(result) == "صراع ألمانيا الشرقية وألمانيا الغربية"
    assert _norm(result) == "الصراع الألماني الشرقي الألماني الغربي"


@pytest.mark.unit
def test_p17_prefix_not_matched_returns_empty():
    """Non-matching suffix should not be handled by P17_PREFIXES."""
    value = "east germany-west germany relationship"
    result = work_relations(value)
    assert result == ""


@pytest.mark.unit
def test_p17_with_unknown_country_returns_empty():
    """Unknown country key in all_country_ar should result in empty label."""
    value = "unknownland-west germany conflict"
    result = work_relations(value)
    assert result == ""
