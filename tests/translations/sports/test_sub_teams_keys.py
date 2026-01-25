#!/usr/bin/python3
""" """

import pytest

from ArWikiCats.new_resolvers.sports_resolvers.raw_sports import resolve_sport_label_unified

examples_labels = {
    "jujutsu racing non-playing staff": "طاقم سباق جوجوتسو غير اللاعبين",
    "men's a' netball": "كرة الشبكة للرجال للمحليين",
    "men's a' nordic combined racing": "سباق التزلج النوردي المزدوج للرجال للمحليين",
    "youth orienteering": "سباق موجه شبابية",
    "men's a' triathlon": "السباق الثلاثي للرجال للمحليين",
    "men's a' triple jump racing": "سباق القفز الثلاثي للرجال للمحليين",
    "figure skating racing mass media": "إعلام سباق التزلج الفني",
}


olympic_examples = {
    "figure skating racing olympic champions": "أبطال سباق تزلج فني أولمبي",
    "figure skating olympic": "تزلج فني أولمبي",
    "figure skating olympics": "تزلج فني أولمبي",
    "jujutsu racing olympic champions": "أبطال سباق جوجوتسو أولمبي",
    "olympic eventing racing": "سباق محاكمة خيول أولمبية",
    "olympic eventing": "محاكمة خيول أولمبية",
    "olympic fencing racing": "سباق مبارزة سيف شيش أولمبية",
    "olympic fencing": "مبارزة سيف شيش أولمبية",
    "olympic field hockey racing": "سباق هوكي ميدان أولمبي",
    "olympic field hockey": "هوكي ميدان أولمبي",
    "olympic fifa futsal world cup racing": "سباق كأس العالم لكرة الصالات الأولمبية",
    "olympic fifa futsal world cup": "كأس العالم لكرة الصالات الأولمبية",
    "olympic fifa world cup racing": "سباق كأس العالم لكرة القدم الأولمبية",
}


@pytest.mark.parametrize("category, expected", examples_labels.items(), ids=examples_labels.keys())
def test_resolves_basic_templates(category: str, expected: str) -> None:
    """Templates driven by the lightweight map should translate correctly."""

    # result = sub_teams_labels.get(category)
    result2 = resolve_sport_label_unified(category)

    # assert result == expected
    assert result2 == expected


@pytest.mark.parametrize("category, expected", olympic_examples.items(), ids=olympic_examples.keys())
def test_handles_olympic_variants(category: str, expected: str) -> None:
    """
    Verify that Olympic-variant sport label strings are translated to their expected Arabic labels by resolve_sport_label_unified.
    
    Parameters:
        category (str): Input sport label (Olympic variant) to translate.
        expected (str): Expected Arabic translation of the input label.
    """

    # result = sub_teams_olympics.get(category)
    result2 = resolve_sport_label_unified(category)

    # assert result == expected
    assert result2 == expected