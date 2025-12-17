# tests/relations/test_resolve_relations_label_conflicts_p17.py
from __future__ import annotations

import pytest

# Adjust this import according to your package layout
from ArWikiCats.make_bots.reslove_relations.rele import resolve_relations_label


def _norm(text: str) -> str:
    """Normalize whitespace for robust assertions."""
    return " ".join(text.split())


@pytest.mark.unit
def test_basic_conflict_uses_p17_prefixes_with_countries_from_all_country_ar() -> None:
    """Plain 'conflict' using all_country_ar and P17_PREFIXES."""
    value = "east germany-west germany conflict"
    result = resolve_relations_label(value)
    # ألمانيا الشرقية + ألمانيا الغربية
    # assert _norm(result) == "صراع ألمانيا الشرقية وألمانيا الغربية"
    assert _norm(result) == "الصراع الألماني الشرقي الألماني الغربي"


@pytest.mark.unit
def test_proxy_conflict_uses_p17_proxy_pattern() -> None:
    """'proxy conflict' formatting with two countries."""
    value = "afghanistan-africa proxy conflict"
    result = resolve_relations_label(value)
    # أفغانستان + إفريقيا
    assert _norm(result) == "صراع أفغانستان وإفريقيا بالوكالة"


@pytest.mark.unit
def test_conflict_with_en_dash_separator() -> None:
    """Conflict branch with en dash instead of hyphen."""
    value = "east germany–west germany conflict"
    result = resolve_relations_label(value)
    # assert _norm(result) == "صراع ألمانيا الشرقية وألمانيا الغربية"
    assert _norm(result) == "الصراع الألماني الشرقي الألماني الغربي"


@pytest.mark.unit
def test_conflict_with_minus_sign_separator() -> None:
    """Conflict branch with minus sign instead of hyphen."""
    value = "east germany−west germany conflict"
    result = resolve_relations_label(value)
    # assert _norm(result) == "صراع ألمانيا الشرقية وألمانيا الغربية"
    assert _norm(result) == "الصراع الألماني الشرقي الألماني الغربي"


@pytest.mark.unit
def test_p17_prefix_not_matched_returns_empty() -> None:
    """Non-matching suffix should not be handled by P17_PREFIXES."""
    value = "east germany-west germany relationship"
    result = resolve_relations_label(value)
    assert result == ""


@pytest.mark.unit
def test_p17_with_unknown_country_returns_empty() -> None:
    """Unknown country key in all_country_ar should result in empty label."""
    value = "unknownland-west germany conflict"
    result = resolve_relations_label(value)
    assert result == ""
