"""
Tests
"""

import pytest

from ArWikiCats.make_bots.jobs_bots.nat_jobs_resolver_womens import get_label

test_data2 = {
    # nat
    "female welsh people": "ويلزيات",
    "women's yemeni people": "يمنيات",

    # jobs
    "female writers people": "كاتبات",
    "female archers": "نبالات",
    "football managers": "مدراء كرة قدم",
    "female expatriate football managers": "مدراء كرة قدم مغتربات",
    "expatriate female actresses": "ممثلات مغتربات",

    # nat + jobs
    "yemeni writers": "كاتبات يمنيات",
    "yemeni female writers": "كاتبات يمنيات",
    "greek female writers": "كاتبات يونانيون",
}


@pytest.mark.parametrize("category,expected", test_data2.items(), ids=test_data2.keys())
def test_nat_pattern_multi(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = get_label(category)
    assert result == expected
