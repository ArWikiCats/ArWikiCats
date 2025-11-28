#!/usr/bin/python3
""" """

import pytest

from ArWikiCats.translations.sports.sub_teams_keys import sub_teams_new


def _get_value(category: str) -> None:
    return sub_teams_new.get(category)


examples = {
    "men's a' netball": "كرة الشبكة للرجال للمحليين",
    "men's a' nordic combined racing": "سباق التزلج النوردي المزدوج للرجال للمحليين",
    "youth orienteering": "سباق موجه للشباب",
    "youth pair skating racing": "سباق التزلج الفني على الجليد للشباب",
    "men's a' triathlon": "السباق الثلاثي للرجال للمحليين",
    "men's a' triple jump racing": "سباق القفز الثلاثي للرجال للمحليين",
    "figure skating racing mass media": "إعلام سباق التزلج الفني",
    "figure skating racing non-playing staff": "طاقم سباق التزلج الفني غير اللاعبين",
}


@pytest.mark.parametrize(
    "category, expected",
    examples.items(),
    ids=[k for k in examples],
)
def test_resolves_basic_templates(category: str, expected: str) -> None:
    """Templates driven by the lightweight map should translate correctly."""

    result = _get_value(category)
    assert result == expected


olympic_examples = {
    "figure skating racing olympic champions": "أبطال سباق تزلج فني أولمبي",
    "figure skating olympic": "تزلج فني أولمبي",
    "figure skating olympics": "تزلج فني أولمبي",
    "jujutsu racing non-playing staff": "طاقم سباق جوجوتسو غير اللاعبين",
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


@pytest.mark.parametrize(
    "category, expected",
    olympic_examples.items(),
    ids=[k for k in olympic_examples],
)
def test_handles_olympic_variants(category: str, expected: str) -> None:
    """Olympic templates should rely on the shared helper translation."""

    result = _get_value(category)
    assert result == expected
