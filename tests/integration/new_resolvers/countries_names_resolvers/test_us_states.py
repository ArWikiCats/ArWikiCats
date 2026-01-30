"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.countries_names_resolvers.us_states import (
    normalize_state,
    resolve_us_states,
    us_states_new_keys,
)
from ArWikiCats.translations import US_STATES
from utils.dump_runner import make_dump_test_name_data_callback

test_data = {
    "{en} in the War of 1812": "{ar} في حرب 1812",
    "{en} democrats": "ديمقراطيون من ولاية {ar}",
    "{en} lawyers": "محامون من ولاية {ar}",
    "{en} state court judges": "قضاة محكمة ولاية {ar}",
    "{en} state courts": "محكمة ولاية {ar}",
    "{en} state senators": "أعضاء مجلس شيوخ ولاية {ar}",
}

all_test_data = {}

for en, ar in US_STATES.items():  # ~150 per state
    test_one = {x.format(en=en).lower(): normalize_state(v.format(ar=ar)) for x, v in us_states_new_keys.items()}
    all_test_data.update(test_one)
    if len(all_test_data) > 360:
        break


@pytest.mark.parametrize("category, expected_key", all_test_data.items(), ids=all_test_data.keys())
@pytest.mark.slow
def test_resolve_us_states(category: str, expected_key: str) -> None:
    label2 = resolve_us_states(category)
    assert label2 == expected_key


Work_US_State_data = {
    "mississippi territory": "إقليم مسيسيبي",
    "indiana territory": "إقليم إنديانا",
    "pennsylvania politicians": "سياسيو بنسلفانيا",
    "louisiana territory": "إقليم لويزيانا",
    "illinois territory": "إقليم إلينوي",
    "michigan territory": "إقليم ميشيغان",
    "missouri territory": "إقليم ميزوري",
    "alabama territory": "إقليم ألاباما",
    "arkansas territory": "إقليم أركنساس",
    "florida territory": "إقليم فلوريدا",
    "maryland politicians": "سياسيو ماريلند",
    "massachusetts politicians": "سياسيو ماساتشوستس",
    "wisconsin territory": "إقليم ويسكونسن",
    "oregon territory": "إقليم أوريغن",
    "iowa territory": "إقليم آيوا",
    "new mexico territory": "إقليم نيومكسيكو",
    "utah territory": "إقليم يوتا",
    "washington territory": "إقليم واشنطن",
    "nebraska territory": "إقليم نبراسكا",
    "kansas territory": "إقليم كانساس",
    "nevada territory": "إقليم نيفادا",
    "colorado territory": "إقليم كولورادو",
    "montana territory": "إقليم مونتانا",
    "arizona territory": "إقليم أريزونا",
    "wyoming territory": "إقليم وايومنغ",
    "idaho territory": "إقليم أيداهو",
    "oklahoma territory": "إقليم أوكلاهوما",
    "connecticut general assembly": "جمعية كونيتيكت العامة",
    "georgia general assembly": "جمعية جورجيا العامة",
    "kentucky general assembly": "جمعية كنتاكي العامة",
    "new jersey legislature": "هيئة نيوجيرسي التشريعية",
    "new york state legislature": "هيئة ولاية نيويورك التشريعية",
    "north carolina general assembly": "جمعية كارولاينا الشمالية العامة",
    "pennsylvania general assembly": "جمعية بنسلفانيا العامة",
    "south carolina general assembly": "جمعية كارولاينا الجنوبية العامة",
    "virginia general assembly": "جمعية فرجينيا العامة",
    "virginia politicians": "سياسيو فرجينيا",
    "connecticut politicians": "سياسيو كونيتيكت",
    "new jersey politicians": "سياسيو نيوجيرسي",
    "new york (state) politicians": "سياسيو ولاية نيويورك",
    "delaware politicians": "سياسيو ديلاوير",
    "kentucky politicians": "سياسيو كنتاكي",
    "south carolina politicians": "سياسيو كارولاينا الجنوبية",
    "california ballot propositions": "اقتراحات اقتراع كاليفورنيا",
    "illinois ballot measures": "إجراءات اقتراع إلينوي",
    "oregon ballot measures": "إجراءات اقتراع أوريغن",
    "washington (state) ballot measures": "إجراءات اقتراع ولاية واشنطن",
    "colorado ballot measures": "إجراءات اقتراع كولورادو",
    "massachusetts ballot measures": "إجراءات اقتراع ماساتشوستس",
    "arizona politicians": "سياسيو أريزونا",
    "arkansas politicians": "سياسيو أركنساس",
    "arkansas state court judges": "قضاة محكمة ولاية أركنساس",
    "colorado politicians": "سياسيو كولورادو",
    "colorado state court judges": "قضاة محكمة ولاية كولورادو",
    "georgia (u.s. state) politicians": "سياسيو ولاية جورجيا",
    "alabama politicians": "سياسيو ألاباما",
    "georgia (u.s. state) state court judges": "قضاة محكمة ولاية جورجيا",
    "alabama state court judges": "قضاة محكمة ولاية ألاباما",
    "indiana politicians": "سياسيو إنديانا",
    "indiana state court judges": "قضاة محكمة ولاية إنديانا",
    "california politicians": "سياسيو كاليفورنيا",
    "california state court judges": "قضاة محكمة ولاية كاليفورنيا",
    "nebraska politicians": "سياسيو نبراسكا",
    "nebraska state court judges": "قضاة محكمة ولاية نبراسكا",
    "tennessee politicians": "سياسيو تينيسي",
    "tennessee state court judges": "قضاة محكمة ولاية تينيسي",
    "nevada politicians": "سياسيو نيفادا",
    "texas politicians": "سياسيو تكساس",
    "new hampshire politicians": "سياسيو نيوهامشير",
    "texas state court judges": "قضاة محكمة ولاية تكساس",
    "new hampshire state court judges": "قضاة محكمة ولاية نيوهامشير",
    "new jersey state court judges": "قضاة محكمة ولاية نيوجيرسي",
    "new mexico politicians": "سياسيو نيومكسيكو",
    "new york state court judges": "قضاة محكمة ولاية نيويورك",
    "louisiana politicians": "سياسيو لويزيانا",
    "louisiana state court judges": "قضاة محكمة ولاية لويزيانا",
    "maine politicians": "سياسيو مين",
    "maine state court judges": "قضاة محكمة ولاية مين",
    "iowa politicians": "سياسيو آيوا",
    "iowa state court judges": "قضاة محكمة ولاية آيوا",
    "utah politicians": "سياسيو يوتا",
    "delaware state court judges": "قضاة محكمة ولاية ديلاوير",
    "vermont politicians": "سياسيو فيرمونت",
    "vermont state court judges": "قضاة محكمة ولاية فيرمونت",
    "south carolina state court judges": "قضاة محكمة ولاية كارولاينا الجنوبية",
    "south dakota politicians": "سياسيو داكوتا الجنوبية",
    "virginia state court judges": "قضاة محكمة ولاية فرجينيا",
    "massachusetts state court judges": "قضاة محكمة ولاية ماساتشوستس",
    "washington (state) politicians": "سياسيو ولاية واشنطن",
}


@pytest.mark.parametrize("category, expected_key", Work_US_State_data.items(), ids=Work_US_State_data.keys())
@pytest.mark.slow
def test_Work_US_State_data(category: str, expected_key: str) -> None:
    label = resolve_us_states(category)
    assert label == expected_key


fast_data = {
    "north carolina politicians": "سياسيو كارولاينا الشمالية",
    "north carolina state court judges": "قضاة محكمة ولاية كارولاينا الشمالية",
    "north dakota politicians": "سياسيو داكوتا الشمالية",
    "west virginia politicians": "سياسيو فرجينيا الغربية",
    "west virginia state court judges": "قضاة محكمة ولاية فرجينيا الغربية",
    "wisconsin politicians": "سياسيو ويسكونسن",
    "wisconsin state court judges": "قضاة محكمة ولاية ويسكونسن",
    "rhode island politicians": "سياسيو رود آيلاند",
    "idaho politicians": "سياسيو أيداهو",
    "illinois politicians": "سياسيو إلينوي",
    "illinois state court judges": "قضاة محكمة ولاية إلينوي",
    "ohio politicians": "سياسيو أوهايو",
    "ohio state court judges": "قضاة محكمة ولاية أوهايو",
    "oregon politicians": "سياسيو أوريغن",
    "florida politicians": "سياسيو فلوريدا",
    "alabama legislature": "هيئة ألاباما التشريعية",
    "arkansas general assembly": "جمعية أركنساس العامة",
    "california state legislature": "هيئة ولاية كاليفورنيا التشريعية",
    "colorado general assembly": "جمعية كولورادو العامة",
    "delaware general assembly": "جمعية ديلاوير العامة",
    "florida legislature": "هيئة فلوريدا التشريعية",
    "pennsylvania state court judges": "قضاة محكمة ولاية بنسلفانيا",
    "illinois general assembly": "جمعية إلينوي العامة",
    "indiana general assembly": "جمعية إنديانا العامة",
    "iowa general assembly": "جمعية آيوا العامة",
    "kansas legislature": "هيئة كانساس التشريعية",
    "wyoming politicians": "سياسيو وايومنغ",
    "louisiana state legislature": "هيئة ولاية لويزيانا التشريعية",
    "maine legislature": "هيئة مين التشريعية",
    "michigan legislature": "هيئة ميشيغان التشريعية",
    "minnesota legislature": "هيئة منيسوتا التشريعية",
    "kansas politicians": "سياسيو كانساس",
    "mississippi legislature": "هيئة مسيسيبي التشريعية",
    "kentucky state court judges": "قضاة محكمة ولاية كنتاكي",
    "missouri general assembly": "جمعية ميزوري العامة",
    "nebraska legislature": "هيئة نبراسكا التشريعية",
    "nevada legislature": "هيئة نيفادا التشريعية",
    "north dakota legislative assembly": "هيئة داكوتا الشمالية التشريعية",
    "ohio general assembly": "جمعية أوهايو العامة",
    "oregon legislative assembly": "هيئة أوريغن التشريعية",
    "rhode island general assembly": "جمعية رود آيلاند العامة",
    "south dakota legislature": "هيئة داكوتا الجنوبية التشريعية",
    "tennessee general assembly": "جمعية تينيسي العامة",
    "texas legislature": "هيئة تكساس التشريعية",
    "vermont general assembly": "جمعية فيرمونت العامة",
    "washington state legislature": "هيئة ولاية واشنطن التشريعية",
    "west virginia legislature": "هيئة فرجينيا الغربية التشريعية",
    "wisconsin legislature": "هيئة ويسكونسن التشريعية",
    "michigan politicians": "سياسيو ميشيغان",
    "michigan state court judges": "قضاة محكمة ولاية ميشيغان",
    "minnesota politicians": "سياسيو منيسوتا",
    "minnesota state court judges": "قضاة محكمة ولاية منيسوتا",
    "mississippi politicians": "سياسيو مسيسيبي",
    "mississippi state court judges": "قضاة محكمة ولاية مسيسيبي",
    "missouri politicians": "سياسيو ميزوري",
    "missouri state court judges": "قضاة محكمة ولاية ميزوري",
    "montana politicians": "سياسيو مونتانا",
    "maine ballot measures": "إجراءات اقتراع مين",
    "new jersey ballot measures": "إجراءات اقتراع نيوجيرسي",
    "missouri ballot measures": "إجراءات اقتراع ميزوري",
    "texas law": "قانون تكساس",
    "alaska politicians": "سياسيو ألاسكا",
    "hawaii politicians": "سياسيو هاواي",
    "connecticut state court judges": "قضاة محكمة ولاية كونيتيكت",
    "south dakota ballot measures": "إجراءات اقتراع داكوتا الجنوبية",
    "oklahoma politicians": "سياسيو أوكلاهوما",
    "alaska legislature": "هيئة ألاسكا التشريعية",
    "arizona state legislature": "هيئة ولاية أريزونا التشريعية",
    "hawaii state legislature": "هيئة ولاية هاواي التشريعية",
    "idaho legislature": "هيئة أيداهو التشريعية",
    "montana legislature": "هيئة مونتانا التشريعية",
    "new mexico legislature": "هيئة نيومكسيكو التشريعية",
    "oklahoma house-of-representatives": "مجلس نواب ولاية أوكلاهوما",
    "oklahoma legislature": "هيئة أوكلاهوما التشريعية",
    "utah legislature": "هيئة يوتا التشريعية",
    "wyoming legislature": "هيئة وايومنغ التشريعية",
    "maryland state court judges": "قضاة محكمة ولاية ماريلند",
}


@pytest.mark.parametrize("category, expected_key", fast_data.items(), ids=fast_data.keys())
@pytest.mark.fast
def test_fast_data(category: str, expected_key: str) -> None:
    label = resolve_us_states(category)
    assert label == expected_key


to_test = [
    ("test_resolve_us_states", all_test_data, resolve_us_states),
]

test_dump_all = make_dump_test_name_data_callback(to_test, run_same=True)
