import pytest
from src.fix.specific_normalizations import apply_category_specific_normalizations, fix_formula


# -----------------------------
# Formula-specific tests
# -----------------------------
def test_fix_formula_year_replacement():
    """Check Formula 1 year normalization."""
    assert fix_formula("فورمولا 1 1995", "") == "فورمولا 1 في سنة 1995"


# -----------------------------
# By-removal category tests
# -----------------------------
@pytest.mark.parametrize("ar,en,expected", [
    ("أفلام بواسطة مخرج", "", "أفلام مخرج"),
    ("أعمال بواسطة فنان", "", "أعمال فنان"),
    ("اختراعات بواسطة عالم", "", "اختراعات عالم"),
    ("مسرحيات بواسطة جون كندي", "", "مسرحيات جون كندي"),
])
def test_by_removal(ar, en, expected):
    """Check removal of 'بواسطة' after category names."""
    assert apply_category_specific_normalizations(ar, en) == expected


# -----------------------------
# Simple replacement tests
# -----------------------------
@pytest.mark.parametrize("ar,expected", [
    ("وفيات بواسطة ضربات عصا", "وفيات بضربات عصا"),
    ("ضربات جوية نفذت بواسطة الجيش", "ضربات جوية نفذتها الجيش"),
    ("أفلام أنتجت بواسطة نتفلكس", "أفلام أنتجها نتفلكس"),
    ("ردود فعل إلى الحدث", "ردود فعل على الحدث"),
    ("مدراء كرة القدم", "مدربو كرة القدم"),
    ("متعلقة 2", "متعلقة ب2"),
    ("هولوكوستية", "الهولوكوست"),
    ("في هولوكوست أوروبا", "في الهولوكوست أوروبا"),
    ("صدور عظام في الدولة العثمانية", "صدور عظام عثمانيون في"),
    ("أعمال بواسطة بيكاسو", "أعمال بيكاسو"),
    ("حكم عليهم الموت", "حكم عليهم بالإعدام"),
    ("محررون من منشورات عالمية", "محررو منشورات عالمية"),
    ("محررات من منشورات عالمية", "محررات منشورات عالمية"),
    ("قديسون صوفيون", "أولياء صوفيون"),
    ("مدربو رياضية عالمية", "مدربو رياضة عالمية"),
    ("أدينوا ب سرقة", "أدينوا بسرقة"),
    ("العسكري القرن 18", "العسكري في القرن 18"),
    ("ق.م 300", "ق م 300"),
    ("أحداث رياضية الرياضية", "أحداث رياضية"),
    ("مغتربون الاردن", "مغتربون من الاردن"),
    ("سفراء إلى فرنسا", "سفراء لدى فرنسا"),
    ("أشخاص أصل تركي", "أشخاص من أصل تركي"),
])
def test_simple_replacements(ar, expected):
    """Check simple direct replacements."""
    assert apply_category_specific_normalizations(ar, "") == expected


# -----------------------------
# Invention → Exhibition tests
# -----------------------------
@pytest.mark.parametrize("ar,expected", [
    ("كاميرات اخترعت في اليابان", "كاميرات عرضت في اليابان"),
    ("هواتف محمولة اخترعت في كوريا", "هواتف محمولة عرضت في كوريا"),
    ("مركبات اخترعت محليًا", "مركبات عرضت محليًا"),
    ("منتجات اخترعت حديثًا", "منتجات عرضت حديثًا"),
])
def test_invention_to_exhibition(ar, expected):
    """Check replacement of 'اخترعت' with 'عرضت' for products."""
    assert apply_category_specific_normalizations(ar, "") == expected


# -----------------------------
# Duplicate word cleanup tests
# -----------------------------
@pytest.mark.parametrize("ar,expected", [
    ("مدينة من من آسيا", "مدينة من آسيا"),
    ("نتائج حسب حسب الدولة", "نتائج حسب الدولة"),
    ("أحداث في في فرنسا", "أحداث في فرنسا"),
    ("سكان في من الهند", "سكان من الهند"),
    ("أشخاص من في العراق", "أشخاص في العراق"),
    ("بيانات في حسب السنة", "بيانات حسب السنة"),
    ("أحداث من حسب النوع", "أحداث حسب النوع"),
])
def test_duplicate_cleanup(ar, expected):
    """Check cleanup of duplicated prepositions."""
    assert apply_category_specific_normalizations(ar, "") == expected


# -----------------------------
# Preposition fixes
# -----------------------------
@pytest.mark.parametrize("ar,expected", [
    ("رياضيون في فائزون بجائزة", "رياضيون فائزون بجائزة"),
    ("قادة في منافسون في الانتخابات", "قادة منافسون في الانتخابات"),
    ("أماكن على السجل الوطني للأماكن التاريخية", "أماكن في السجل الوطني للأماكن التاريخية"),
    ("مواقع من قبل البلد", "مواقع حسب البلد"),
    ("أحداث حسب بواسطة الشركة", "أحداث بواسطة الشركة"),
    ("أبطال في رياضة في أوروبا", "أبطال في الرياضة في أوروبا"),
])
def test_preposition_fixes(ar, expected):
    """Check preposition-specific fixes."""
    assert apply_category_specific_normalizations(ar, "") == expected


# -----------------------------
# Time period expressions
# -----------------------------
@pytest.mark.parametrize("ar,expected", [
    ("شخصيات من القرن 19", "شخصيات في القرن 19"),
    ("جنود من حروب الاستقلال", "جنود في حروب الاستقلال"),
    ("قادة من الحروب الصليبية", "قادة في الحروب الصليبية"),
    ("أبطال من حرب 1812", "أبطال في حرب 1812"),
    ("أشخاص من الحرب العالمية الأولى", "أشخاص في الحرب العالمية الأولى"),
    ("شخصيات من الثورة الفرنسية", "شخصيات في الثورة الفرنسية"),
])
def test_time_expressions(ar, expected):
    """Check normalization of time-related expressions."""
    assert apply_category_specific_normalizations(ar, "") == expected


# -----------------------------
# Media expressions
# -----------------------------
@pytest.mark.parametrize("ar,expected", [
    ("مسلسلات بدأ عرضها حسب السنة", "مسلسلات حسب سنة بدء العرض"),
    ("برامج أنتهت حسب السنة", "برامج حسب سنة انتهاء العرض"),
])
def test_media_expressions(ar, expected):
    """Check fixes in media-related expressions."""
    assert apply_category_specific_normalizations(ar, "") == expected


# -----------------------------
# Short stories with year
# -----------------------------
def test_short_stories_year():
    """Check special case: short stories with years."""
    assert apply_category_specific_normalizations("قصص قصيرة 1613", "") == "قصص قصيرة كتبت سنة 1613"


# -----------------------------
# English context: 'attacks on'
# -----------------------------
def test_attacks_on_context():
    """Change 'هجمات في' to 'هجمات على' when English contains 'attacks on'."""
    ar = "هجمات في باريس"
    en = "attacks on Paris"
    assert apply_category_specific_normalizations(ar, en) == "هجمات على باريس"
