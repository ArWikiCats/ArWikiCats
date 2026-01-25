# -*- coding: utf-8 -*-

from .companies import COMPANY_TYPE_TRANSLATIONS
from .deaths import medical_keys
from .languages import (
    COMPLEX_LANGUAGE_TRANSLATIONS,
    LANGUAGE_TOPIC_FORMATS,
    MEDIA_CATEGORY_TRANSLATIONS,
    PRIMARY_LANGUAGE_TRANSLATIONS,
    language_key_translations,
)
from .ministers import ministers_keys
from .tax_table import Taxons_table

__all__ = [
    "COMPANY_TYPE_TRANSLATIONS",
    "COMPLEX_LANGUAGE_TRANSLATIONS",
    "LANGUAGE_TOPIC_FORMATS",
    "PRIMARY_LANGUAGE_TRANSLATIONS",
    "MEDIA_CATEGORY_TRANSLATIONS",
    "language_key_translations",
    "ministers_keys",
    "Taxons_table",
    "medical_keys",
]
