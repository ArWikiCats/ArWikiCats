"""
Tests
"""

import pytest

from src.make2_bots.countries_formats.p17_bot_2 import (
    Get_P17_2,
    _resolve_p17_2_label,
    en_is_P17_ar_is_mens,
    en_is_P17_ar_is_al_women,
)

# --------------------------------------------
# Direct tests for _resolve_p17_2_label
# --------------------------------------------

@pytest.mark.unit
def test_resolve_p17_mens_basic():
    # "government officials": "مسؤولون حكوميون {}"
    category = "yemen government officials"
    out = _resolve_p17_2_label(category, en_is_P17_ar_is_mens, "mens")
    assert out == "مسؤولون حكوميون يمنيون"


@pytest.mark.unit
def test_resolve_p17_women_basic_with_article():
    # women nationality + definite article
    # en_is_P17_ar_is_al_women["air force"] = "القوات الجوية {}"
    category = "syria air force"
    out = _resolve_p17_2_label(category, en_is_P17_ar_is_al_women, "women", add_article=True)
    # "سورية" → add_definite_article → "السورية"
    assert out == "القوات الجوية السورية"


@pytest.mark.unit
def test_resolve_p17_country_not_found():
    category = "unknowncountry air force"
    out = _resolve_p17_2_label(category, en_is_P17_ar_is_al_women, "women")
    assert out == ""


@pytest.mark.unit
def test_resolve_p17_suffix_not_matching():
    category = "yemen strange_suffix"
    out = _resolve_p17_2_label(category, en_is_P17_ar_is_mens, "mens")
    assert out == ""


@pytest.mark.unit
def test_resolve_p17_case_insensitive():
    category = "YEMEN GOVERNMENT OFFICIALS"
    out = _resolve_p17_2_label(category, en_is_P17_ar_is_mens, "mens")
    assert out == "مسؤولون حكوميون يمنيون"


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
