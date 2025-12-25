#!/usr/bin/python3
""" """

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.sports_formats_teams.sport_lab2 import wrap_team_xo_normal_2025
from ArWikiCats.new_resolvers.sports_formats_national.sport_lab_nat import sport_lab_nat_load_new

sport_lab2_data = {
    "defunct football cup competitions": "منافسات كؤوس كرة قدم سابقة",
    "defunct football cups": "كؤوس كرة قدم سابقة",
    "professional football cups": "كؤوس كرة قدم للمحترفين",
    "domestic football cup": "كؤوس كرة قدم محلية",
    "domestic football cups": "كؤوس كرة قدم محلية",
    "football cup competitions": "منافسات كؤوس كرة قدم",
    "football cups": "كؤوس كرة قدم",
    "basketball cup competitions": "منافسات كؤوس كرة سلة",
    "field hockey cup competitions": "منافسات كؤوس هوكي ميدان",
    "sports cup competitions": "منافسات كؤوس رياضية",
    "baseball world cup": "كأس العالم لكرة القاعدة",
    "biathlon world cup": "كأس العالم للبياثلون",
    "cricket world cup": "كأس العالم للكريكت",
    "curling world cup": "كأس العالم للكيرلنغ",
    "esports world cup": "كأس العالم للرياضة إلكترونية",
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
    "wrestling world cup": "كأس العالم للمصارعة"
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

test_find_teams_bot_data = {
}


@pytest.mark.parametrize("category, expected", sport_lab2_data.items(), ids=sport_lab2_data.keys())
@pytest.mark.fast
def test_sport_lab2_data(category: str, expected: str) -> None:
    label1 = wrap_team_xo_normal_2025(category)
    assert isinstance(label1, str)
    assert label1 == expected


@pytest.mark.parametrize("category, expected", sport_lab_nat_load_new_data.items(), ids=sport_lab_nat_load_new_data.keys())
@pytest.mark.fast
def test_sport_lab_nat_load_new(category: str, expected: str) -> None:
    label1 = sport_lab_nat_load_new(category)
    assert isinstance(label1, str)
    assert label1 == expected
