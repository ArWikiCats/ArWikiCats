"""
from .memory import print_memory
"""

import psutil
import os


def print_memory():
    yellow, purple = "\033[93m%s\033[00m", "\033[95m%s\033[00m"

    usage = psutil.Process(os.getpid()).memory_info().rss
    usage = usage / 1024 // 1024

    print(yellow % "Memory usage:", purple % f"{usage} MB")
