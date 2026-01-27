"""Tests for build_sport_keys.py sport key translation utilities."""

import pytest

from ArWikiCats.translations.data_builders.build_sport_keys import (
    SportKeyRecord,
    SportKeyTables,
    _apply_aliases,
    _build_tables,
    _coerce_record,
    _copy_record,
    _generate_variants,
    _initialise_tables,
    _load_base_records,
)


class TestCoerceRecord:
    """Tests for _coerce_record function."""

    def test_coerce_full_record(self) -> None:
        raw = {"label": "كرة القدم", "jobs": "رياضة", "team": "للرياضة", "olympic": "أولمبية"}
        result = _coerce_record(raw)

        assert result["label"] == "كرة القدم"
        assert result["jobs"] == "رياضة"
        assert result["team"] == "للرياضة"
        assert result["olympic"] == "أولمبية"

    def test_coerce_partial_record(self) -> None:
        raw = {"label": "كرة السلة"}
        result = _coerce_record(raw)

        assert result["label"] == "كرة السلة"
        assert result["jobs"] == ""
        assert result["team"] == ""
        assert result["olympic"] == ""

    def test_coerce_empty_record(self) -> None:
        result = _coerce_record({})
        assert result == {"label": "", "jobs": "", "team": "", "olympic": ""}

    def test_coerce_with_numeric_values(self) -> None:
        raw = {"label": 123, "jobs": None}
        result = _coerce_record(raw)

        assert result["label"] == "123"
        assert result["jobs"] == "None"


class TestLoadBaseRecords:
    """Tests for _load_base_records function."""

    def test_load_valid_mapping(self) -> None:
        data = {
            "football": {"label": "كرة القدم", "jobs": "رياضة"},
            "basketball": {"label": "كرة السلة"},
        }
        result = _load_base_records(data)

        assert "football" in result
        assert result["football"]["label"] == "كرة القدم"
        assert result["basketball"]["label"] == "كرة السلة"

    def test_load_ignores_entries_with_ignore_key(self) -> None:
        data = {
            "football": {"label": "كرة القدم"},
            "ignored": {"label": "تجاهل", "ignore": True},
        }
        result = _load_base_records(data)

        assert "football" in result
        assert "ignored" not in result

    def test_load_non_mapping_returns_empty(self) -> None:
        result = _load_base_records("not a mapping")
        assert result == {}

    def test_load_skips_malformed_entries(self) -> None:
        data = {
            "valid": {"label": "صحيح"},
            "invalid": "not a mapping",
        }
        result = _load_base_records(data)

        assert "valid" in result
        assert result["valid"]["label"] == "صحيح"


class TestCopyRecord:
    """Tests for _copy_record function."""

    def test_copy_without_overrides(self) -> None:
        record: SportKeyRecord = {
            "label": "كرة القدم",
            "jobs": "رياضية",
            "team": "للرياضة",
            "olympic": "أولمبية",
        }
        result = _copy_record(record)

        assert result == record

    def test_copy_with_overrides(self) -> None:
        record: SportKeyRecord = {"label": "كرة القدم", "jobs": "", "team": "", "olympic": ""}
        result = _copy_record(record, label="كرة السلة", jobs="كرة سلة")

        assert result["label"] == "كرة السلة"
        assert result["jobs"] == "كرة سلة"
        assert result["team"] == ""
        assert result["olympic"] == ""

    def test_copy_skips_empty_overrides(self) -> None:
        record: SportKeyRecord = {"label": "كرة القدم", "jobs": "", "team": "", "olympic": ""}
        result = _copy_record(record, label="", jobs="new jobs")

        assert result["label"] == "كرة القدم"  # unchanged
        assert result["jobs"] == "new jobs"


class TestApplyAliases:
    """Tests for _apply_aliases function."""

    def test_apply_aliases_adds_entries(self) -> None:
        records: dict[str, SportKeyRecord] = {
            "football": {"label": "كرة القدم", "jobs": "", "team": "", "olympic": ""}
        }
        aliases = {"soccer": "football"}

        _apply_aliases(records, aliases)

        assert "soccer" in records
        assert records["soccer"]["label"] == "كرة القدم"

    def test_apply_aliases_missing_source(self, caplog) -> None:
        records: dict[str, SportKeyRecord] = {}
        aliases = {"alias": "missing"}

        _apply_aliases(records, aliases)

        assert "alias" not in records


class TestGenerateVariants:
    """Tests for _generate_variants function."""

    def test_generate_racing_variants(self) -> None:
        records = {
            "athletics": {"label": "ألعاب قوى", "jobs": "ألعاب قوى", "team": "للألعاب القوى", "olympic": ""}
        }
        result = _generate_variants(records)

        assert "athletics racing" in result
        assert result["athletics racing"]["label"] == "سباق ألعاب قوى"

    def test_skips_existing_racing_sports(self) -> None:
        records = {
            "racing": {"label": "سباق", "jobs": "", "team": "", "olympic": ""},
            "other": {"label": "أخرى", "jobs": "", "team": "", "olympic": ""},
        }
        result = _generate_variants(records)

        assert "racing racing" not in result
        assert "other racing" in result

    def test_generate_wheelchair_variants(self) -> None:
        records = {
            "basketball": {
                "label": "كرة السلة",
                "jobs": "كرة سلة",
                "team": "لكرة السلة",
                "olympic": "",
            }
        }
        result = _generate_variants(records)

        assert "wheelchair basketball" in result
        assert "على الكراسي المتحركة" in result["wheelchair basketball"]["label"]

    def test_wheelchair_only_for_allowed_sports(self) -> None:
        records = {
            "basketball": {"label": "كرة السلة", "jobs": "", "team": "", "olympic": ""},
            "swimming": {"label": "السباحة", "jobs": "", "team": "", "olympic": ""},
        }
        result = _generate_variants(records)

        assert "wheelchair basketball" in result
        assert "wheelchair swimming" not in result


class TestBuildTables:
    """Tests for _build_tables function."""

    def test_build_returns_sport_key_tables(self) -> None:
        records = {
            "football": {
                "label": "كرة القدم",
                "jobs": "كرة قدم",
                "team": "لكرة القدم",
                "olympic": "كرة قدم أولمبية",
            },
            "basketball": {"label": "كرة السلة", "jobs": "", "team": "", "olympic": ""},
        }
        result = _build_tables(records)

        assert isinstance(result, SportKeyTables)
        assert result.label["football"] == "كرة القدم"
        assert result.jobs["football"] == "كرة قدم"
        assert result.team["football"] == "لكرة القدم"
        assert result.olympic["football"] == "كرة قدم أولمبية"
        assert result.label["basketball"] == "كرة السلة"
        assert "basketball" not in result.jobs  # empty values skipped

    def test_build_lowercases_keys(self) -> None:
        records = {
            "Football": {"label": "كرة القدم", "jobs": "", "team": "", "olympic": ""}
        }
        result = _build_tables(records)

        assert "football" in result.label
        assert "Football" not in result.label


class TestInitialiseTables:
    """Tests for _initialise_tables function."""

    def test_initialise_loads_and_applies_aliases(self) -> None:
        data = {"football": {"label": "كرة القدم", "jobs": "", "team": "", "olympic": ""}}
        aliases = {"soccer": "football"}

        result = _initialise_tables(data, aliases)

        assert "football" in result
        assert "soccer" in result
        assert result["soccer"]["label"] == "كرة القدم"

    def test_initialise_with_non_mapping_data(self) -> None:
        result = _initialise_tables("invalid", {})
        assert result == {}
