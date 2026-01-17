"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.legacy_bots.sport_lab_suffixes import resolve_team_suffix

resolve_team_suffix_data = {
    "australian rules football awards": "جوائز كرة قدم أسترالية",
    "baseball commissioners": "مفوضو كرة قاعدة",
    "baseball music": "موسيقى كرة قاعدة",
    "baseball video games": "ألعاب فيديو كرة قاعدة",
    "basketball awards": "جوائز كرة سلة",
    "basketball comics": "قصص مصورة كرة سلة",
    "basketball terminology": "مصطلحات كرة سلة",
    "bowling broadcasters": "مذيعو بولينج",
    "bowling television series": "مسلسلات تلفزيونية بولينج",
    "canoeing logos": "شعارات ركوب الكنو",
    "cycling television series": "مسلسلات تلفزيونية سباق دراجات هوائية",
    "fencing logos": "شعارات مبارزة سيف شيش",
    "figure skating media": "إعلام تزلج فني",
    "football governing bodies": "هيئات تنظيم كرة قدم",
    "go comics": "قصص مصورة غو",
    "muay thai video games": "ألعاب فيديو موياي تاي",
    "roller hockey logos": "شعارات هوكي دحرجة",
    "rowing equipment": "معدات تجديف",
    "rugby union stadiums": "ملاعب اتحاد رجبي",
    "shooting sports equipment": "معدات رماية",
    "snooker terminology": "مصطلحات سنوكر",
    "tennis logos": "شعارات كرة مضرب",
    "water polo comics": "قصص مصورة كرة ماء",
    "water polo competition": "منافسات كرة ماء",
    "wheelchair basketball terminology": "مصطلحات كرة سلة على كراسي متحركة",
}


@pytest.mark.parametrize(
    "category, expected_key", resolve_team_suffix_data.items(), ids=resolve_team_suffix_data.keys()
)
@pytest.mark.fast
def test_resolve_team_suffix_data(category: str, expected_key: str) -> None:
    label = resolve_team_suffix(category)
    assert label == expected_key


to_test = [
    ("test_resolve_team_suffix_data", resolve_team_suffix_data),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_team_suffix)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
