#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

data_virginia2_1 = {
    "Baptists from West Virginia": "معمدانيون من فرجينيا الغربية",
    "Defunct private universities and colleges in West Virginia": "جامعات وكليات خاصة سابقة في فرجينيا الغربية",
    "1607 establishments in the Colony of Virginia": "تأسيسات سنة 1607 في مستعمرة فرجينيا",
    "1648 establishments in the Colony of Virginia": "تأسيسات سنة 1648 في مستعمرة فرجينيا",
    "1651 establishments in the Colony of Virginia": "تأسيسات سنة 1651 في مستعمرة فرجينيا",
    "1671 establishments in the Colony of Virginia": "تأسيسات سنة 1671 في مستعمرة فرجينيا",
    "1673 establishments in the Colony of Virginia": "تأسيسات سنة 1673 في مستعمرة فرجينيا",
    "1759 establishments in the Colony of Virginia": "تأسيسات سنة 1759 في مستعمرة فرجينيا",
}

data_virginia2_3 = {
    "Faculty by university or college in Virginia": "هيئة تدريس حسب الجامعة أو الكلية في فرجينيا",
    "Faculty by university or college in West Virginia": "هيئة تدريس حسب الجامعة أو الكلية في فرجينيا الغربية",
    "19th-century West Virginia state court judges": "قضاة محكمة ولاية فرجينيا الغربية في القرن 19",
    "20th-century West Virginia state court judges": "قضاة محكمة ولاية فرجينيا الغربية في القرن 20",
    "21st century in Virginia": "فرجينيا في القرن 21",
    "Adaptations of works by Virginia Woolf": "أعمال مقتبسة عن أعمال فرجينيا وولف",
    "African-American people in West Virginia politics": "أمريكيون أفارقة في سياسة فرجينيا الغربية",
    "Alumni by university or college in Virginia": "خريجون حسب الجامعة أو الكلية في فرجينيا",
    "Architecture in West Virginia": "هندسة معمارية في فرجينيا الغربية",
    "Demographics of Virginia": "التركيبة السكانية في فرجينيا",
    "Education in Williamsburg, Virginia": "التعليم في ويليامزبرغ (فرجينيا)",
    "Jews from West Virginia": "يهود من فرجينيا الغربية",
    "Mayors of Williamsburg, Virginia": "عمدات ويليامزبرغ (فرجينيا)",
    "Musicians from West Virginia by populated place": "موسيقيون من فرجينيا الغربية حسب المكان المأهول",
    "Singer-songwriters from West Virginia": "مغنون وكتاب أغاني من فرجينيا الغربية",
    "Towns in Accomack County, Virginia": "بلدات في مقاطعة أكوماك (فرجينيا)",
    "Towns in Botetourt County, Virginia": "بلدات في مقاطعة بوتيتورت (فرجينيا)",
    "Towns in Brunswick County, Virginia": "بلدات في مقاطعة برونزويك (فرجينيا)",
    "Towns in Franklin County, Virginia": "بلدات في مقاطعة فرانكلين (فرجينيا)",
    "Towns in Grayson County, Virginia": "بلدات في مقاطعة غرايسون (فرجينيا)",
    "Towns in Halifax County, Virginia": "بلدات في مقاطعة هاليفاكس (فرجينيا)",
    "Towns in Loudoun County, Virginia": "بلدات في مقاطعة لودون (فرجينيا)",
    "Towns in Middlesex County, Virginia": "بلدات في مقاطعة ميديلسكس (فرجينيا)",
    "Towns in Southampton County, Virginia": "بلدات في مقاطعة ساوثهامبتون (فرجينيا)",
    "Towns in Tazewell County, Virginia": "بلدات في مقاطعة تازويل (فرجينيا)",
    "Towns in West Virginia": "بلدات في فرجينيا الغربية",
    "Towns in Wythe County, Virginia": "بلدات في مقاطعة وايذ (فرجينيا)",
    "West Virginia Republicans": "أعضاء الحزب الجمهوري في فرجينيا الغربية",
    "Census-designated places in Campbell County, Virginia": "مناطق إحصاء سكاني في مقاطعة كامبل (فرجينيا)",
    "Census-designated places in Henry County, Virginia": "مناطق إحصاء سكاني في مقاطعة هنري (فرجينيا)",
    "Census-designated places in Tazewell County, Virginia": "مناطق إحصاء سكاني في مقاطعة تازويل (فرجينيا)",
    "Geography of Charlottesville, Virginia": "جغرافيا شارلوتسفيل (فرجينيا)",
    "Parks in Charlottesville, Virginia": "متنزهات في شارلوتسفيل (فرجينيا)",
    "Victorian architecture in West Virginia": "عمارة فكتورية في فرجينيا الغربية",
}

data_virginia2_4 = {
    "Democratic Party United States representatives from West Virginia": "أعضاء الحزب الديمقراطي في مجلس النواب الأمريكي من فرجينيا الغربية",
    "Infectious disease deaths in Virginia": "وفيات بأمراض معدية في فرجينيا",
    "Infectious disease deaths in West Virginia": "وفيات بأمراض معدية في فرجينيا الغربية",
    "Metropolitan areas of Virginia": "مناطق فرجينيا الحضرية",
    "Metropolitan areas of West Virginia": "مناطق فرجينيا الغربية الحضرية",
    "Republican Party United States representatives from West Virginia": "أعضاء الحزب الجمهوري في مجلس النواب الأمريكي من فرجينيا الغربية",
    "Unconditional Union Party United States representatives from West Virginia": "أعضاء حزب الاتحاد غير المشروط في مجلس النواب الأمريكي من فرجينيا الغربية",
    "Respiratory disease deaths in West Virginia": "وفيات بأمراض الجهاز التنفسي في فرجينيا الغربية",
    "Eastern Virginia Medical School alumni": "x",
    "University of Virginia School of Medicine alumni": "x",
    "University of Virginia School of Medicine faculty": "x",
    "Virginia Tech alumni": "x",
}

to_test = [
    ("test_virginia2_1", data_virginia2_1),
    ("test_virginia2_3", data_virginia2_3),
    # ("test_virginia2_4", data_virginia2_4),
]


@pytest.mark.parametrize("category, expected", data_virginia2_1.items(), ids=data_virginia2_1.keys())
@pytest.mark.fast
def test_virginia2_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=False)
