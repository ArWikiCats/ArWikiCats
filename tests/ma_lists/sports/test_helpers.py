from __future__ import annotations

import logging
import sys

import pytest

from src.ma_lists.sports import _helpers
from src.ma_lists.sports import cycling
from src.ma_lists.sports import sports_lists


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


def test_log_length_stats_uses_logging_when_len_print_missing(
    monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture
) -> None:
    monkeypatch.setitem(sys.modules, "src.helps", None)
    monkeypatch.setitem(sys.modules, "src.helps.len_print", None)

    with caplog.at_level(logging.DEBUG):
        _helpers.log_length_stats("sports.module", {"templates": 10})

    assert "sports.module[templates]=10" in caplog.text


def test_log_length_stats_invokes_len_print(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import src.helps.len_print as len_print

    calls: dict[str, object] = {}

    def recorder(bot: str, tab: dict[str, int], *, Max: int | None = None) -> None:
        calls["bot"] = bot
        calls["tab"] = tab
        calls["Max"] = Max

    monkeypatch.setattr(len_print, "lenth_pri", recorder)

    _helpers.log_length_stats("sports.module", {"templates": 10}, max_entries=50)

    assert calls == {
        "bot": "sports.module",
        "tab": {"templates": 10},
        "Max": 50,
    }


def test_build_cycling_templates_produces_derivative_keys() -> None:
    templates = cycling.build_cycling_templates()
    base_label = cycling.BASE_CYCLING_EVENTS["tour de france"]

    assert templates["tour de france"] == base_label
    assert templates["tour de france media"] == f"إعلام {base_label}"
    assert templates["tour de france stage winners"] == f"فائزون في مراحل {base_label}"


def test_cycling_aliases_match_primary_templates() -> None:
    assert cycling.new2019_cycling is cycling.CYCLING_TEMPLATES
    assert cycling.new_cy is cycling.CYCLING_TEMPLATES


def test_new_tato_nat_includes_year_templates() -> None:
    result = sports_lists.NEW_TATO_NAT

    assert result[" under-17"] == "{nat} تحت 17 سنة"
    assert result["national under-17"] == "{nat} تحت 17 سنة"
    assert result[""] == "{nat}"

