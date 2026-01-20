#!/usr/bin/python3
""" """

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.sports_resolvers.raw_sports_with_suffixes import wrap_team_xo_normal_2025_with_ends

data_0 = {}

data_1 = {
    "defunct sports clubs": "أندية رياضية سابقة",
    "defunct sports competitions": "منافسات رياضية سابقة",
    "defunct sports leagues": "دوريات رياضية سابقة",
    "professional sports leagues": "دوريات رياضية للمحترفين",
    "basketball league": "دوري كرة السلة",
    "current football seasons": "مواسم كرة قدم حالية",
    "cycling races": "سباقات سباق دراجات هوائية",
    "defunct american football teams": "فرق كرة قدم أمريكية سابقة",
    "defunct baseball leagues": "دوريات كرة قاعدة سابقة",
    "defunct baseball teams": "فرق كرة قاعدة سابقة",
    "defunct basketball competitions": "منافسات كرة سلة سابقة",
    "defunct basketball teams": "فرق كرة سلة سابقة",
    "defunct cycling teams": "فرق سباق دراجات هوائية سابقة",
    "defunct esports competitions": "منافسات رياضة إلكترونية سابقة",
    "defunct football clubs": "أندية كرة قدم سابقة",
    "defunct football competitions": "منافسات كرة قدم سابقة",
    "defunct football leagues": "دوريات كرة قدم سابقة",
    "defunct gaelic football competitions": "منافسات كرة قدم غالية سابقة",
    "defunct hockey competitions": "منافسات هوكي سابقة",
    "defunct ice hockey leagues": "دوريات هوكي جليد سابقة",
    "defunct ice hockey teams": "فرق هوكي جليد سابقة",
    "defunct indoor soccer leagues": "دوريات كرة قدم داخل الصالات سابقة",
    "defunct netball leagues": "دوريات كرة شبكة سابقة",
    "defunct rugby league teams": "فرق دوري رجبي سابقة",
    "defunct rugby union leagues": "دوريات اتحاد رجبي سابقة",
    "defunct rugby union teams": "فرق اتحاد رجبي سابقة",
    "defunct soccer clubs": "أندية كرة قدم سابقة",
    "defunct water polo clubs": "أندية كرة ماء سابقة",
    "defunct water polo competitions": "منافسات كرة ماء سابقة",
    "domestic cricket competitions": "منافسات كريكت محلية",
    "domestic football leagues": "دوريات كرة قدم محلية",
    "domestic football": "كرة قدم محلية",
    "domestic handball leagues": "دوريات كرة يد محلية",
    "domestic women's football leagues": "دوريات كرة قدم محلية للسيدات",
    "first-class cricket": "كريكت من الدرجة الأولى",
    "football chairmen and investors": "رؤساء ومسيرو كرة قدم",
    "football league": "دوري كرة القدم",
    "indoor football": "كرة قدم داخل الصالات",
    "indoor hockey": "هوكي داخل الصالات",
    "indoor track and field": "سباقات مضمار وميدان داخل الصالات",
    "international aquatics competitions": "منافسات رياضات مائية دولية",
    "international archery competitions": "منافسات نبالة دولية",
    "international athletics competitions": "منافسات ألعاب قوى دولية",
    "international bandy competitions": "منافسات باندي دولية",
    "international baseball competitions": "منافسات كرة قاعدة دولية",
    "international basketball competitions": "منافسات كرة سلة دولية",
    "international boxing competitions": "منافسات بوكسينغ دولية",
    "international cricket competitions": "منافسات كريكت دولية",
    "international cricket records and statistics": "سجلات وإحصائيات كريكت دولية",
    "international cycle races": "سباقات دراجات دولية",
    "international fencing competitions": "منافسات مبارزة سيف شيش دولية",
    "international field hockey competitions": "منافسات هوكي ميدان دولية",
    "international figure skating competitions": "منافسات تزلج فني دولية",
    "international football competitions": "منافسات كرة قدم دولية",
    "international futsal competitions": "منافسات كرة صالات دولية",
    "international gymnastics competitions": "منافسات جمباز دولية",
    "international handball competitions": "منافسات كرة يد دولية",
    "international ice hockey competitions": "منافسات هوكي جليد دولية",
    "international karate competitions": "منافسات كاراتيه دولية",
    "international kickboxing competitions": "منافسات كيك بوكسينغ دولية",
    "international men's football competitions": "منافسات كرة قدم دولية للرجال",
    "international netball players": "لاعبو كرة شبكة دوليون",
    "international roller hockey competitions": "منافسات هوكي دحرجة دولية",
    "international rugby league competitions": "منافسات دوري رجبي دولية",
    "international rugby union competitions": "منافسات اتحاد رجبي دولية",
    "international shooting competitions": "منافسات رماية دولية",
    "international softball competitions": "منافسات كرة لينة دولية",
    "international speed skating competitions": "منافسات تزلج سريع دولية",
    "international volleyball competitions": "منافسات كرة طائرة دولية",
    "international water polo competitions": "منافسات كرة ماء دولية",
    "international weightlifting competitions": "منافسات رفع أثقال دولية",
    "international women's basketball competitions": "منافسات كرة سلة دولية للسيدات",
    "international women's cricket competitions": "منافسات كريكت دولية للسيدات",
    "international women's field hockey competitions": "منافسات هوكي ميدان دولية للسيدات",
    "international women's football competitions": "منافسات كرة قدم دولية للسيدات",
    "international wrestling competitions": "منافسات مصارعة دولية",
    "international youth basketball competitions": "منافسات كرة سلة شبابية دولية",
    "international youth football competitions": "منافسات كرة قدم شبابية دولية",
    "ju-jitsu world championships": "بطولة العالم للجوجوتسو",
    "men's international basketball": "كرة سلة دولية للرجال",
    "men's international football": "كرة قدم دولية للرجال",
    "multi-national basketball leagues": "دوريات كرة سلة متعددة الجنسيات",
    "national basketball team results": "نتائج منتخبات كرة سلة وطنية",
    "national cycling champions": "أبطال بطولات سباق دراجات هوائية وطنية",
    "national equestrian manager history": "تاريخ مدربو فروسية وطنية",
    "national football team results": "نتائج منتخبات كرة قدم وطنية",
    "national ice hockey teams": "منتخبات هوكي جليد وطنية",
    "national junior football teams": "منتخبات كرة قدم وطنية للناشئين",
    "national junior men's handball teams": "منتخبات كرة يد وطنية للناشئين",
    "national lacrosse league": "دوريات لاكروس وطنية",
    "national men's equestrian manager history": "تاريخ مدربو فروسية وطنية للرجال",
    "national rugby union teams": "منتخبات اتحاد رجبي وطنية",
    "national shooting championships": "بطولات رماية وطنية",
    "national squash teams": "منتخبات اسكواش وطنية",
    "national under-13 equestrian manager history": "تاريخ مدربو فروسية تحت 13 سنة",
    "national under-14 equestrian manager history": "تاريخ مدربو فروسية تحت 14 سنة",
    "national water polo teams": "منتخبات كرة ماء وطنية",
    "national women's equestrian manager history": "تاريخ مدربو فروسية وطنية للسيدات",
    "national youth baseball teams": "منتخبات كرة قاعدة وطنية شبابية",
    "national youth basketball teams": "منتخبات كرة سلة وطنية شبابية",
    "outdoor equestrian": "فروسية في الهواء الطلق",
    "outdoor ice hockey": "هوكي جليد في الهواء الطلق",
    "premier lacrosse league": "دوريات لاكروس من الدرجة الممتازة",
    "professional ice hockey leagues": "دوريات هوكي جليد للمحترفين",
    "rugby league chairmen and investors": "رؤساء ومسيرو دوري الرجبي",
    "summer olympics football": "كرة القدم في الألعاب الأولمبية الصيفية",
    "summer olympics volleyball": "كرة الطائرة في الألعاب الأولمبية الصيفية",
    "summer olympics water polo": "كرة الماء في الألعاب الأولمبية الصيفية",
    "under-13 equestrian manager history": "تاريخ مدربو فروسية تحت 13 سنة",
    "under-13 equestrian": "فروسية تحت 13 سنة",
    "under-14 equestrian manager history": "تاريخ مدربو فروسية تحت 14 سنة",
    "under-14 equestrian": "فروسية تحت 14 سنة",
    "under-16 basketball": "كرة سلة تحت 16 سنة",
    "under-19 basketball": "كرة سلة تحت 19 سنة",
    "under-23 cycle racing": "سباق دراجات تحت 23 سنة",
    "women's international football": "كرة قدم دولية للسيدات",
    "women's international futsal": "كرة صالات دولية للسيدات",
    "world athletics championships": "بطولة العالم لألعاب القوى",
    "world netball championship": "بطولة العالم لكرة الشبكة",
    "world netball championships": "بطولة العالم لكرة الشبكة",
    "world rowing championships medalists": "فائزون بميداليات بطولة العالم للتجديف",
    "world taekwondo championships": "بطولة العالم للتايكوندو",
}


test_2025 = {}


@pytest.mark.parametrize("category, expected_key", test_2025.items(), ids=test_2025.keys())
@pytest.mark.fast
def test_wrap_team_xo_normal_2025(category: str, expected_key: str) -> None:
    label = wrap_team_xo_normal_2025_with_ends(category)
    assert label == expected_key


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_Get_New_team_xo_data(category: str, expected: str) -> None:
    label1 = wrap_team_xo_normal_2025_with_ends(category)
    assert label1 == expected


TEMPORAL_CASES = [
    ("test_find_labels_bot_0", data_0, wrap_team_xo_normal_2025_with_ends),
    ("test_find_labels_bot_1", data_1, wrap_team_xo_normal_2025_with_ends),
]


@pytest.mark.parametrize("name,data,callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
