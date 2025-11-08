"""Tests for the refactored city translation dataset loader."""

from __future__ import annotations

from src.ma_lists.geo.Cities import (
    CITY_LABEL_PATCHES,
    CITY_TRANSLATIONS,
    CITY_TRANSLATIONS_LOWER,
    CITY_OVERRIDES,
    CityTranslationDataset,
    build_city_translation_dataset,
)


def test_city_dataset_includes_manual_overrides() -> None:
    """Manual overrides should take precedence over JSON entries."""

    assert CITY_TRANSLATIONS["Jerusalem"] == CITY_OVERRIDES["Jerusalem"]
    assert CITY_TRANSLATIONS_LOWER["jerusalem"] == CITY_OVERRIDES["Jerusalem"]


def test_city_dataset_contains_base_translations() -> None:
    """Existing JSON keys should still be present in the merged dataset."""

    assert CITY_TRANSLATIONS["yangon"] == "يانغون"
    assert CITY_TRANSLATIONS_LOWER["yangon"] == "يانغون"


def test_city_label_patches_are_loaded() -> None:
    """Patch mappings should expose lowercase helper entries."""

    assert CITY_LABEL_PATCHES["lionhead studios"] == "ليونهيد استوديو"


def test_build_city_dataset_with_custom_sources(monkeypatch) -> None:
    """The builder should merge arbitrary mappings using provided filenames."""

    fake_sources = {
        "base": {"Alpha": "ألفا"},
        "supp": {"Beta": "بيتا"},
        "patch": {"alpha": "ألفا"},
    }

    def fake_loader(name: str):
        return fake_sources[name]

    monkeypatch.setattr("src.ma_lists.geo.Cities.open_json_file", fake_loader)
    monkeypatch.setattr("src.ma_lists.geo.Cities.CITY_OVERRIDES", {}, raising=False)

    dataset = build_city_translation_dataset(
        base_file="base",
        supplement_file="supp",
        patch_file="patch",
    )

    assert isinstance(dataset, CityTranslationDataset)
    assert dataset.translations == {"Alpha": "ألفا", "Beta": "بيتا"}
    assert dataset.patches == {"alpha": "ألفا"}
    assert dataset.lowercase_translations == {"alpha": "ألفا", "beta": "بيتا"}
