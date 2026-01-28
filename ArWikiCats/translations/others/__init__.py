# -*- coding: utf-8 -*-

from .deaths import get_death_label, medical_keys
from .languages import (
    COMPLEX_LANGUAGE_TRANSLATIONS,
    LANGUAGE_TOPIC_FORMATS,
    MEDIA_CATEGORY_TRANSLATIONS,
    PRIMARY_LANGUAGE_TRANSLATIONS,
    language_key_translations,
)
from .ministers import ministers_keys
from .tax_table import TAXON_TABLE

__all__ = [
    "COMPLEX_LANGUAGE_TRANSLATIONS",
    "LANGUAGE_TOPIC_FORMATS",
    "PRIMARY_LANGUAGE_TRANSLATIONS",
    "MEDIA_CATEGORY_TRANSLATIONS",
    "language_key_translations",
    "ministers_keys",
    "TAXON_TABLE",
    "medical_keys",
    "get_death_label",
]
