"""Tests for jobs_defs.py gendered label utilities."""

import pytest

from ArWikiCats.translations.data_builders.jobs_defs import (
    GenderedLabel,
    GenderedLabelMap,
    combine_gender_labels,
    combine_gendered_labels,
    copy_gendered_map,
    ensure_gendered_label,
    join_terms,
    merge_gendered_maps,
)


class TestJoinTerms:
    """Tests for join_terms function."""

    def test_join_single_term(self) -> None:
        assert join_terms("hello") == "hello"

    def test_join_multiple_terms(self) -> None:
        assert join_terms("hello", "world", "test") == "hello world test"

    def test_join_with_empty_strings(self) -> None:
        assert join_terms("hello", "", "world") == "hello world"

    def test_join_with_none(self) -> None:
        assert join_terms("hello", None, "world") == "hello world"

    def test_join_with_whitespace(self) -> None:
        assert join_terms("  hello  ", "\tworld\t") == "hello world"

    def test_join_all_empty(self) -> None:
        assert join_terms("", "", None) == ""

    def test_join_no_args(self) -> None:
        assert join_terms() == ""


class TestCombineGenderLabels:
    """Tests for combine_gender_labels function (legacy wrapper)."""

    def test_combine_both_labels(self) -> None:
        result = combine_gender_labels("label1", "label2")
        assert result == "label1 label2"

    def test_combine_first_empty(self) -> None:
        assert combine_gender_labels("", "label2") == ""

    def test_combine_second_empty(self) -> None:
        assert combine_gender_labels("label1", "") == ""

    def test_combine_both_empty(self) -> None:
        assert combine_gender_labels("", "") == ""


class TestCopyGenderedMap:
    """Tests for copy_gendered_map function."""

    def test_copy_creates_new_dict(self) -> None:
        source: GenderedLabelMap = {
            "key1": {"males": "male1", "females": "female1"},
            "key2": {"males": "male2", "females": "female2"},
        }
        copy = copy_gendered_map(source)

        assert copy == source
        assert copy is not source
        assert copy["key1"] is not source["key1"]

    def test_copy_empty_map(self) -> None:
        assert copy_gendered_map({}) == {}

    def test_copy_preserves_values(self) -> None:
        source: GenderedLabelMap = {"key": {"males": "ملاكمون", "females": "ملاكمات"}}
        copy = copy_gendered_map(source)

        assert copy["key"]["males"] == "ملاكمون"
        assert copy["key"]["females"] == "ملاكمات"


class TestMergeGenderedMaps:
    """Tests for merge_gendered_maps function."""

    def test_merge_into_target(self) -> None:
        target: GenderedLabelMap = {"key1": {"males": "male1", "females": "female1"}}
        source: GenderedLabelMap = {"key2": {"males": "male2", "females": "female2"}}

        merge_gendered_maps(target, source)

        assert "key1" in target
        assert "key2" in target
        assert target["key2"]["males"] == "male2"

    def test_merge_overwrites_existing(self) -> None:
        target: GenderedLabelMap = {"key": {"males": "old", "females": "old_f"}}
        source: GenderedLabelMap = {"key": {"males": "new", "females": "new_f"}}

        merge_gendered_maps(target, source)

        assert target["key"]["males"] == "new"
        assert target["key"]["females"] == "new_f"

    def test_merge_creates_copies(self) -> None:
        target: GenderedLabelMap = {}
        source: GenderedLabelMap = {"key": {"males": "value", "females": "value_f"}}

        merge_gendered_maps(target, source)

        # Modifying source should not affect target
        source["key"]["males"] = "modified"
        assert target["key"]["males"] == "value"


class TestEnsureGenderedLabel:
    """Tests for ensure_gendered_label function."""

    def test_ensure_adds_new_key(self) -> None:
        target: GenderedLabelMap = {}
        value: GenderedLabel = {"males": "male", "females": "female"}

        ensure_gendered_label(target, "new_key", value)

        assert "new_key" in target
        assert target["new_key"]["males"] == "male"

    def test_ensure_skips_existing_key(self) -> None:
        target: GenderedLabelMap = {"key": {"males": "original", "females": "original_f"}}
        value: GenderedLabel = {"males": "new", "females": "new_f"}

        ensure_gendered_label(target, "key", value)

        assert target["key"]["males"] == "original"
        assert target["key"]["females"] == "original_f"

    def test_ensure_creates_copy(self) -> None:
        target: GenderedLabelMap = {}
        value: GenderedLabel = {"males": "value", "females": "value_f"}

        ensure_gendered_label(target, "key", value)

        # Modifying original value should not affect target
        value["males"] = "modified"
        assert target["key"]["males"] == "value"


class TestCombineGenderedLabels:
    """Tests for combine_gendered_labels function."""

    def test_combine_both_genders(self) -> None:
        base: GenderedLabel = {"males": "لاعبو", "females": "لاعبات"}
        suffix: GenderedLabel = {"males": "كرة القدم", "females": "كرة القدم"}

        result = combine_gendered_labels(base, suffix)

        assert result["males"] == "لاعبو كرة القدم"
        assert result["females"] == "لاعبات كرة القدم"

    def test_combine_with_empty_base_gender(self) -> None:
        base: GenderedLabel = {"males": "لاعبو", "females": ""}
        suffix: GenderedLabel = {"males": "كرة القدم", "females": "كرة القدم"}

        result = combine_gendered_labels(base, suffix)

        assert result["males"] == "لاعبو كرة القدم"
        assert result["females"] == "كرة القدم"

    def test_combine_with_empty_suffix_gender(self) -> None:
        base: GenderedLabel = {"males": "لاعبو", "females": "لاعبات"}
        suffix: GenderedLabel = {"males": "", "females": ""}

        result = combine_gendered_labels(base, suffix)

        assert result["males"] == "لاعبو"
        assert result["females"] == "لاعبات"

    def test_combine_require_base_womens_true(self) -> None:
        base: GenderedLabel = {"males": "رجال دين", "females": ""}
        suffix: GenderedLabel = {"males": "أمريكيون", "females": "أمريكيات"}

        result = combine_gendered_labels(base, suffix, require_base_womens=True)

        assert result["males"] == "رجال دين أمريكيون"
        assert result["females"] == ""

    def test_combine_require_base_womens_false(self) -> None:
        base: GenderedLabel = {"males": "رجال دين", "females": ""}
        suffix: GenderedLabel = {"males": "أمريكيون", "females": "أمريكيات"}

        result = combine_gendered_labels(base, suffix, require_base_womens=False)

        assert result["males"] == "رجال دين أمريكيون"
        assert result["females"] == "أمريكيات"

    def test_combine_with_trimming(self) -> None:
        base: GenderedLabel = {"males": "لاعبو  ", "females": "  لاعبات"}
        suffix: GenderedLabel = {"males": "  كرة القدم", "females": "كرة القدم  "}

        result = combine_gendered_labels(base, suffix)

        assert result["males"] == "لاعبو كرة القدم"
        assert result["females"] == "لاعبات كرة القدم"

    def test_combine_all_empty(self) -> None:
        base: GenderedLabel = {"males": "", "females": ""}
        suffix: GenderedLabel = {"males": "", "females": ""}

        result = combine_gendered_labels(base, suffix)

        assert result["males"] == ""
        assert result["females"] == ""
