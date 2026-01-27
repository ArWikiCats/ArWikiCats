
from ArWikiCats.new_resolvers.sports_resolvers.nationalities_and_sports import resolve_nats_sport_multi_v2
from utils.dump_runner import make_dump_test_name_data_callback
from utils.resolver_runner import make_resolver_fast_test

data1 = {
    "yemeni major indoor wheelchair football league": "الدوري الرئيسي اليمني لكرة القدم على الكراسي المتحركة داخل الصالات",
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
    "welsh rugby league": "الدوري الويلزي للرجبي",
}

data_2 = {
    "argentine grand prix": "جائزة الأرجنتين الكبرى",
    "british open": "المملكة المتحدة المفتوحة",
    "croatian ice hockey league": "الدوري الكرواتي لهوكي الجليد",
    "eritrean premier league": "الدوري الإريتري الممتاز",
    "french rugby union leagues": "اتحاد دوري الرجبي الفرنسي",
    "irish league": "الدوري الأيرلندي",
    "saudi super cup": "كأس السوبر السعودي",
}

data_3 = {}

data_4 = {}

to_test = [
    ("test_mans_data_1", data1, resolve_nats_sport_multi_v2),
    ("test_mans_data_3", data_3, resolve_nats_sport_multi_v2),
    ("test_mans_data_4", data_4, resolve_nats_sport_multi_v2),
]

test_mans_data_1 = make_resolver_fast_test(
    resolver=resolve_nats_sport_multi_v2,
    data=data1,
    test_name="test_mans_data_1",
)

test_mans_data_3 = make_resolver_fast_test(
    resolver=resolve_nats_sport_multi_v2,
    data=data_3,
    test_name="test_mans_data_3",
)
test_mans_data_4 = make_resolver_fast_test(
    resolver=resolve_nats_sport_multi_v2,
    data=data_4,
    test_name="test_mans_data_4",
)

test_dump_all = make_dump_test_name_data_callback(to_test, run_same=True)
