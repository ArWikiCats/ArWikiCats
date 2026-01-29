"""
Text fixing utilities for the ArWikiCats project.
This module provides functions for cleaning up and normalizing Arabic
category labels, such as removing duplicate spaces or prepositions.
"""

import re

from ...helps import getLogger

logger = getLogger(__name__)


def fix_minor(ar: str, ar_separator: str = "", en: str = "") -> str:
    """Clean up duplicate spaces and repeated prepositions in labels."""

    arlabel = " ".join(ar.strip().split())

    sps_list = [
        "من",
        "في",
        "و",
    ]

    ar_separator = ar_separator.strip()

    if ar_separator not in sps_list:
        sps_list.append(ar_separator)

    for ar_separator in sps_list:
        arlabel = re.sub(rf" {ar_separator}\s+{ar_separator} ", f" {ar_separator} ", arlabel)
        if ar_separator == "و":
            arlabel = re.sub(rf" {ar_separator} ", f" {ar_separator}", arlabel)

    arlabel = " ".join(arlabel.strip().split())

    logger.debug(f"fix_minor: {en=}| {ar=}  ==> {arlabel=}")

    return arlabel
