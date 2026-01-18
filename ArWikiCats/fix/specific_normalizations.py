"""
Specific normalization rules for Arabic category labels.
This module provides functions for applying context-dependent and
pattern-based fixes to Arabic category names, addressing issues like
misleading prepositions or awkward phrasing.
"""

import re


def fix_formula(ar_label: str, en_label: str) -> str:
    """Adjust Formula 1 phrasing to highlight the event year."""
    ar_label = re.sub(r"\bفورمولا 1\s*([12]\d+)", r"فورمولا 1 في سنة \g<1>", ar_label)

    return ar_label


def by_removal(ar_label: str) -> str:
    """Remove misleading 'بواسطة' phrasing from creative works."""
    fix_bys = [
        "أفلام",
        "أعمال",
        "اختراعات",
        "لوحات",
        "شعر",
        "مسرحيات",
        "روايات",
        "كتب",
    ]
    for replacement in fix_bys:
        ar_label = re.sub(f"{replacement} بواسطة ", f"{replacement} ", ar_label)

    return ar_label


def simple_replace(ar_label: str) -> str:
    """Apply quick search-and-replace rules for frequent phrasing issues."""
    data = {
        "وفيات حسب بضربة جوية": "وفيات بضربة جوية",
        "وفيات حسب بضربات": "وفيات بضربات",
        "وفيات بواسطة ضربات": "وفيات بضربات",
        "ضربات جوية نفذت بواسطة": "ضربات جوية نفذتها",
        "أفلام أنتجت بواسطة": "أفلام أنتجها",
        "ردود فعل إلى": "ردود فعل على",
        "مدراء كرة": "مدربو كرة",
        "هولوكوستية": "الهولوكوست",
        "في هولوكوست": "في الهولوكوست",
        "صدور عظام في الدولة العثمانية": "صدور عظام عثمانيون في",
        "أعمال بواسطة": "أعمال",
        "حكم عليهم الموت": "حكم عليهم بالإعدام",
        "محررون من منشورات": "محررو منشورات",
        "محررات من منشورات": "محررات منشورات",
        "قديسون صوفيون": "أولياء صوفيون",
        "مدربو رياضية": "مدربو رياضة",
        "العسكري القرن": "العسكري في القرن",
        "أحداث رياضية الرياضية": "أحداث رياضية",
        "سفراء إلى": "سفراء لدى",
        "أشخاص أصل": "أشخاص من أصل",
    }
    for old, new in data.items():
        ar_label = re.sub(rf"\b{old}\b", new, ar_label)

    ar_label = re.sub(r"\bأدينوا ب\s+", "أدينوا ب", ar_label)
    ar_label = re.sub("مغتربون ال", "مغتربون من ال", ar_label)

    ar_label = ar_label.replace("وفيات حسب ب", "وفيات ب")

    return ar_label


def invention_to_exhibition(ar_label: str) -> str:
    """Swap invention wording with exhibition phrasing for select items."""
    data = ["كاميرات", "هواتف محمولة", "مركبات", "منتجات"]
    for item in data:
        ar_label = re.sub(f"{item} اخترعت ", f"{item} عرضت ", ar_label)
    return ar_label


def media_expressions(ar_label: str) -> str:
    """Normalize phrases used for media start and end dates."""
    data = {
        "بدأ عرضها حسب السنة": "حسب سنة بدء العرض",
        "أنتهت حسب السنة": "حسب سنة انتهاء العرض",
    }
    for old, new in data.items():
        ar_label = re.sub(rf"\b{old}\b", new, ar_label)

    return ar_label


def time_expressions(ar_label: str) -> str:
    """Standardize prepositions used in time-related expressions."""
    data = {
        r"من القرن": "في القرن",
        r"من حروب": "في حروب",
        r"من الحروب": "في الحروب",
        r"من حرب": "في حرب",
        r"من الحرب": "في الحرب",
        r"من الثورة": "في الثورة",
    }
    for old, new in data.items():
        ar_label = re.sub(rf"\b{old}\b", new, ar_label)

    return ar_label


def duplicate_cleanup(ar_label: str) -> str:
    """Remove repeated prepositions and duplicated short phrases."""
    # Group patterns for better organization and maintainability
    patterns = {
        "من من": "من",
        "حسب حسب": "حسب",
        "في في": "في",
        "في من": "من",
        "من في": "في",
        "في حسب": "حسب",
        "من حسب": "حسب",
    }
    for pattern, replacement in patterns.items():
        # ar_label = re.sub(rf"\b{pattern}\b", replacement, ar_label)
        ar_label = re.sub(rf"(?<![\w-])({pattern})(?![\w-])", replacement, ar_label)

    return ar_label


def preposition_fixes(ar_label: str) -> str:
    """Resolve awkward preposition combinations in labels."""
    # Group patterns for better organization and maintainability
    patterns = {
        r"في فائزون": "فائزون",
        r"في منافسون": "منافسون",
        r"على السجل الوطني للأماكن": "في السجل الوطني للأماكن",
        r"من قبل البلد": "حسب البلد",
        r"حسب بواسطة": "بواسطة",
        r"في رياضة في": "في الرياضة في",
    }
    for pattern, replacement in patterns.items():
        ar_label = re.sub(rf"\b{pattern}\b", replacement, ar_label)

    return ar_label


def apply_category_specific_normalizations(ar_label: str, en_label: str) -> str:
    """Apply normalizations that depend on the English context string.

    # مسلسلات تلفزيونية > to > مسلسلات تلفازية أنتجها أو أنتجتها ...
    # مبان ومنشآت بواسطة > to > مبان ومنشآت صممها أو خططها ...
    # ألبومات ... بواسطة ... > ألبومات ... ل.....
    # لاعبو كرة بواسطة > لاعبو كرة حسب
    #"""
    ar_label = by_removal(ar_label)
    ar_label = simple_replace(ar_label)
    ar_label = invention_to_exhibition(ar_label)
    ar_label = duplicate_cleanup(ar_label)
    ar_label = preposition_fixes(ar_label)
    ar_label = media_expressions(ar_label)
    ar_label = time_expressions(ar_label)

    # Special case: short stories with years
    # قصص قصيرة 1613 > قصص قصيرة كتبت سنة 1613
    # قصص قصيرة من تأليف إرنست همينغوي > قصص إرنست همينغوي القصيرة
    # قصص قصيرة لأنطون تشيخوف > قصص أنطون تشيخوف القصيرة
    ar_label = re.sub(r"^قصص قصيرة (\d+)$", r"قصص قصيرة كتبت سنة \1", ar_label)

    # Apply formula-specific normalizations
    ar_label = fix_formula(ar_label, en_label)

    ar_label = re.sub(r"\bق\.م\b", "ق م", ar_label)
    # ar_label = re.sub(r"تأسيسات سنة", "تأسيسات", ar_label)

    # Context-dependent normalization for "attacks on"
    if "attacks on" in en_label and "هجمات في " in ar_label:
        ar_label = re.sub(r"هجمات في ", "هجمات على ", ar_label)

    return ar_label
