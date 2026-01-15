from ..config import print_settings
from ..helps.log import LoggerWrap

logger = LoggerWrap(__name__, disable_log=print_settings.noprint or print_settings.noprint_formats)


__all__ = [
    "logger",
]
