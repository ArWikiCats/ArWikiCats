#
import pytest
from load_one_data import dump_diff, one_dump_test
from ArWikiCats import resolve_arabic_category_label
from ArWikiCats.main_processers.main_resolve import resolve_label_ar

data_1 = {
    "senate (france)": "مجلس الشيوخ الفرنسي",
    "senate (netherlands)": "مجلس الشيوخ (هولندا)",
    "senate of canada": "مجلس الشيوخ الكندي",
    "senate of iran": "مجلس سنا",
    "senate of spain": "مجلس الشيوخ الإسباني",

    "parliament of egypt": "البرلمان المصري",
    "parliament of greenland": "برلمان جرينلاند",
    "parliament of india": "برلمان الهند",
    "parliament of jordan": "مجلس الأمة الأردني",
    "parliament of pakistan": "مجلس شورى باكستان",
    "parliament of romania": "البرلمان الروماني",
    "parliament of united kingdom": "برلمان المملكة المتحدة",

    "supreme court of afghanistan": "المحكمة العليا الأفغانية",
    "supreme court of india": "المحكمة العليا الهندية",
    "supreme court of indonesia": "المحكمة العليا الإندونيسية",
    "supreme court of israel": "المحكمة العليا (إسرائيل)",
    "supreme court of japan": "المحكمة العليا اليابانية",
    "supreme court of sri lanka": "المحكمة العليا السيريلانكية",
    "supreme court of united states": "المحكمة العليا للولايات المتحدة",
}

data_2 = {

    "malaysian nationality law": "قانون الجنسية الماليزي",
    "maryland general assembly": "مجلس النواب في ماريلند",
    "media law": "قانون إعلام",
    "ministry of defence (ukraine)": "وزارة الدفاع (أوكرانيا)",
    "ministry of foreign affairs of people's republic of china": "وزارة الخارجية لجمهورية الصين الشعبية",
    "ministry of higher education and scientific research (jordan)": "وزارة التعليم العالي والبحث العلمي (الأردن)",
    "ministry of intelligence": "وزارة الاستخبارات والأمن الوطني (إيران)",
    "ministry of national defense (colombia)": "وزارة الدفاع (كولومبيا)",
    "mitt romney presidential campaign, 2012": "حملة ميت رومني الرئاسية 2012",
    "national assembly (france)": "الجمعية الوطنية الفرنسية",
    "national assembly of pakistan": "المجلس الوطني الباكستاني",
    "natural law": "حق طبيعي",
    "o. j. simpson murder case": "قضية جريمة أو جاي سيمبسون",
    "one-child policy": "سياسة الطفل الواحد",
    "open government": "الحوكمة المفتوحة",
    "permanent court of international justice": "المحكمة الدائمة للعدل الدولي",
    "podemos (spanish political party)": "بوديموس",
    "polish presidential election, 2010": "الانتخابات الرئاسية البولندية 2010",
    "politics of abruzzo": "سياسة أبروتسو",
    "politics of emilia-romagna": "سياسة إميليا رومانيا",
    "politics of sicily": "سياسة صقلية",
    "politics of umbria": "سياسة أومبريا",
    "privacy law": "قانون الخصوصية",
    "russian provisional government": "حكومة روسيا المؤقتة",
    "sociology of law": "علم اجتماع القانون",
    "special court for sierra leone": "المحكمة الخاصة بسيراليون",
    "supreme people's assembly": "الجمعية الشعبية العليا",
    "supreme people's court": "المحكمة الشعبية العليا",
    "syrian interim government": "الحكومة السورية المؤقتة",
    "thing (assembly)": "ثينج",
    "treaty of brest-litovsk": "معاهدة برست ليتوفسك",
    "treaty of nanking": "معاهدة نانجينغ",
    "turkish general election, june 2015": "الانتخابات التشريعية التركية يونيو 2015",
    "turkish general election, november 2015": "الانتخابات التشريعية التركية نوفمبر 2015",
    "united kingdom general election, 2010": "انتخابات المملكة المتحدة لعام 2010",
    "united kingdom general election, 2017": "الانتخابات التشريعية البريطانية 2017",
    "united states presidential election, 1860": "انتخابات الرئاسة الأمريكية 1860",
    "united states presidential election, 1880": "الانتخابات الرئاسية الأمريكية عام 1880",
    "united states presidential election, 2008": "انتخابات الرئاسة الأمريكية 2008",
    "united states presidential election, 2012": "انتخابات الرئاسة الأمريكية 2012",
    "united states presidential election, 2016": "انتخابات الرئاسة الأمريكية 2016"
}

to_test = [
    ("test_yy2_non_1", data_1),
    ("test_yy2_non_2", data_2),
]


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
def test_yy2_non_1(category: str, expected: str) -> None:
    assert resolve_label_ar(category) == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)

    # add_result = {x: v for x, v in data.items() if x in diff_result and "" == diff_result.get(x)}
    # dump_diff(add_result, f"{name}_add")
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
