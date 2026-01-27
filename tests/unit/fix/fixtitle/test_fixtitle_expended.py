"""Unit tests for the refactored :mod:`ArWikiCats.fix.fixtitle` helpers."""

from __future__ import annotations

import pytest

from ArWikiCats.fix.fixtitle import (
    _apply_basic_normalizations,
    _apply_prefix_replacements,
    _apply_regex_replacements,
    _apply_suffix_replacements,
    _insert_year_preposition,
    _normalize_conflict_phrases,
    _normalize_sub_regions,
    add_fee,
    fix_it,
    fixlabel,
)


@pytest.mark.parametrize(
    "text, expected",
    [("المكان المأهول واحتلال", "المكان المأهول والمهنة"), ("قضاة من مصر", "قضاة في مصر")],
)
def test_apply_regex_replacements(text: str, expected: str) -> None:
    assert (
        _apply_regex_replacements(text, {"المكان المأهول واحتلال": "المكان المأهول والمهنة", "قضاة من ": "قضاة في "})
        == expected
    )


@pytest.mark.parametrize(
    "text, expected",
    [("هجمات ضد المدنيين", "هجمات على المدنيين"), ("تعليم في اليمن", "التعليم في اليمن")],
)
def test_apply_prefix_replacements(text: str, expected: str) -> None:
    assert _apply_prefix_replacements(text, {"هجمات ضد": "هجمات على", "تعليم في ": "التعليم في "}) == expected


@pytest.mark.parametrize(
    "text, expected",
    [("صناعة إعلامية", "صناعة الإعلام"), ("انتهت في", "انتهت")],
)
def test_apply_suffix_replacements(text: str, expected: str) -> None:
    assert _apply_suffix_replacements(text, {"صناعة إعلامية": "صناعة الإعلام", "انتهت في": "انتهت"}) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("كوارث صحية 2020", "كوارث صحية في 2020"),
        ("كوارث طبيعية عقد 1990", "كوارث طبيعية في عقد 1990"),
    ],
)
def test_insert_year_preposition(text: str, expected: str) -> None:
    assert _insert_year_preposition(text, ["كوارث صحية", "كوارث طبيعية"]) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("الغزو الأمريكي في العراق", "الغزو الأمريكي للعراق"),
        ("الحرب العالمية في أوروبا", "الحرب العالمية في أوروبا"),
        ("الغزو الفرنسي في الجزائر", "الغزو الفرنسي للجزائر"),
    ],
)
def test_normalize_conflict_phrases(text: str, expected: str) -> None:
    assert _normalize_conflict_phrases(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("اليابان حسب الولاية", "اليابان حسب المحافظة"),
        ("في سريلانكا الإقليم", "في سريلانكا المقاطعة"),
        ("مديريات تركيا", "أقضية تركيا"),
        ("مديريات جزائر", "دوائر جزائر"),
    ],
)
def test_normalize_sub_regions(text: str, expected: str) -> None:
    assert _normalize_sub_regions(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [("كوارث صحية 2010", "كوارث صحية في 2010"), ("تاريخ التعليم في مصر", "تاريخ التعليم في مصر")],
)
def test_basic_normalizations(text: str, expected: str) -> None:
    assert _apply_basic_normalizations(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [("البلد حسب السنة 2020", "البلد حسب السنة في 2020"), ("المدينة حسب العقد 1990", "المدينة حسب العقد في 1990")],
)
def test_add_fee(text: str, expected: str) -> None:
    assert add_fee(text) == expected


@pytest.mark.parametrize(
    "ar_label, en_label, expected",
    [
        ("كأس العالم لكرة القدم 2022", "World Cup", "كأس العالم 2022"),
        ("تأسيسات سنة 1990", "establishments", "تأسيسات سنة 1990"),
        ("انحلالات سنة 1985", "disestablishments", "انحلالات سنة 1985"),
    ],
)
def test_fix_it_common(ar_label: str, en_label: str, expected: str) -> None:
    result = fix_it(ar_label, en_label)
    assert expected in result


@pytest.mark.parametrize(
    "label_old, expected",
    [("تصنيف:كوارث طبيعية 2010", "كوارث طبيعية في 2010"), ("كأس العالم لكرة القدم 2018", "كأس العالم 2018")],
)
def test_fixlab_integration(label_old: str, expected: str) -> None:
    assert fixlabel(label_old) == expected


@pytest.mark.parametrize(
    "label_old",
    ["مشاعر معادية للإسرائيليون", "abc_english"],
)
def test_fixlab_rejected(label_old: str) -> None:
    assert fixlabel(label_old) == ""


@pytest.mark.parametrize(
    "ar_label, en_label",
    [
        ("من القرن 19", "19th century"),
        ("من الحروب", "wars"),
        ("من الثورة", "revolutions"),
    ],
)
def test_fix_it_expanded_patterns(ar_label: str, en_label: str) -> None:
    result = fix_it(ar_label, en_label)
    assert isinstance(result, str)
    assert result != ""


@pytest.mark.parametrize(
    "ar_label, en_label",
    [("فورمولا 1 2020", "Formula 1 2020"), ("فورمولا 1 1990", "Formula 1 1990")],
)
def test_fix_it_formula_patterns(ar_label: str, en_label: str) -> None:
    result = fix_it(ar_label, en_label)
    assert "سنة" in result, f"Expected 'سنة' in {result}"
