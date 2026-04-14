"""
Module for processing category events and resolving labels.
This module provides classes and functions to normalize category names and
resolve their corresponding Arabic labels using internal processors.
"""

#
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Dict, Iterable, List

from .main_processers.main_resolve import CategoryResult, resolve_label

logger = logging.getLogger(__name__)

LABEL_PREFIX = "تصنيف:"


@dataclass
class ProcessingStats:
    """Statistics about batch processing performance.

    Attributes:
        total: Total number of categories processed.
        successful: Number of categories with resolved labels.
        failed: Number of categories without resolved labels.
        pattern_matches: Number of categories matched by pattern resolvers.
        cache_hits: Number of cache hits (for future cache implementation).
        avg_time_ms: Average processing time per category in milliseconds.
    """

    total: int = 0
    successful: int = 0
    failed: int = 0
    pattern_matches: int = 0
    cache_hits: int = 0
    avg_time_ms: float = 0.0

    def record_success(self, is_pattern_match: bool = False) -> None:
        """Record a successful resolution."""
        self.total += 1
        self.successful += 1
        if is_pattern_match:
            self.pattern_matches += 1

    def record_failure(self) -> None:
        """Record a failed resolution."""
        self.total += 1
        self.failed += 1

    def compute_avg_time(self, total_time_ms: float) -> None:
        """Compute average time per category."""
        if self.total > 0:
            self.avg_time_ms = total_time_ms / self.total


@dataclass
class ProcessedCategory:
    """Data structure representing each processed category.

    Attributes:
        original: The original input category string.
        normalized: The normalized category string (underscores replaced).
        raw_label: The raw Arabic label without prefix.
        final_label: The final label with Arabic prefix added.
        has_label: Whether a valid label was resolved.
    """

    original: str
    normalized: str
    raw_label: str
    final_label: str
    has_label: bool


@dataclass
class EventProcessingResult:
    """Structured results for a batch of processed categories.

    Attributes:
        processed: List of all processed category records.
        labels: Dictionary mapping normalized categories to final labels.
        no_labels: List of categories that could not be resolved.
        category_patterns: Count of categories matched by pattern resolvers.
        stats: Processing statistics.
    """

    processed: List[ProcessedCategory] = field(default_factory=list)
    labels: Dict[str, str] = field(default_factory=dict)
    no_labels: List[str] = field(default_factory=list)
    category_patterns: int = 0
    stats: ProcessingStats = field(default_factory=ProcessingStats)


class EventProcessor:
    """Fast, pure processing engine for categories."""

    def __init__(self) -> None:
        """Create a processor with a placeholder for future configuration."""
        self.config = None

    @staticmethod
    def _normalize_category(category: str) -> str:
        """Normalize the input category string quickly."""
        category = category.removeprefix("\ufeff")
        return category.replace("_", " ")

    @staticmethod
    def _prefix_label(raw_label: str) -> str:
        """Add prefix only when needed."""
        if not raw_label:
            return ""

        stripped = raw_label.strip()
        if not stripped or stripped == LABEL_PREFIX:
            return ""

        if stripped.startswith(LABEL_PREFIX):
            return stripped

        return f"{LABEL_PREFIX}{raw_label}"

    def process(self, categories: Iterable[str]) -> EventProcessingResult:
        """Process a batch of categories."""
        result = EventProcessingResult()

        for original in categories:
            if not original:
                continue

            normalized = self._normalize_category(original)

            raw_label: CategoryResult = resolve_label(normalized)

            final_label = self._prefix_label(raw_label.ar)
            has_label = bool(final_label)

            if has_label:
                result.labels[normalized] = final_label
                if raw_label.from_match:
                    result.category_patterns += 1
                result.stats.record_success(is_pattern_match=raw_label.from_match)
            else:
                result.no_labels.append(normalized)
                result.stats.record_failure()

            result.processed.append(
                ProcessedCategory(
                    original=original,
                    normalized=normalized,
                    raw_label=raw_label.ar,
                    final_label=final_label,
                    has_label=has_label,
                )
            )

        return result

    def process_single(self, category: str) -> ProcessedCategory:
        """Process a single category and return the detailed record."""
        processed = self.process([category]).processed
        if not processed:
            return ProcessedCategory(category, category, "", "", False)
        return processed[0]


def _get_processed_category(category_r: str) -> ProcessedCategory:
    """Helper to process a single category with a default processor."""
    processor = EventProcessor()
    return processor.process_single(category_r)


def resolve_arabic_category_label(category_r: str) -> str:
    """Return final AR label with prefix."""
    return _get_processed_category(category_r).final_label


def batch_resolve_labels(
    new_list: List[str],
) -> EventProcessingResult:
    """Run the event processor on the given list of categories."""
    processor = EventProcessor()
    result = processor.process(new_list)

    return result


__all__ = [
    "ProcessingStats",
    "ProcessedCategory",
    "EventProcessingResult",
    "EventProcessor",
    "resolve_arabic_category_label",
    "batch_resolve_labels",
]
