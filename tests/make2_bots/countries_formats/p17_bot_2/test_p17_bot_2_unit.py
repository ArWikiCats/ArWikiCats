"""
Tests
"""

import pytest

from src.make_bots.countries_formats.p17_bot_2 import (
    Get_P17_2,
)


# --------------------------------------------
# Tests for full Get_P17_2
# --------------------------------------------

@pytest.mark.unit
def test_get_p17_2_mens_full():
    category = "zambia government officials"
    result = Get_P17_2(category)
    assert result == "مسؤولون حكوميون زامبيون"


@pytest.mark.unit
def test_get_p17_2_women_full():
    category = "yemen air force"
    result = Get_P17_2(category)
    # اليمن → يمنية → with article → اليمنية
    assert result == "القوات الجوية اليمنية"


@pytest.mark.unit
def test_get_p17_2_falls_back_from_mens_to_women():
    # "air force" not found in mens dict → fallback women
    category = "vietnam air force"
    result = Get_P17_2(category)
    assert result == "القوات الجوية الفيتنامية"


@pytest.mark.unit
def test_get_p17_2_no_match_returns_empty():
    category = "zambia unknown_suffix"
    result = Get_P17_2(category)
    assert result == ""


@pytest.mark.unit
def test_get_p17_2_country_not_found_returns_empty():
    category = "something air force"
    result = Get_P17_2(category)
    assert result == ""


@pytest.mark.unit
def test_get_p17_2_handles_extra_spaces():
    category = "  yemen   air force   ".strip()
    result = Get_P17_2(category)
    assert result == "القوات الجوية اليمنية"


@pytest.mark.unit
def test_get_p17_2_capital_letters():
    category = "ZIMBABWE AIR FORCE"
    result = Get_P17_2(category)
    assert result == "القوات الجوية الزيمبابوية"
