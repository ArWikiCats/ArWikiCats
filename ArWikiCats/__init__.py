"""
ArWikiCats: A package for processing and resolving Arabic Wikipedia category labels.
"""

# -*- coding: utf-8 -*-
import logging

from .config import all_params as config_all_params
from .config import print_settings
from .event_processing import (
    EventProcessor,
    batch_resolve_labels,
    resolve_arabic_category_label,
)
from .helps.len_print import dump_all_len
from .helps.log import getLogger
from .helps.memory import print_memory
from .main_processers.main_resolve import resolve_label_ar

if print_settings.noprint_formats:
    logging.getLogger("ArWikiCats.translations_formats").setLevel(logging.ERROR)

if print_settings.noprint:
    logging.getLogger("ArWikiCats").setLevel(logging.ERROR)

__version__ = "0.1.0b6"

__all__ = [
    "getLogger",
    "resolve_label_ar",
    "batch_resolve_labels",
    "resolve_arabic_category_label",
    "EventProcessor",
    "print_memory",
    "dump_all_len",
    "config_all_params",
]
