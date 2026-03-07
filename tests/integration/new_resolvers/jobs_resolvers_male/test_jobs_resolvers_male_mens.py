"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.jobs_resolvers_male import males_resolver_labels

test_data2 = {
    "Category:Turkish expatriate sports-people": "تصنيف:رياضيون أتراك مغتربون",
    # jobs
    "eugenicists": "علماء متخصصون في تحسين النسل",
    "politicians who committed suicide": "سياسيون أقدموا على الانتحار",
    "archers": "نبالون",
    "male archers": "نبالون ذكور",
    "football managers": "مدربو كرة قدم",
    # jobs + expatriate
    "expatriate football managers": "مدربو كرة قدم مغتربون",
    "expatriate male actors": "ممثلون ذكور مغتربون",
    "expatriate actors": "ممثلون مغتربون",
    "male actors": "ممثلون ذكور",
    "yemeni writers": "كتاب يمنيون",
    "yemeni male writers": "كتاب ذكور يمنيون",
    "greek male writers": "كتاب ذكور يونانيون",
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
    result = males_resolver_labels(category)
    assert result == expected


@pytest.mark.parametrize("category,expected", test_data_2.items(), ids=test_data_2.keys())
@pytest.mark.fast
def test_mens_2(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = males_resolver_labels(category)
    assert result == expected


@pytest.mark.fast
def test_people_key() -> None:
    result = males_resolver_labels("people")
    assert result == ""
