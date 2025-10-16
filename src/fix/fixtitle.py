import re
from .fixlists import replase, Starting, Ending, fix_years
from .mv_years import move_years, YEARS_REGEX
from ..helps.print_bot import print_put


def fix_n(arlabel: str) -> str:
    """Fix and format a given label string based on predefined rules.

    This function takes an input string `arlabel` and applies a series of
    transformations to fix its format according to specific patterns. It
    utilizes regular expressions to replace certain substrings, adjust
    prefixes and suffixes, and ensure the label adheres to the desired
    formatting standards. The function also handles specific cases for years
    and categories, ensuring that the output is consistent and correctly
    formatted.

    Args:
        arlabel (str): The input label string that needs to be fixed.

    Returns:
        str: The formatted label string after applying the necessary
        transformations.
    """

    # ---
    for ree, reelab in replase.items():
        arlabel = re.sub(ree, reelab, arlabel)
    # ---
    for tt in fix_years:
        arlabel = re.sub(rf"(\s*{tt}) (\d+\s*|عقد \d+\s*|القرن \d+\s*)", r"\g<1> في \g<2>", arlabel)
    # ---
    for f_a, f_lab in Starting.items():
        if arlabel.startswith(f_a):
            # arlabel = re.sub(r"^%s" % f_a, f_lab, arlabel)
            arlabel = f_lab + arlabel[len(f_a) :]
    # ---
    arlabel = arlabel.strip()
    for fa, falab in Ending.items():
        if arlabel.endswith(fa):
            arlabel = re.sub(f"{fa}$", falab, arlabel).strip()
            # arlabel = arlabel[:-len(fa)] + " " + falab
    # ---
    # نصب تذكارية إلى الملكة
    # نصب تذكارية لالملكة
    # ---
    # tab[Category:Monuments and memorials to women] = "تصنيف:معالم أثرية ونصب تذكارية لالمرأة"
    # ---
    arlabel = arlabel.replace("نصب تذكارية لال", "نصب تذكارية لل")
    # ---
    mates = [
        # "^تصنيف\:(\d+|عقد \d+) مسلسلات تلفزيونية .*بدأ عرضها$",
        r"^(\d+|عقد \d+) مسلسلات تلفزيونية .*بدأ عرضها$",
        # "^(\d+|عقد \d+) مسلسلات تلفزيونية .*بدأ عرضها في$",
        # "^(\d+|عقد \d+) مسلسلات تلفزيونية .*انتهت في$"
        r"^(\d+|عقد \d+) مسلسلات تلفزيونية .*انتهت$",
        # "^معاهد أبحاث أسست في (\d+)$"
    ]
    # ---
    for mat in mates:
        if re.match(mat, arlabel):
            year = re.sub(mat, r"\g<1>", arlabel)
            print_put(f"year: {year}")
            fa = re.sub(year, "", arlabel)
            arlabel = f"{fa} في {year}"
    # ---
    for fa, falab in Ending.items():
        if arlabel.endswith(fa):
            arlabel = re.sub(f"{fa}$", falab, arlabel).strip()
            # arlabel = arlabel[:-len(fa)] + " " + falab
    # ---
    return arlabel


def fix_2(text: str) -> str:
    if rus := re.match(r"^(الغزو \w+|\w+ الغزو \w+) في (\w+.*?)$", text):
        s1 = rus.group(1)
        s2 = rus.group(2)
        if s2.startswith("ال"):
            s2 = s2[2:]
        text = f"{s1} ل{s2}"
    # ---
    return text


def fix_sub(text: str) -> str:
    if "اليابان" in text or "يابانيون" in text or "يابانيات" in text:
        text = re.sub(r"حسب الولاية", "حسب المحافظة", text)
    # ---
    if "سريلانكي" in text or "سريلانكا" in text:
        text = re.sub(r"الإقليم", "المقاطعة", text)
        text = re.sub(r"أقاليم", "مقاطعات", text)
    # ---
    if "تركيا" in text:  # Turkey
        text = re.sub(r"مديريات", "أقضية", text)
    # ---
    if "جزائر" in text:
        text = re.sub(r"المقاطعة", "الإقليم", text)
        text = re.sub(r"مقاطعات", "أقاليم", text)
        text = re.sub(r"مديريات", "دوائر", text)
        text = re.sub(r"المديرية", "الدائرة", text)
    # ---
    return text


def fix_it2(arlabel: str, en: str) -> str:
    # مسلسلات تلفزيونية ...> مسلسلات تلفازية أنتجها أو أنتجتها ...
    # مبان ومنشآت بواسطة ...> مبان ومنشآت صممها أو خططها ...
    # ألبومات ... بواسطة ... > ألبومات ... ل.....
    # لاعبو كرة بواسطة > لاعبو كرة حسب
    fixx_byy = [
        "أفلام",
        "أعمال",
        "اختراعات",
        "لوحات",
        "شعر",
        "مسرحيات",
        "روايات",
        "كتب",
    ]
    for x in fixx_byy:
        arlabel = re.sub(f"{x} بواسطة ", f"{x} ", arlabel)

    arlabel = re.sub(r"وفيات بواسطة ضربات ", "وفيات بضربات ", arlabel)
    arlabel = re.sub(r"ضربات جوية نفذت بواسطة ", "ضربات جويت نفذتها ", arlabel)
    arlabel = re.sub(r"أفلام أنتجت بواسطة ", "أفلام أنتجها ", arlabel)
    arlabel = re.sub(r"كاميرات اخترعت ", "كاميرات عرضت ", arlabel)
    arlabel = re.sub(r"هواتف محمولة اخترعت ", "هواتف محمولة عرضت ", arlabel)
    arlabel = re.sub(r"مركبات اخترعت ", "مركبات عرضت ", arlabel)
    arlabel = re.sub(r"منتجات اخترعت ", "منتجات عرضت ", arlabel)
    # ---

    # قصص قصيرة 1613 > قصص قصيرة كتبت سنة 1613
    # قصص قصيرة من تأليف إرنست همينغوي > قصص إرنست همينغوي القصيرة
    # قصص قصيرة لأنطون تشيخوف > قصص أنطون تشيخوف القصيرة
    arlabel = re.sub(r"^قصص قصيرة (\d+)$", r"قصص قصيرة كتبت سنة \1", arlabel)
    # ---
    arlabel = re.sub(r"ردود فعل إلى ", "ردود فعل على ", arlabel)
    arlabel = re.sub(r"مدراء كرة", "مدربو كرة", arlabel)
    arlabel = re.sub(r"متعلقة 2", "متعلقة ب2", arlabel)
    arlabel = re.sub(r"هولوكوستية", "الهولوكوست", arlabel)
    arlabel = re.sub(r"في هولوكوست", "في الهولوكوست", arlabel)
    arlabel = re.sub(r"صدور عظام في الدولة العثمانية", "صدور عظام عثمانيون في", arlabel)
    arlabel = re.sub(r"أعمال بواسطة ", "أعمال ", arlabel)
    arlabel = re.sub(r" في فائزون ", " فائزون ", arlabel)
    arlabel = re.sub(r" في منافسون ", " منافسون ", arlabel)
    arlabel = re.sub(r" على السجل الوطني للأماكن ", " في السجل الوطني للأماكن ", arlabel)
    arlabel = re.sub(r" من قبل البلد", " حسب البلد", arlabel)
    arlabel = re.sub(r"حكم عليهم الموت", "حكم عليهم بالإعدام", arlabel)
    arlabel = re.sub(r"محررون من منشورات", "محررو منشورات", arlabel)
    arlabel = re.sub(r"محررات من منشورات", "محررات منشورات", arlabel)
    arlabel = re.sub(r"قديسون صوفيون", "أولياء صوفيون", arlabel)
    arlabel = re.sub(r"مدربو رياضية", "مدربو رياضة", arlabel)
    arlabel = re.sub(r" من من ", " من ", arlabel)
    arlabel = re.sub(r" حسب حسب ", " حسب ", arlabel)
    arlabel = re.sub(r" حسب بواسطة ", " بواسطة ", arlabel)
    arlabel = re.sub(r" في في ", " في ", arlabel)
    arlabel = re.sub(r" في في ", " في ", arlabel)
    arlabel = re.sub(r" في في ", " في ", arlabel)
    arlabel = re.sub(r"أدينوا ب ", "أدينوا ب", arlabel)
    arlabel = re.sub(r" في من ", " من ", arlabel)
    arlabel = re.sub(r" العسكري القرن ", " العسكري في القرن ", arlabel)
    arlabel = re.sub(r" من في ", " في ", arlabel)
    arlabel = re.sub(r" فورمولا 1 2", " فورمولا 1 في سنة 2", arlabel)
    arlabel = re.sub(r" فورمولا 1 1", " فورمولا 1 في سنة 1", arlabel)
    arlabel = re.sub(r" في حسب ", " حسب ", arlabel)
    arlabel = re.sub(r" من حسب ", " حسب ", arlabel)
    arlabel = re.sub(r" ق\.م ", " ق م ", arlabel)
    # arlabel = re.sub(r"تأسيسات سنة", "تأسيسات", arlabel)

    # ---
    arlabel = re.sub(r"أحداث رياضية الرياضية", "أحداث رياضية", arlabel)
    arlabel = re.sub(r" من القرن", " في القرن", arlabel)
    arlabel = re.sub(r" من حروب", " في حروب", arlabel)
    arlabel = re.sub(r" من الحروب", " في الحروب", arlabel)
    arlabel = re.sub(r" من حرب", " في حرب", arlabel)
    arlabel = re.sub(r" من الحرب", " في الحرب", arlabel)
    arlabel = re.sub(r" من الثورة", " في الثورة", arlabel)
    arlabel = re.sub(r"مغتربون ال", "مغتربون من ال", arlabel)
    arlabel = re.sub(r"سفراء إلى ", "سفراء لدى ", arlabel)
    arlabel = re.sub(r"أشخاص أصل ", "أشخاص من أصل ", arlabel)
    # ---
    arlabel = re.sub(r" بدأ عرضها حسب السنة", " حسب سنة بدء العرض", arlabel)
    # ---
    arlabel = re.sub(r" أنتهت حسب السنة", " حسب سنة انتهاء العرض", arlabel)
    arlabel = re.sub(r" في رياضة في ", " في الرياضة في ", arlabel)
    # ---
    return arlabel


def fix_it(arlabel: str, en: str) -> str:
    """Fix and normalize the Arabic label based on specific rules.

    This function takes an Arabic label and an English string, processes the
    label to correct formatting issues, and applies various transformations
    based on predefined patterns. It handles whitespace, specific phrases,
    and formats dates and other elements according to the rules defined in
    the function. The output is a cleaned and normalized version of the
    input Arabic label.

    Args:
        arlabel (str): The Arabic label that needs to be fixed.
        en (str): An English string that may influence the transformation of
            the Arabic label.

    Returns:
        str: The normalized Arabic label after applying the necessary fixes.
    """

    # ---
    arlabel = re.sub(r"\s+", " ", arlabel)
    arlabel = re.sub(r"\{\}", "", arlabel)
    # ---
    if arlabel.endswith(" في"):
        # arlabel = re.sub(r"في$" ,"" , arlabel ).strip()
        arlabel = arlabel[: -len(" في")]
    # ---
    if arlabel.startswith("لاعبو ") and arlabel.endswith(" للسيدات"):
        arlabel = re.sub(r"^لاعبو ", "لاعبات ", arlabel)
    # ---
    en = en.replace("_", " ").lower()
    # print_put("fixlab : " + en )
    # if arlabel.find( "سرائيل") != -1 and "israeli" not in sys.argv :
    # return ""
    # ---
    # if arlabel.find( "ذكور") != -1 :
    # return ""
    # ---
    # RE2 = re.compile(r'(\d\d\d\d)\-(\d\d)', flags = re.IGNORECASE )#
    # ---
    if mat := re.match(r".*(\d\d\d\d)\-(\d\d).*", arlabel, flags=re.IGNORECASE):
        te_1 = mat.group(1)
        te_2 = mat.group(2)
        arlabel = re.sub(f"{te_1}-{te_2}", f"{te_1}–{te_2}", arlabel)
        print_put(" fixlab : fixlab :  replace - by  u2013.. ")
    # ---
    if re.sub(r"^\–\d+", "", arlabel) != arlabel:
        return ""
    # ---
    arlabel = arlabel.strip()
    # ---
    arlabel = fix_n(arlabel)
    # ---
    arlabel = re.sub(r"كأس العالم لكرة القدم (\d)", r"كأس العالم \g<1>", arlabel)
    arlabel = re.sub(r",", "،", arlabel)
    arlabel = re.sub(r"^(.*) تصفيات مؤهلة إلى (.*)$", r"تصفيات \g<1> مؤهلة إلى \g<2>", arlabel)
    arlabel = re.sub(r"تأسيسات (\d+.*)$", r"تأسيسات سنة \g<1>", arlabel)
    arlabel = re.sub(r"انحلالات (\d+.*)$", r"انحلالات سنة \g<1>", arlabel)
    arlabel = re.sub(r" من حسب ", " حسب ", arlabel)
    # arlabel = re.sub(r"لاعبو في " , "لاعبو ", arlabel)
    # arlabel = re.sub(r"لاعبو من " , "لاعبو " , arlabel)
    # ---
    arlabel = fix_it2(arlabel, en)
    # ---
    arlabel = arlabel.strip()
    # ---
    # if arlabel.endswith("أنتهت في"):
    # arlabel = re.sub(r"أنتهت في$" , "أنتهت" , arlabel ).strip()
    # ---
    arlabel = fix_n(arlabel)
    # ---
    if "مبنية على" not in arlabel:
        arlabel = re.sub(r" على أفلام$", " في الأفلام", arlabel)
    # ---
    arlabel = fix_sub(arlabel)
    # ---
    if "attacks on" in en and "هجمات في " in arlabel:
        arlabel = re.sub(r"هجمات في ", "هجمات على ", arlabel)
    # ---
    arlabel = arlabel.replace("(توضيح)", "")
    # ---
    arlabel = arlabel.replace(" تأسست في ", " أسست في ")
    # ---
    arlabel = arlabel.replace("ب201", "بسنة 201")
    arlabel = arlabel.replace("ب202", "بسنة 202")
    # arlabel = arlabel.replace("ب2020" , "بسنة 2020")
    # arlabel = arlabel.replace("ب2021" , "بسنة 2021")
    # arlabel = arlabel.replace("ب2022" , "بسنة 2022")
    # arlabel = arlabel.replace("ب2023" , "بسنة 2023")
    # arlabel = arlabel.replace("ب2024" , "بسنة 2024")
    # arlabel = arlabel.replace("ب2025" , "بسنة 2025")
    # arlabel = arlabel.replace("ب2026" , "بسنة 2026")
    # ---
    arlabel = arlabel.replace("على المريخ", "في المريخ")
    # ---
    arlabel = arlabel.replace("  ", " ")
    # ---
    arlabel = re.sub(r"^شغب (\d+)", r"شغب في \g<1>", arlabel)
    # ---
    arlabel = re.sub(r"قوائممتعلقة", "قوائم متعلقة", arlabel)
    arlabel = re.sub(r" في أصل ", " من أصل ", arlabel)
    # ---
    arlabel = fix_2(arlabel)
    # ---
    arlabel = arlabel.strip()
    # ---
    return arlabel


def add_fee(new_text: str) -> str:
    # ---
    # تصنيف:قضاة حسب الجنسية عقد 2010
    # تصنيف:فنانون ذكور حسب الجنسية 2020
    # تصنيف:فنانون ذكور حسب الجنسية القرن 20
    # ---
    hasab = [
        "الآلة",
        "البلد",
        "البوابة",
        "الجنسية والمجموعة العرقية",
        "المجموعة العرقية",
        "الجنسية والمهنة",
        "الدين والجنسية",
        "المهنة والجنسية",
        "البلد أو اللغة",
        "النوع الفني",
        "الجنسية",
        "الحرب",
        "الدين",
        "السنة",
        "العقد",
        "القارة",
        "اللغة",
        "المدينة",
        "المنظمة",
        "المهنة",
        "الموقع",
        "النزاع",
        "الولاية",
    ]
    # ---
    hasab_line = "|".join(hasab)
    # ---
    new_text = re.sub(rf" حسب\s({hasab_line}) ({YEARS_REGEX})$", r" حسب \1 في \2", new_text)
    # ---
    return new_text


def fixlab(label_old: str, out: bool = False, en: str = "") -> str:
    # ---
    en_literes = "[abcdefghijklmnopqrstuvwxyz]"
    # output_main('fixlab:"%s"' % label_old)
    # ---
    if re.sub(en_literes, "", label_old, flags=re.IGNORECASE) != label_old:
        return ""
    # ---
    if "مشاعر معادية للإسرائيليون" in label_old:
        return ""
    # ---
    label_old = label_old.strip()
    label_old = re.sub(r"_", " ", label_old)
    label_old = re.sub(r"تصنيف\:\s*", "", label_old)
    label_old = re.sub(r"تصنيف:", "", label_old)
    # ---
    arlabel = fix_it(label_old, en)
    # ---
    arlabel = add_fee(arlabel)
    # ---
    arlabel = move_years(arlabel)
    # ---
    if label_old != arlabel:
        if out is True:
            printe.output(f'fixtitle: label_old before:"{label_old}", after:"{arlabel}"')
    # ---
    return arlabel
