# tests/relations/test_resolve_relations_label_female.py
from __future__ import annotations

import pytest

# Adjust this import according to your package layout
from ArWikiCats.make_bots.reslove_relations.rele import resolve_relations_label


def _norm(text: str) -> str:
    """Normalize whitespace for robust assertions."""
    return " ".join(text.split())


test_data = {
    "ireland–spain military relations": "العلاقات الأيرلندية الإسبانية العسكرية",
    "ireland–united kingdom military relations": "العلاقات الأيرلندية البريطانية العسكرية",
    "iran–iraq war films": "أفلام الحرب الإيرانية العراقية",
    "mexican–american war films": "أفلام الحرب الأمريكية المكسيكية",
    "soviet–afghan war films": "أفلام الحرب الأفغانية السوفيتية",
    "soviet–afghan war video games": "ألعاب فيديو الحرب الأفغانية السوفيتية",
    "spanish–american war films": "أفلام الحرب الأمريكية الإسبانية",
}


@pytest.mark.parametrize("category, expected", test_data.items(), ids=test_data.keys())
@pytest.mark.fast
def test_work_relations_new(category: str, expected: str) -> None:
    label = resolve_relations_label(category)
    assert label == expected


@pytest.mark.unit
def test_burma_cambodia_relations_from_country_table() -> None:
    """Female 'relations' using countries_nat_en_key women demonyms."""
    value = "burma-cambodia relations"
    result = resolve_relations_label(value)
    assert _norm(result) == "العلاقات البورمية الكمبودية"


@pytest.mark.unit
def test_burundi_canada_military_relations() -> None:
    """Female 'military relations' with two countries from country table."""
    value = "burundi-canada military relations"
    result = resolve_relations_label(value)
    # بوروندية + كندية
    assert _norm(result) == "العلاقات البوروندية الكندية العسكرية"


@pytest.mark.unit
def test_nat_women_fallback_for_singapore_luxembourg() -> None:
    """Female 'relations' using Nat_women fallback (no entry in main country table)."""
    value = "singapore-luxembourg relations"
    result = resolve_relations_label(value)
    # سنغافورية + لوكسمبورغية
    assert _norm(result) == "العلاقات السنغافورية اللوكسمبورغية"


@pytest.mark.unit
def test_dash_variants_en_dash() -> None:
    """Relations using en dash instead of hyphen."""
    value = "burma–cambodia relations"
    result = resolve_relations_label(value)
    assert _norm(result) == "العلاقات البورمية الكمبودية"


@pytest.mark.unit
def test_dash_variants_minus_sign() -> None:
    """Relations using minus sign instead of hyphen."""
    value = "burma−cambodia relations"
    result = resolve_relations_label(value)
    assert _norm(result) == "العلاقات البورمية الكمبودية"


def test_nato_relations_special_case() -> None:
    """Special-case NATO handling for plain 'relations'."""
    value = "nato-afghanistan relations"
    result = resolve_relations_label(value)
    # Uses hard-coded "الناتو" plus country label
    assert _norm(result) == "علاقات أفغانستان والناتو"


@pytest.mark.unit
def test_female_suffix_not_matched_returns_empty() -> None:
    """No recognized female or male suffix should return empty string."""
    value = "burma-cambodia partnership"
    result = resolve_relations_label(value)
    assert result == ""
