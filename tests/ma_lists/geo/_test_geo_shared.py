import logging

import pytest

from src.ma_lists.geo import _shared


def test_load_json_mapping_filters_and_normalizes(monkeypatch):
    mock_data = {1: "value", "empty": "", "none": None}

    def fake_open_json(file_key: str):
        assert file_key == "example"
        return mock_data

    monkeypatch.setattr(_shared, "open_json_file", fake_open_json)

    result = _shared.load_json_mapping("example")

    assert result == {"1": "value"}
    # Original dictionary should be unchanged by the loader.
    assert mock_data[1] == "value"


def test_load_json_mapping_logs_when_no_entries(monkeypatch, caplog):
    def fake_open_json(file_key: str):
        return {"empty": ""}

    monkeypatch.setattr(_shared, "open_json_file", fake_open_json)

    caplog.set_level(logging.DEBUG)
    result = _shared.load_json_mapping("empty")

    assert result == {}
    assert "did not contain usable labels" in caplog.text


def test_merge_mappings_prefers_later_entries():
    merged = _shared.merge_mappings({"a": "1"}, {"b": "2"}, {"a": "3"})

    assert merged == {"a": "3", "b": "2"}


def test_update_with_lowercased_skips_empty_values():
    target: dict[str, str] = {"existing": "value"}
    _shared.update_with_lowercased(target, {"Key": "Value", "Other": "", "None": None})

    assert target["key"] == "Value"
    assert "Other" not in target


def test_apply_suffix_templates_formats_entries():
    target: dict[str, str] = {}
    mapping = {"Base": "أساس"}
    suffixes = ((" suffix", "%s الموسعة"),)

    _shared.apply_suffix_templates(target, mapping, suffixes)

    assert target == {"base suffix": "أساس الموسعة"}


def test_normalize_to_lower_returns_new_dict():
    original = {"Key": "Value"}
    normalized = _shared.normalize_to_lower(original)

    assert normalized == {"key": "Value"}
    assert normalized is not original


def test_log_mapping_stats_emits_debug(caplog):
    caplog.set_level(logging.DEBUG)

    _shared.log_mapping_stats("example", first={"a": 1, "b": 2})

    assert "example.first" in caplog.text
    assert "2 entries" in caplog.text
