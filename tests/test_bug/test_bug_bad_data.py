"""
Tests for country2_label_bot module functions.
"""

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats.ma_bots.country2_bot import Get_country2
from ArWikiCats.ma_bots2.country2_bots.country2_label_bot import country_2_title_work

data_new = {
    "australia by century": "أستراليا حسب القرن",
    "belgium by decade": "بلجيكا حسب العقد",
    "canada by city": "كندا حسب المدينة",
    "canada by month": "كندا حسب الشهر",
    "china by month": "الصين حسب الشهر",
    "disestablishments in australia": "انحلالات في أستراليا",
    "disestablishments in dominica": "انحلالات في دومينيكا",
    "disestablishments in ecuador": "انحلالات في الإكوادور",
    "disestablishments in georgia (u.s. state)": "انحلالات في ولاية جورجيا",
    "disestablishments in new zealand": "انحلالات في نيوزيلندا",
    "disestablishments in ottoman empire": "انحلالات في الدولة العثمانية",
    "disestablishments in papua new guinea": "انحلالات في بابوا غينيا الجديدة",
    "disestablishments in spain": "انحلالات في إسبانيا",
    "disestablishments in yugoslavia": "انحلالات في يوغسلافيا",
    "establishments in guernsey": "تأسيسات في غيرنزي",
    "establishments in north macedonia": "تأسيسات في مقدونيا الشمالية",
    "establishments in sint maarten": "تأسيسات في سينت مارتن",
    "establishments in southeast asia": "تأسيسات في جنوب شرق آسيا",
    "football by country": "كرة القدم حسب البلد",
    "men's football by continent": "كرة القدم للرجال حسب القارة",
    "new zealand by decade": "نيوزيلندا حسب العقد",
    "united states by state or territory": "الولايات المتحدة حسب الولاية أو الإقليم",
    "united states by state": "الولايات المتحدة حسب الولاية",
    "united states in 1520": "الولايات المتحدة في 1520",
    "women's football by country": "كرة القدم للسيدات حسب البلد",
    "youth football by continent": "كرة القدم للشباب حسب القارة"
}


@pytest.mark.parametrize("category,expected", data_new.items(), ids=data_new.keys())
@pytest.mark.skip2
def test_country_2_title_work(category: str, expected: str) -> None:
    result = country_2_title_work(category)
    assert result == expected


@pytest.mark.parametrize("category, expected", data_new.items(), ids=data_new.keys())
@pytest.mark.skip2
def test_Get_country2_slow(category: str, expected: str) -> None:
    label = Get_country2(category, fix_title=True)
    assert label == expected


TEMPORAL_CASES = [
    ("test_bug_bad_data_Get_country2", data_new, Get_country2),
    ("test_bug_bad_data_country_2_title_work", data_new, country_2_title_work),
]


@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
