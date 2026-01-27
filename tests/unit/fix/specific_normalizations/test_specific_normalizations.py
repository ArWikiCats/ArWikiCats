import pytest

from ArWikiCats.fix.specific_normalizations import (
    apply_category_specific_normalizations,
    fix_formula,
)


# -----------------------------
# Formula-specific tests
# -----------------------------
def test_fix_formula_year_replacement() -> None:
    """Check Formula 1 year normalization."""
    assert fix_formula("فورمولا 1 1995", "") == "فورمولا 1 في سنة 1995"


# -----------------------------
# By-removal category tests
# (covers all categories in the list)
# -----------------------------
@pytest.mark.parametrize(
    "ar,en,expected",
    [
        ("أفلام بواسطة مخرج", "", "أفلام مخرج"),
        ("أعمال بواسطة فنان", "", "أعمال فنان"),
        ("اختراعات بواسطة عالم", "", "اختراعات عالم"),
        ("لوحات بواسطة رسام", "", "لوحات رسام"),
        ("شعر بواسطة شاعر", "", "شعر شاعر"),
        ("مسرحيات بواسطة كاتب", "", "مسرحيات كاتب"),
        ("روايات بواسطة مؤلف", "", "روايات مؤلف"),
        ("كتب بواسطة مؤلف", "", "كتب مؤلف"),
    ],
)
def test_by_removal_all_categories(ar: str, en: str, expected: str) -> None:
    """Check removal of 'بواسطة' after all configured categories."""
    assert apply_category_specific_normalizations(ar, en) == expected


# -----------------------------
# Simple replacement tests
# (covers every pattern in simple_replace)
# -----------------------------
@pytest.mark.parametrize(
    "ar,expected",
    [
        # r"وفيات بواسطة ضربات " -> "وفيات بضربات "
        ("وفيات بواسطة ضربات عصا", "وفيات بضربات عصا"),
        # r"ضربات جوية نفذت بواسطة " -> "ضربات جوية نفذتها "
        ("ضربات جوية نفذت بواسطة الجيش", "ضربات جوية نفذتها الجيش"),
        # r"أفلام أنتجت بواسطة " -> "أفلام أنتجها "
        ("أفلام أنتجت بواسطة نتفلكس", "أفلام أنتجها نتفلكس"),
        # r"ردود فعل إلى " -> "ردود فعل على "
        ("ردود فعل إلى الحدث", "ردود فعل على الحدث"),
        # r"مدراء كرة" -> "مدربو كرة"
        ("مدراء كرة القدم", "مدربو كرة القدم"),
        # r"هولوكوستية" -> "الهولوكوست"
        ("مجازر هولوكوستية", "مجازر الهولوكوست"),
        # r"في هولوكوست" -> "في الهولوكوست"
        ("قضايا في هولوكوست أوروبا", "قضايا في الهولوكوست أوروبا"),
        # r"صدور عظام في الدولة العثمانية" -> "صدور عظام عثمانيون في"
        ("صدور عظام في الدولة العثمانية إسطنبول", "صدور عظام عثمانيون في إسطنبول"),
        # r"أعمال بواسطة " -> "أعمال "
        ("أعمال بواسطة بيكاسو", "أعمال بيكاسو"),
        # r"حكم عليهم الموت" -> "حكم عليهم بالإعدام"
        ("أشخاص حكم عليهم الموت", "أشخاص حكم عليهم بالإعدام"),
        # r"محررون من منشورات" -> "محررو منشورات"
        ("محررون من منشورات عالمية", "محررو منشورات عالمية"),
        # r"محررات من منشورات" -> "محررات منشورات"
        ("محررات من منشورات عالمية", "محررات منشورات عالمية"),
        # r"قديسون صوفيون" -> "أولياء صوفيون"
        ("قديسون صوفيون مشهورون", "أولياء صوفيون مشهورون"),
        # r"مدربو رياضية" -> "مدربو رياضة"
        ("مدربو رياضية عالمية", "مدربو رياضة عالمية"),
        # r"أدينوا ب " -> "أدينوا ب"
        ("أشخاص أدينوا ب سرقة", "أشخاص أدينوا بسرقة"),
        # r"العسكري القرن " -> "العسكري في القرن "
        ("تاريخ العسكري القرن 18", "تاريخ العسكري في القرن 18"),
        # r"ق\.م " -> "ق م "
        ("حروب 300 ق.م  في المنطقة", "حروب 300 ق م  في المنطقة"),
        # r"أحداث رياضية الرياضية" -> "أحداث رياضية"
        ("أحداث رياضية الرياضية العالمية", "أحداث رياضية العالمية"),
        # r"مغتربون ال" -> "مغتربون من ال"
        ("مغتربون الاردن", "مغتربون من الاردن"),
        # r"سفراء إلى " -> "سفراء لدى "
        ("سفراء إلى فرنسا", "سفراء لدى فرنسا"),
        # r"أشخاص أصل " -> "أشخاص من أصل "
        ("أشخاص أصل تركي", "أشخاص من أصل تركي"),
    ],
)
def test_simple_replacements_all(ar: str, expected: str) -> None:
    """Check every simple replacement rule."""
    assert apply_category_specific_normalizations(ar, "") == expected


# -----------------------------
# Invention → Exhibition tests
# (covers all items: كاميرات، هواتف محمولة، مركبات، منتجات)
# -----------------------------
@pytest.mark.parametrize(
    "ar,expected",
    [
        ("كاميرات اخترعت في اليابان", "كاميرات عرضت في اليابان"),
        ("هواتف محمولة اخترعت في كوريا", "هواتف محمولة عرضت في كوريا"),
        ("مركبات اخترعت محليًا", "مركبات عرضت محليًا"),
        ("منتجات اخترعت حديثًا", "منتجات عرضت حديثًا"),
    ],
)
def test_invention_to_exhibition_all(ar: str, expected: str) -> None:
    """Check replacement of 'اخترعت' with 'عرضت' for all configured items."""
    assert apply_category_specific_normalizations(ar, "") == expected


# -----------------------------
# Duplicate word cleanup tests
# (covers all patterns in duplicate_cleanup)
# -----------------------------
@pytest.mark.parametrize(
    "ar,expected",
    [
        # r" من من " -> " من "
        ("مدينة من من آسيا", "مدينة من آسيا"),
        # r" حسب حسب " -> " حسب "
        ("نتائج حسب حسب الدولة", "نتائج حسب الدولة"),
        # r" في في " -> " في "
        ("أحداث في في فرنسا", "أحداث في فرنسا"),
        # r" في من " -> " من "
        ("سكان في من الهند", "سكان من الهند"),
        # r" من في " -> " في "
        ("أشخاص من في العراق", "أشخاص في العراق"),
        # r" في حسب " -> " حسب "
        ("بيانات في حسب السنة", "بيانات حسب السنة"),
        # r" من حسب " -> " حسب "
        ("أحداث من حسب النوع", "أحداث حسب النوع"),
    ],
)
def test_duplicate_cleanup_all(ar: str, expected: str) -> None:
    """Check all duplicate preposition cleanup rules."""
    assert apply_category_specific_normalizations(ar, "") == expected


# -----------------------------
# Preposition fixes
# (covers all patterns in preposition_fixes)
# -----------------------------
@pytest.mark.parametrize(
    "ar,expected",
    [
        # r" في فائزون " -> " فائزون "
        ("رياضيون في فائزون بجائزة", "رياضيون فائزون بجائزة"),
        # r" في منافسون " -> " منافسون "
        ("قادة في منافسون في الانتخابات", "قادة منافسون في الانتخابات"),
        # r" على السجل الوطني للأماكن " -> " في السجل الوطني للأماكن "
        ("أماكن على السجل الوطني للأماكن التاريخية", "أماكن في السجل الوطني للأماكن التاريخية"),
        # r" من قبل البلد" -> " حسب البلد"
        ("مواقع مصنفة من قبل البلد", "مواقع مصنفة حسب البلد"),
        # r" حسب بواسطة " -> " بواسطة "
        ("أحداث مرتبة حسب بواسطة الشركة", "أحداث مرتبة بواسطة الشركة"),
        # r" في رياضة في " -> " في الرياضة في "
        ("أبطال في رياضة في أوروبا", "أبطال في الرياضة في أوروبا"),
    ],
)
def test_preposition_fixes_all(ar: str, expected: str) -> None:
    """Check all preposition-specific fixes."""
    assert apply_category_specific_normalizations(ar, "") == expected


# -----------------------------
# Time period expressions
# (covers all patterns in time_expressions)
# -----------------------------
@pytest.mark.parametrize(
    "ar,expected",
    [
        # r" من القرن" -> " في القرن"
        ("شخصيات من القرن 19", "شخصيات في القرن 19"),
        # r" من حروب" -> " في حروب"
        ("جنود من حروب الاستقلال", "جنود في حروب الاستقلال"),
        # r" من الحروب" -> " في الحروب"
        ("قادة من الحروب الصليبية", "قادة في الحروب الصليبية"),
        # r" من حرب" -> " في حرب"
        ("أبطال من حرب 1812", "أبطال في حرب 1812"),
        # r" من الحرب" -> " في الحرب"
        ("أشخاص من الحرب العالمية الأولى", "أشخاص في الحرب العالمية الأولى"),
        # r" من الثورة" -> " في الثورة"
        ("شخصيات من الثورة الفرنسية", "شخصيات في الثورة الفرنسية"),
    ],
)
def test_time_expressions_all(ar: str, expected: str) -> None:
    """Check all time-related expression normalizations."""
    assert apply_category_specific_normalizations(ar, "") == expected


# -----------------------------
# Media expressions
# (covers all patterns in media_expressions)
# -----------------------------
@pytest.mark.parametrize(
    "ar,expected",
    [
        # r" بدأ عرضها حسب السنة" -> " حسب سنة بدء العرض"
        ("مسلسلات بدأ عرضها حسب السنة", "مسلسلات حسب سنة بدء العرض"),
        # r" أنتهت حسب السنة" -> " حسب سنة انتهاء العرض"
        ("برامج أنتهت حسب السنة", "برامج حسب سنة انتهاء العرض"),
    ],
)
def test_media_expressions_all(ar: str, expected: str) -> None:
    """Check all media-related expression fixes."""
    assert apply_category_specific_normalizations(ar, "") == expected


# -----------------------------
# Short stories with year
# (special regex at end of function)
# -----------------------------
def test_short_stories_year_special_case() -> None:
    """Check special case: short stories with years."""
    assert apply_category_specific_normalizations("قصص قصيرة 1613", "") == "قصص قصيرة كتبت سنة 1613"


# -----------------------------
# English context: 'attacks on'
# (context-dependent normalization)
# -----------------------------
def test_attacks_on_context_changes_preposition() -> None:
    """Change 'هجمات في' to 'هجمات على' when English contains 'attacks on'."""
    ar = "هجمات في باريس"
    en = "attacks on Paris"
    assert apply_category_specific_normalizations(ar, en) == "هجمات على باريس"


@pytest.mark.parametrize(
    "ar_label, en_label, expected",
    [
        ("أفلام بواسطة ستيفن سبيلبرغ", "films by", "أفلام ستيفن سبيلبرغ"),
        ("وفيات بواسطة ضربات جوية", "deaths by airstrikes", "وفيات بضربات جوية"),
        ("قصص قصيرة 1613", "short stories 1613", "قصص قصيرة كتبت سنة 1613"),
        ("ردود فعل إلى القرار", "reactions to", "ردود فعل على القرار"),
    ],
)
def test_apply_category_specific_normalizations(ar_label: str, en_label: str, expected: str) -> None:
    assert apply_category_specific_normalizations(ar_label, en_label) == expected
