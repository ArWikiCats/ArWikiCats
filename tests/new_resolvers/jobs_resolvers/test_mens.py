"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.jobs_resolvers.mens import mens_resolver_labels, nat_and_gender_keys

test_data2 = {
    # Category:Turkish expatriate sports-people
    "Category:Turkish expatriate sports-people": "تصنيف:رياضيون أتراك مغتربون",
    # nat
    "welsh people": "ويلزيون",
    "yemeni people": "يمنيون",
    # "abkhazian-american": "أبخازيون أمريكيون",
    # "abkhazian-american people": "أبخازيون أمريكيون",
    # jobs
    "eugenicists": "علماء متخصصون في تحسين النسل",
    "politicians who committed suicide": "سياسيون أقدموا على الانتحار",
    "writers people": "أعلام كتاب",
    "archers": "نبالون",
    "male archers": "نبالون ذكور",
    "football managers": "مدربو كرة قدم",
    # jobs + expatriate
    "expatriate football managers": "مدربو كرة قدم مغتربون",
    "expatriate male actors": "ممثلون ذكور مغتربون",
    "expatriate actors": "ممثلون مغتربون",
    "male actors": "ممثلون ذكور",
    # nat + jobs
    "yemeni eugenicists": "علماء يمنيون متخصصون في تحسين النسل",
    "yemeni politicians who committed suicide": "سياسيون يمنيون أقدموا على الانتحار",
    "yemeni contemporary artists": "فنانون يمنيون معاصرون",
    "yemeni writers": "كتاب يمنيون",
    "yemeni male writers": "كتاب ذكور يمنيون",
    "greek male writers": "كتاب ذكور يونانيون",
    # "abkhazian-american archers": "نبالون أمريكيون أبخازيون",
    "greek writers blind": "كتاب يونانيون مكفوفون",
    "writers greek blind": "كتاب يونانيون مكفوفون",
}

test_data_2 = {
    "Category:Pakistani expatriate male actors": "تصنيف:ممثلون ذكور باكستانيون مغتربون",
    "Category:expatriate male actors": "تصنيف:ممثلون ذكور مغتربون",
    "Category:Pakistani expatriate footballers": "تصنيف:لاعبو كرة قدم باكستانيون مغتربون",
    "educators": "معلمون",
    "medical doctors": "أطباء",
    "singers": "مغنون",
    "northern ireland": "",
    "republic of ireland": "",
    "republic-of ireland": "",
}


@pytest.mark.parametrize("category,expected", test_data2.items(), ids=test_data2.keys())
@pytest.mark.fast
def test_nat_pattern_multi(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = mens_resolver_labels(category)
    assert result == expected


@pytest.mark.parametrize("category,expected", test_data_2.items(), ids=test_data_2.keys())
@pytest.mark.fast
def test_religions_2(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = mens_resolver_labels(category)
    assert result == expected


@pytest.mark.fast
def test_people_key() -> None:
    result = mens_resolver_labels("people")
    assert result == ""


def test_nat_and_gender_keys():
    data = nat_and_gender_keys("{en_nat}", "emigrants", "male", "{ar_nat} مهاجرون ذكور")

    assert data == {
        "{en_nat} male emigrants": "{ar_nat} مهاجرون ذكور",
        "{en_nat} emigrants male": "{ar_nat} مهاجرون ذكور",
        "male {en_nat} emigrants": "{ar_nat} مهاجرون ذكور",
    }, print(data)
