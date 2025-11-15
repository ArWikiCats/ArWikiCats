#
from __future__ import annotations

import functools
from dataclasses import dataclass, field
from typing import Dict, Iterable, List

from .make2_bots.co_bots import filter_en
from .make2_bots.date_bots import labs_years
from .fix import fixtitle
from .make2_bots.format_bots import change_cat
from .make2_bots.ma_bots import event2bot, event_lab_bot, ye_ts_bot
from .make2_bots.matables_bots.bot import cash_2022
from . import app_settings

LABEL_PREFIX = "تصنيف"


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


@functools.lru_cache(maxsize=None)
def resolve_label(category: str) -> str:
    """Resolve the label using multi-step logic."""
    changed_cat = change_cat(category)
    is_cat_okay = filter_en.filter_cat(category)

    category_lab = ""
    cat_year, from_year = labs_years.lab_from_year(category)

    if from_year:
        category_lab = from_year

    start_ylab = ""

    if not category_lab:
        start_ylab = ye_ts_bot.translate_general_category(changed_cat)

    if not category_lab and is_cat_okay:
        category_lower = category.lower()
        category_lab = cash_2022.get(category_lower, "")

        if not category_lab and app_settings.start_yementest:
            category_lab = start_ylab

        if not category_lab:
            category_lab = event2bot.event2(changed_cat)

        if not category_lab:
            category_lab = event_lab_bot.event_Lab(changed_cat)

    if not category_lab and is_cat_okay:
        category_lab = start_ylab

    if category_lab:
        category_lab = fixtitle.fixlab(category_lab, en=category)

    if not from_year and cat_year:
        labs_years.lab_from_year_add(category, category_lab, cat_year)

    return category_lab


class EventProcessor:
    """Fast, pure processing engine for categories."""

    def __init__(self) -> None:
        self.config = None

    @staticmethod
    def _normalize_category(category: str) -> str:
        """Normalize the input category string quickly."""
        if category.startswith("\ufeff"):
            category = category[1:]
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

        return f"{LABEL_PREFIX}:{raw_label}"

    def process(self, categories: Iterable[str]) -> EventProcessingResult:
        """Process a batch of categories."""
        result = EventProcessingResult()

        for original in categories:
            if not original:
                continue

            normalized = self._normalize_category(original)

            raw_label = resolve_label(normalized)

            final_label = self._prefix_label(raw_label)
            has_label = bool(final_label)

            if has_label:
                result.labels[normalized] = final_label
            else:
                result.no_labels.append(normalized)

            result.processed.append(
                ProcessedCategory(
                    original=original,
                    normalized=normalized,
                    raw_label=raw_label,
                    final_label=final_label,
                    has_label=has_label,
                )
            )

        return result

    def process_single(self, category: str) -> ProcessedCategory:
        processed = self.process([category]).processed
        if not processed:
            return ProcessedCategory(category, category, "", "", False)
        return processed[0]


def _get_processed_category(category_r: str) -> ProcessedCategory:
    """Helper to process a single category with a default processor."""
    processor = EventProcessor()
    return processor.process_single(category_r)


def new_func_lab(category_r: str) -> str:
    """Return raw AR label."""
    return _get_processed_category(category_r).raw_label


def new_func_lab_final_label(category_r: str) -> str:
    """Return final AR label with prefix."""
    return _get_processed_category(category_r).final_label


def event_result(
    NewList: List[str],
) ->EventProcessingResult:

    processor = EventProcessor()
    result = processor.process(NewList)

    return result
