# -*- coding: utf-8 -*-
"""Tests for the sports match resolver that relies on ``FormatData``."""

import pytest

from ArWikiCats.new import Match_sports


CASES = [
    ("men's football world cup", "كأس العالم للرجال في كرة القدم"),
    ("women's basketball world cup", "كأس العالم للسيدات في كرة السلة"),
    ("softball world cup", "كأس العالم في سوفتبول"),
    ("men's volleyball world championship", "بطولة العالم للرجال في كرة الطائرة"),
    ("women's handball world championship", "بطولة العالم للسيدات في كرة اليد"),
    ("rugby union world championship", "بطولة العالم في اتحاد الرجبي"),
    ("men's football asian championship", "بطولة آسيا للرجال في كرة القدم"),
    ("men's futsal league", "دوري الرجال في كرة الصالات"),
    ("women's cricket league", "دوري السيدات في كريكيت"),
    ("baseball league", "الدوري في بيسبول"),
    ("u23 football championship", "بطولة تحت 23 سنة في كرة القدم"),
    ("u17 basketball world cup", "كأس العالم تحت 17 سنة في كرة السلة"),
    ("wheelchair tennis", "تنس على كراسي متحركة"),
    ("sport climbing racing", "سباقات تسلق"),
    ("men's national football team", "منتخب كرة القدم الوطني للرجال"),
    ("women's national volleyball team", "منتخب كرة الطائرة الوطني للسيدات"),
    ("national basketball team", "المنتخب الوطني في كرة السلة"),
    ("random unknown title", ""),
]


@pytest.mark.parametrize("category, expected", CASES, ids=[pair[0] for pair in CASES])
@pytest.mark.fast
def test_resolve_team_label_known_examples(category: str, expected: str) -> None:
    assert Match_sports.resolve_team_label(category) == expected


@pytest.mark.fast
def test_resolve_team_label_handles_relaxed_variants_and_whitespace() -> None:
    """Ensure normalization keeps relaxed matching intact when using FormatData."""

    assert (
        Match_sports.resolve_team_label("  MENS   football   world   cup ")
        == "كأس العالم للرجال في كرة القدم"
    )
    assert (
        Match_sports.resolve_team_label("  women's   BASKETBALL   world   cup  ")
        == "كأس العالم للسيدات في كرة السلة"
    )


@pytest.mark.fast
def test_expand_templates_adds_relaxed_and_singular_variants() -> None:
    """_expand_templates should preserve base keys and add relaxed variants."""

    base_templates = {"women's xoxo leagues": "leagues"}
    expanded = Match_sports._expand_templates(base_templates)

    # Original key remains untouched
    assert expanded["women's xoxo leagues"] == "leagues"
    # Relaxed apostrophe-less key is added
    assert expanded["womens xoxo leagues"] == "leagues"
    # Singular variant is included to mirror previous fallbacks
    assert expanded["women' xoxo league"] == "leagues"


@pytest.mark.fast
def test_load_sports_bot_is_cached() -> None:
    """Repeated calls should return the same cached FormatData instance."""

    first = Match_sports._load_sports_bot()
    second = Match_sports._load_sports_bot()

    assert first is second


@pytest.mark.fast
def test_normalize_collapses_whitespace_and_dashes() -> None:
    """_normalize should lower-case, trim, and replace en dashes with hyphens."""

    assert (
        Match_sports._normalize("  Men's – Football   World Cup  ")
        == "men's - football world cup"
    )
