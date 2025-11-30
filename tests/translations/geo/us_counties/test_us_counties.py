#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label
from ArWikiCats.translations_resolvers.us_states import _STATE_SUFFIX_TEMPLATES_BASE, normalize_state
from ArWikiCats.translations import US_STATES


test_data_keys = {
    # "{en} republicans": "أعضاء الحزب الجمهوري في {ar}",
    "{en} counties": "مقاطعات {ar}",
    "{en} democratic-republicans": "أعضاء الحزب الديمقراطي الجمهوري في {ar}",
    "{en} elections by decade": "انتخابات {ar} حسب العقد",
    "{en} elections by year": "انتخابات {ar} حسب السنة",
    "{en} elections": "انتخابات {ar}",
    "{en} federalists": "أعضاء الحزب الفيدرالي الأمريكي في {ar}",
    "{en} greenbacks": "أعضاء حزب الدولار الأمريكي في {ar}",
    "{en} greens": "أعضاء حزب الخضر في {ar}",
    "{en} in fiction by city": "{ar} في الخيال حسب المدينة",
    "{en} in fiction": "{ar} في الخيال",
    "{en} in the american civil war": "{ar} في الحرب الأهلية الأمريكية",
    "{en} in the american revolution": "{ar} في الثورة الأمريكية",
    "{en} independents": "أعضاء في {ar}",
    "{en} know nothings": "أعضاء حزب لا أدري في {ar}",
    "{en} law-related lists": "قوائم متعلقة بقانون {ar}",
    "{en} navigational boxes": "صناديق تصفح {ar}",
    "{en} politicians by century": "سياسيو {ar} حسب القرن",
    "{en} politicians by party": "سياسيو {ar} حسب الحزب",
    "{en} politicians by populated place": "سياسيو {ar} حسب المكان المأهول",
    "{en} politicians convicted of crimes": "سياسيو {ar} أدينوا بجرائم",
    "{en} politics-related lists": "قوائم متعلقة بسياسة {ar}",
    "{en} socialists": "أعضاء الحزب الاشتراكي في {ar}",
    "{en} templates": "قوالب {ar}",
    "{en} unionists": "أعضاء الحزب الوحدوي في {ar}",
    "{en} whigs": "أعضاء حزب اليمين في {ar}",
    "{en}-related lists": "قوائم متعلقة ب{ar}",
}

test_data_keys.update(_STATE_SUFFIX_TEMPLATES_BASE)
if "{en} republicans" in test_data_keys:
    del test_data_keys["{en} republicans"]

all_test_data={}

data_1={
    "iowa": {},
    "montana": {},
    "georgia (u.s. state)": {},
    "nebraska": {},
    "wisconsin": {},
    "new mexico": {},
    "arizona": {},
}

for en in data_1.keys():
    if US_STATES.get(en):
        ar=US_STATES.get(en)
        test_one={
            f"Category:{x.format(en=en)}": f"تصنيف:{normalize_state(v.format(ar=ar))}"
            for x, v in test_data_keys.items()
        }
        data_1[en]=test_one
        all_test_data.update(test_one)


to_test=[
    (f"test_us_counties_{x}", v) for x, v in data_1.items()
]

to_test.append(("test_all_test_data", all_test_data))


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_all_dump(name: str, data: dict[str, str]) -> None:

    expected, diff_result=one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


@pytest.mark.parametrize("input,expected", all_test_data.items(), ids=[x for x in all_test_data])
@pytest.mark.slow
def test_all_data(input, expected) -> None:
    result=resolve_arabic_category_label(input)
    assert result == expected


empty_data={
    "Category:Georgia (U.S. state) National Republicans": "تصنيف:أعضاء الحزب الجمهوري الوطني في ولاية جورجيا",
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


@pytest.mark.dump
def test_us_counties_empty() -> None:
    expected, diff_result=one_dump_test(empty_data, resolve_arabic_category_label)

    dump_diff(diff_result, "test_us_counties_empty")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
