"""
"""

# ---
from .log import logger

error = logger.error_red
output = logger.output
debug = logger.debug
warn = logger.warning
warning = logger.warning
info = logger.info


__all__ = [
    "output",
    "debug",
    "warning",
    "warn",
    "error",
    "info",
]
