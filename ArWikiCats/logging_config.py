"""
Logging configuration with colored output.
"""

import logging
import sys
from typing import Optional

import colorlog


def setup_logging(level: str = "INFO", log_file: Optional[str] = None) -> None:
    """
    Configure colored logging for console and optional file output.

    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional file path for log output

    Example:
        >>> setup_logging(level="DEBUG", log_file="app.log")
    """
    # Convert string level to logging constant
    numeric_level = getattr(logging, level.upper(), logging.INFO) if isinstance(level, str) else level

    # Create color formatter for console
    console_formatter = colorlog.ColoredFormatter(
        # fmt="%(log_color)s%(asctime)s - %(name)s - %(levelname)-8s%(reset)s %(message)s",
        fmt="%(name)s - %(log_color)s%(levelname)-8s%(reset)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        },
        secondary_log_colors={},
        style="%",
    )

    # Console handler with colors
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(numeric_level)

    # Root logger configuration
    root_logger = logging.getLogger()
    root_logger.setLevel(numeric_level)
    root_logger.addHandler(console_handler)

    # Optional file handler (no colors)
    if log_file:
        file_formatter = logging.Formatter(
            fmt="%(asctime)s - %(name)s - %(levelname)-8s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(numeric_level)
        root_logger.addHandler(file_handler)

    # Silence noisy third-party loggers
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("pymysql").setLevel(logging.WARNING)


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance for a module.

    Args:
        name: Module name (typically __name__)

    Returns:
        Logger instance

    Example:
        >>> logger = get_logger(__name__)
        >>> logger.info("Module initialized")
    """
    return logging.getLogger(name)
