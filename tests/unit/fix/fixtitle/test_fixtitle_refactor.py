"""Unit tests for the refactored :mod:`ArWikiCats.fix.fixtitle` helpers."""

from __future__ import annotations

from ArWikiCats.fix.fixtitle import add_fee, fix_it, fixlabel


def test_fix_it_applies_expected_normalizations() -> None:
    """``fix_it`` should apply key replacements from the refactor."""
    data = [
        ("الشعر العربي", "", "شعر العربي"),
        ("هجمات في باريس", "attacks on paris", "هجمات على باريس"),
        ("اقتصاد اليابان حسب الولاية", "", "اقتصاد اليابان حسب المحافظة"),
        ("حرب 1990-91", "", "حرب 1990–91"),
    ]
    for raw_label, en_label, expected in data:
        assert fix_it(raw_label, en_label) == expected


def test_fixlab_rejects_invalid_labels() -> None:
    """``fixlabel`` should discard labels with latin letters or stray dashes."""
    data = [
        "Label مع حروف انجليزية",
        "–1990 في القاهرة",
    ]
    for raw_label in data:
        assert fixlabel(raw_label) == ""


def test_fixlab_pipeline_strips_namespace_and_moves_years() -> None:
    """Full ``fixlabel`` pipeline should normalise underscores and year placement."""

    assert fixlabel("تصنيف:2020_في_الرياضة_في_تكساس") == "الرياضة في تكساس في 2020"


def test_add_fee_inserts_preposition_for_supported_categories() -> None:
    """``add_fee`` should only insert the preposition for configured categories."""
    data = [
        ("قوائم أفلام حسب البلد أو اللغة 1999", "قوائم أفلام حسب البلد أو اللغة في 1999"),
        ("أحداث حسب القارة 1999", "أحداث حسب القارة في 1999"),
    ]
    for text, expected in data:
        assert add_fee(text) == expected


def test_fix_it_should_not_remove_fe_from_endings() -> None:
    en = "people from santa fe province"
    ar = "أشخاص من محافظة سانتا-في"

    assert fix_it(ar, en) == ar


def test_fix_it_should_not_remove_fe_from_endings2() -> None:
    en = "people from santa fe province by city"
    ar = "أشخاص من محافظة سانتا-في حسب المدينة"

    assert fixlabel(ar, en) == ar
