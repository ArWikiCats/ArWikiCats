from unittest.mock import patch

import pytest

from src.make2_bots.o_bots.rele import work_relations  # افتراض اسم الموديول
from src.make2_bots.o_bots.rele import (Nat_men, Nat_women, all_country_ar,
                                        all_country_with_nat_keys_is_en)

# بيانات اختبارية موسعة لدعم السيناريوهات المختلفة
TEST_ALL_COUNTRY_AR = {**all_country_ar, "canada": "كندا", "burma": "ميانمار", "nato": "الناتو", "pakistan": "باكستان", "india": "الهند", "germany": "ألمانيا", "poland": "بولندا"}

TEST_NAT_MEN = {**Nat_men, "canadian": "كندي", "burmese": "بورمي", "german": "ألماني", "polish": "بولندي", "pakistani": "باكستاني", "indian": "هندي"}

TEST_NAT_WOMEN = {**Nat_women, "canadian": "كندية", "burmese": "بورمية", "german": "ألمانية", "polish": "بولندية", "pakistani": "باكستانية", "indian": "هندية"}

TEST_ALL_COUNTRY_WITH_NAT = {**all_country_with_nat_keys_is_en, "nato": {"ar": "الناتو"}, "pakistan": {"men": "باكستاني", "women": "باكستانية", "ar": "باكستان"}, "india": {"men": "هندي", "women": "هندية", "ar": "الهند"}}

# ======================
# اختبارات العلاقات النسائية
# ======================


def test_female_relations_basic():
    """اختبار حالة أساسية للعلاقات النسائية مع دول موجودة في القاموس"""
    with patch.dict("src.make2_bots.o_bots.rele.all_country_with_nat_keys_is_en", TEST_ALL_COUNTRY_WITH_NAT), patch.dict("src.make2_bots.o_bots.rele.Nat_women", TEST_NAT_WOMEN):

        result = work_relations("canada–burma military relations")
        assert result == "العلاقات البورمية الكندية العسكرية"


def test_female_relations_special_nato():
    """اختبار حالة خاصة للناتو مع دولة موجودة"""
    with patch.dict("src.make2_bots.o_bots.rele.all_country_ar", TEST_ALL_COUNTRY_AR), patch.dict("src.make2_bots.o_bots.rele.all_country_with_nat_keys_is_en", TEST_ALL_COUNTRY_WITH_NAT):

        result = work_relations("nato–canada relations")
        assert result == "علاقات الناتو وكندا"


def test_female_relations_mixed_sources():
    """اختبار دول من مصادر مختلفة (all_country_with_nat و Nat_women)"""
    with patch.dict("src.make2_bots.o_bots.rele.all_country_with_nat_keys_is_en", TEST_ALL_COUNTRY_WITH_NAT), patch.dict("src.make2_bots.o_bots.rele.Nat_women", TEST_NAT_WOMEN):

        result = work_relations("burma–zanzibari border crossings")
        assert result == "معابر الحدود البورمية الزنجبارية"


def test_female_relations_unknown_country():
    """اختبار حالة وجود دولة غير موجودة في القواميس"""
    with patch.dict("src.make2_bots.o_bots.rele.all_country_with_nat_keys_is_en", TEST_ALL_COUNTRY_WITH_NAT), patch.dict("src.make2_bots.o_bots.rele.Nat_women", TEST_NAT_WOMEN):

        result = work_relations("unknown–canada relations")
        assert result == ""


# ======================
# اختبارات العلاقات الذكورية
# ======================


def test_male_relations_basic():
    """اختبار حالة أساسية للعلاقات الذكورية"""
    with patch.dict("src.make2_bots.o_bots.rele.Nat_men", TEST_NAT_MEN):
        result = work_relations("german–polish football rivalry")
        assert result == "التنافس الألماني البولندي في كرة القدم"


def test_male_relations_with_en_dash():
    """اختبار استخدام en-dash (–) بدلاً من hyphen (-)"""
    with patch.dict("src.make2_bots.o_bots.rele.Nat_men", TEST_NAT_MEN):
        result = work_relations("afghan–prussian conflict")
        assert result == "الصراع الأفغاني البروسي"


def test_male_relations_with_minus_sign():
    """اختبار استخدام علامة الطرح (−)"""
    with patch.dict("src.make2_bots.o_bots.rele.Nat_men", TEST_NAT_MEN):
        result = work_relations("indian−pakistani wars")
        assert result == "الحروب الباكستانية الهندية"


# ======================
# اختبارات البادئات (P17_PREFIXES)
# ======================


def test_p17_prefixes_basic():
    """اختبار حالة أساسية للبادئات"""
    with patch.dict("src.make2_bots.o_bots.rele.all_country_ar", TEST_ALL_COUNTRY_AR):
        result = work_relations("afghanistan–pakistan proxy conflict")
        assert result == "صراع أفغانستان وباكستان بالوكالة"


def test_p17_prefixes_unknown_country():
    """اختبار حالة وجود دولة غير معروفة في P17"""
    with patch.dict("src.make2_bots.o_bots.rele.all_country_ar", TEST_ALL_COUNTRY_AR):
        result = work_relations("unknown–pakistan conflict")
        assert result == ""


# ======================
# حالات خاصة وحالات فاشلة
# ======================


def test_special_nato_case_male():
    """اختبار حالة الناتو في العلاقات الذكورية (يتطلب معالجة خاصة)"""
    with patch.dict("src.make2_bots.o_bots.rele.all_country_ar", TEST_ALL_COUNTRY_AR), patch.dict("src.make2_bots.o_bots.rele.all_country_with_nat_keys_is_en", TEST_ALL_COUNTRY_WITH_NAT):

        result = work_relations("nato–germany conflict")
        assert result == "صراع ألمانيا والناتو"


def test_unsupported_relation_type():
    """اختبار نوع علاقة غير مدعومة"""
    result = work_relations("mars–venus space relations")
    assert result == ""


def test_missing_separator():
    """اختبار نص بدون فاصل بين الدول"""
    with patch.dict("src.make2_bots.o_bots.rele.Nat_women", TEST_NAT_WOMEN):
        result = work_relations("canadaburma relations")
        assert result == ""


def test_empty_input():
    """اختبار إدخال فارغ"""
    result = work_relations("")
    assert result == ""


# ======================
# اختبارات الحدود (Edge Cases)
# ======================


def test_trailing_whitespace():
    """اختبار مسافات زائدة في النهاية"""
    with patch.dict("src.make2_bots.o_bots.rele.Nat_women", TEST_NAT_WOMEN):
        result = work_relations("canada–burma relations   ")
        assert result == "العلاقات البورمية الكندية"


def test_leading_whitespace():
    """اختبار مسافات زائدة في البداية"""
    with patch.dict("src.make2_bots.o_bots.rele.Nat_women", TEST_NAT_WOMEN):
        result = work_relations("   canada–burma relations")
        assert result == "العلاقات البورمية الكندية"


def test_mixed_case_input():
    """اختبار حالة أحرف مختلطة (أعلى وأسفل)"""
    with patch.dict("src.make2_bots.o_bots.rele.Nat_women", TEST_NAT_WOMEN):
        result = work_relations("CaNaDa–BuRmA ReLaTiOnS")
        assert result == "العلاقات البورمية الكندية"


def test_multiple_dashes():
    """اختبار نص يحتوي على أكثر من فاصل"""
    with patch.dict("src.make2_bots.o_bots.rele.Nat_women", TEST_NAT_WOMEN):
        result = work_relations("canada–burma–india relations")
        assert result == ""


def test_numeric_country_codes():
    """اختبار أكواد دول رقمية (غير مدعومة)"""
    result = work_relations("123–456 relations")
    assert result == ""
