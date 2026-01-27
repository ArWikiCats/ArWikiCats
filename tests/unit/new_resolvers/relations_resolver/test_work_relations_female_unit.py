from __future__ import annotations

import pytest

from ArWikiCats.new_resolvers.relations_resolver import main_relations_resolvers


@pytest.mark.unit
def test_burma_cambodia_relations_from_country_table() -> None:
    """Female 'relations' using countries_nat_en_key women demonyms."""
    value = "burma-cambodia relations"
    result = main_relations_resolvers(value)
    assert result == "العلاقات البورمية الكمبودية"


@pytest.mark.unit
def test_burundi_canada_military_relations() -> None:
    """Female 'military relations' with two countries from country table."""
    value = "burundi-canada military relations"
    result = main_relations_resolvers(value)
    # بوروندية + كندية
    assert result == "العلاقات البوروندية الكندية العسكرية"


@pytest.mark.unit
def test_nat_women_fallback_for_singapore_luxembourg() -> None:
    """Female 'relations' using Nat_women fallback (no entry in main country table)."""
    value = "singapore-luxembourg relations"
    result = main_relations_resolvers(value)
    # سنغافورية + لوكسمبورغية
    assert result == "العلاقات السنغافورية اللوكسمبورغية"


@pytest.mark.unit
def test_dash_variants_en_dash() -> None:
    """Relations using en dash instead of hyphen."""
    value = "burma–cambodia relations"
    result = main_relations_resolvers(value)
    assert result == "العلاقات البورمية الكمبودية"


@pytest.mark.unit
def test_dash_variants_minus_sign() -> None:
    """Relations using minus sign instead of hyphen."""
    value = "burma−cambodia relations"
    result = main_relations_resolvers(value)
    assert result == "العلاقات البورمية الكمبودية"


@pytest.mark.unit
def test_female_suffix_not_matched_returns_empty() -> None:
    """No recognized female or male suffix should return empty string."""
    value = "burma-cambodia partnership"
    result = main_relations_resolvers(value)
    assert result == ""
