#
import pytest
from load_one_data import dump_diff, dump_diff_text, one_dump_test

from ArWikiCats import resolve_label_ar

data0 = {}

data1 = {
    "australian rugby union": "اتحاد الرجبي الأسترالي",
    "australian women's ice hockey league": "الدوري الأسترالي لهوكي الجليد للسيدات",
    "brazilian rugby league players": "لاعبو الدوري البرازيلي للرجبي",
    "british rugby union": "اتحاد الرجبي البريطاني",
    "canadian military": "الجيش الكندي",
    "egyptian league": "الدوري المصري",
    "english football league": "الدوري الإنجليزي لكرة القدم",
    "english rugby league": "الدوري الإنجليزي للرجبي",
    "french rugby league": "الدوري الفرنسي للرجبي",
    "french rugby union": "اتحاد الرجبي الفرنسي",
    "hong kong fa cup": "كأس الاتحاد الهونغ الكونغي",
    "indian federation cup": "كأس الاتحاد الهندي",
    "italian rugby union": "اتحاد الرجبي الإيطالي",
    "japanese army": "الجيش الياباني",
    "lebanese federation cup": "كأس الاتحاد اللبناني",
    "moroccan army": "الجيش المغربي",
    "north american hockey league": "الدوري الأمريكي الشمالي للهوكي",
    "north american soccer league": "الدوري الأمريكي الشمالي لكرة القدم",
    "oceanian rugby union": "اتحاد الرجبي الأوقيانوسي",
    "russian rugby union": "اتحاد الرجبي الروسي",
    "south american rugby union": "اتحاد الرجبي الأمريكي الجنوبي",
    "welsh rugby league": "الدوري الويلزي للرجبي"
}

data_2 = {
    "argentine grand prix": "جائزة الأرجنتين الكبرى",
    "british open": "المملكة المتحدة المفتوحة",
    "canadian labour law": "قانون العمل الكندي",
    "croatian ice hockey league": "الدوري الكرواتي لهوكي الجليد",
    "eritrean premier league": "الدوري الإريتري الممتاز",
    "french rugby union leagues": "اتحاد دوري الرجبي الفرنسي",
    "irish league": "الدوري الأيرلندي",
    "saudi super cup": "كأس السوبر السعودي"
}

data_3 = {
}

data_4 = {
}

to_test = [
    ("test_mans_data_0", data0),
    ("test_mans_data_1", data1),
    ("test_mans_data_3", data_3),
    ("test_mans_data_4", data_4),
]


@pytest.mark.parametrize("category, expected", data0.items(), ids=data0.keys())
def test_mans_data_0(category: str, expected: str) -> None:
    assert resolve_label_ar(category) == expected


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
def test_mans_data_1(category: str, expected: str) -> None:
    assert resolve_label_ar(category) == expected


@pytest.mark.parametrize("category, expected", data_3.items(), ids=data_3.keys())
def test_mans_data_3(category: str, expected: str) -> None:
    assert resolve_label_ar(category) == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)

    # dump_diff_text (expected, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
