"""
ArWikiCats: A package for processing and resolving Arabic Wikipedia category labels.
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
