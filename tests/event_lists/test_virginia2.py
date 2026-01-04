#
import pytest
from load_one_data import dump_diff, one_dump_test, dump_same_and_not_same

from ArWikiCats import resolve_arabic_category_label

data_virginia2_1 = {
    "Category:Baptists from West Virginia": "تصنيف:معمدانيون من فرجينيا الغربية",
    "Category:Defunct private universities and colleges in West Virginia": "تصنيف:جامعات وكليات خاصة سابقة في فرجينيا الغربية"

}

data_virginia2_3 = {
    "Category:19th-century West Virginia state court judges": "تصنيف:قضاة محكمة ولاية فرجينيا الغربية القرن 19",
    "Category:20th-century West Virginia state court judges": "تصنيف:قضاة محكمة ولاية فرجينيا الغربية القرن 20",
    "Category:21st century in Virginia": "تصنيف:سنوات القرن 21 في فرجينيا",
    "Category:Actors from Alexandria, Virginia": "تصنيف:ممثلون وممثلات من الإسكندرية (فرجينيا)",
    "Category:Adaptations of works by Virginia Woolf": "تصنيف:تكييفات أعمال فرجينيا وولف",
    "Category:African-American people in West Virginia politics": "تصنيف:أعلام أمريكيون أفارقة في سياسة فرجينيا الغربية",
    "Category:Alumni by university or college in Virginia": "تصنيف:خريجون حسب الكلية أو الجامعة في فرجينيا",
    "Category:Architecture in West Virginia": "تصنيف:عمارة في فرجينيا الغربية",
    "Category:Buildings and structures in Pocahontas County, West Virginia": "تصنيف:مبان ومنشآت في مقاطعة بوكاهونتس، فرجينيا الغربية",
    "Category:Census-designated places in Campbell County, Virginia": "تصنيف:مناطق إحصاء سكاني في مقاطعة كامبل (فرجينيا)",
    "Category:Census-designated places in Henry County, Virginia": "تصنيف:مناطق إحصاء سكاني في مقاطعة هنري (فرجينيا)",
    "Category:Census-designated places in Tazewell County, Virginia": "تصنيف:مناطق إحصاء سكاني في مقاطعة تازويل (فرجينيا)",
    "Category:Census-designated places in Wetzel County, West Virginia": "تصنيف:مناطق إحصاء سكاني في مقاطعة ويتزل، فرجينيا الغربية",
    "Category:Coaches of American football from West Virginia": "تصنيف:مدربو كرة القدم الأمريكية من فرجينيا الغربية",
    "Category:Demographics of Virginia": "تصنيف:سكان فرجينيا",
    "Category:Education in Williamsburg, Virginia": "تصنيف:تعليم في ويليامزبرغ (فرجينيا)",
    "Category:Faculty by university or college in Virginia": "تصنيف:أعضاء هيئة التدريس حسب الجامعة أو الكلية في فرجينيا",
    "Category:Faculty by university or college in West Virginia": "تصنيف:أعضاء هيئات تدريس حسب الجامعة أو الكلية في فرجينيا الغربية",
    "Category:Films set in Alexandria, Virginia": "تصنيف:أفلام تقع أحداثها في الإسكندرية، فرجينيا",
    "Category:Geography of Charlottesville, Virginia": "تصنيف:جغرافيا شارلوتسفيل (فرجينيا)",
    "Category:History of Jefferson County, West Virginia": "تصنيف:تاريخ مقاطعة جيفيرسون، فرجينيا الغربية",
    "Category:Jews from West Virginia": "تصنيف:يهود أمريكيون من فرجينيا الغربية",
    "Category:Male actors from Alexandria, Virginia": "تصنيف:ممثلون من الإسكندرية (فرجينيا)",
    "Category:Male actors from Virginia": "تصنيف:ممثلون من ولاية فرجينيا",
    "Category:Mayors of Williamsburg, Virginia": "تصنيف:عمدات في ويليامزبرغ (فرجينيا)",
    "Category:Motorsport in West Virginia": "تصنيف:رياضة المحركات في فرجينيا الغربية",
    "Category:Musicians from West Virginia by populated place": "تصنيف:موسيقيون حسب المكان المأهول في فرجينيا الغربية",
    "Category:Parks in Charlottesville, Virginia": "تصنيف:متنزهات في شارلوتسفيل (فرجينيا)",
    "Category:Public education in West Virginia": "تصنيف:تعليم حكومي في فرجينيا الغربية",
    "Category:Singer-songwriters from West Virginia": "تصنيف:مغنون وكتاب أغان من فرجينيا الغربية",
    "Category:Soccer players from Alexandria, Virginia": "تصنيف:لاعبو كرة قدم من الإسكندرية، فرجينيا",
    "Category:Towns in Accomack County, Virginia": "تصنيف:بلدات مقاطعة أكوماك (فرجينيا)",
    "Category:Towns in Botetourt County, Virginia": "تصنيف:بلدات مقاطعة بوتيتورت (فرجينيا)",
    "Category:Towns in Brunswick County, Virginia": "تصنيف:بلدات مقاطعة برونزويك (فرجينيا)",
    "Category:Towns in Franklin County, Virginia": "تصنيف:بلدات مقاطعة فرانكلين (فرجينيا)",
    "Category:Towns in Grayson County, Virginia": "تصنيف:بلدات مقاطعة غرايسون (فرجينيا)",
    "Category:Towns in Halifax County, Virginia": "تصنيف:بلدات مقاطعة هاليفاكس (فرجينيا)",
    "Category:Towns in Loudoun County, Virginia": "تصنيف:بلدات مقاطعة لودون (فرجينيا)",
    "Category:Towns in Middlesex County, Virginia": "تصنيف:بلدات مقاطعة ميديلسكس (فرجينيا)",
    "Category:Towns in Southampton County, Virginia": "تصنيف:بلدات مقاطعة ساوثهامبتون (فرجينيا)",
    "Category:Towns in Tazewell County, Virginia": "تصنيف:بلدات مقاطعة تازويل (فرجينيا)",
    "Category:Towns in West Virginia": "تصنيف:بلدات ولاية فرجينيا الغربية",
    "Category:Towns in Wythe County, Virginia": "تصنيف:بلدات مقاطعة وايذ (فرجينيا)",
    "Category:Victorian architecture in West Virginia": "تصنيف:عمارة فيكتورية في فرجينيا الغربية",
    "Category:West Virginia Republicans": "تصنيف:جمهوريون من ولاية فرجينيا الغربية",
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
    "Category:1607 establishments in the Colony of Virginia": "x",
    "Category:1648 establishments in the Colony of Virginia": "x",
    "Category:1651 establishments in the Colony of Virginia": "x",
    "Category:1671 establishments in the Colony of Virginia": "x",
    "Category:1673 establishments in the Colony of Virginia": "x",
    "Category:1759 establishments in the Colony of Virginia": "x",
    "Category:Buildings and structures in Falls Church, Virginia": "x",
    "Category:Eastern Virginia Medical School alumni": "x",
    "Category:Isle of Wight County, Virginia": "x",
    "Category:Politicians from Falls Church, Virginia": "x",
    "Category:Sportspeople from Falls Church, Virginia": "x",
    "Category:University of Virginia School of Medicine alumni": "x",
    "Category:University of Virginia School of Medicine faculty": "x",
    "Category:Virginia Beach Mariners players": "x",
    "Category:Virginia Military Institute alumni": "x",
    "Category:Virginia Tech alumni": "x",
    "Category:West Virginia United players": "x",
}

to_test = [
    ("test_virginia2_1", data_virginia2_1),
    ("test_virginia2_3", data_virginia2_3),
    ("test_virginia2_4", data_virginia2_4),
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

    dump_diff(diff_result, name)
    # dump_same_and_not_same(data, diff_result, name, True)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
