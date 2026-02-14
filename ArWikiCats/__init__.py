"""
ArWikiCats: A package for processing and resolving Arabic Wikipedia category labels.

This library provides automatic translation of English Wikipedia category names to Arabic,
handling complex patterns including temporal (years, centuries), geographical (countries,
cities), occupational, and sports-related categories.

Version
-------
__version__ = "0.2.0"

Quick Start
-----------
Resolve a single category::

    from ArWikiCats import resolve_label_ar

    arabic_label = resolve_label_ar("British footballers")
    # Returns: 'لاعبو كرة قدم بريطانيون'

Batch processing::

    from ArWikiCats import batch_resolve_labels

    categories = ["British footballers", "French politicians", "2020 deaths"]
    result = batch_resolve_labels(categories)
    print(result.labels)  # Dict mapping categories to Arabic labels
    print(result.no_labels)  # List of unresolved categories

Using the EventProcessor::

    from ArWikiCats import EventProcessor

    processor = EventProcessor()
    processed = processor.process_single("American actors")
    print(processed.final_label)  # With "تصنيف:" prefix

Main Components
---------------
- resolve_label_ar: Single category resolution
- batch_resolve_labels: Batch processing with statistics
- EventProcessor: Full-featured processing engine
"""

from .event_processing import (
    EventProcessor,
    batch_resolve_labels,
    resolve_arabic_category_label,
)
from .helps.len_print import dump_all_len
from .helps.memory import print_memory
from .logging_config import setup_logging
from .main_processers.main_resolve import resolve_label_ar

setup_logging()

__version__ = "0.2.0"

__all__ = [
    "resolve_label_ar",
    "batch_resolve_labels",
    "resolve_arabic_category_label",
    "EventProcessor",
    "print_memory",
    "dump_all_len",
]
