#!/usr/bin/python3
""" """

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.sports_resolvers.countries_names_and_sports import (
    resolve_countries_names_sport_with_ends,
)
from ArWikiCats.new_resolvers.sports_resolvers.nationalities_and_sports import resolve_nats_sport_multi_v2
from ArWikiCats.new_resolvers.sports_resolvers.raw_sports import wrap_team_xo_normal_2025_with_ends
from ArWikiCats.new_resolvers.sports_resolvers.sport_lab_nat import sport_lab_nat_load_new

sport_lab2_test_data = {
    "defunct indoor boxing": "بوكسينغ داخل الصالات سابقة",
    "defunct indoor boxing clubs": "أندية بوكسينغ داخل الصالات سابقة",
    "defunct indoor boxing cups": "كؤوس بوكسينغ داخل الصالات سابقة",
    "defunct football cup competitions": "منافسات كؤوس كرة قدم سابقة",
    "defunct football cups": "كؤوس كرة قدم سابقة",
    "professional football cups": "كؤوس كرة قدم للمحترفين",
    "domestic football cup": "كؤوس كرة قدم محلية",
    "domestic football cups": "كؤوس كرة قدم محلية",
    "football cup competitions": "منافسات كؤوس كرة قدم",
    "football cups": "كؤوس كرة قدم",
    "basketball cup competitions": "منافسات كؤوس كرة سلة",
    "field hockey cup competitions": "منافسات كؤوس هوكي ميدان",
    "baseball world cup": "كأس العالم لكرة القاعدة",
    "biathlon world cup": "كأس العالم للبياثلون",
    "cricket world cup": "كأس العالم للكريكت",
    "curling world cup": "كأس العالم للكيرلنغ",
    "esports world cup": "كأس العالم للرياضة الإلكترونية",
    "hockey world cup": "كأس العالم للهوكي",
    "men's hockey world cup": "كأس العالم للهوكي للرجال",
    "men's rugby world cup": "كأس العالم للرجبي للرجال",
    "men's softball world cup": "كأس العالم للكرة اللينة للرجال",
    "netball world cup": "كأس العالم لكرة الشبكة",
    "rugby league world cup": "كأس العالم لدوري الرجبي",
    "rugby world cup": "كأس العالم للرجبي",
    "wheelchair rugby league world cup": "كأس العالم لدوري الرجبي على الكراسي المتحركة",
    "wheelchair rugby world cup": "كأس العالم للرجبي على الكراسي المتحركة",
    "women's cricket world cup ": "كأس العالم للكريكت للسيدات",
    "women's cricket world cup tournaments": "بطولات كأس العالم للكريكت للسيدات",
    "women's cricket world cup": "كأس العالم للكريكت للسيدات",
    "women's field hockey world cup": "كأس العالم لهوكي الميدان للسيدات",
    "women's hockey world cup": "كأس العالم للهوكي للسيدات",
    "women's rugby league world cup": "كأس العالم لدوري الرجبي للسيدات",
    "women's rugby world cup": "كأس العالم للرجبي للسيدات",
    "women's softball world cup": "كأس العالم للكرة اللينة للسيدات",
    "wrestling world cup": "كأس العالم للمصارعة",
}

nats_sport_multi_v2_data = {
    "yemeni mens basketball cup": "كأس اليمن لكرة السلة للرجال",
    "yemeni womens basketball cup": "كأس اليمن لكرة السلة للسيدات",
    "yemeni basketball cup": "كأس اليمن لكرة السلة",
    "yemeni defunct basketball cup": "كؤوس كرة سلة يمنية سابقة",
    "chinese domestic boxing cup": "كؤوس بوكسينغ صينية محلية",
    "chinese boxing cup": "كأس الصين للبوكسينغ",
    "chinese boxing cup competitions": "منافسات كأس الصين للبوكسينغ",
    "chinese defunct boxing cup competitions": "منافسات كؤوس بوكسينغ صينية سابقة",
    "chinese defunct indoor boxing cups": "كؤوس بوكسينغ صينية داخل الصالات سابقة",
    "chinese defunct boxing cups": "كؤوس بوكسينغ صينية سابقة",
    "chinese defunct outdoor boxing cups": "كؤوس بوكسينغ صينية في الهواء الطلق سابقة",
    "chinese professional boxing cups": "كؤوس بوكسينغ صينية للمحترفين",
    "chinese indoor boxing cups": "كؤوس بوكسينغ صينية داخل الصالات",
    "chinese outdoor boxing cups": "كؤوس بوكسينغ صينية في الهواء الطلق",
    "chinese domestic boxing cups": "كؤوس بوكسينغ صينية محلية",
    "chinese domestic women's boxing cups": "كؤوس بوكسينغ صينية محلية للسيدات",
    "chinese boxing cups": "كؤوس بوكسينغ صينية",
}

sport_lab_nat_load_new_data = {
    "asian domestic football cups": "كؤوس كرة قدم آسيوية محلية",
    "austrian football cups": "كؤوس كرة قدم نمساوية",
    "belgian football cups": "كؤوس كرة قدم بلجيكية",
    "dutch football cups": "كؤوس كرة قدم هولندية",
    "english football cups": "كؤوس كرة قدم إنجليزية",
    "european domestic football cups": "كؤوس كرة قدم أوروبية محلية",
    "german football cups": "كؤوس كرة قدم ألمانية",
    "irish football cups": "كؤوس كرة قدم أيرلندية",
    "italian football cups": "كؤوس كرة قدم إيطالية",
    "north american domestic football cups": "كؤوس كرة قدم أمريكية شمالية محلية",
    "oceanian domestic football cups": "كؤوس كرة قدم أوقيانوسية محلية",
    "republic-of ireland football cups": "كؤوس كرة قدم أيرلندية",
    "scottish football cups": "كؤوس كرة قدم إسكتلندية",
    "spanish basketball cups": "كؤوس كرة سلة إسبانية",
    "spanish football cups": "كؤوس كرة قدم إسبانية",
    "thai football cups": "كؤوس كرة قدم تايلندية",
    "welsh football cups": "كؤوس كرة قدم ويلزية",
}

rcn_sport_with_ends_data = {
    "new zealand amateur kick boxing cup": "كأس نيوزيلندا للكيك بوكسينغ للهواة",
    "new zealand youth kick boxing cup": "كأس نيوزيلندا للكيك بوكسينغ للشباب",
    "new zealand men's kick boxing cup": "كأس نيوزيلندا للكيك بوكسينغ للرجال",
    "new zealand women's kick boxing cup": "كأس نيوزيلندا للكيك بوكسينغ للسيدات",
    "new zealand kick boxing cup": "كأس نيوزيلندا للكيك بوكسينغ",
    "yemen amateur kick boxing cup": "كأس اليمن للكيك بوكسينغ للهواة",
    "yemen youth kick boxing cup": "كأس اليمن للكيك بوكسينغ للشباب",
    "yemen men's kick boxing cup": "كأس اليمن للكيك بوكسينغ للرجال",
    "yemen women's kick boxing cup": "كأس اليمن للكيك بوكسينغ للسيدات",
    "yemen kick boxing cup": "كأس اليمن للكيك بوكسينغ",
}

to_test = [
    ("test_sport_lab2_data", sport_lab2_test_data, wrap_team_xo_normal_2025_with_ends),
    ("test_resolve_nats_sport_multi_v2", nats_sport_multi_v2_data, resolve_nats_sport_multi_v2),
    ("test_sport_lab_nat_load_new", sport_lab_nat_load_new_data, sport_lab_nat_load_new),
    ("test_rcn_sport_with_ends", rcn_sport_with_ends_data, resolve_countries_names_sport_with_ends),
    # ---
    ("test_test_sport_cup_1", sport_lab2_test_data, resolve_nats_sport_multi_v2),
    ("test_test_sport_cup_2", sport_lab2_test_data, sport_lab_nat_load_new),
    ("test_test_sport_cup_3", sport_lab2_test_data, resolve_countries_names_sport_with_ends),
    # ---
]


@pytest.mark.parametrize("category, expected", nats_sport_multi_v2_data.items(), ids=nats_sport_multi_v2_data.keys())
@pytest.mark.skip2
def test_resolve_nats_sport_multi_v2(category: str, expected: str) -> None:
    label1 = resolve_nats_sport_multi_v2(category)
    assert isinstance(label1, str)
    assert label1 == expected


@pytest.mark.parametrize("category, expected", sport_lab2_test_data.items(), ids=sport_lab2_test_data.keys())
@pytest.mark.skip2
def test_sport_lab2_data(category: str, expected: str) -> None:
    label1 = wrap_team_xo_normal_2025_with_ends(category)
    assert isinstance(label1, str)
    assert label1 == expected


@pytest.mark.parametrize(
    "category, expected", sport_lab_nat_load_new_data.items(), ids=sport_lab_nat_load_new_data.keys()
)
@pytest.mark.skip2
def test_sport_lab_nat_load_new(category: str, expected: str) -> None:
    label1 = sport_lab_nat_load_new(category)
    assert isinstance(label1, str)
    assert label1 == expected


@pytest.mark.parametrize("category, expected", rcn_sport_with_ends_data.items(), ids=rcn_sport_with_ends_data.keys())
@pytest.mark.skip2
def test_rcn_sport_with_ends(category: str, expected: str) -> None:
    label1 = resolve_countries_names_sport_with_ends(category)
    assert isinstance(label1, str)
    assert label1 == expected


@pytest.mark.parametrize("name,data,callback", to_test)
@pytest.mark.skip2
def test_dump_it(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)

    # add_result = {x: v for x, v in data.items() if x in diff_result and "" == diff_result.get(x)}
    # dump_diff(add_result, f"{name}_add")
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
