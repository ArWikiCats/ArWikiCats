#
import pytest
from load_one_data import dump_diff, one_dump_test

from src import resolve_arabic_category_label
from src.translations.geo.us_counties import (
    US_STATES_NAME_TRANSLATIONS,
    normalize_state,
)

test_data = {
    "Category:{en} in the War of 1812": "تصنيف:{ar} في حرب 1812",
    "Category:{en} Democrats": "تصنيف:ديمقراطيون من ولاية {ar}",
    "Category:{en} lawyers": "تصنيف:محامون من ولاية {ar}",
    "Category:{en} state court judges": "تصنيف:قضاة محكمة ولاية {ar}",
    "Category:{en} state courts": "تصنيف:محكمة ولاية {ar}",
    "Category:{en} state senators": "تصنيف:أعضاء مجلس شيوخ ولاية {ar}",

    "Category:{en} attorneys general": "تصنيف:مدعي {ar} العام",
    "Category:{en} ballot measures": "تصنيف:إجراءات اقتراع {ar}",
    "Category:{en} city councils": "تصنيف:مجالس مدن {ar}",
    "Category:{en} counties": "تصنيف:مقاطعات {ar}",
    "Category:{en} Democratic-Republicans": "تصنيف:أعضاء الحزب الديمقراطي الجمهوري في {ar}",
    "Category:{en} elections": "تصنيف:انتخابات {ar}",
    "Category:{en} elections by decade": "تصنيف:انتخابات {ar} حسب العقد",
    "Category:{en} elections by year": "تصنيف:انتخابات {ar} حسب السنة",
    "Category:{en} Federalists": "تصنيف:أعضاء الحزب الفيدرالي الأمريكي في {ar}",
    "Category:{en} Greenbacks": "تصنيف:أعضاء حزب الدولار الأمريكي في {ar}",
    "Category:{en} Greens": "تصنيف:أعضاء حزب الخضر في {ar}",
    "Category:{en} gubernatorial elections": "تصنيف:انتخابات حاكم {ar}",
    "Category:{en} independents": "تصنيف:أعضاء في {ar}",
    "Category:{en} in fiction": "تصنيف:{ar} في الخيال",
    "Category:{en} in fiction by city": "تصنيف:{ar} في الخيال حسب المدينة",
    "Category:{en} in the American Civil War": "تصنيف:{ar} في الحرب الأهلية الأمريكية",
    "Category:{en} in the American Revolution": "تصنيف:{ar} في الثورة الأمريكية",
    "Category:{en} Jacksonians": "تصنيف:أعضاء جاكسونيون في {ar}",
    "Category:{en} Know Nothings": "تصنيف:أعضاء حزب لا أدري في {ar}",
    "Category:{en} law": "تصنيف:قانون {ar}",
    "Category:{en} law-related lists": "تصنيف:قوائم متعلقة بقانون {ar}",
    "Category:{en} local politicians": "تصنيف:سياسيون محليون في {ar}",
    "Category:{en} navigational boxes": "تصنيف:صناديق تصفح {ar}",
    "Category:{en} politicians": "تصنيف:سياسيو {ar}",
    "Category:{en} politicians by century": "تصنيف:سياسيو {ar} حسب القرن",
    "Category:{en} politicians by party": "تصنيف:سياسيو {ar} حسب الحزب",
    "Category:{en} politicians by populated place": "تصنيف:سياسيو {ar} حسب المكان المأهول",
    "Category:{en} politicians convicted of crimes": "تصنيف:سياسيو {ar} أدينوا بجرائم",
    "Category:{en} politics-related lists": "تصنيف:قوائم متعلقة بسياسة {ar}",
    "Category:{en}-related lists": "تصنيف:قوائم متعلقة ب{ar}",
    "Category:{en} Republicans": "تصنيف:أعضاء الحزب الجمهوري في {ar}",
    "Category:{en} sheriffs": "تصنيف:مأمورو {ar}",
    "Category:{en} socialists": "تصنيف:أعضاء الحزب الاشتراكي في {ar}",
    "Category:{en} templates": "تصنيف:قوالب {ar}",
    "Category:{en} Unionists": "تصنيف:أعضاء الحزب الوحدوي في {ar}",
    "Category:{en} Whigs": "تصنيف:أعضاء حزب اليمين في {ar}",
}

data_1 = {
    "iowa": {},
    "montana": {},
    "georgia (u.s. state)": {},
    "nebraska": {},
    "wisconsin": {},
    "new mexico": {},
    "arizona": {},
}

for en in data_1.keys():
    if US_STATES_NAME_TRANSLATIONS.get(en):
        ar = US_STATES_NAME_TRANSLATIONS.get(en)
        data_1[en] = {
            x.format(en=en): normalize_state(v.format(ar=ar))
            for x, v in test_data.items()
        }


to_test = [
    (f"test_us_counties_{x}", v) for x, v in data_1.items()
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.slow
def test_all_dump(name, data):

    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


@pytest.mark.parametrize("input,expected", data_1["iowa"].items(), ids=[x for x in data_1["iowa"]])
@pytest.mark.slow
def test_iowa(input, expected):
    result = resolve_arabic_category_label(input)
    assert result == expected


@pytest.mark.parametrize("input,expected", data_1["montana"].items(), ids=[x for x in data_1["montana"]])
@pytest.mark.slow
def test_montana(input, expected):
    result = resolve_arabic_category_label(input)
    assert result == expected


@pytest.mark.parametrize(
    "input,expected", data_1["georgia (u.s. state)"].items(), ids=[x for x in data_1["georgia (u.s. state)"]]
)
@pytest.mark.slow
def test_georgia(input, expected):
    result = resolve_arabic_category_label(input)
    assert result == expected


@pytest.mark.parametrize("input,expected", data_1["nebraska"].items(), ids=[x for x in data_1["nebraska"]])
@pytest.mark.slow
def test_nebraska(input, expected):
    result = resolve_arabic_category_label(input)
    assert result == expected


@pytest.mark.parametrize("input,expected", data_1["wisconsin"].items(), ids=[x for x in data_1["wisconsin"]])
@pytest.mark.slow
def test_wisconsin(input, expected):
    result = resolve_arabic_category_label(input)
    assert result == expected


@pytest.mark.parametrize("input,expected", data_1["new mexico"].items(), ids=[x for x in data_1["new mexico"]])
@pytest.mark.slow
def test_new_mexico(input, expected):
    result = resolve_arabic_category_label(input)
    assert result == expected


@pytest.mark.parametrize("input,expected", data_1["arizona"].items(), ids=[x for x in data_1["arizona"]])
@pytest.mark.slow
def test_arizona(input, expected):
    result = resolve_arabic_category_label(input)
    assert result == expected


empty_data = {
    "Category:Georgia (U.S. state) Attorney General elections": "",
    "Category:Georgia (U.S. state) case law": "",
    "Category:Georgia (U.S. state) city council members": "",
    "Category:Georgia (U.S. state) city user templates": "",
    "Category:Georgia (U.S. state) college and university user templates": "",
    "Category:Georgia (U.S. state) commissioners of agriculture": "",
    "Category:Georgia (U.S. state) Constitutional Unionists": "",
    "Category:Georgia (U.S. state) county navigational boxes": "",
    "Category:Georgia (U.S. state) culture by city": "",
    "Category:Georgia (U.S. state) education navigational boxes": "",
    "Category:Georgia (U.S. state) education-related lists": "",
    "Category:Georgia (U.S. state) election templates": "",
    "Category:Georgia (U.S. state) geography-related lists": "",
    "Category:Georgia (U.S. state) government navigational boxes": "",
    "Category:Georgia (U.S. state) high school athletic conference navigational boxes": "",
    "Category:Georgia (U.S. state) history-related lists": "",
    "Category:Georgia (U.S. state) judicial elections": "",
    "Category:Georgia (U.S. state) labor commissioners": "",
    "Category:Georgia (U.S. state) legislative districts": "",
    "Category:Georgia (U.S. state) legislative sessions": "",
    "Category:Georgia (U.S. state) Libertarians": "",
    "Category:Georgia (U.S. state) lieutenant gubernatorial elections": "",
    "Category:Georgia (U.S. state) location map modules": "",
    "Category:Georgia (U.S. state) maps": "",
    "Category:Georgia (U.S. state) mass media navigational boxes": "",
    "Category:Georgia (U.S. state) militia": "",
    "Category:Georgia (U.S. state) militiamen in the American Revolution": "",
    "Category:Georgia (U.S. state) National Republicans": "",
    "Category:Georgia (U.S. state) Oppositionists": "",
    "Category:Georgia (U.S. state) placenames of Native American origin": "",
    "Category:Georgia (U.S. state) Populists": "",
    "Category:Georgia (U.S. state) portal": "",
    "Category:Georgia (U.S. state) postmasters": "",
    "Category:Georgia (U.S. state) presidential primaries": "",
    "Category:Georgia (U.S. state) Progressives (1912)": "",
    "Category:Georgia (U.S. state) Prohibitionists": "",
    "Category:Georgia (U.S. state) radio market navigational boxes": "",
    "Category:Georgia (U.S. state) railroads": "",
    "Category:Georgia (U.S. state) Sea Islands": "",
    "Category:Georgia (U.S. state) shopping mall templates": "",
    "Category:Georgia (U.S. state) society": "",
    "Category:Georgia (U.S. state) special elections": "",
    "Category:Georgia (U.S. state) sports-related lists": "",
    "Category:Georgia (U.S. state) state constitutional officer elections": "",
    "Category:Georgia (U.S. state) state forests": "",
    "Category:Georgia (U.S. state) statutes": "",
    "Category:Georgia (U.S. state) television station user templates": "",
    "Category:Georgia (U.S. state) transportation-related lists": "",
    "Category:Georgia (U. S. state) universities and colleges leaders navigational boxes": "",
    "Category:Georgia (U.S. state) universities and colleges navigational boxes": "",
    "Category:Georgia (U.S. state) user categories": "",
    "Category:Georgia (U.S. state) user templates": "",
    "Category:Georgia (U.S. state) Wikipedians": "",
    "Category:Georgia (U.S. state) wine": "",
}


@pytest.mark.fast
def test_us_counties_empty():
    expected, diff_result = one_dump_test(empty_data, resolve_arabic_category_label)

    dump_diff(diff_result, "test_us_counties_empty")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
