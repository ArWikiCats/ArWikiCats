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
class ProcessedCategory:
    """Data structure representing each processed category."""

    original: str
    normalized: str
    raw_label: str
    final_label: str
    has_label: bool


@dataclass
class EventProcessingResult:
    """Structured results for a batch."""

    processed: List[ProcessedCategory] = field(default_factory=list)
    labels: Dict[str, str] = field(default_factory=dict)
    no_labels: List[str] = field(default_factory=list)
    category_patterns: int = 0


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
            else:
                result.no_labels.append(normalized)

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
