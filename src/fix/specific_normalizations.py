
import re


def fix_formula(ar_label: str, en_label: str) -> str:

    ar_label = re.sub(r"\bفورمولا 1\s*([12]\d+)", r"فورمولا 1 في سنة \g<1>", ar_label)

    return ar_label


def by_removal(ar_label: str) -> str:
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
    data = {
        r"وفيات بواسطة ضربات": "وفيات بضربات",
        r"ضربات جوية نفذت بواسطة": "ضربات جوية نفذتها",
        r"أفلام أنتجت بواسطة": "أفلام أنتجها",
        r"ردود فعل إلى": "ردود فعل على",
        r"مدراء كرة": "مدربو كرة",
        r"هولوكوستية": "الهولوكوست",
        r"في هولوكوست": "في الهولوكوست",
        r"صدور عظام في الدولة العثمانية": "صدور عظام عثمانيون في",
        r"أعمال بواسطة": "أعمال",
        r"حكم عليهم الموت": "حكم عليهم بالإعدام",
        r"محررون من منشورات": "محررو منشورات",
        r"محررات من منشورات": "محررات منشورات",
        r"قديسون صوفيون": "أولياء صوفيون",
        r"مدربو رياضية": "مدربو رياضة",
        r"العسكري القرن": "العسكري في القرن",
        r"أحداث رياضية الرياضية": "أحداث رياضية",
        r"سفراء إلى": "سفراء لدى",
        r"أشخاص أصل": "أشخاص من أصل",
    }
    for old, new in data.items():
        ar_label = re.sub(fr"\b{old}\b", new, ar_label)

    ar_label = re.sub(r"\bأدينوا ب\s+", "أدينوا ب", ar_label)
    ar_label = re.sub("مغتربون ال", "مغتربون من ال", ar_label)

    return ar_label


def invention_to_exhibition(ar_label: str) -> str:
    data = ["كاميرات", "هواتف محمولة", "مركبات", "منتجات"]
    for item in data:
        ar_label = re.sub(f"{item} اخترعت ", f"{item} عرضت ", ar_label)
    return ar_label


def media_expressions(ar_label: str) -> str:
    data = {
        "بدأ عرضها حسب السنة": "حسب سنة بدء العرض",
        "أنتهت حسب السنة": "حسب سنة انتهاء العرض",
    }
    for old, new in data.items():
        ar_label = re.sub(fr"\b{old}\b", new, ar_label)

    return ar_label


def time_expressions(ar_label: str) -> str:
    data = {
        r"من القرن": "في القرن",
        r"من حروب": "في حروب",
        r"من الحروب": "في الحروب",
        r"من حرب": "في حرب",
        r"من الحرب": "في الحرب",
        r"من الثورة": "في الثورة",
    }
    for old, new in data.items():
        ar_label = re.sub(fr"\b{old}\b", new, ar_label)

    return ar_label


def duplicate_cleanup(ar_label):

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
        ar_label = re.sub(fr"\b{pattern}\b", replacement, ar_label)

    return ar_label


def preposition_fixes(ar_label):

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
        ar_label = re.sub(fr"\b{pattern}\b", replacement, ar_label)

    return ar_label


def apply_category_specific_normalizations(ar_label: str, en_label: str) -> str:
    """Apply normalizations that depend on the English context string.

    # مسلسلات تلفزيونية > to > مسلسلات تلفازية أنتجها أو أنتجتها ...
    # مبان ومنشآت بواسطة > to > مبان ومنشآت صممها أو خططها ...
    # ألبومات ... بواسطة ... > ألبومات ... ل.....
    # لاعبو كرة بواسطة > لاعبو كرة حسب
    # """
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
