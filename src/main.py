#!/usr/bin/python3
"""
python3 core8/pwb.py make/m test Category:People executed by the International Military Tribunal in Nuremberg

python3 core8/pwb.py -m cProfile -s ncalls make2/main.py

"""

from typing import Any, Dict, List, Optional

from .event_processing import event_result, new_func_lab
from .helps import printe
from .helps.log import logger


def _summarise_labels(labels: Dict[str, str], printfirst: bool) -> None:
    """Print the collected labels for debugging or inspection."""
    if not labels:
        printe.output("<<lightyellow>>> event: Labels == None len = 0")
        return

    for cat, cat_lab in labels.items():
        if printfirst:
            formatted = f'"{cat}"'.ljust(60)
            print(f'     {formatted} : "{cat_lab}",')


def event(
    new_list: List[str],
    printfirst: bool = False,
    return_no_labs: bool = False,
    **kwargs: Any,
) -> Dict[str, str] | Dict[str, Dict[str, Any]] | tuple[Dict[str, str], List[str]]:
    """Process a list of categories and generate corresponding labels."""

    try:
        total = len(new_list)
    except TypeError:
        total = 0

    logger.info("<<lightred>> vvvvvvvvvvvv event start vvvvvvvvvvvv ")
    logger.info(f"<<lightblue>> event work with >  {total} cats. ")

    result = event_result(new_list)

    if total == 0:
        total = len(result.processed)

    category_patterns = result.category_patterns
    labels = result.labels
    no_labels = result.no_labels

    _summarise_labels(labels, printfirst)

    if no_labels and not return_no_labs:
        printe.output(f"a<<lightred>>> {len(no_labels)} cat in no_labels ")
        for idx, cat in enumerate(no_labels, start=1):
            printe.output(f'  {idx}:  "{cat}" : "",')

    logger.info(f"<<green>>> category_patterns: {category_patterns}")
    logger.info("<<lightred>>> ^^^^^^^^^ event end ^^^^^^^^^ ")

    if return_no_labs:
        return labels, no_labels

    return labels


__all__ = ["event", "new_func_lab"]
