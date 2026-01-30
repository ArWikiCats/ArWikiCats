"""
Unit tests for the event_processing module.
"""

import pytest

from ArWikiCats.event_processing import (
    LABEL_PREFIX,
    EventProcessingResult,
    EventProcessor,
    ProcessedCategory,
    _get_processed_category,
    batch_resolve_labels,
    resolve_arabic_category_label,
)


class TestProcessedCategory:
    """Tests for ProcessedCategory dataclass."""

    def test_creates_with_all_fields(self) -> None:
        """Should create ProcessedCategory with all required fields."""
        category = ProcessedCategory(
            original="Test_Category",
            normalized="Test Category",
            raw_label="تصنيف:اختبار",
            final_label="تصنيف:اختبار",
            has_label=True,
        )
        assert category.original == "Test_Category"
        assert category.normalized == "Test Category"
        assert category.raw_label == "تصنيف:اختبار"
        assert category.final_label == "تصنيف:اختبار"
        assert category.has_label is True

    def test_has_label_false_for_empty_labels(self) -> None:
        """Should handle has_label=False correctly."""
        category = ProcessedCategory(
            original="Unknown", normalized="unknown", raw_label="", final_label="", has_label=False
        )
        assert category.has_label is False
        assert category.final_label == ""


class TestEventProcessingResult:
    """Tests for EventProcessingResult dataclass."""

    def test_creates_with_defaults(self) -> None:
        """Should create with default empty collections."""
        result = EventProcessingResult()
        assert result.processed == []
        assert result.labels == {}
        assert result.no_labels == []
        assert result.category_patterns == 0

    def test_accumulates_data(self) -> None:
        """Should allow accumulation of processed data."""
        result = EventProcessingResult()
        result.processed.append(
            ProcessedCategory(
                original="Test", normalized="test", raw_label="اختبار", final_label="تصنيف:اختبار", has_label=True
            )
        )
        result.labels["test"] = "تصنيف:اختبار"
        result.category_patterns = 1

        assert len(result.processed) == 1
        assert "test" in result.labels
        assert result.category_patterns == 1


class TestEventProcessorNormalizeCategory:
    """Tests for EventProcessor._normalize_category static method."""

    def test_replaces_underscores_with_spaces(self) -> None:
        """Should replace underscores with spaces."""
        result = EventProcessor._normalize_category("Test_Category_Name")
        assert result == "Test Category Name"

    def test_removes_bom_character(self) -> None:
        """Should remove BOM (byte order mark) from beginning."""
        result = EventProcessor._normalize_category("\ufeffTest Category")
        assert result == "Test Category"
        assert not result.startswith("\ufeff")

    def test_handles_empty_string(self) -> None:
        """Should handle empty string."""
        result = EventProcessor._normalize_category("")
        assert result == ""

    def test_handles_normal_string(self) -> None:
        """Should handle strings without special characters."""
        result = EventProcessor._normalize_category("Normal Category")
        assert result == "Normal Category"

    def test_handles_multiple_underscores(self) -> None:
        """Should replace all underscores."""
        result = EventProcessor._normalize_category("A_B_C_D_E")
        assert result == "A B C D E"


class TestEventProcessorPrefixLabel:
    """Tests for EventProcessor._prefix_label static method."""

    def test_adds_prefix_to_non_empty_label(self) -> None:
        """Should add prefix to non-empty label without prefix."""
        result = EventProcessor._prefix_label("اختبار")
        assert result == "تصنيف:اختبار"

    def test_returns_empty_for_empty_string(self) -> None:
        """Should return empty string for empty input."""
        result = EventProcessor._prefix_label("")
        assert result == ""

    def test_returns_empty_for_whitespace(self) -> None:
        """Should return empty string for whitespace-only input."""
        result = EventProcessor._prefix_label("   ")
        assert result == ""

    def test_does_not_double_prefix(self) -> None:
        """Should not add prefix if already present."""
        result = EventProcessor._prefix_label("تصنيف:اختبار")
        assert result == "تصنيف:اختبار"
        assert result.count("تصنيف:") == 1

    def test_returns_empty_for_prefix_only(self) -> None:
        """Should return empty string when input is just the prefix."""
        result = EventProcessor._prefix_label("تصنيف:")
        assert result == ""

    def test_handles_prefix_with_whitespace(self) -> None:
        """Should handle prefix with surrounding whitespace."""
        result = EventProcessor._prefix_label("  تصنيف:اختبار  ")
        assert result == "تصنيف:اختبار"


class TestEventProcessorProcessSingle:
    """Tests for EventProcessor.process_single method."""

    def test_processes_single_valid_category(self) -> None:
        """Should process a single category and return ProcessedCategory."""
        processor = EventProcessor()
        result = processor.process_single("Test_Category")
        assert isinstance(result, ProcessedCategory)
        assert result.original == "Test_Category"
        assert result.normalized == "Test Category"

    def test_returns_default_for_empty_string(self) -> None:
        """Should return default ProcessedCategory for empty string."""
        processor = EventProcessor()
        result = processor.process_single("")
        assert isinstance(result, ProcessedCategory)
        assert result.has_label is False

    def test_normalizes_input(self) -> None:
        """Should normalize the input category."""
        processor = EventProcessor()
        result = processor.process_single("Test_With_Underscores")
        assert result.normalized == "Test With Underscores"


class TestEventProcessorProcess:
    """Tests for EventProcessor.process method."""

    def test_processes_empty_list(self) -> None:
        """Should handle empty list of categories."""
        processor = EventProcessor()
        result = processor.process([])
        assert isinstance(result, EventProcessingResult)
        assert len(result.processed) == 0
        assert len(result.labels) == 0
        assert len(result.no_labels) == 0

    def test_processes_multiple_categories(self) -> None:
        """Should process multiple categories."""
        processor = EventProcessor()
        categories = ["Category_1", "Category_2", "Category_3"]
        result = processor.process(categories)
        assert isinstance(result, EventProcessingResult)
        assert len(result.processed) == 3

    def test_skips_empty_strings(self) -> None:
        """Should skip empty string entries."""
        processor = EventProcessor()
        categories = ["Valid", "", "Another_Valid", ""]
        result = processor.process(categories)
        assert len(result.processed) == 2

    def test_collects_labels_and_no_labels(self) -> None:
        """Should collect categories into labels or no_labels."""
        processor = EventProcessor()
        categories = ["Test_Category"]
        result = processor.process(categories)
        # Either in labels or no_labels
        total_collected = len(result.labels) + len(result.no_labels)
        assert total_collected == 1

    def test_tracks_pattern_matches(self) -> None:
        """Should track categories resolved from patterns."""
        processor = EventProcessor()
        categories = ["Test"]
        result = processor.process(categories)
        assert isinstance(result.category_patterns, int)
        assert result.category_patterns >= 0

    def test_preserves_original_category(self) -> None:
        """Should preserve original category string in processed results."""
        processor = EventProcessor()
        original = "Test_Category_Name"
        result = processor.process([original])
        assert result.processed[0].original == original


class TestEventProcessorInit:
    """Tests for EventProcessor initialization."""

    def test_initializes_with_none_config(self) -> None:
        """Should initialize with config set to None."""
        processor = EventProcessor()
        assert processor.config is None

    def test_is_reusable(self) -> None:
        """Should be reusable for multiple process calls."""
        processor = EventProcessor()
        result1 = processor.process(["Category1"])
        result2 = processor.process(["Category2"])
        assert len(result1.processed) == 1
        assert len(result2.processed) == 1


class TestModuleLevelFunctions:
    """Tests for module-level convenience functions."""

    def test_get_processed_category(self) -> None:
        """Should process a single category using default processor."""
        result = _get_processed_category("Test_Category")
        assert isinstance(result, ProcessedCategory)
        assert result.normalized == "Test Category"

    def test_resolve_arabic_category_label(self) -> None:
        """Should return final label with prefix."""
        result = resolve_arabic_category_label("Test_Category")
        assert isinstance(result, str)
        # Should either be empty or start with prefix
        if result:
            assert result.startswith(LABEL_PREFIX) or result == ""

    def test_batch_resolve_labels(self) -> None:
        """Should process a list of categories."""
        categories = ["Category1", "Category2"]
        result = batch_resolve_labels(categories)
        assert isinstance(result, EventProcessingResult)
        assert len(result.processed) == 2

    def test_batch_resolve_labels_empty_list(self) -> None:
        """Should handle empty list."""
        result = batch_resolve_labels([])
        assert isinstance(result, EventProcessingResult)
        assert len(result.processed) == 0


class TestEventProcessingEdgeCases:
    """Edge case tests for event processing."""

    def test_handles_special_characters(self) -> None:
        """Should handle categories with special characters."""
        processor = EventProcessor()
        result = processor.process_single("Category:Test-Name_123")
        assert isinstance(result, ProcessedCategory)

    def test_handles_unicode_characters(self) -> None:
        """Should handle Unicode characters in category names."""
        processor = EventProcessor()
        result = processor.process_single("تصنيف_عربي")
        assert isinstance(result, ProcessedCategory)
        assert "عربي" in result.normalized

    def test_handles_very_long_category_names(self) -> None:
        """Should handle very long category names."""
        processor = EventProcessor()
        long_name = "A" * 500
        result = processor.process_single(long_name)
        assert isinstance(result, ProcessedCategory)

    def test_batch_with_mixed_valid_invalid(self) -> None:
        """Should handle batch with mixed valid and invalid entries."""
        categories = ["Valid", "", "   ", "Another"]
        result = batch_resolve_labels(categories)
        # Should skip empty strings, but whitespace is normalized not skipped
        assert len(result.processed) == 3  # Valid, "   ", and Another are processed


class TestLabelPrefixConstant:
    """Tests for LABEL_PREFIX constant."""

    def test_label_prefix_is_arabic(self) -> None:
        """LABEL_PREFIX should be the Arabic category prefix."""
        assert LABEL_PREFIX == "تصنيف:"

    def test_label_prefix_used_in_output(self) -> None:
        """Labels should use the LABEL_PREFIX constant."""
        result = EventProcessor._prefix_label("test")
        assert result.startswith(LABEL_PREFIX)


class TestEventProcessorNormalizationConsistency:
    """Tests for normalization consistency across methods."""

    def test_same_normalization_in_process_and_process_single(self) -> None:
        """Normalization should be consistent between process and process_single."""
        processor = EventProcessor()
        category = "Test_Category_Name"

        single_result = processor.process_single(category)
        batch_result = processor.process([category])

        assert single_result.normalized == batch_result.processed[0].normalized

    def test_normalization_idempotent(self) -> None:
        """Normalizing twice should produce the same result."""
        normalized_once = EventProcessor._normalize_category("Test_Category")
        normalized_twice = EventProcessor._normalize_category(normalized_once)
        assert normalized_once == normalized_twice
