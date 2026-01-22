"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.jobs_resolvers.womens import nat_and_gender_keys, womens_resolver_labels
from ArWikiCats.translations import jobs_mens_data, jobs_womens_data

test_data2 = {
    "Category:Canadian women film directors": "تصنيف:مخرجات أفلام كنديات",
    "Category:Canadian women's film directors": "تصنيف:مخرجات أفلام كنديات",
    "Category:Canadian womens film directors": "تصنيف:مخرجات أفلام كنديات",
    "Category:Canadian female film directors": "تصنيف:مخرجات أفلام كنديات",
    # nat
    "female welsh people": "ويلزيات",
    "women's yemeni people": "يمنيات",
    # jobs
    "female eugenicists": "عالمات متخصصات في تحسين النسل",
    "female politicians who committed suicide": "سياسيات أقدمن على الانتحار",
    "female writers people": "كاتبات",
    "female archers": "نبالات",
    # "female football managers": "مديرات كرة قدم",
    "female football managers": "مدربات كرة قدم",
    "actresses": "ممثلات",
    "female actresses": "ممثلات",
    # jobs + expatriate
    "female expatriate football managers": "مدربات كرة قدم مغتربات",
    "expatriate female actresses": "ممثلات مغتربات",
    # nat + jobs
    "yemeni female eugenicists": "عالمات يمنيات متخصصات في تحسين النسل",
    "yemeni female politicians who committed suicide": "سياسيات يمنيات أقدمن على الانتحار",
    "yemeni female contemporary artists": "فنانات يمنيات معاصرات",
    "yemeni actresses": "ممثلات يمنيات",
    "yemeni female writers": "كاتبات يمنيات",
    "greek female writers": "كاتبات يونانيات",
    # "yemeni expatriate female actresses": "ممثلات يمنيات مغتربات",
    "female greek blind": "يونانيات مكفوفات",
    "female writers blind": "كاتبات مكفوفات",
    "female greek writers blind": "كاتبات يونانيات مكفوفات",
    "female writers greek blind": "كاتبات يونانيات مكفوفات",
}


@pytest.mark.parametrize("category,expected", test_data2.items(), ids=test_data2.keys())
def test_nat_pattern_multi(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = womens_resolver_labels(category)
    assert result == expected


def test_must_be_empty() -> None:
    result = womens_resolver_labels("Yemeni singers")
    assert result == ""


def test_must_not_be_empty() -> None:
    result = womens_resolver_labels("Yemeni actresses")
    assert result == "ممثلات يمنيات"


test_religions_data_2 = {
    "Pakistani expatriate female actors": "ممثلات باكستانيات مغتربات",
    "expatriate female actors": "ممثلات مغتربات",
    "women's guitarists": "عازفات قيثارة",
    "women educators": "معلمات",
    "women medical doctors": "طبيبات",
    "women singers": "مغنيات",
    "northern ireland": "",
}


@pytest.mark.parametrize("category,expected", test_religions_data_2.items(), ids=test_religions_data_2.keys())
def test_religions_2(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = womens_resolver_labels(category)
    assert result == expected


def test_nat_and_gender_keys():
    data = nat_and_gender_keys("{en_nat}", "expatriate", "{women}", "{ar_nat} مغتربات")

    assert data == {
        "{en_nat} {women} expatriate": "{ar_nat} مغتربات",
        "{en_nat} expatriate {women}": "{ar_nat} مغتربات",
        "{women} {en_nat} expatriate": "{ar_nat} مغتربات",
    }, print(data)


def test_compare():
    # jobs_mens_data jobs_womens_data
    new_keys = {x: v for x, v in jobs_womens_data.items() if x not in jobs_mens_data}
    expected = {
        "women": "نساء",
        "sportswomen": "رياضيات",
        "midwives": "قابلات",
        "prostitutes": "داعرات",
        "video game actresses": "ممثلات ألعاب فيديو",
        "women's-footballers": "لاعبات كرة قدم",
    }
    # assert new_keys == expected
    assert all(key in jobs_womens_data for key in expected.keys())
