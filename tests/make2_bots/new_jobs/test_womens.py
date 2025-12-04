"""
Tests
"""

import pytest

from ArWikiCats.make_bots.new_jobs.womens import get_label

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
    # "female expatriate football managers": "مدربات كرة قدم مغتربات",
    # "expatriate female actresses": "ممثلات مغتربات",

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
}


@pytest.mark.parametrize("category,expected", test_data2.items(), ids=test_data2.keys())
def test_nat_pattern_multi(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = get_label(category)
    assert result == expected
