"""Unit tests for :mod:`ArWikiCats.translations.jobs.jobs_defs`."""

from __future__ import annotations

from typing import Any, Mapping

import pytest

from ArWikiCats.translations.jobs import jobs_defs


def test_join_terms_trims_and_skips_empty_strings() -> None:
    """``join_terms`` should normalise whitespace and ignore empty values."""

    result = jobs_defs.join_terms("  leading", "", "middle  ", " trailing ")
    assert result == "leading middle trailing"


def test_combine_gendered_labels_respects_require_base_womens() -> None:
    """When ``require_base_womens`` is set the feminine label may remain blank."""

    base = {"males": "راهب", "females": ""}
    suffix = {"males": "كاثوليكي", "females": "كاثوليكية"}
    combined = jobs_defs.combine_gendered_labels(base, suffix, require_base_womens=True)
    assert combined == {"males": "راهب كاثوليكي", "females": ""}


def test_merge_gendered_maps_copies_source_values() -> None:
    """Merged mappings should copy the source entries to avoid shared state."""

    target = {"key": {"males": "أ", "females": "ب"}}
    source_value = {"males": "ج", "females": "د"}
    source = {"key": source_value}

    jobs_defs.merge_gendered_maps(target, source)

    assert target["key"] == source_value
    assert target["key"] is not source_value


def test_load_gendered_label_map_filters_invalid_entries(monkeypatch: pytest.MonkeyPatch) -> None:
    """``load_gendered_label_map`` should ignore non-mapping or malformed items."""

    def fake_loader(filename: str) -> Mapping[str, Any]:
        return {
            "valid": {"males": "لاعب", "females": "لاعبة"},
            "missing": {"males": "", "females": ""},
            # Non-mapping and non-string entries should be skipped silently.
            "bad": ["not", "a", "mapping"],
            10: {"males": "number", "females": "number"},
        }

    monkeypatch.setattr(jobs_defs, "open_json_file", fake_loader)

    result = jobs_defs.load_gendered_label_map("ignored")

    assert result == {
        "valid": {"males": "لاعب", "females": "لاعبة"},
        "missing": {"males": "", "females": ""},
    }
