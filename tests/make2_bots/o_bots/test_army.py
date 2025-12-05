"""
Tests for :mod:`make_bots.o_bots.army`.
TODO: write tests
"""

from __future__ import annotations

import pytest

from ArWikiCats.make_bots.o_bots import army


def _patch_army_datasets(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(army, "all_country_with_nat", {}, raising=False)
    monkeypatch.setattr(army, "countries_nat_en_key", {}, raising=False)
    monkeypatch.setattr(army, "military_format_men", {}, raising=False)
    monkeypatch.setattr(army, "military_format_women", {}, raising=False)
    monkeypatch.setattr(army, "military_format_women_without_al", {}, raising=False)
    monkeypatch.setattr(army, "military_format_women_without_al_from_end", {}, raising=False)


@pytest.fixture
def base_army_datasets(monkeypatch: pytest.MonkeyPatch) -> None:
    _patch_army_datasets(monkeypatch)


@pytest.mark.usefixtures("base_army_datasets")
def test_te_army_resolves_women_without_article_prefix(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(army, "military_format_women_without_al_from_end", {"women of": "{nat} بدون ال"}, raising=False)
    monkeypatch.setattr(
        army,
        "countries_nat_en_key",
        {"canada": {"female": "كنديات"}},
        raising=False,
    )

    result = army.te_army("women of canada")
    assert result == "كنديات بدون ال"


@pytest.mark.usefixtures("base_army_datasets")
def test_te_army_resolves_men_suffix(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        army,
        "all_country_with_nat",
        {"France": {"en": "France", "male": "فرنسي"}},
        raising=False,
    )
    monkeypatch.setattr(army, "military_format_men", {"army": "{nat} العسكري"}, raising=False)

    result = army.te_army("France army")
    assert result == "الفرنسي العسكري"
