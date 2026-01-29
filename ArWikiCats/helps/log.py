"""
Logging utility for the ArWikiCats project.
This module provides a LoggerWrap class that simplifies logging with
colorized output and text diffing capabilities.
"""

import difflib
import logging
from typing import Union

from ..helps.printe_helper import make_str


class LoggerWrap:
    """Project-scoped logger with colorized helpers."""

    def __init__(self, name: str, disable_log: bool = False, level: int = logging.ERROR) -> None:
        """Initialize the wrapped logger and optionally disable output."""
        self._logger = logging.getLogger(name)

        # Prevent leaking to root logger
        self._logger.propagate = False

        if disable_log:
            self._logger.disabled = True
            return

        if not self._logger.handlers:
            self._logger.setLevel(level)

            handler = logging.StreamHandler()
            formatter = logging.Formatter("%(name)s - %(lineno)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)

            self._logger.addHandler(handler)

    def set_level(self, level: Union[int, str]) -> None:
        """Set the logging level for the underlying logger."""
        self._logger.setLevel(level)

    def setLevel(self, level: Union[int, str]) -> None:
        """Set the logging level for the underlying logger."""
        return self.set_level(level)

    def disable_logger(self, is_disabled: bool) -> None:
        """Enable or disable the underlying logger dynamically."""
        self._logger.disabled = is_disabled

    def logger(self) -> logging.Logger:
        """Expose the raw ``logging.Logger`` instance."""
        return self._logger

    def debug(self, msg: str, *args, **kwargs) -> None:
        """Log a debug message after formatting color codes."""
        self._logger.debug(make_str(msg), *args, **kwargs)

    def info(self, msg: str, *args, **kwargs) -> None:
        """Log an info message after formatting color codes."""
        self._logger.info(make_str(msg), *args, **kwargs)

    def info_if_or_debug(self, msg: str, value: str) -> None:
        """Log an info message if value is truthy, otherwise log a debug message."""
        if value:
            self._logger.info(make_str(msg))
        else:
            self._logger.debug(make_str(msg))

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

    def showDiff(self, oldtext: str, newtext: str) -> None:
        """Show the difference between two text strings using the logger."""

        diff = difflib.unified_diff(
            oldtext.splitlines(),
            newtext.splitlines(),
            lineterm="",
            fromfile="Old Text",
            tofile="New Text",
        )
        for line in diff:
            if line.startswith("+") and not line.startswith("+++"):
                self._logger.warning(make_str(f"<<lightgreen>>{line}<<default>>"))
            elif line.startswith("-") and not line.startswith("---"):
                self._logger.warning(make_str(f"<<lightred>>{line}<<default>>"))
            else:
                self._logger.warning(make_str(line))


def getLogger(name: str, disable_log: bool = False, level: int = logging.DEBUG) -> LoggerWrap:
    """Get a LoggerWrap instance for the specified name."""
    return LoggerWrap(name, disable_log=disable_log, level=level)


__all__ = [
    "getLogger",
]
