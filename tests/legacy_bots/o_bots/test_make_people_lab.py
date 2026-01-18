"""
Tests
"""

import pytest

from ArWikiCats.legacy_bots.o_bots.peoples_resolver import make_people_lab

fast_data = {
    "video games people": "أعلام ألعاب فيديو",
    "soap opera people": "أعلام مسلسلات طويلة",
    "television characters people": "أعلام شخصيات تلفزيونية",
    "television programs people": "أعلام برامج تلفزيونية",
    "television programmes people": "أعلام برامج تلفزيونية",
    "web series people": "أعلام مسلسلات ويب",
    "television series people": "أعلام مسلسلات تلفزيونية",
    "film series people": "أعلام سلاسل أفلام",
    "television episodes people": "أعلام حلقات تلفزيونية",
    "television news people": "أعلام أخبار تلفزيونية",
    "comics people": "أعلام قصص مصورة",
    "television films people": "أعلام أفلام تلفزيونية",
    "miniseries people": "أعلام مسلسلات قصيرة",
    "television miniseries people": "أعلام مسلسلات قصيرة تلفزيونية",
    "video games": "أعلام ألعاب فيديو",
    "television series": "أعلام مسلسلات تلفزيونية",
    "unknown category people": "",
    "": "",
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
@pytest.mark.fast
def test_make_people_lab(category: str, expected: str) -> None:
    label = make_people_lab(category)
    assert label == expected
