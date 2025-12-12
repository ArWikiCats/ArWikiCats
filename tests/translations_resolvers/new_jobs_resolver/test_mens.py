"""
Tests
"""

import pytest

from ArWikiCats.translations_resolvers.new_jobs_resolver.mens import mens_resolver_labels
from ArWikiCats.make_bots.jobs_bots.relegin_jobs_new import new_religions_jobs_with_suffix

test_data2 = {
    # Category:Turkish expatriate sports-people
    "Category:Turkish expatriate sports-people": "تصنيف:رياضيون أتراك مغتربون",

    # nat
    "welsh people": "أعلام ويلزيون",
    "yemeni people": "أعلام يمنيون",
    # "abkhazian-american": "أمريكيون أبخازيون",
    # "abkhazian-american people": "أمريكيون أبخازيون",

    # jobs
    "eugenicists": "علماء متخصصون في تحسين النسل",
    "politicians who committed suicide": "سياسيون أقدموا على الانتحار",

    "writers people": "أعلام كتاب",
    "archers": "نبالون",
    "male archers": "نبالون ذكور",
    "football managers": "مدربو كرة قدم",
    # "expatriate football managers": "مدربو كرة قدم مغتربون",
    # "expatriate male actors": "ممثلون ذكور مغتربون",

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


@pytest.mark.parametrize("category,expected", test_data2.items(), ids=test_data2.keys())
def test_nat_pattern_multi(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = mens_resolver_labels(category)
    assert result == expected


test_religions_data = {
    "Category:Yemeni shi'a muslims": "تصنيف:يمنيون مسلمون شيعة",
    "Category:Yemeni shia muslims": "تصنيف:يمنيون مسلمون شيعة",
    "Category:Yemeni male muslims": "تصنيف:يمنيون مسلمون ذكور",
    "Category:Yemeni muslims male": "تصنيف:يمنيون مسلمون ذكور",

    "Category:Yemeni muslims": "تصنيف:يمنيون مسلمون",
    "Category:Yemeni people muslims": "تصنيف:يمنيون مسلمون",

    "Category:Pakistani expatriate footballers": "تصنيف:لاعبو كرة قدم باكستانيون مغتربون",

}


@pytest.mark.parametrize("category,expected", test_religions_data.items(), ids=test_religions_data.keys())
def test_religions(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    # result = new_religions_jobs_with_suffix(category)
    result = mens_resolver_labels(category)
    assert result == expected


test_religions_data_2 = {
    "Category:Pakistani expatriate male actors": "تصنيف:ممثلون ذكور باكستانيون مغتربون",
    "Category:expatriate male actors": "تصنيف:ممثلون ذكور مغتربون",
}


@pytest.mark.parametrize("category,expected", test_religions_data_2.items(), ids=test_religions_data_2.keys())
@pytest.mark.skip2
def test_religions_2(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = mens_resolver_labels(category)
    assert result == expected
