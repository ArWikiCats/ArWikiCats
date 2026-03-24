#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar
from ArWikiCats.new_resolvers.countries_names_resolvers.us_states import _STATE_SUFFIX_TEMPLATES_BASE, normalize_state
from ArWikiCats.translations import US_STATES
from utils.dump_runner import make_dump_test_name_data

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

all_test_data = {}

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
    if US_STATES.get(en):
        ar = US_STATES.get(en)
        test_one = {f"{x.format(en=en)}": f"{normalize_state(v.format(ar=ar))}" for x, v in test_data_keys.items()}
        data_1[en] = test_one
        all_test_data.update(test_one)


@pytest.mark.parametrize("input_text,expected", all_test_data.items(), ids=all_test_data.keys())
@pytest.mark.slow
def test_all_data(input_text: str, expected: str) -> None:
    result = resolve_label_ar(input_text)
    assert result == expected


empty_data = {
    "Georgia (U.S. state) government navigational boxes": "صناديق تصفح حكومة ولاية جورجيا",
    "Georgia (U.S. state) National Republicans": "أعضاء الحزب الجمهوري الوطني في ولاية جورجيا",
    "Georgia (U.S. state) Attorney General elections": "",
    "Georgia (U.S. state) case law": "",
    "Georgia (U.S. state) city council members": "",
    "Georgia (U.S. state) city user templates": "",
    "Georgia (U.S. state) college and university user templates": "",
    "Georgia (U.S. state) commissioners of agriculture": "",
    "Georgia (U.S. state) Constitutional Unionists": "",
    "Georgia (U.S. state) county navigational boxes": "",
    "Georgia (U.S. state) culture by city": "",
    "Georgia (U.S. state) education navigational boxes": "",
    "Georgia (U.S. state) education-related lists": "",
    "Georgia (U.S. state) election templates": "",
    "Georgia (U.S. state) geography-related lists": "",
    "Georgia (U.S. state) high school athletic conference navigational boxes": "",
    "Georgia (U.S. state) history-related lists": "",
    "Georgia (U.S. state) judicial elections": "",
    "Georgia (U.S. state) labor commissioners": "",
    "Georgia (U.S. state) legislative districts": "",
    "Georgia (U.S. state) legislative sessions": "",
    "Georgia (U.S. state) Libertarians": "",
    "Georgia (U.S. state) lieutenant gubernatorial elections": "",
    "Georgia (U.S. state) location map modules": "",
    "Georgia (U.S. state) maps": "",
    "Georgia (U.S. state) mass media navigational boxes": "",
    "Georgia (U.S. state) militia": "",
    "Georgia (U.S. state) militiamen in the American Revolution": "",
    "Georgia (U.S. state) Oppositionists": "",
    "Georgia (U.S. state) placenames of Native American origin": "",
    "Georgia (U.S. state) Populists": "",
    "Georgia (U.S. state) portal": "",
    "Georgia (U.S. state) postmasters": "",
    "Georgia (U.S. state) presidential primaries": "",
    "Georgia (U.S. state) Progressives (1912)": "",
    "Georgia (U.S. state) Prohibitionists": "",
    "Georgia (U.S. state) radio market navigational boxes": "",
    "Georgia (U.S. state) railroads": "",
    "Georgia (U.S. state) Sea Islands": "",
    "Georgia (U.S. state) shopping mall templates": "",
    "Georgia (U.S. state) society": "",
    "Georgia (U.S. state) special elections": "",
    "Georgia (U.S. state) sports-related lists": "",
    "Georgia (U.S. state) state constitutional officer elections": "",
    "Georgia (U.S. state) state forests": "",
    "Georgia (U.S. state) statutes": "",
    "Georgia (U.S. state) television station user templates": "",
    "Georgia (U.S. state) transportation-related lists": "",
    "Georgia (U. S. state) universities and colleges leaders navigational boxes": "",
    "Georgia (U.S. state) universities and colleges navigational boxes": "",
    "Georgia (U.S. state) user categories": "",
    "Georgia (U.S. state) user templates": "",
    "Georgia (U.S. state) Wikipedians": "",
    "Georgia (U.S. state) wine": "",
}


@pytest.mark.dump
def test_us_counties_empty() -> None:
    expected, diff_result = one_dump_test(empty_data, resolve_label_ar)

    dump_diff(diff_result, "test_us_counties_empty")
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(empty_data):,}"


to_test = [
    # (f"test_us_counties_{x}", v) for x, v in data_1.items()
    ("test_us_counties_iowa", data_1["iowa"])
]

to_test.append(("test_all_test_data", all_test_data))


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=False)
