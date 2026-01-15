#
import pytest
from load_one_data import dump_diff, dump_diff_text, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data_virginia2_1 = {
    "Category:Baptists from West Virginia": "تصنيف:معمدانيون من فرجينيا الغربية",
    "Category:Defunct private universities and colleges in West Virginia": "تصنيف:جامعات وكليات خاصة سابقة في فرجينيا الغربية",
    "Category:1607 establishments in the Colony of Virginia": "تصنيف:تأسيسات سنة 1607 في مستعمرة فرجينيا",
    "Category:1648 establishments in the Colony of Virginia": "تصنيف:تأسيسات سنة 1648 في مستعمرة فرجينيا",
    "Category:1651 establishments in the Colony of Virginia": "تصنيف:تأسيسات سنة 1651 في مستعمرة فرجينيا",
    "Category:1671 establishments in the Colony of Virginia": "تصنيف:تأسيسات سنة 1671 في مستعمرة فرجينيا",
    "Category:1673 establishments in the Colony of Virginia": "تصنيف:تأسيسات سنة 1673 في مستعمرة فرجينيا",
    "Category:1759 establishments in the Colony of Virginia": "تصنيف:تأسيسات سنة 1759 في مستعمرة فرجينيا",
}

data_virginia2_3 = {
    "Category:Faculty by university or college in Virginia": "تصنيف:هيئة تدريس حسب الجامعة أو الكلية في فرجينيا",
    "Category:Faculty by university or college in West Virginia": "تصنيف:هيئة تدريس حسب الجامعة أو الكلية في فرجينيا الغربية",
    "Category:19th-century West Virginia state court judges": "تصنيف:قضاة محكمة ولاية فرجينيا الغربية في القرن 19",
    "Category:20th-century West Virginia state court judges": "تصنيف:قضاة محكمة ولاية فرجينيا الغربية في القرن 20",
    "Category:21st century in Virginia": "تصنيف:فرجينيا في القرن 21",
    "Category:Adaptations of works by Virginia Woolf": "تصنيف:أعمال مقتبسة عن أعمال فرجينيا وولف",
    "Category:African-American people in West Virginia politics": "تصنيف:أمريكيون أفارقة في سياسة فرجينيا الغربية",
    "Category:Alumni by university or college in Virginia": "تصنيف:خريجون حسب الجامعة أو الكلية في فرجينيا",
    "Category:Architecture in West Virginia": "تصنيف:هندسة معمارية في فرجينيا الغربية",
    "Category:Coaches of American football from West Virginia": "تصنيف:مدربو كرة قدم أمريكية من فرجينيا الغربية",
    "Category:Demographics of Virginia": "تصنيف:التركيبة السكانية في فرجينيا",
    "Category:Education in Williamsburg, Virginia": "تصنيف:التعليم في ويليامزبرغ (فرجينيا)",
    "Category:Jews from West Virginia": "تصنيف:يهود من فرجينيا الغربية",
    "Category:Mayors of Williamsburg, Virginia": "تصنيف:عمدات ويليامزبرغ (فرجينيا)",
    "Category:Motorsport in West Virginia": "تصنيف:رياضة محركات في فرجينيا الغربية",
    "Category:Musicians from West Virginia by populated place": "تصنيف:موسيقيون من فرجينيا الغربية حسب المكان المأهول",
    "Category:Singer-songwriters from West Virginia": "تصنيف:مغنون وكتاب أغاني من فرجينيا الغربية",
    "Category:Towns in Accomack County, Virginia": "تصنيف:بلدات في مقاطعة أكوماك (فرجينيا)",
    "Category:Towns in Botetourt County, Virginia": "تصنيف:بلدات في مقاطعة بوتيتورت (فرجينيا)",
    "Category:Towns in Brunswick County, Virginia": "تصنيف:بلدات في مقاطعة برونزويك (فرجينيا)",
    "Category:Towns in Franklin County, Virginia": "تصنيف:بلدات في مقاطعة فرانكلين (فرجينيا)",
    "Category:Towns in Grayson County, Virginia": "تصنيف:بلدات في مقاطعة غرايسون (فرجينيا)",
    "Category:Towns in Halifax County, Virginia": "تصنيف:بلدات في مقاطعة هاليفاكس (فرجينيا)",
    "Category:Towns in Loudoun County, Virginia": "تصنيف:بلدات في مقاطعة لودون (فرجينيا)",
    "Category:Towns in Middlesex County, Virginia": "تصنيف:بلدات في مقاطعة ميديلسكس (فرجينيا)",
    "Category:Towns in Southampton County, Virginia": "تصنيف:بلدات في مقاطعة ساوثهامبتون (فرجينيا)",
    "Category:Towns in Tazewell County, Virginia": "تصنيف:بلدات في مقاطعة تازويل (فرجينيا)",
    "Category:Towns in West Virginia": "تصنيف:بلدات في فرجينيا الغربية",
    "Category:Towns in Wythe County, Virginia": "تصنيف:بلدات في مقاطعة وايذ (فرجينيا)",
    "Category:West Virginia Republicans": "تصنيف:أعضاء الحزب الجمهوري في فرجينيا الغربية",
    "Category:Census-designated places in Campbell County, Virginia": "تصنيف:مناطق إحصاء سكاني في مقاطعة كامبل (فرجينيا)",
    "Category:Census-designated places in Henry County, Virginia": "تصنيف:مناطق إحصاء سكاني في مقاطعة هنري (فرجينيا)",
    "Category:Census-designated places in Tazewell County, Virginia": "تصنيف:مناطق إحصاء سكاني في مقاطعة تازويل (فرجينيا)",
    "Category:Geography of Charlottesville, Virginia": "تصنيف:جغرافيا شارلوتسفيل (فرجينيا)",
    "Category:Parks in Charlottesville, Virginia": "تصنيف:متنزهات في شارلوتسفيل (فرجينيا)",
    "Category:Victorian architecture in West Virginia": "تصنيف:عمارة فكتورية في فرجينيا الغربية",
}

data_virginia2_4 = {
    "Category:Democratic Party United States representatives from West Virginia": "تصنيف:أعضاء الحزب الديمقراطي في مجلس النواب الأمريكي من فرجينيا الغربية",
    "Category:Infectious disease deaths in Virginia": "تصنيف:وفيات بأمراض معدية في فرجينيا",
    "Category:Infectious disease deaths in West Virginia": "تصنيف:وفيات بأمراض معدية في فرجينيا الغربية",
    "Category:Metropolitan areas of Virginia": "تصنيف:مناطق فرجينيا الحضرية",
    "Category:Metropolitan areas of West Virginia": "تصنيف:مناطق فرجينيا الغربية الحضرية",
    "Category:Republican Party United States representatives from West Virginia": "تصنيف:أعضاء الحزب الجمهوري في مجلس النواب الأمريكي من فرجينيا الغربية",
    "Category:Unconditional Union Party United States representatives from West Virginia": "تصنيف:أعضاء حزب الاتحاد غير المشروط في مجلس النواب الأمريكي من فرجينيا الغربية",
    "Category:Respiratory disease deaths in West Virginia": "تصنيف:وفيات بأمراض الجهاز التنفسي في فرجينيا الغربية",
    "Category:Eastern Virginia Medical School alumni": "x",
    "Category:University of Virginia School of Medicine alumni": "x",
    "Category:University of Virginia School of Medicine faculty": "x",
    "Category:Virginia Tech alumni": "x",
}

to_test = [
    ("test_virginia2_1", data_virginia2_1),
    ("test_virginia2_3", data_virginia2_3),
    # ("test_virginia2_4", data_virginia2_4),
]


@pytest.mark.parametrize("category, expected", data_virginia2_1.items(), ids=data_virginia2_1.keys())
@pytest.mark.fast
def test_virginia2_1(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    # dump_diff_text(expected, diff_result, name)
    dump_diff(diff_result, name)
    # dump_same_and_not_same(data, diff_result, name, True)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
