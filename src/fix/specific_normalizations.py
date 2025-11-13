
import re


def fix_formula(ar_label: str, en_label: str) -> str:

    ar_label = re.sub(r"\bفورمولا 1\s*([12]\d+)", r"فورمولا 1 في سنة \g<1>", ar_label)

    return ar_label


def apply_category_specific_normalizations(ar_label: str, en_label: str) -> str:
    """Apply normalizations that depend on the English context string.

    # مسلسلات تلفزيونية > to > مسلسلات تلفازية أنتجها أو أنتجتها ...
    # مبان ومنشآت بواسطة > to > مبان ومنشآت صممها أو خططها ...
    # ألبومات ... بواسطة ... > ألبومات ... ل.....
    # لاعبو كرة بواسطة > لاعبو كرة حسب
    # """

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

    ar_label = re.sub(r"وفيات بواسطة ضربات ", "وفيات بضربات ", ar_label)
    ar_label = re.sub(r"ضربات جوية نفذت بواسطة ", "ضربات جوية نفذتها ", ar_label)
    ar_label = re.sub(r"أفلام أنتجت بواسطة ", "أفلام أنتجها ", ar_label)
    ar_label = re.sub(r"كاميرات اخترعت ", "كاميرات عرضت ", ar_label)
    ar_label = re.sub(r"هواتف محمولة اخترعت ", "هواتف محمولة عرضت ", ar_label)
    ar_label = re.sub(r"مركبات اخترعت ", "مركبات عرضت ", ar_label)
    ar_label = re.sub(r"منتجات اخترعت ", "منتجات عرضت ", ar_label)

    # قصص قصيرة 1613 > قصص قصيرة كتبت سنة 1613
    # قصص قصيرة من تأليف إرنست همينغوي > قصص إرنست همينغوي القصيرة
    # قصص قصيرة لأنطون تشيخوف > قصص أنطون تشيخوف القصيرة
    ar_label = re.sub(r"^قصص قصيرة (\d+)$", r"قصص قصيرة كتبت سنة \1", ar_label)

    ar_label = re.sub(r"ردود فعل إلى ", "ردود فعل على ", ar_label)
    ar_label = re.sub(r"مدراء كرة", "مدربو كرة", ar_label)
    ar_label = re.sub(r"متعلقة 2", "متعلقة ب2", ar_label)
    ar_label = re.sub(r"هولوكوستية", "الهولوكوست", ar_label)
    ar_label = re.sub(r"في هولوكوست", "في الهولوكوست", ar_label)
    ar_label = re.sub(r"صدور عظام في الدولة العثمانية", "صدور عظام عثمانيون في", ar_label)
    ar_label = re.sub(r"أعمال بواسطة ", "أعمال ", ar_label)
    ar_label = re.sub(r" في فائزون ", " فائزون ", ar_label)
    ar_label = re.sub(r" في منافسون ", " منافسون ", ar_label)
    ar_label = re.sub(r" على السجل الوطني للأماكن ", " في السجل الوطني للأماكن ", ar_label)
    ar_label = re.sub(r" من قبل البلد", " حسب البلد", ar_label)
    ar_label = re.sub(r"حكم عليهم الموت", "حكم عليهم بالإعدام", ar_label)
    ar_label = re.sub(r"محررون من منشورات", "محررو منشورات", ar_label)
    ar_label = re.sub(r"محررات من منشورات", "محررات منشورات", ar_label)
    ar_label = re.sub(r"قديسون صوفيون", "أولياء صوفيون", ar_label)
    ar_label = re.sub(r"مدربو رياضية", "مدربو رياضة", ar_label)
    ar_label = re.sub(r" من من ", " من ", ar_label)
    ar_label = re.sub(r" حسب حسب ", " حسب ", ar_label)
    ar_label = re.sub(r" حسب بواسطة ", " بواسطة ", ar_label)
    ar_label = re.sub(r" في في ", " في ", ar_label)
    ar_label = re.sub(r" في في ", " في ", ar_label)
    ar_label = re.sub(r" في في ", " في ", ar_label)
    ar_label = re.sub(r"أدينوا ب ", "أدينوا ب", ar_label)
    ar_label = re.sub(r" في من ", " من ", ar_label)
    ar_label = re.sub(r" العسكري القرن ", " العسكري في القرن ", ar_label)
    ar_label = re.sub(r" من في ", " في ", ar_label)

    ar_label = fix_formula(ar_label, en_label)

    ar_label = re.sub(r" في حسب ", " حسب ", ar_label)
    ar_label = re.sub(r" من حسب ", " حسب ", ar_label)
    ar_label = re.sub(r" ق\.م ", " ق م ", ar_label)
    # ar_label = re.sub(r"تأسيسات سنة", "تأسيسات", ar_label)

    ar_label = re.sub(r"أحداث رياضية الرياضية", "أحداث رياضية", ar_label)
    ar_label = re.sub(r" من القرن", " في القرن", ar_label)
    ar_label = re.sub(r" من حروب", " في حروب", ar_label)
    ar_label = re.sub(r" من الحروب", " في الحروب", ar_label)
    ar_label = re.sub(r" من حرب", " في حرب", ar_label)
    ar_label = re.sub(r" من الحرب", " في الحرب", ar_label)
    ar_label = re.sub(r" من الثورة", " في الثورة", ar_label)
    ar_label = re.sub(r"مغتربون ال", "مغتربون من ال", ar_label)
    ar_label = re.sub(r"سفراء إلى ", "سفراء لدى ", ar_label)
    ar_label = re.sub(r"أشخاص أصل ", "أشخاص من أصل ", ar_label)
    ar_label = re.sub(r" بدأ عرضها حسب السنة", " حسب سنة بدء العرض", ar_label)
    ar_label = re.sub(r" أنتهت حسب السنة", " حسب سنة انتهاء العرض", ar_label)
    ar_label = re.sub(r" في رياضة في ", " في الرياضة في ", ar_label)

    if "attacks on" in en_label and "هجمات في " in ar_label:
        ar_label = re.sub(r"هجمات في ", "هجمات على ", ar_label)

    return ar_label
