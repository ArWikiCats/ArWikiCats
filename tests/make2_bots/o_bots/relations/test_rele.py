from unittest.mock import patch

import pytest

from ArWikiCats.make_bots.o_bots.rele import (
    Nat_men,
    Nat_women,
    all_country_ar,
    countries_nat_en_key,
    work_relations,
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


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=list(fast_data.keys()))
@pytest.mark.fast
def test_work_relations(category: str, expected: str) -> None:
    label = work_relations(category)
    assert label == expected


fast_data2 = {
    "democratic-republic-of-congo–libya relations": "العلاقات الكونغوية الديمقراطية الليبية",
    "democratic-republic-of-congo–netherlands relations": "العلاقات الكونغوية الديمقراطية الهولندية",
    "Democratic republic of congo–Libya relations": "العلاقات الكونغوية الديمقراطية الليبية",
    "Democratic republic of congo–Netherlands relations": "العلاقات الكونغوية الديمقراطية الهولندية",
}


@pytest.mark.parametrize("category, expected", fast_data2.items(), ids=list(fast_data2.keys()))
@pytest.mark.fast
def test_relations_congo(category: str, expected: str) -> None:
    label = work_relations(category)
    assert label == expected


# ======================
# Basic tests
# ======================


def test_female_relations_basic() -> None:
    """اختبار حالة أساسية للعلاقات النسائية مع دول موجودة في القاموس"""
    with (
        patch.dict("ArWikiCats.make_bots.o_bots.rele.countries_nat_en_key", TEST_ALL_COUNTRY_WITH_NAT),
        patch.dict("ArWikiCats.make_bots.o_bots.rele.Nat_women", TEST_NAT_WOMEN),
    ):
        result = work_relations("canada–burma military relations")
        assert result == "العلاقات البورمية الكندية العسكرية"


def test_female_relations_special_nato() -> None:
    """اختبار حالة خاصة للناتو مع دولة موجودة"""
    with (
        patch.dict("ArWikiCats.make_bots.o_bots.rele.all_country_ar", TEST_ALL_COUNTRY_AR),
        patch.dict("ArWikiCats.make_bots.o_bots.rele.countries_nat_en_key", TEST_ALL_COUNTRY_WITH_NAT),
    ):
        result = work_relations("nato–canada relations")
        assert result == "علاقات الناتو وكندا"


def test_female_relations_mixed_sources() -> None:
    """اختبار دول من مصادر مختلفة (all_country_with_nat و Nat_women)"""
    with (
        patch.dict("ArWikiCats.make_bots.o_bots.rele.countries_nat_en_key", TEST_ALL_COUNTRY_WITH_NAT),
        patch.dict("ArWikiCats.make_bots.o_bots.rele.Nat_women", TEST_NAT_WOMEN),
    ):
        result = work_relations("burma–zanzibari border crossings")
        assert result == "معابر الحدود البورمية الزنجبارية"


def test_female_relations_unknown_country() -> None:
    """اختبار حالة وجود دولة غير موجودة في القواميس"""
    with (
        patch.dict("ArWikiCats.make_bots.o_bots.rele.countries_nat_en_key", TEST_ALL_COUNTRY_WITH_NAT),
        patch.dict("ArWikiCats.make_bots.o_bots.rele.Nat_women", TEST_NAT_WOMEN),
    ):
        result = work_relations("unknown–canada relations")
        assert result == ""


# ======================
# اختبارات العلاقات الذكورية
# ======================


def test_male_relations_basic() -> None:
    """اختبار حالة أساسية للعلاقات الذكورية"""
    with patch.dict("ArWikiCats.make_bots.o_bots.rele.Nat_men", TEST_NAT_MEN):
        result = work_relations("german–polish football rivalry")
        assert result == "التنافس الألماني البولندي في كرة القدم"


def test_male_relations_with_en_dash() -> None:
    """اختبار استخدام en-dash (–) بدلاً من hyphen (-)"""
    with patch.dict("ArWikiCats.make_bots.o_bots.rele.Nat_men", TEST_NAT_MEN):
        result = work_relations("afghan–prussian conflict")
        assert result == "الصراع الأفغاني البروسي"


def test_male_relations_with_minus_sign() -> None:
    """اختبار استخدام علامة الطرح (−)"""
    with patch.dict("ArWikiCats.make_bots.o_bots.rele.Nat_men", TEST_NAT_MEN):
        result = work_relations("indian−pakistani wars")
        assert result == "الحروب الباكستانية الهندية"


# ======================
# اختبارات البادئات (P17_PREFIXES)
# ======================


def test_p17_prefixes_basic() -> None:
    """اختبار حالة أساسية للبادئات"""
    with patch.dict("ArWikiCats.make_bots.o_bots.rele.all_country_ar", TEST_ALL_COUNTRY_AR):
        result = work_relations("afghanistan–pakistan proxy conflict")
        assert result == "صراع أفغانستان وباكستان بالوكالة"


def test_p17_prefixes_unknown_country() -> None:
    """اختبار حالة وجود دولة غير معروفة في P17"""
    with patch.dict("ArWikiCats.make_bots.o_bots.rele.all_country_ar", TEST_ALL_COUNTRY_AR):
        result = work_relations("unknown–pakistan conflict")
        assert result == ""


# ======================
# حالات خاصة وحالات فاشلة
# ======================


def test_special_nato_case_male() -> None:
    """اختبار حالة الناتو في العلاقات الذكورية (يتطلب معالجة خاصة)"""
    with (
        patch.dict("ArWikiCats.make_bots.o_bots.rele.all_country_ar", TEST_ALL_COUNTRY_AR),
        patch.dict("ArWikiCats.make_bots.o_bots.rele.countries_nat_en_key", TEST_ALL_COUNTRY_WITH_NAT),
    ):
        result = work_relations("nato–germany conflict")
        assert result == "صراع ألمانيا والناتو"


def test_unsupported_relation_type() -> None:
    """اختبار نوع علاقة غير مدعومة"""
    result = work_relations("mars–venus space relations")
    assert result == ""


def test_missing_separator() -> None:
    """اختبار نص بدون فاصل بين الدول"""
    with patch.dict("ArWikiCats.make_bots.o_bots.rele.Nat_women", TEST_NAT_WOMEN):
        result = work_relations("canadaburma relations")
        assert result == ""


def test_empty_input() -> None:
    """اختبار إدخال فارغ"""
    result = work_relations("")
    assert result == ""


# ======================
# اختبارات الحدود (Edge Cases)
# ======================


def test_trailing_whitespace() -> None:
    """اختبار مسافات زائدة في النهاية"""
    with patch.dict("ArWikiCats.make_bots.o_bots.rele.Nat_women", TEST_NAT_WOMEN):
        result = work_relations("canada–burma relations   ")
        assert result == "العلاقات البورمية الكندية"


def test_leading_whitespace() -> None:
    """اختبار مسافات زائدة في البداية"""
    with patch.dict("ArWikiCats.make_bots.o_bots.rele.Nat_women", TEST_NAT_WOMEN):
        result = work_relations("   canada–burma relations")
        assert result == "العلاقات البورمية الكندية"


def test_mixed_case_input() -> None:
    """اختبار حالة أحرف مختلطة (أعلى وأسفل)"""
    with patch.dict("ArWikiCats.make_bots.o_bots.rele.Nat_women", TEST_NAT_WOMEN):
        result = work_relations("CaNaDa–BuRmA ReLaTiOnS")
        assert result == "العلاقات البورمية الكندية"


def test_multiple_dashes() -> None:
    """اختبار نص يحتوي على أكثر من فاصل"""
    with patch.dict("ArWikiCats.make_bots.o_bots.rele.Nat_women", TEST_NAT_WOMEN):
        result = work_relations("canada–burma–india relations")
        assert result == ""


def test_numeric_country_codes() -> None:
    """اختبار أكواد دول رقمية (غير مدعومة)"""
    result = work_relations("123–456 relations")
    assert result == ""
