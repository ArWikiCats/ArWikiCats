from __future__ import annotations

import re
import sys
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List, Optional

from .co_bots import filter_en
from .date_bots import labs_years
from .fix import fixtitle
from .format_bots import change_cat
from .helps.print_bot import output_test
from .ma_bots import event2bot, event_lab_bot, ye_ts_bot
from .matables_bots.bot import cash_2022, set_table_sink

LABEL_PREFIX = "تصنيف"
_SHARED_EVENT_CACHE: Dict[str, str] = {}


def get_shared_event_cache() -> Dict[str, str]:
    """Expose the cache used to memoise event processing results."""

    return _SHARED_EVENT_CACHE


@dataclass
class EventProcessorConfig:
    """Configuration bundle for :class:`EventProcessor`."""

    start_yementest: bool = "yementest" in sys.argv
    use_main_s: bool = "usemains" in sys.argv or "use_main_s" in sys.argv
    find_from_wikidata: bool = "nowikidata" not in sys.argv
    make_tab: bool = False
    event_cache: Optional[Dict[str, str]] = None

    def resolved_event_cache(self) -> Dict[str, str]:
        """Return the cache backing this configuration."""

        if self.event_cache is None:
            return _SHARED_EVENT_CACHE
        return self.event_cache


@dataclass
class ProcessedCategory:
    """Details captured for every processed category."""

    original: str
    normalized: str
    raw_label: str
    final_label: str
    has_label: bool


@dataclass
class EventProcessingResult:
    """Structured result returned after processing a batch of categories."""

    processed: List[ProcessedCategory] = field(default_factory=list)
    labels: Dict[str, str] = field(default_factory=dict)
    no_labels: List[str] = field(default_factory=list)
    tables: Dict[str, Dict[str, Any]] = field(default_factory=dict)


class _TableCollector:
    """Capture data emitted through ``Add_to_main2_tab``."""

    def __init__(self, title: str):
        self.title = title
        self.ar = ""
        self.lab: Dict[str, str] = {}
        self.nolab: Dict[str, str] = {}

    def add_label(self, en: str, ar: str) -> None:
        if not en or not ar:
            return
        self.lab[en] = ar

    def set_result(self, ar: str) -> None:
        self.ar = ar

    def snapshot(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "ar": self.ar,
            "lab": dict(self.lab),
            "nolab": dict(self.nolab),
        }


@contextmanager
def _table_sink_context(collector: Optional[_TableCollector]):
    if not collector:
        yield
        return
    set_table_sink(collector.add_label)
    try:
        yield
    finally:
        set_table_sink(None)


class EventProcessor:
    """Pure processing core for category → label resolution."""

    def __init__(self, config: Optional[EventProcessorConfig] = None):
        self.config = config or EventProcessorConfig()
        self._event_done = self.config.resolved_event_cache()

    def process(self, categories: Iterable[str]) -> EventProcessingResult:
        result = EventProcessingResult()

        for original in categories:
            if not original:
                continue

            normalized = self._normalize_category(original)
            collector: Optional[_TableCollector] = None
            if self.config.make_tab:
                collector = _TableCollector(normalized)

            with _table_sink_context(collector):
                raw_label = self._resolve_label(normalized)

            final_label = self._prefix_label(raw_label)
            has_label = bool(final_label)

            if has_label:
                result.labels[normalized] = final_label
            else:
                result.no_labels.append(normalized)

            if collector:
                collector.set_result(final_label)
                result.tables[normalized] = collector.snapshot()

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

    @staticmethod
    def _normalize_category(category: str) -> str:
        category = re.sub(r"^\ufeff", "", category)
        return re.sub(r"_", " ", category)

    def _resolve_label(self, category: str) -> str:
        if category in self._event_done:
            cached = self._event_done[category]
            output_test(f'>>>> category_r: "{category}" in event_done, lab:"{cached}"')
            return cached

        category_lab = ""
        cat_year, from_year = labs_years.lab_from_year(category)
        if from_year:
            category_lab = from_year

        if not category_lab and filter_en.filter_cat(category):
            changed_cat = change_cat(category)

            category_lower = category.lower()
            if not category_lab and category_lower in cash_2022:
                category_lab = cash_2022[category_lower]

            if not category_lab and self.config.start_yementest:
                category_lab = ye_ts_bot.translate_general_category(changed_cat)

            if not category_lab:
                category_lab = event2bot.event2(changed_cat)

            if not category_lab and self.config.find_from_wikidata:
                category_lab = event_lab_bot.event_Lab(changed_cat)

        if category_lab:
            category_lab = fixtitle.fixlab(category_lab, en=category)

        if not from_year and cat_year:
            labs_years.lab_from_year_add(category, category_lab, cat_year)

        self._event_done[category] = category_lab
        return category_lab

    @staticmethod
    def _prefix_label(raw_label: str) -> str:
        if not raw_label:
            return ""

        stripped = raw_label.strip()
        if not stripped or stripped == LABEL_PREFIX:
            return ""

        if stripped.startswith(LABEL_PREFIX):
            return stripped
        return f"{LABEL_PREFIX}:{raw_label}"


def new_func_lab(category_r: str) -> str:
    processor = EventProcessor(EventProcessorConfig(make_tab=False))
    return processor.process_single(category_r).raw_label
