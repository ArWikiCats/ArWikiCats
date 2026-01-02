# tests/relations/test_resolve_relations_label_male.py
from __future__ import annotations

import pytest

# Adjust this import according to your package layout
from ArWikiCats.make_bots.reslove_relations.rele import resolve_relations_label


def _norm(text: str) -> str:
    """Normalize whitespace for robust assertions."""
    return " ".join(text.split())


males_data = {}


@pytest.mark.parametrize("category, expected", males_data.items(), ids=males_data.keys())
@pytest.mark.fast
def test_males_data(category: str, expected: str) -> None:
    label = resolve_relations_label(category)
    assert label == expected


@pytest.mark.unit
def test_zanzibari_anguillan_conflict_from_nat_men() -> None:
    """Male 'conflict' using Nat_men demonyms."""
    value = "zanzibari-anguillan conflict"
    result = resolve_relations_label(value)
    # زنجباري + أنغويلاني
    assert _norm(result) == "الصراع الأنغويلاني الزنجباري"


@pytest.mark.unit
def test_prussian_afghan_conflict_video_games() -> None:
    """Male 'conflict video games' using Nat_men."""
    value = "prussian-afghan conflict video games"
    result = resolve_relations_label(value)
    # بروسي + أفغاني
    assert _norm(result) == "ألعاب فيديو الصراع الأفغاني البروسي"


@pytest.mark.unit
def test_football_rivalry_uses_correct_male_prefix_and_suffix() -> None:
    """Male 'football rivalry' formatting."""
    value = "zanzibari-anguillan football rivalry"
    result = resolve_relations_label(value)
    assert _norm(result) == "التنافس الأنغويلاني الزنجباري في كرة القدم"


@pytest.mark.unit
def test_male_branch_with_en_dash() -> None:
    """Male 'conflict' using en dash separator."""
    value = "zanzibari–anguillan conflict"
    result = resolve_relations_label(value)
    assert _norm(result) == "الصراع الأنغويلاني الزنجباري"


@pytest.mark.unit
def test_unknown_demonym_in_male_branch_returns_empty() -> None:
    """Unknown demonym in Nat_men should produce empty result."""
    value = "unknownland-anguillan conflict"
    result = resolve_relations_label(value)
    assert result == ""


@pytest.mark.unit
def test_male_suffix_without_hyphen_returns_empty() -> None:
    """No hyphen-like separator means the function cannot split the pair."""
    value = "zanzibari anguillan conflict"
    result = resolve_relations_label(value)
    assert result == ""
