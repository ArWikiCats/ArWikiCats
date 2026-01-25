#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

data_1 = {
    "senate of canada": "مجلس شيوخ كندا",
    "senate of iran": "مجلس شيوخ إيران",
    "senate of spain": "مجلس شيوخ إسبانيا",
    "parliament of egypt": "برلمان مصر",
    "parliament of romania": "برلمان رومانيا",
    "senate (france)": "مجلس الشيوخ (فرنسا)",
    "senate (netherlands)": "مجلس الشيوخ (هولندا)",
    "parliament of greenland": "برلمان جرينلاند",
    "parliament of india": "برلمان الهند",
    "parliament of united kingdom": "برلمان المملكة المتحدة",
    "supreme court of israel": "المحكمة العليا الإسرائيلية",
    "supreme court of sri lanka": "المحكمة العليا السريلانكية",
    "supreme court of united states": "المحكمة العليا الأمريكية",
    "supreme court of afghanistan": "المحكمة العليا الأفغانية",
    "supreme court of india": "المحكمة العليا الهندية",
    "supreme court of indonesia": "المحكمة العليا الإندونيسية",
    "supreme court of japan": "المحكمة العليا اليابانية",
    "maryland general assembly": "جمعية ماريلند العامة",
    "politics of emilia-romagna": "سياسة إميليا-رومانيا",
    "malaysian nationality law": "قانون الجنسية الماليزي",
    "united states presidential election 1860": "انتخابات الرئاسة الأمريكية 1860",
    "united states presidential election 1880": "انتخابات الرئاسة الأمريكية 1880",
    "united states presidential election 2008": "انتخابات الرئاسة الأمريكية 2008",
    "united states presidential election 2012": "انتخابات الرئاسة الأمريكية 2012",
    "united states presidential election 2016": "انتخابات الرئاسة الأمريكية 2016",
}

data_2 = {
    "media law": "قانون إعلام",
    "ministry of defence (ukraine)": "وزارة الدفاع (أوكرانيا)",
    "ministry of foreign affairs of people's republic of china": "وزارة الخارجية لجمهورية الصين الشعبية",
    "ministry of higher education and scientific research (jordan)": "وزارة التعليم العالي والبحث العلمي (الأردن)",
    "ministry of intelligence": "وزارة الاستخبارات والأمن الوطني (إيران)",
    "ministry of national defense (colombia)": "وزارة الدفاع (كولومبيا)",
    "mitt romney presidential campaign, 2012": "حملة ميت رومني الرئاسية 2012",
    "national assembly of pakistan": "الجمعية الوطنية الباكستانية",
    "natural law": "حق طبيعي",
    "o. j. simpson murder case": "قضية جريمة أو جاي سيمبسون",
    "one-child policy": "سياسة الطفل الواحد",
    "open government": "الحوكمة المفتوحة",
    "permanent court of international justice": "المحكمة الدائمة للعدل الدولي",
    "podemos (spanish political party)": "بوديموس",
    "politics of abruzzo": "سياسة أبروتسو",
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
}

to_test = [
    ("test_yy2_non_1", data_1),
    # ("test_yy2_non_2", data_2),
]


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
def test_yy2_non_1(category: str, expected: str) -> None:
    assert resolve_label_ar(category) == expected


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=False)
