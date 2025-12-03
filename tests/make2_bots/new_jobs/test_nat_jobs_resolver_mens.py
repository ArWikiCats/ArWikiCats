"""
Tests
"""

import pytest

from ArWikiCats.make_bots.jobs_bots.nat_jobs_resolver_mens import get_label

test_data2 = {
    # nat
    "welsh people": "ويلزيون",
    "yemeni people": "يمنيون",
    "abkhazian-american": "أمريكيون أبخازيون",
    "abkhazian-american people": "أمريكيون أبخازيون",

    # jobs
    "writers people": "كتاب",
    "archers": "نبالون",
    "male archers": "نبالون ذكور",
    "football managers": "مدراء كرة قدم",
    "expatriate football managers": "مدراء كرة قدم مغتربون",
    "expatriate male actors": "ممثلون ذكور مغتربون",

    # nat + jobs
    "yemeni writers": "كتاب يمنيون",
    "yemeni male writers": "كتاب ذكور يمنيون",
    "greek male writers": "كتاب ذكور يونانيون",
    "abkhazian-american archers": "نبالون أمريكيون أبخازيون",
}


@pytest.mark.parametrize("category,expected", test_data2.items(), ids=test_data2.keys())
def test_nat_pattern_multi(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = get_label(category)
    assert result == expected
