"""Helpers for printing the current process memory usage."""

import importlib.util
import os
import sys


def _resident_memory_bytes() -> int:
    """Return the resident set size for the current process in bytes."""
    if importlib.util.find_spec("psutil") is not None:
        import psutil  # type: ignore

        return psutil.Process(os.getpid()).memory_info().rss

    import resource

    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform == "darwin":
        return usage
    return usage * 1024


def print_memory() -> None:
    """Print the current process memory usage to stdout."""
    yellow, purple = "\033[93m%s\033[00m", "\033[95m%s\033[00m"

    usage_mb = _resident_memory_bytes() / (1024 * 1024)

    print(yellow % "Memory usage:", purple % f"{usage_mb:.0f} MB")
