import pytest

from ArWikiCats.new_resolvers.relations_resolver import main_relations_resolvers

# ======================
# Basic tests
# ======================


def test_unsupported_relation_type() -> None:
    """اختبار نوع علاقة غير مدعومة"""
    result = main_relations_resolvers("mars–venus space relations")
    assert result == ""


def test_empty_input() -> None:
    """اختبار إدخال فارغ"""
    result = main_relations_resolvers("")
    assert result == ""


def test_numeric_country_codes() -> None:
    """اختبار أكواد دول رقمية (غير مدعومة)"""
    result = main_relations_resolvers("123–456 relations")
    assert result == ""


# ======================
# اختبارات العلاقات النسائية
# ======================


def test_female_relations_basic() -> None:
    """Basic female relations with countries in dictionary"""

    result = main_relations_resolvers("canada–burma military relations")
    assert result == "العلاقات البورمية الكندية العسكرية"


def test_female_relations_special_nato() -> None:
    """Special NATO case with known country"""

    result = main_relations_resolvers("nato–canada relations")
    assert result == "علاقات الناتو وكندا"


def test_female_relations_unknown_country() -> None:
    """Unknown country should return empty string"""

    result = main_relations_resolvers("unknown–canada relations")
    assert result == ""


# ======================
# اختبارات العلاقات الذكورية
# ======================


def test_male_relations_basic() -> None:
    """Basic male relations"""

    result = main_relations_resolvers("german–polish football rivalry")
    assert result == "التنافس الألماني البولندي في كرة القدم"


def test_male_relations_with_en_dash() -> None:
    """Use en-dash instead of hyphen"""
    result = main_relations_resolvers("afghan–prussian conflict")
    assert result == "الصراع الأفغاني البروسي"


# ======================
# اختبارات البادئات (P17_PREFIXES)
# ======================


def test_p17_prefixes_basic() -> None:
    """Basic P17 prefix handling"""

    result = main_relations_resolvers("afghanistan–pakistan proxy conflict")
    assert result == "صراع أفغانستان وباكستان بالوكالة"


def test_p17_prefixes_unknown_country() -> None:
    """Unknown country in P17 context"""

    result = main_relations_resolvers("unknown–pakistan conflict")
    assert result == ""


# ======================
# حالات خاصة
# ======================


def test_special_nato_case_male() -> None:
    """Male NATO relation handling"""

    result = main_relations_resolvers("nato–germany conflict")
    assert result == "صراع ألمانيا والناتو"


def test_missing_separator() -> None:
    """Missing separator should fail"""
    result = main_relations_resolvers("canadaburma relations")
    assert result == ""


# ======================
# Edge cases
# ======================


def test_trailing_whitespace() -> None:
    """Trailing whitespace"""

    result = main_relations_resolvers("canada–burma relations   ")
    assert result == "العلاقات البورمية الكندية"


def test_leading_whitespace() -> None:
    """Leading whitespace"""

    result = main_relations_resolvers("   canada–burma relations")
    assert result == "العلاقات البورمية الكندية"


def test_mixed_case_input() -> None:
    """Mixed-case input"""

    result = main_relations_resolvers("CaNaDa–BuRmA ReLaTiOnS")
    assert result == "العلاقات البورمية الكندية"


def test_multiple_dashes() -> None:
    """Multiple separators should fail"""

    result = main_relations_resolvers("canada–burma–india relations")
    assert result == ""
