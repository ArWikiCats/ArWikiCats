"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.jobs_resolvers.mens import mens_resolver_labels

test_data2 = {
    # "yemeni philosophers and theologians": "فلاسفة ولاهوتيون يمنيون",
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
    "football managers": "مدربو كرة قدم",
    # jobs + expatriate
    "expatriate football managers": "مدربو كرة قدم مغتربون",
    "expatriate actors": "ممثلون مغتربون",
    # nat + jobs
    "yemeni eugenicists": "علماء يمنيون متخصصون في تحسين النسل",
    "yemeni politicians who committed suicide": "سياسيون يمنيون أقدموا على الانتحار",
    "yemeni contemporary artists": "فنانون يمنيون معاصرون",
    "yemeni writers": "كتاب يمنيون",
    # "abkhazian-american archers": "نبالون أمريكيون أبخازيون",
    "greek writers blind": "كتاب يونانيون مكفوفون",
    "writers greek blind": "كتاب يونانيون مكفوفون",
}

test_data_2 = {
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
def test_mens_2(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = mens_resolver_labels(category)
    assert result == expected


@pytest.mark.fast
def test_people_key() -> None:
    result = mens_resolver_labels("people")
    assert result == ""
