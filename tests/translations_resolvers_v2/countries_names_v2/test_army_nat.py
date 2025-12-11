"""
Tests for :mod:`make_bots.o_bots.army`.
TODO: write tests
"""

from __future__ import annotations

import pytest

from ArWikiCats.translations_resolvers_v2.nats_v2 import resolve_by_nats

test_army_nat_data_1 = {
    "albanian congress": "الكونغرس الألباني",
    "argentine army personnel": "أفراد الجيش الأرجنتيني",
    "australian army personnel": "أفراد الجيش الأسترالي",
    "australian courts": "محاكم أسترالية",
    "australian senate elections": "انتخابات مجلس الشيوخ الأسترالي",
    "austrian parliament": "البرلمان النمساوي",
    "bahraini second division": "الدوري البحريني الدرجة الثانية",
    "bangladesh army generals": "جنرالات الجيش البنغلاديشي",
    "belgian army personnel": "أفراد الجيش البلجيكي",
    "belgian second division": "الدوري البلجيكي الدرجة الثانية",
    "brazilian air force generals": "جنرالات القوات الجوية البرازيلية",
    "british army personnel": "أفراد الجيش البريطاني",
    "canadian air force generals": "جنرالات القوات الجوية الكندية",
    "canadian army personnel": "أفراد الجيش الكندي",
    "canadian coast guard": "خفر السواحل الكندي",
    "canadian congress": "الكونغرس الكندي",
    "canadian federal legislation": "تشريعات فيدرالية كندية",
    "canadian house-of-commons": "مجلس العموم الكندي",
    "canadian parliament": "البرلمان الكندي",
    "central american parliament": "البرلمان الأمريكي الأوسطي",
    "czech senate election": "انتخابات مجلس الشيوخ التشيكي",
    "dutch senate elections": "انتخابات مجلس الشيوخ الهولندي",
    "european parliament": "البرلمان الأوروبي",
    "libyan second division": "الدوري الليبي الدرجة الثانية",
    "nigerian senate elections": "انتخابات مجلس الشيوخ النيجيري",
    "chilean air force generals": "جنرالات القوات الجوية التشيلية",
    "chilean army personnel": "أفراد الجيش التشيلي",
    "scottish parliament": "البرلمان الإسكتلندي",
    "south african parliament": "البرلمان الجنوب الإفريقي",
}

test_army_nat_data_2 = {
}


@pytest.mark.fast
@pytest.mark.parametrize("category,expected", test_army_nat_data_1.items(), ids=test_army_nat_data_1.keys())
def test_army_nat_1(category: str, expected: str) -> None:
    result = resolve_by_nats(category)
    assert result == expected


@pytest.mark.fast
@pytest.mark.parametrize("category,expected", test_army_nat_data_2.items(), ids=test_army_nat_data_2.keys())
def test_army_nat_2(category: str, expected: str) -> None:
    result = resolve_by_nats(category)
    assert result == expected
