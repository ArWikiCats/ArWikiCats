import pytest

from ArWikiCats.translations import (
    Nat_men,
    Nat_women,
    all_country_ar,
)
from ArWikiCats.new_resolvers.relations_resolver import new_relations_resolvers
from ArWikiCats.make_bots.reslove_relations.rele import (
    countries_nat_en_key,
    resolve_relations_label,
)

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

fast_data = {
    "Georgia (country)–Luxembourg relations": "العلاقات الجورجية اللوكسمبورغية",
    "France–Papua New Guinea relations": "العلاقات الغينية الفرنسية",
    "Democratic republic of congo–Norway relations": "العلاقات الكونغوية الديمقراطية النرويجية",
    "Albania–Democratic republic of congo relations": "العلاقات الألبانية الكونغوية الديمقراطية",
    "Algeria–Democratic republic of congo relations": "العلاقات الجزائرية الكونغوية الديمقراطية",
    "Angola–Democratic republic of congo border": "الحدود الأنغولية الكونغوية الديمقراطية",
    "Angola–Democratic republic of congo relations": "العلاقات الأنغولية الكونغوية الديمقراطية",
    "Angola–Guinea-Bissau relations": "العلاقات الأنغولية الغينية البيساوية",
    "Angola–republic of congo border": "الحدود الأنغولية الكونغوية",
    "Argentina–Democratic republic of congo relations": "العلاقات الأرجنتينية الكونغوية الديمقراطية",
    "Australia–Democratic republic of congo relations": "العلاقات الأسترالية الكونغوية الديمقراطية",
    "Austria–Democratic republic of congo relations": "العلاقات الكونغوية الديمقراطية النمساوية",
    "Azerbaijan–Democratic republic of congo relations": "العلاقات الأذربيجانية الكونغوية الديمقراطية",
    "Azerbaijan–Guinea-Bissau relations": "العلاقات الأذربيجانية الغينية البيساوية",
    "Bahrain–Democratic republic of congo relations": "العلاقات البحرينية الكونغوية الديمقراطية",
    "Belgium–Guinea-Bissau relations": "العلاقات البلجيكية الغينية البيساوية",
    "Brazil–Guinea-Bissau relations": "العلاقات البرازيلية الغينية البيساوية",
    "Bulgaria–Democratic republic of congo relations": "العلاقات البلغارية الكونغوية الديمقراطية",
    "Bulgaria–Guinea-Bissau relations": "العلاقات البلغارية الغينية البيساوية",
    "Burkina Faso–Democratic republic of congo relations": "العلاقات البوركينابية الكونغوية الديمقراطية",
    "Burundi–Democratic republic of congo border": "الحدود البوروندية الكونغوية الديمقراطية",
    "Burundi–Democratic republic of congo relations": "العلاقات البوروندية الكونغوية الديمقراطية",
    "Canada–Democratic republic of congo relations": "العلاقات الكندية الكونغوية الديمقراطية",
    "Cape Verde–Democratic republic of congo relations": "العلاقات الرأس الأخضرية الكونغوية الديمقراطية",
    "Cape Verde–Guinea-Bissau relations": "العلاقات الرأس الأخضرية الغينية البيساوية",
    "Central African Republic–Democratic republic of congo relations": "العلاقات الإفريقية الأوسطية الكونغوية الديمقراطية",
    "Chad–Democratic republic of congo relations": "العلاقات التشادية الكونغوية الديمقراطية",
    "China–Democratic republic of congo relations": "العلاقات الصينية الكونغوية الديمقراطية",
    "China–Guinea-Bissau relations": "العلاقات الصينية الغينية البيساوية",
    "Croatia–Democratic republic of congo relations": "العلاقات الكرواتية الكونغوية الديمقراطية",
    "Cyprus–Democratic republic of congo relations": "العلاقات القبرصية الكونغوية الديمقراطية",
    "Cyprus–Guinea-Bissau relations": "العلاقات الغينية البيساوية القبرصية",
    "Czech Republic–Democratic republic of congo relations": "العلاقات التشيكية الكونغوية الديمقراطية",
    "Democratic republic of congo–republic of congo border": "الحدود الكونغوية الكونغوية الديمقراطية",
    "Democratic republic of congo–republic of congo border crossings": "معابر الحدود الكونغوية الكونغوية الديمقراطية",
    "Egypt–Guinea-Bissau relations": "العلاقات الغينية البيساوية المصرية",
    "Ethiopia–Guinea-Bissau relations": "العلاقات الإثيوبية الغينية البيساوية",
    "Finland–Guinea-Bissau relations": "العلاقات الغينية البيساوية الفنلندية",
    "France–Guinea-Bissau relations": "العلاقات الغينية البيساوية الفرنسية",
    "Gabon–republic of congo relations": "العلاقات الغابونية الكونغوية",
    "Georgia (country)–Guinea-Bissau relations": "العلاقات الجورجية الغينية البيساوية",
    "Greece–Guinea-Bissau relations": "العلاقات الغينية البيساوية اليونانية",
    "Iran–republic of congo relations": "العلاقات الإيرانية الكونغوية",
    "Malta–republic of congo relations": "العلاقات الكونغوية المالطية",
    "Netherlands–republic of congo relations": "العلاقات الكونغوية الهولندية",
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
@pytest.mark.fast
def test_resolve_relations_label(category: str, expected: str) -> None:
    label = resolve_relations_label(category)
    assert label == expected


fast_data2 = {
    "democratic-republic-of-congo–libya relations": "العلاقات الكونغوية الديمقراطية الليبية",
    "democratic-republic-of-congo–netherlands relations": "العلاقات الكونغوية الديمقراطية الهولندية",
    "Democratic republic of congo–Libya relations": "العلاقات الكونغوية الديمقراطية الليبية",
    "Democratic republic of congo–Netherlands relations": "العلاقات الكونغوية الديمقراطية الهولندية",
}


@pytest.mark.parametrize("category, expected", fast_data2.items(), ids=fast_data2.keys())
@pytest.mark.fast
def test_relations_congo(category: str, expected: str) -> None:
    label = resolve_relations_label(category)
    assert label == expected


# ======================
# Basic tests
# ======================


def test_unsupported_relation_type() -> None:
    """اختبار نوع علاقة غير مدعومة"""
    result = resolve_relations_label("mars–venus space relations")
    assert result == ""


def test_empty_input() -> None:
    """اختبار إدخال فارغ"""
    result = resolve_relations_label("")
    assert result == ""


def test_numeric_country_codes() -> None:
    """اختبار أكواد دول رقمية (غير مدعومة)"""
    result = resolve_relations_label("123–456 relations")
    assert result == ""


# ======================
# اختبارات العلاقات النسائية
# ======================


def test_female_relations_basic(monkeypatch: pytest.MonkeyPatch) -> None:
    """Basic female relations with countries in dictionary"""
    monkeypatch.setattr(
        "ArWikiCats.make_bots.reslove_relations.rele.countries_nat_en_key",
        TEST_ALL_COUNTRY_WITH_NAT,
        raising=False,
    )
    result = resolve_relations_label("canada–burma military relations")
    assert result == "العلاقات البورمية الكندية العسكرية"


def test_female_relations_special_nato(monkeypatch: pytest.MonkeyPatch) -> None:
    """Special NATO case with known country"""
    monkeypatch.setattr(
        "ArWikiCats.make_bots.reslove_relations.rele.all_country_ar",
        TEST_ALL_COUNTRY_AR,
        raising=False,
    )
    monkeypatch.setattr(
        "ArWikiCats.make_bots.reslove_relations.rele.countries_nat_en_key",
        TEST_ALL_COUNTRY_WITH_NAT,
        raising=False,
    )

    result = resolve_relations_label("nato–canada relations")
    assert result == "علاقات الناتو وكندا"


def test_female_relations_mixed_sources(monkeypatch: pytest.MonkeyPatch) -> None:
    """Countries resolved from mixed sources"""
    monkeypatch.setattr(
        "ArWikiCats.make_bots.reslove_relations.rele.countries_nat_en_key",
        TEST_ALL_COUNTRY_WITH_NAT,
        raising=False,
    )
    result = resolve_relations_label("burma–zanzibari border crossings")
    assert result == "معابر الحدود البورمية الزنجبارية"


def test_female_relations_unknown_country(monkeypatch: pytest.MonkeyPatch) -> None:
    """Unknown country should return empty string"""
    monkeypatch.setattr(
        "ArWikiCats.make_bots.reslove_relations.rele.countries_nat_en_key",
        TEST_ALL_COUNTRY_WITH_NAT,
        raising=False,
    )
    result = resolve_relations_label("unknown–canada relations")
    assert result == ""


# ======================
# اختبارات العلاقات الذكورية
# ======================


def test_male_relations_basic(monkeypatch: pytest.MonkeyPatch) -> None:
    """Basic male relations"""

    result = resolve_relations_label("german–polish football rivalry")
    assert result == "التنافس الألماني البولندي في كرة القدم"


def test_male_relations_with_en_dash(monkeypatch: pytest.MonkeyPatch) -> None:
    """Use en-dash instead of hyphen"""
    result = resolve_relations_label("afghan–prussian conflict")
    assert result == "الصراع الأفغاني البروسي"


def test_male_relations_with_minus_sign(monkeypatch: pytest.MonkeyPatch) -> None:
    """Use minus sign separator"""
    result = resolve_relations_label("indian−pakistani wars")
    assert result == "الحروب الباكستانية الهندية"


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

    result = resolve_relations_label("afghanistan–pakistan proxy conflict")
    assert result == "صراع أفغانستان وباكستان بالوكالة"


def test_p17_prefixes_unknown_country(monkeypatch: pytest.MonkeyPatch) -> None:
    """Unknown country in P17 context"""
    monkeypatch.setattr(
        "ArWikiCats.make_bots.reslove_relations.rele.all_country_ar",
        TEST_ALL_COUNTRY_AR,
        raising=False,
    )

    result = resolve_relations_label("unknown–pakistan conflict")
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
        "ArWikiCats.make_bots.reslove_relations.rele.countries_nat_en_key",
        TEST_ALL_COUNTRY_WITH_NAT,
        raising=False,
    )

    result = resolve_relations_label("nato–germany conflict")
    assert result == "صراع ألمانيا والناتو"


def test_missing_separator(monkeypatch: pytest.MonkeyPatch) -> None:
    """Missing separator should fail"""
    result = resolve_relations_label("canadaburma relations")
    assert result == ""


# ======================
# Edge cases
# ======================


def test_trailing_whitespace(monkeypatch: pytest.MonkeyPatch) -> None:
    """Trailing whitespace"""

    result = resolve_relations_label("canada–burma relations   ")
    assert result == "العلاقات البورمية الكندية"


def test_leading_whitespace(monkeypatch: pytest.MonkeyPatch) -> None:
    """Leading whitespace"""

    result = resolve_relations_label("   canada–burma relations")
    assert result == "العلاقات البورمية الكندية"


def test_mixed_case_input(monkeypatch: pytest.MonkeyPatch) -> None:
    """Mixed-case input"""

    result = resolve_relations_label("CaNaDa–BuRmA ReLaTiOnS")
    assert result == "العلاقات البورمية الكندية"


def test_multiple_dashes(monkeypatch: pytest.MonkeyPatch) -> None:
    """Multiple separators should fail"""

    result = resolve_relations_label("canada–burma–india relations")
    assert result == ""
