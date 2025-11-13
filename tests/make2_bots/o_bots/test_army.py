
"""Tests for :mod:`make2_bots.o_bots.army`."""

from __future__ import annotations

import pytest

from src.make2_bots.o_bots import army


@pytest.fixture(autouse=True)
def reset_army_cache() -> None:
    army.TEST_ARMY_CACHE.clear()


def _patch_army_datasets(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(army, "all_country_with_nat", {}, raising=False)
    monkeypatch.setattr(army, "all_country_with_nat_keys_is_en", {}, raising=False)
    monkeypatch.setattr(army, "military_format_men", {}, raising=False)
    monkeypatch.setattr(army, "military_format_women", {}, raising=False)
    monkeypatch.setattr(army, "military_format_women_without_al", {}, raising=False)
    monkeypatch.setattr(army, "military_format_women_without_al_from_end", {}, raising=False)
    monkeypatch.setattr(army, "SPORT_FORMTS_EN_P17_AR_NAT", {}, raising=False)


@pytest.fixture
def base_army_datasets(monkeypatch: pytest.MonkeyPatch) -> None:
    _patch_army_datasets(monkeypatch)


@pytest.mark.usefixtures("base_army_datasets")
def test_test_army_resolves_women_without_article_prefix(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(army, "military_format_women_without_al_from_end", {"women of": "{nat} بدون ال"}, raising=False)
    monkeypatch.setattr(
        army,
        "all_country_with_nat_keys_is_en",
        {"canada": {"women": "كنديات"}},
        raising=False,
    )

    result = army.test_army("women of canada")
    assert result == "كنديات بدون ال"


@pytest.mark.usefixtures("base_army_datasets")
def test_test_army_resolves_men_suffix(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        army,
        "all_country_with_nat",
        {"France": {"en": "France", "men": "فرنسي"}},
        raising=False,
    )
    monkeypatch.setattr(army, "military_format_men", {"army": "{nat} العسكري"}, raising=False)

    result = army.test_army("France army")
    assert result == "الفرنسي العسكري"


@pytest.mark.usefixtures("base_army_datasets")
def test_test_army_returns_cached_value(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        army,
        "all_country_with_nat",
        {"France": {"en": "France", "men": "فرنسي"}},
        raising=False,
    )
    monkeypatch.setattr(army, "military_format_men", {"army": "{nat} العسكري"}, raising=False)

    first = army.test_army("France army")
    monkeypatch.setattr(army, "all_country_with_nat", {}, raising=False)
    second = army.test_army("France army")

    assert first == "الفرنسي العسكري"
    assert second == "الفرنسي العسكري"
