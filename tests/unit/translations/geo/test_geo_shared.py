import logging

import pytest

from ArWikiCats.translations.geo import _shared


def test_load_json_mapping_filters_empty_entries(monkeypatch: pytest.MonkeyPatch) -> None:
    """``load_json_mapping`` drops empty keys/values and coerces to strings."""

    def fake_open(filename: str) -> dict[object, object]:  # pragma: no cover - helper
        assert filename == "demo"
        return {
            "": "ignored",
            "valid": 123,
            42: 3.14,
            "none": None,
        }

    monkeypatch.setattr(_shared, "open_json_file", fake_open)

    data = _shared.load_json_mapping("demo")

    assert data == {"valid": "123", "42": "3.14"}


def test_load_json_mapping_filters_and_normalizes(monkeypatch) -> None:
    mock_data = {1: "value", "empty": "", "none": None}

    def fake_open_json(file_key: str) -> dict:
        assert file_key == "example"
        return mock_data

    monkeypatch.setattr(_shared, "open_json_file", fake_open_json)

    result = _shared.load_json_mapping("example")

    assert result == {"1": "value"}
    # Original dictionary should be unchanged by the loader.
    assert mock_data[1] == "value"


def test_merge_mappings_prefers_later_entries() -> None:
    merged = _shared.merge_mappings({"a": "1"}, {"b": "2"}, {"a": "3"})

    assert merged == {"a": "3", "b": "2"}


def test_update_with_lowercased_skips_empty_values() -> None:
    target: dict[str, str] = {"existing": "value"}
    _shared.update_with_lowercased(target, {"Key": "Value", "Other": "", "None": None})

    assert target["key"] == "Value"
    assert "Other" not in target


def test_apply_suffix_templates_formats_entries() -> None:
    target: dict[str, str] = {}
    mapping = {"Base": "أساس"}
    suffixes = ((" suffix", "%s الموسعة"),)

    _shared.apply_suffix_templates(target, mapping, suffixes)

    assert target == {"base suffix": "أساس الموسعة"}


def test_normalize_to_lower_returns_new_dict() -> None:
    original = {"Key": "Value"}
    normalized = _shared.normalize_to_lower(original)

    assert normalized == {"key": "Value"}
    assert normalized is not original
