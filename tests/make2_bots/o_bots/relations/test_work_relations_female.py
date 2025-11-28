# tests/relations/test_work_relations_female.py
from __future__ import annotations

import pytest

# Adjust this import according to your package layout
from ArWikiCats.make_bots.o_bots.rele import work_relations


def _norm(text: str) -> str:
    """Normalize whitespace for robust assertions."""
    return " ".join(text.strip().split())


@pytest.mark.unit
def test_burma_cambodia_relations_from_country_table():
    """Female 'relations' using all_country_with_nat_keys_is_en women demonyms."""
    value = "burma-cambodia relations"
    result = work_relations(value)
    assert _norm(result) == "العلاقات البورمية الكمبودية"


@pytest.mark.unit
def test_burundi_canada_military_relations():
    """Female 'military relations' with two countries from country table."""
    value = "burundi-canada military relations"
    result = work_relations(value)
    # بوروندية + كندية
    assert _norm(result) == "العلاقات البوروندية الكندية العسكرية"


@pytest.mark.unit
def test_nat_women_fallback_for_singapore_luxembourg():
    """Female 'relations' using Nat_women fallback (no entry in main country table)."""
    value = "singapore-luxembourg relations"
    result = work_relations(value)
    # سنغافورية + لوكسمبورغية
    assert _norm(result) == "العلاقات السنغافورية اللوكسمبورغية"


@pytest.mark.unit
def test_dash_variants_en_dash():
    """Relations using en dash instead of hyphen."""
    value = "burma–cambodia relations"
    result = work_relations(value)
    assert _norm(result) == "العلاقات البورمية الكمبودية"


@pytest.mark.unit
def test_dash_variants_minus_sign():
    """Relations using minus sign instead of hyphen."""
    value = "burma−cambodia relations"
    result = work_relations(value)
    assert _norm(result) == "العلاقات البورمية الكمبودية"


def test_nato_relations_special_case():
    """Special-case NATO handling for plain 'relations'."""
    value = "nato-afghanistan relations"
    result = work_relations(value)
    # Uses hard-coded "الناتو" plus country label
    assert _norm(result) == "علاقات أفغانستان والناتو"


@pytest.mark.unit
def test_female_suffix_not_matched_returns_empty():
    """No recognized female or male suffix should return empty string."""
    value = "burma-cambodia partnership"
    result = work_relations(value)
    assert result == ""
