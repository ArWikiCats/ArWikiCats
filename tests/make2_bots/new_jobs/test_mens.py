"""
Tests
"""

import pytest

from ArWikiCats.make_bots.new_jobs.mens import get_label

test_data2 = {
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
}


@pytest.mark.parametrize("category,expected", test_data2.items(), ids=test_data2.keys())
def test_nat_pattern_multi(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = get_label(category)
    assert result == expected
