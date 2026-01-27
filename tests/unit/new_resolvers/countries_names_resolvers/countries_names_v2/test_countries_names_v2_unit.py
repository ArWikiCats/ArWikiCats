"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.countries_names_resolvers.countries_names_v2 import resolve_by_countries_names_v2

# --------------------------------------------
# Tests for full resolve_by_countries_names_v2
# --------------------------------------------


@pytest.mark.unit
def test_resolve_by_countries_names_v2_mens_full() -> None:
    category = "zambia government officials"
    result = resolve_by_countries_names_v2(category)
    assert result == "مسؤولون حكوميون زامبيون"


@pytest.mark.unit
def test_resolve_by_countries_names_v2_women_full() -> None:
    category = "yemen air force"
    result = resolve_by_countries_names_v2(category)
    # اليمن → يمنية → with article → اليمنية
    assert result == "القوات الجوية اليمنية"


@pytest.mark.unit
def test_resolve_by_countries_names_v2_falls_back_from_mens_to_women() -> None:
    # "air force" not found in males dict → fallback women
    category = "vietnam air force"
    result = resolve_by_countries_names_v2(category)
    assert result == "القوات الجوية الفيتنامية"


@pytest.mark.unit
def test_resolve_by_countries_names_v2_no_match_returns_empty() -> None:
    category = "zambia unknown_suffix"
    result = resolve_by_countries_names_v2(category)
    assert result == ""


@pytest.mark.unit
def test_resolve_by_countries_names_v2_country_not_found_returns_empty() -> None:
    category = "something air force"
    result = resolve_by_countries_names_v2(category)
    assert result == ""


@pytest.mark.unit
def test_resolve_by_countries_names_v2_handles_extra_spaces() -> None:
    category = "  yemen   air force   "
    result = resolve_by_countries_names_v2(category)
    assert result == "القوات الجوية اليمنية"


@pytest.mark.unit
def test_resolve_by_countries_names_v2_capital_letters() -> None:
    category = "ZIMBABWE AIR FORCE"
    result = resolve_by_countries_names_v2(category)
    assert result == "القوات الجوية الزيمبابوية"
