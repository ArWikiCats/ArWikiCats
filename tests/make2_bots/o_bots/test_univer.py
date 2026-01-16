"""
Tests
"""

import pytest

from ArWikiCats.legacy_bots.o_bots.univer import te_universities

te_universities_data = {
    "seoul national university": "جامعة سول الوطنية",
    "i̇zmir university of economics": "جامعة إزمير للاقتصاد",
    "shandong university of science and technology": "جامعة شاندونغ للعلوم والتكنولوجيا",
    "kano university of science and technology": "جامعة كانو للعلوم والتكنولوجيا",
    "kaunas university-of-technology": "جامعة كاوناس للتكنولوجيا",
    "shanghai university-of-technology": "جامعة شانغهاي للتكنولوجيا",
    "beijing university-of-technology": "جامعة بكين للتكنولوجيا",
    "kharkiv national university": "جامعة خاركيف الوطنية",
    "kraków university of economics": "جامعة كراكوف للاقتصاد",
    "lille university of science and technology": "جامعة مدينة ليل للعلوم والتكنولوجيا",
    "luleå university-of-technology": "جامعة لوليو للتكنولوجيا",
    "kunming university of science and technology": "جامعة كونمينغ للعلوم والتكنولوجيا",
    "kyoto university of arts": "جامعة كيوتو للفنون",
    "munich university of applied sciences": "جامعة ميونخ للعلوم التطبيقية",
    "lanzhou university-of-technology": "جامعة لانتشو للتكنولوجيا",
    "lappeenranta university-of-technology": "جامعة لابينرنتا للتكنولوجيا",
    "wuhan university-of-technology": "جامعة ووهان للتكنولوجيا",
    "chengdu university-of-technology": "جامعة تشنغدو للتكنولوجيا",
    "xi'an university of science and technology": "جامعة شيان للعلوم والتكنولوجيا",
    "xi'an university-of-technology": "جامعة شيان للتكنولوجيا",
    "tabriz university of medical sciences": "جامعة تبريز للعلوم الطبية",
    "tainan national university": "جامعة تاينان الوطنية",
    "chinhoyi university-of-technology": "جامعة تشينهوي للتكنولوجيا",
    "taipei national university": "جامعة تايبيه الوطنية",
    "taiyuan university-of-technology": "جامعة تاي يوان للتكنولوجيا",
    "yokohama national university": "جامعة يوكوهاما الوطنية",
    "zhejiang university-of-technology": "جامعة تشيجيانغ للتكنولوجيا",
    "macau university of science and technology": "جامعة ماكاو للعلوم والتكنولوجيا",
    "tehran university of art": "جامعة طهران للفنون",
    "tehran university of medical sciences": "جامعة طهران للعلوم الطبية",
    "dalian university-of-technology": "جامعة داليان للتكنولوجيا",
    "university of science and technology beijing": "جامعة بكين للعلوم والتكنولوجيا",
    "mashhad university of medical sciences": "جامعة مشهد للعلوم الطبية",
    "donetsk national university": "جامعة دونيتسك الوطنية",
    "university-of-technology sydney": "جامعة سيدني للتكنولوجيا",
    "auckland university-of-technology": "جامعة أوكلاند للتكنولوجيا",
    "nanjing university of science and technology": "جامعة نانجينغ للعلوم والتكنولوجيا",
    "nanjing university of arts": "جامعة نانجينغ للفنون",
    "poznań university-of-technology": "جامعة بوزنان للتكنولوجيا",
    "berlin university of arts": "جامعة برلين للفنون",
    "bern university of applied sciences": "جامعة برن للعلوم التطبيقية",
    "braunschweig university of art": "جامعة براونشفايغ للفنون",
    "brno university-of-technology": "جامعة برنو للتكنولوجيا",
    "bucharest national university": "جامعة بوخارست الوطنية",
    "budapest university-of-technology": "جامعة بودابست للتكنولوجيا",
    "warsaw university-of-technology": "جامعة وارسو للتكنولوجيا",
    "osaka university of arts": "جامعة أوساكا للفنون",
    "wrocław university of economics": "جامعة فروتسواف للاقتصاد",
    "wrocław university of science and technology": "جامعة فروتسواف للعلوم والتكنولوجيا",
    "guilin university-of-technology": "جامعة غويلين للتكنولوجيا",
    "zurich university of arts": "جامعة زيورخ للفنون",
    "tianjin university-of-technology": "جامعة تيانجين للتكنولوجيا",
    "hanoi national university": "جامعة هانوي الوطنية",
    "hanoi university of science and technology": "جامعة هانوي للعلوم والتكنولوجيا",
    "tokyo university of science": "جامعة طوكيو للعلوم",
    "tokyo university of arts": "جامعة طوكيو للفنون",
    "hefei university-of-technology": "جامعة خفي للتكنولوجيا",
    "pohang university of science and technology": "جامعة بوهانغ للعلوم والتكنولوجيا",
    "szczecin university-of-technology": "جامعة شتتين للتكنولوجيا",
    "tallinn university-of-technology": "جامعة تالين للتكنولوجيا",
    "delft university-of-technology": "جامعة دلفت للتكنولوجيا",
    "eindhoven university-of-technology": "جامعة أيندهوفن للتكنولوجيا",
    "incheon national university": "جامعة إنتشون الوطنية",
    "isfahan university of medical sciences": "جامعة أصفهان للعلوم الطبية",
    "isfahan university-of-technology": "جامعة أصفهان للتكنولوجيا",
    "frankfurt university of applied sciences": "جامعة فرانكفورت للعلوم التطبيقية",
}


@pytest.mark.parametrize("category, expected_key", te_universities_data.items(), ids=te_universities_data.keys())
@pytest.mark.fast
def test_universities_data(category: str, expected_key: str) -> None:
    label = te_universities(category)
    assert label == expected_key


def test_te_universities() -> None:
    # Test with a basic university category
    result = te_universities("university of california")
    assert isinstance(result, str)

    result_empty = te_universities("")
    assert isinstance(result_empty, str)

    # Test with a specific major
    result_major = te_universities("university of engineering")
    assert isinstance(result_major, str)

    # Test with "the" prefix
    result_the = te_universities("the university of law")
    assert isinstance(result_the, str)
