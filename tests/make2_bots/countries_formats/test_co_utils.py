"""
Tests
"""

import pytest

from ArWikiCats.make_bots.countries_formats.utils import (
    add_definite_article,
    resolve_p17_2_label,
)

from ArWikiCats.translations import (
    en_is_P17_ar_is_mens,
    en_is_P17_ar_is_al_women,
    countries_nat_en_key,
)

definite_article_data = {
    "أمريكية": "الأمريكية",
    "صينية": "الصينية",
    "شمالية يمنية": "الشمالية اليمنية",
    "باكستانية": "الباكستانية",
    "نيوزيلندية": "النيوزيلندية",
    "كورية": "الكورية",
    "يمنية": "اليمنية",
    "فيتنامية": "الفيتنامية",
    "ميانمارية": "الميانمارية",
    "هولندية": "الهولندية",
    "إيرانية": "الإيرانية",
    "سريلانكية": "السريلانكية",
    "بهامية": "البهامية",
    "جنوبية يمنية": "الجنوبية اليمنية",
    "سيراليونية": "السيراليونية",
    "يابانية": "اليابانية",
    "إماراتية": "الإماراتية",
    "بنينية": "البنينية",
    "قبرصية": "القبرصية",
    "برونية": "البرونية",
}


def test_add_all():
    # Test with a basic input
    result = add_definite_article("test label")
    assert isinstance(result, str)
    assert "ال" in result  # The function adds "ال" prefix

    # Test with empty string
    result_empty = add_definite_article("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = add_definite_article("another label")
    assert isinstance(result_various, str)


@pytest.mark.parametrize("category, expected", definite_article_data.items(), ids=list(definite_article_data.keys()))
@pytest.mark.fast
def test_add_definite_article(category: str, expected: str) -> None:
    label = add_definite_article(category)
    assert label == expected

# --------------------------------------------
# Tests for add_definite_article
# --------------------------------------------


@pytest.mark.unit
def test_add_definite_article_simple():
    # Ensures proper prefixing of words with ال
    assert add_definite_article("سورية") == "السورية"
    assert add_definite_article("فيتنامي") == "الفيتنامي"
    assert add_definite_article("كندي غربي") == "الكندي الغربي"
    # assert add_definite_article("كندي الغربي") == "الكندي الغربي"


# --------------------------------------------
# Direct tests for resolve_p17_2_label
# --------------------------------------------


@pytest.mark.unit
def test_resolve_p17_mens_basic():
    # "government officials": "مسؤولون حكوميون {}"
    category = "yemen government officials"
    out = resolve_p17_2_label(category, en_is_P17_ar_is_mens, "mens", countries_nat_en_key)
    assert out == "مسؤولون حكوميون يمنيون"


@pytest.mark.unit
def test_resolve_p17_women_basic_with_article():
    # women nationality + definite article
    # en_is_P17_ar_is_al_women["air force"] = "القوات الجوية {}"
    category = "syria air force"
    out = resolve_p17_2_label(category, en_is_P17_ar_is_al_women, "women", countries_nat_en_key, add_article=True)
    # "سورية" → add_definite_article → "السورية"
    assert out == "القوات الجوية السورية"


@pytest.mark.unit
def test_resolve_p17_country_not_found():
    category = "unknowncountry air force"
    out = resolve_p17_2_label(category, en_is_P17_ar_is_al_women, "women", countries_nat_en_key)
    assert out == ""


@pytest.mark.unit
def test_resolve_p17_suffix_not_matching():
    category = "yemen strange_suffix"
    out = resolve_p17_2_label(category, en_is_P17_ar_is_mens, "mens", countries_nat_en_key)
    assert out == ""


@pytest.mark.unit
def test_resolve_p17_case_insensitive():
    category = "YEMEN GOVERNMENT OFFICIALS"
    out = resolve_p17_2_label(category, en_is_P17_ar_is_mens, "mens", countries_nat_en_key)
    assert out == "مسؤولون حكوميون يمنيون"
