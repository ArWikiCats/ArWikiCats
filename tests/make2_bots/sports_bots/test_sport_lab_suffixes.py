"""
Tests
"""
import pytest

from src.make2_bots.sports_bots.sport_lab_suffixes import get_teams_new

get_teams_new_data = {
    "defunct ice hockey teams": "فرق هوكي جليد سابقة",
    "professional sports leagues": "دوريات رياضية للمحترفين",
    "basketball awards": "جوائز كرة سلة",
    "domestic football": "كرة قدم محلية",
    "international football competitions": "منافسات كرة قدم دولية",
    "defunct football leagues": "دوريات كرة قدم سابقة",
    "international weightlifting competitions": "منافسات رفع أثقال دولية",
    "national junior men's handball teams": "منتخبات كرة يد وطنية للناشئين",
    "international figure skating competitions": "منافسات تزلج فني دولية",
    "international fencing competitions": "منافسات مبارزة سيف شيش دولية",
    "bowling television series": "مسلسلات تلفزيونية بولينج",
    "international volleyball competitions": "منافسات كرة طائرة دولية",
    "defunct soccer clubs": "أندية كرة قدم سابقة",
    "international women's field hockey competitions": "منافسات هوكي ميدان نسائية دولية",
    "women's international football": "كرة قدم دولية للسيدات",
    "world netball championships": "بطولة العالم لكرة الشبكة",
    "international baseball competitions": "منافسات كرة قاعدة دولية",
    "football cup competitions": "منافسات كؤوس كرة قدم",
    "world rowing championships medalists": "فائزون بميداليات بطولة العالم للتجديف",
    "international basketball competitions": "منافسات كرة سلة دولية",
    "professional ice hockey leagues": "دوريات هوكي جليد للمحترفين",
    "domestic football cups": "كؤوس كرة قدم محلية",
    "international water polo competitions": "منافسات كرة ماء دولية",
    "summer olympics water polo": "كرة الماء في الألعاب الأولمبية الصيفية",
    "defunct cycling teams": "فرق سباق دراجات هوائية سابقة",
    "under-23 cycle racing": "سباق دراجات تحت 23 سنة",
    "baseball video games": "ألعاب فيديو كرة قاعدة",
    "domestic football leagues": "دوريات كرة قدم محلية",
    "defunct football clubs": "أندية كرة قدم سابقة",
    "international field hockey competitions": "منافسات هوكي ميدان دولية",
    "summer olympics volleyball": "كرة الطائرة في الألعاب الأولمبية الصيفية",
    "world athletics championships": "بطولة العالم لألعاب القوى",
    "international boxing competitions": "منافسات بوكسينغ دولية",
    "international gymnastics competitions": "منافسات جمباز دولية",
    "defunct ice hockey leagues": "دوريات هوكي جليد سابقة",
    "defunct sports competitions": "منافسات رياضية سابقة",
    "defunct american football teams": "فرق كرة قدم أمريكية سابقة",
    "defunct water polo competitions": "منافسات كرة ماء سابقة",
    "international women's basketball competitions": "منافسات كرة سلة نسائية دولية",
    "international ice hockey competitions": "منافسات هوكي جليد دولية",
    "domestic handball leagues": "دوريات كرة يد محلية",
    "national football team results": "نتائج منتخبات كرة قدم وطنية",
    "netball world cup": "كأس العالم لكرة الشبكة",
    "international youth football competitions": "منافسات كرة قدم شبابية دولية",
    "defunct baseball teams": "فرق كرة قاعدة سابقة",
    "defunct sports clubs": "أندية رياضية سابقة",
    "international athletics competitions": "منافسات ألعاب قوى دولية",
    "defunct esports competitions": "منافسات رياضة إلكترونية سابقة",
}


@pytest.mark.parametrize("category, expected_key", get_teams_new_data.items(), ids=list(get_teams_new_data.keys()))
@pytest.mark.fast
def test_get_teams_new_data(category, expected_key) -> None:

    label = get_teams_new(category)
    assert label.strip() == expected_key


data_slow = {
}


@pytest.mark.parametrize("category, expected_key", data_slow.items(), ids=list(data_slow.keys()))
@pytest.mark.slow
def test_data_slow(category, expected_key) -> None:

    label = get_teams_new(category)
    assert label.strip() == expected_key


def test_get_teams_new():
    # Test with a basic input
    result = get_teams_new("football team")
    assert isinstance(result, str)

    # Test with empty string
    result_empty = get_teams_new("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = get_teams_new("basketball team")
    assert isinstance(result_various, str)
