"""
Tests
"""

import pytest

from ArWikiCats.translations_resolvers.new_jobs_resolver.womens import womens_resolver_labels, nat_and_gender_keys

test_data2 = {
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

    "professional artificial intelligence researchers": "باحثات ذكاء اصطناعي محترفات",
    "professional association football managers": "مدربات كرة قدم محترفات",

    # nat + jobs
    "yemeni female eugenicists": "عالمات يمنيات متخصصات في تحسين النسل",
    "yemeni female politicians who committed suicide": "سياسيات يمنيات أقدمن على الانتحار",
    "yemeni female contemporary artists": "فنانات يمنيات معاصرات",

    "yemeni actresses": "ممثلات يمنيات",
    "yemeni female writers": "كاتبات يمنيات",
    "greek female writers": "كاتبات يونانيات",
    "malian professional artificial intelligence researchers": "باحثات ذكاء اصطناعي محترفات ماليات",
    "malian professional association football managers": "مدربات كرة قدم محترفات ماليات",

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


@pytest.mark.skip2
def test_must_be_empty() -> None:
    result = womens_resolver_labels("Yemeni singers")
    assert result == ""


test_religions_data_2 = {
    "Category:Pakistani expatriate female actors": "تصنيف:ممثلات باكستانيات مغتربات",
    "Category:expatriate female actors": "تصنيف:ممثلات مغتربات",
}


@pytest.mark.parametrize("category,expected", test_religions_data_2.items(), ids=test_religions_data_2.keys())
@pytest.mark.skip2
def test_religions_2(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = womens_resolver_labels(category)
    assert result == expected


def test_nat_and_gender_keys():
    data = nat_and_gender_keys("expatriate", "{women}", "{ar_nat} مغتربات")

    assert data == {
        '{en_nat} {women} expatriate': '{ar_nat} مغتربات',
        '{en_nat} expatriate {women}': '{ar_nat} مغتربات',
        '{women} {en_nat} expatriate': '{ar_nat} مغتربات'
    }, print(data)
