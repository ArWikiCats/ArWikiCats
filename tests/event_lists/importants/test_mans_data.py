#
import pytest
from load_one_data import dump_diff, dump_diff_text, one_dump_test, dump_same_and_not_same

from ArWikiCats import resolve_label_ar

from ArWikiCats.new_resolvers.sports_resolvers.nationalities_and_sports import resolve_nats_sport_multi_v2

data0 = {

    "yemeni women's rugby union": "اتحاد الرجبي اليمني للنساء",
    "yemeni rugby union leagues": "اتحاد دوري الرجبي اليمني",

    "yemeni indoor rugby league": "الدوري اليمني للرجبي داخل الصالات",
    "yemeni indoor wheelchair rugby league": "الدوري اليمني للرجبي على الكراسي المتحركة داخل الصالات",
    "yemeni major indoor rugby league": "الدوري الرئيسي اليمني للرجبي داخل الصالات",
    "yemeni major indoor wheelchair rugby league": "الدوري الرئيسي اليمني للرجبي على الكراسي المتحركة داخل الصالات",
    "yemeni outdoor rugby league": "الدوري اليمني للرجبي في الهواء الطلق",
    "yemeni outdoor wheelchair rugby league": "الدوري اليمني للرجبي على الكراسي المتحركة في الهواء الطلق",
    "yemeni professional rugby league": "دوري الرجبي اليمني للمحترفين",
    "yemeni professional wheelchair rugby league": "دوري الرجبي على الكراسي المتحركة اليمني للمحترفين",
    "yemeni rugby league administrators": "مدراء الدوري اليمني للرجبي",
    "yemeni rugby league players": "لاعبو الدوري اليمني للرجبي",
    "yemeni wheelchair rugby league": "الدوري اليمني للرجبي على الكراسي المتحركة",
    "yemeni wheelchair rugby league administrators": "مدراء الدوري اليمني للرجبي على الكراسي المتحركة",
    "yemeni wheelchair rugby league players": "لاعبو الدوري اليمني للرجبي على الكراسي المتحركة",
    "yemeni wheelchair rugby league playerss": "لاعبو الدوري اليمني للرجبي على الكراسي المتحركة",
    "yemeni women's rugby league": "الدوري اليمني للرجبي للسيدات",
    "yemeni women's wheelchair rugby league": "الدوري اليمني للرجبي على الكراسي المتحركة للسيدات",
}

data1 = {
    "australian rugby union": "اتحاد الرجبي الأسترالي",
    "australian women's ice hockey league": "الدوري الأسترالي لهوكي الجليد للسيدات",
    "british rugby union": "اتحاد الرجبي البريطاني",
    "egyptian league": "الدوري المصري",
    "english football league": "الدوري الإنجليزي لكرة القدم",
    "english rugby league": "الدوري الإنجليزي للرجبي",
    "french rugby league": "الدوري الفرنسي للرجبي",
    "french rugby union": "اتحاد الرجبي الفرنسي",
    "hong kong fa cup": "كأس الاتحاد الهونغ الكونغي",
    "indian federation cup": "كأس الاتحاد الهندي",
    "italian rugby union": "اتحاد الرجبي الإيطالي",
    "lebanese federation cup": "كأس الاتحاد اللبناني",
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
    ("test_mans_data_0", data0, resolve_label_ar),
    ("test_mans_data_1", data1, resolve_nats_sport_multi_v2),
    ("test_mans_data_3", data_3, resolve_nats_sport_multi_v2),
    ("test_mans_data_4", data_4, resolve_nats_sport_multi_v2),
]


@pytest.mark.parametrize("category, expected", data0.items(), ids=data0.keys())
def test_mans_data_0(category: str, expected: str) -> None:
    assert resolve_label_ar(category) == expected


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
def test_mans_data_1(category: str, expected: str) -> None:
    assert resolve_nats_sport_multi_v2(category) == expected


@pytest.mark.parametrize("category, expected", data_3.items(), ids=data_3.keys())
def test_mans_data_3(category: str, expected: str) -> None:
    assert resolve_nats_sport_multi_v2(category) == expected


@pytest.mark.parametrize("name,data,callback", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)

    # dump_diff_text (expected, diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
