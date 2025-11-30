"""
Tests
"""

import pytest

from ArWikiCats.make_bots.countries_formats.p17_bot_2 import (
    get_p17_2,
)


# --------------------------------------------
# Tests for full get_p17_2
# --------------------------------------------

@pytest.mark.unit
def test_get_p17_2_mens_full() -> None:
    category = "zambia government officials"
    result = get_p17_2(category)
    assert result == "مسؤولون حكوميون زامبيون"


@pytest.mark.unit
def test_get_p17_2_women_full() -> None:
    category = "yemen air force"
    result = get_p17_2(category)
    # اليمن → يمنية → with article → اليمنية
    assert result == "القوات الجوية اليمنية"


@pytest.mark.unit
def test_get_p17_2_falls_back_from_mens_to_women() -> None:
    # "air force" not found in mens dict → fallback women
    category = "vietnam air force"
    result = get_p17_2(category)
    assert result == "القوات الجوية الفيتنامية"


@pytest.mark.unit
def test_get_p17_2_no_match_returns_empty() -> None:
    category = "zambia unknown_suffix"
    result = get_p17_2(category)
    assert result == ""


@pytest.mark.unit
def test_get_p17_2_country_not_found_returns_empty() -> None:
    category = "something air force"
    result = get_p17_2(category)
    assert result == ""


@pytest.mark.unit
def test_get_p17_2_handles_extra_spaces() -> None:
    category = "  yemen   air force   "
    result = get_p17_2(category)
    assert result == "القوات الجوية اليمنية"


@pytest.mark.unit
def test_get_p17_2_capital_letters() -> None:
    category = "ZIMBABWE AIR FORCE"
    result = get_p17_2(category)
    assert result == "القوات الجوية الزيمبابوية"
