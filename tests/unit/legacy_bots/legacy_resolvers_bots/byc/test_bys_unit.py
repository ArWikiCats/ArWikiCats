"""Tests for :mod:`legacy_bots.legacy_resolvers_bots.bys`."""

from __future__ import annotations

import pytest

from ArWikiCats.legacy_bots.legacy_resolvers_bots import bys


@pytest.mark.unit
def test_make_by_label_prefers_film_labels(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "ArWikiCats.legacy_bots.legacy_resolvers_bots.bys.all_new_resolvers",
        lambda name: {"The Matrix": "فيلم"}.get(name, ""),
    )

    result = bys.make_by_label("by The Matrix")
    assert result == "بواسطة فيلم"


@pytest.mark.unit
def test_make_by_label_falls_back_to_nationality(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "ArWikiCats.legacy_bots.legacy_resolvers_bots.bys.all_new_resolvers",
        lambda name: {"Ali": "مصري"}.get(name, ""),
    )

    result = bys.make_by_label("by Ali")
    assert result == "بواسطة مصري"


@pytest.mark.unit
def test_find_dual_by_keys_supports_dual_categories(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "ArWikiCats.legacy_bots.legacy_resolvers_bots.bys.resolve_by_labels",
        lambda name: {"alpha": "ألفا", "beta": "بيتا"}.get(name, ""),
    )

    result = bys.find_dual_by_keys("by alpha and beta")
    assert result == "حسب ألفا وبيتا"


@pytest.mark.unit
def test_get_by_label_combines_entity_and_suffix(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "ArWikiCats.legacy_bots.legacy_resolvers_bots.bys.resolve_by_labels",
        lambda name: {"by birth": "حسب الميلاد"}.get(name, ""),
    )
    monkeypatch.setattr(
        "ArWikiCats.legacy_bots.legacy_resolvers_bots.bys.get_from_new_p17_final",
        lambda name: {"artist": "فنان"}.get(name, ""),
    )

    result = bys.get_by_label("Artist by birth")
    assert result == "فنان حسب الميلاد"
