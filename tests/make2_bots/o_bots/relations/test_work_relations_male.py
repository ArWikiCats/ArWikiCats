# tests/relations/test_work_relations_male.py
from __future__ import annotations

import pytest

# Adjust this import according to your package layout
from src.make2_bots.o_bots.rele import work_relations


def _norm(text: str) -> str:
    """Normalize whitespace for robust assertions."""
    return " ".join(text.strip().split())


@pytest.mark.unit
def test_zanzibari_anguillan_conflict_from_nat_men():
    """Male 'conflict' using Nat_men demonyms."""
    value = "zanzibari-anguillan conflict"
    result = work_relations(value)
    # زنجباري + أنغويلاني
    assert _norm(result) == "الصراع الأنغويلاني الزنجباري"


@pytest.mark.unit
def test_prussian_afghan_conflict_video_games():
    """Male 'conflict video games' using Nat_men."""
    value = "prussian-afghan conflict video games"
    result = work_relations(value)
    # بروسي + أفغاني
    assert _norm(result) == "ألعاب فيديو الصراع الأفغاني البروسي"


@pytest.mark.unit
def test_football_rivalry_uses_correct_male_prefix_and_suffix():
    """Male 'football rivalry' formatting."""
    value = "zanzibari-anguillan football rivalry"
    result = work_relations(value)
    assert _norm(result) == "التنافس الأنغويلاني الزنجباري في كرة القدم"


@pytest.mark.unit
def test_male_branch_with_en_dash():
    """Male 'conflict' using en dash separator."""
    value = "zanzibari–anguillan conflict"
    result = work_relations(value)
    assert _norm(result) == "الصراع الأنغويلاني الزنجباري"


@pytest.mark.unit
def test_unknown_demonym_in_male_branch_returns_empty():
    """Unknown demonym in Nat_men should produce empty result."""
    value = "unknownland-anguillan conflict"
    result = work_relations(value)
    assert result == ""


@pytest.mark.unit
def test_male_suffix_without_hyphen_returns_empty():
    """No hyphen-like separator means the function cannot split the pair."""
    value = "zanzibari anguillan conflict"
    result = work_relations(value)
    assert result == ""
