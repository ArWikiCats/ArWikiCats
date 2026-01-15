import pytest

from ArWikiCats.translations import (
    Nat_men,
    Nat_women,
    all_country_ar,
)
from ArWikiCats.new_resolvers.relations_resolver import new_relations_resolvers
from ArWikiCats.new_resolvers.relations_resolver.countries_names_double_v2 import countries_nat_en_key

#
TEST_ALL_COUNTRY_AR = {
    **all_country_ar,
    "canada": "كندا",
    "burma": "بورما",
    "nato": "الناتو",
    "pakistan": "باكستان",
    "india": "الهند",
    "germany": "ألمانيا",
    "poland": "بولندا",
}

TEST_NAT_MEN = {
    **Nat_men,
    "canadian": "كندي",
    "burmese": "بورمي",
    "german": "ألماني",
    "polish": "بولندي",
    "pakistani": "باكستاني",
    "indian": "هندي",
}

TEST_NAT_WOMEN = {
    **Nat_women,
    "canadian": "كندية",
    "burmese": "بورمية",
    "german": "ألمانية",
    "polish": "بولندية",
    "pakistani": "باكستانية",
    "indian": "هندية",
}

TEST_ALL_COUNTRY_WITH_NAT = {
    **countries_nat_en_key,
    "nato": {"ar": "الناتو"},
    "pakistan": {"male": "باكستاني", "female": "باكستانية", "ar": "باكستان"},
    "india": {"male": "هندي", "female": "هندية", "ar": "الهند"},
}


# ======================
# Basic tests
# ======================


def test_unsupported_relation_type() -> None:
    """اختبار نوع علاقة غير مدعومة"""
    result = new_relations_resolvers("mars–venus space relations")
    assert result == ""


def test_empty_input() -> None:
    """اختبار إدخال فارغ"""
    result = new_relations_resolvers("")
    assert result == ""


def test_numeric_country_codes() -> None:
    """اختبار أكواد دول رقمية (غير مدعومة)"""
    result = new_relations_resolvers("123–456 relations")
    assert result == ""


# ======================
# اختبارات العلاقات النسائية
# ======================


def test_female_relations_basic(monkeypatch: pytest.MonkeyPatch) -> None:
    """Basic female relations with countries in dictionary"""
    monkeypatch.setattr(
        "ArWikiCats.new_resolvers.countries_names_resolvers.countries_names_double_v2",
        TEST_ALL_COUNTRY_WITH_NAT,
        raising=False,
    )
    result = new_relations_resolvers("canada–burma military relations")
    assert result == "العلاقات البورمية الكندية العسكرية"


def test_female_relations_special_nato(monkeypatch: pytest.MonkeyPatch) -> None:
    """Special NATO case with known country"""
    monkeypatch.setattr(
        "ArWikiCats.make_bots.reslove_relations.rele.all_country_ar",
        TEST_ALL_COUNTRY_AR,
        raising=False,
    )
    monkeypatch.setattr(
        "ArWikiCats.new_resolvers.countries_names_resolvers.countries_names_double_v2",
        TEST_ALL_COUNTRY_WITH_NAT,
        raising=False,
    )

    result = new_relations_resolvers("nato–canada relations")
    assert result == "علاقات الناتو وكندا"


def test_female_relations_unknown_country(monkeypatch: pytest.MonkeyPatch) -> None:
    """Unknown country should return empty string"""
    monkeypatch.setattr(
        "ArWikiCats.new_resolvers.countries_names_resolvers.countries_names_double_v2",
        TEST_ALL_COUNTRY_WITH_NAT,
        raising=False,
    )
    result = new_relations_resolvers("unknown–canada relations")
    assert result == ""


# ======================
# اختبارات العلاقات الذكورية
# ======================


def test_male_relations_basic(monkeypatch: pytest.MonkeyPatch) -> None:
    """Basic male relations"""

    result = new_relations_resolvers("german–polish football rivalry")
    assert result == "التنافس الألماني البولندي في كرة القدم"


def test_male_relations_with_en_dash(monkeypatch: pytest.MonkeyPatch) -> None:
    """Use en-dash instead of hyphen"""
    result = new_relations_resolvers("afghan–prussian conflict")
    assert result == "الصراع الأفغاني البروسي"

# ======================
# اختبارات البادئات (P17_PREFIXES)
# ======================


def test_p17_prefixes_basic(monkeypatch: pytest.MonkeyPatch) -> None:
    """Basic P17 prefix handling"""
    monkeypatch.setattr(
        "ArWikiCats.make_bots.reslove_relations.rele.all_country_ar",
        TEST_ALL_COUNTRY_AR,
        raising=False,
    )

    result = new_relations_resolvers("afghanistan–pakistan proxy conflict")
    assert result == "صراع أفغانستان وباكستان بالوكالة"


def test_p17_prefixes_unknown_country(monkeypatch: pytest.MonkeyPatch) -> None:
    """Unknown country in P17 context"""
    monkeypatch.setattr(
        "ArWikiCats.make_bots.reslove_relations.rele.all_country_ar",
        TEST_ALL_COUNTRY_AR,
        raising=False,
    )

    result = new_relations_resolvers("unknown–pakistan conflict")
    assert result == ""


# ======================
# حالات خاصة
# ======================


def test_special_nato_case_male(monkeypatch: pytest.MonkeyPatch) -> None:
    """Male NATO relation handling"""
    monkeypatch.setattr(
        "ArWikiCats.make_bots.reslove_relations.rele.all_country_ar",
        TEST_ALL_COUNTRY_AR,
        raising=False,
    )
    monkeypatch.setattr(
        "ArWikiCats.new_resolvers.countries_names_resolvers.countries_names_double_v2",
        TEST_ALL_COUNTRY_WITH_NAT,
        raising=False,
    )

    result = new_relations_resolvers("nato–germany conflict")
    assert result == "صراع ألمانيا والناتو"


def test_missing_separator(monkeypatch: pytest.MonkeyPatch) -> None:
    """Missing separator should fail"""
    result = new_relations_resolvers("canadaburma relations")
    assert result == ""


# ======================
# Edge cases
# ======================


def test_trailing_whitespace(monkeypatch: pytest.MonkeyPatch) -> None:
    """Trailing whitespace"""

    result = new_relations_resolvers("canada–burma relations   ")
    assert result == "العلاقات البورمية الكندية"


def test_leading_whitespace(monkeypatch: pytest.MonkeyPatch) -> None:
    """Leading whitespace"""

    result = new_relations_resolvers("   canada–burma relations")
    assert result == "العلاقات البورمية الكندية"


def test_mixed_case_input(monkeypatch: pytest.MonkeyPatch) -> None:
    """Mixed-case input"""

    result = new_relations_resolvers("CaNaDa–BuRmA ReLaTiOnS")
    assert result == "العلاقات البورمية الكندية"


def test_multiple_dashes(monkeypatch: pytest.MonkeyPatch) -> None:
    """Multiple separators should fail"""

    result = new_relations_resolvers("canada–burma–india relations")
    assert result == ""
