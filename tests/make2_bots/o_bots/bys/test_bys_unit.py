"""Tests for :mod:`make_bots.o_bots.bys`."""

from __future__ import annotations

import pytest
from ArWikiCats.make_bots.o_bots import bys


@pytest.fixture(autouse=True)
def reset_bys_tables(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("ArWikiCats.translations.by_type.by_orginal2", {}, raising=False)
    monkeypatch.setattr("ArWikiCats.translations.by_type.by_table_main", {}, raising=False)
    monkeypatch.setattr("ArWikiCats.make_bots.lazy_data_bots.bot_2018.pop_All_2018", {}, raising=False)


def test_make_by_label_prefers_film_labels(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(bys, "te_films", lambda name: "فيلم" if name == "The Matrix" else "", raising=False)

    result = bys.make_by_label("by The Matrix")
    assert result == "بواسطة فيلم"


def test_make_by_label_falls_back_to_nationality(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(bys, "te_films", lambda name: "مصري" if name == "Ali" else "", raising=False)

    result = bys.make_by_label("by Ali")
    assert result == "بواسطة مصري"


def test_make_by_label_supports_dual_categories(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(bys, "te_films", lambda name: "", raising=False)
    monkeypatch.setattr("ArWikiCats.translations.by_type.by_orginal2", {"alpha": "ألفا", "beta": "بيتا"}, raising=False)

    result = bys.make_by_label("by alpha and beta")
    assert result == "حسب ألفا وبيتا"


def test_get_by_label_combines_entity_and_suffix(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("ArWikiCats.make_bots.lazy_data_bots.bot_2018.pop_All_2018", {"artist": "فنان"}, raising=False)
    monkeypatch.setattr("ArWikiCats.translations.by_type.by_table_main", {"by birth": "حسب الميلاد"}, raising=False)

    result = bys.get_by_label("Artist by birth")
    assert result == "فنان حسب الميلاد"


def test_get_and_label_returns_joined_entities(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("ArWikiCats.make_bots.lazy_data_bots.bot_2018.pop_All_2018", {"artist": "فنان", "painter": "رسام"}, raising=False)

    result = bys.get_and_label("Artist and Painter")
    assert result == "فنان ورسام"
