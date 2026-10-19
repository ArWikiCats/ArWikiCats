"""
Data models for double-key translation patterns.
This package provides models specialized in handling categories that
require matching against two adjacent keys.
"""

from .model_data_double import FormatDataDouble
from .model_data_double_v2 import FormatDataDoubleV2
from .model_multi_data_double import MultiDataFormatterDataDouble

__all__ = [
    "FormatDataDouble",
    "FormatDataDoubleV2",
    "MultiDataFormatterDataDouble",
]
