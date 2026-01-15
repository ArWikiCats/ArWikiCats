

from ..config import print_settings
from ..helps.log import LoggerWrap

logger = LoggerWrap(__name__, disable_log=print_settings.noprint)


__all__ = [
    "logger",
]
