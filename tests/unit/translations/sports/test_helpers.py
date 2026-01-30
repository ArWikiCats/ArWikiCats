from __future__ import annotations

from ArWikiCats.translations.sports import _helpers, cycling


def test_extend_with_templates_preserves_positional_placeholders() -> None:
    target: dict[str, str] = {}
    templates = {"{} national team": "{} national team {year}"}

    _helpers.extend_with_templates(target, templates, year=2024)

    assert target == {"{} national team": "{} national team 2024"}


def test_extend_with_year_templates_default_years() -> None:
    target: dict[str, str] = {}

    _helpers.extend_with_year_templates(target, {"under-{year}": "under {year}"})

    expected = {f"under-{year}": f"under {year}" for year in _helpers.YEARS}
    assert target == expected


def test_build_cycling_templates_produces_derivative_keys() -> None:
    templates = cycling.build_cycling_templates()
    base_label = cycling.BASE_CYCLING_EVENTS["tour de france"]

    assert templates["tour de france"] == base_label
    assert templates["tour de france media"] == f"إعلام {base_label}"
    assert templates["tour de france stage winners"] == f"فائزون في مراحل {base_label}"


def test_cycling_aliases_match_primary_templates() -> None:
    assert cycling.CYCLING_TEMPLATES is cycling.CYCLING_TEMPLATES
    assert cycling.CYCLING_TEMPLATES is cycling.CYCLING_TEMPLATES
