"""
Specialized logger for translation formats.
This module provides a logger instance configured specifically for
formatting-related messages, allowing them to be suppressed independently.
"""

from ..config import print_settings
from ..helps.log import LoggerWrap

logger = LoggerWrap(__name__, disable_log=print_settings.noprint or print_settings.noprint_formats)


__all__ = [
    "logger",
]
