import logging
from typing import Optional, Union

from ..config import print_settings
from ..helps.printe_helper import make_str


class LoggerWrap:
    """Light wrapper around ``logging.Logger`` with colorized helpers."""

    def __init__(self, name: str, disable_log=False) -> None:
        """Initialize the wrapped logger and optionally disable output."""
        self._logger = logging.getLogger(name)

        if disable_log:
            self._logger.disabled = True

    def disable_logger(self, Bool: bool) -> None:
        """Enable or disable the underlying logger dynamically."""
        self._logger.disabled = Bool

    def logger(self) -> logging.Logger:
        """Expose the raw ``logging.Logger`` instance."""
        return self._logger

    def debug(self, msg: str, *args, **kwargs) -> None:
        """Log a debug message after formatting color codes."""
        self._logger.debug(make_str(msg), *args, **kwargs)

    def info(self, msg: str, *args, **kwargs) -> None:
        """Log an info message after formatting color codes."""
        self._logger.info(make_str(msg), *args, **kwargs)

    def output(self, msg: str, *args, **kwargs) -> None:
        """Alias for info logging while preserving formatting."""
        self._logger.info(make_str(msg), *args, **kwargs)

    def warning(self, msg: str, *args, **kwargs) -> None:
        """Log a warning message with formatted content."""
        self._logger.warning(make_str(msg), *args, **kwargs)

    def error(self, msg: str, *args, **kwargs) -> None:
        """Log an error message with formatted content."""
        self._logger.error(make_str(msg), *args, **kwargs)

    def error_red(self, msg: str) -> None:
        """Log an error message while forcing red coloring."""
        text = f"<<red>> {str(msg)} <<default>>"
        self._logger.error(make_str(text))

    def critical(self, msg: str, *args, **kwargs) -> None:
        """Log a critical message with formatted content."""
        self._logger.critical(make_str(msg), *args, **kwargs)

    def exception(self, msg: str, *args, **kwargs) -> None:
        """Log an exception with traceback using formatted content."""
        self._logger.exception(make_str(msg), *args, **kwargs)

    def log(self, level: int, msg: str, *args, **kwargs) -> None:
        """Log at an arbitrary level with formatted content."""
        self._logger.log(level, make_str(msg), *args, **kwargs)


logger = LoggerWrap(__name__, print_settings.noprint)


def config_logger(level: Optional[Union[int, str]] = None) -> None:
    """Configure the root logger with sensible defaults for the project."""
    _levels = [
        "CRITICAL",
        "ERROR",
        "WARNING",
        "INFO",
        "DEBUG",
        "NOTSET",
    ]

    if not level:
        level = logging.DEBUG

    logging.basicConfig(
        level=level,
        # format='%(asctime)s - %(levelname)s - %(message)s',
        format="%(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


__all__ = [
    "logger",
    "LoggerWrap",
    "config_logger",
]
