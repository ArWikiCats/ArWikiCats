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
    NewList: List[str],
    noprint: str = "",
    printfirst: bool = False,
    printhead: bool = False,
    tst_prnt_all: Optional[bool] = None,
    return_no_labs: bool = False,
) -> Dict[str, str] | Dict[str, Dict[str, Any]] | tuple[Dict[str, str], List[str]]:
    """Process a list of categories and generate corresponding labels."""

    try:
        total = len(NewList)
    except TypeError:
        total = 0

    logger.info("<<lightred>> vvvvvvvvvvvv event start vvvvvvvvvvvv ")
    logger.info(f"<<lightblue>> event work with >  {total} cats. ")

    result = event_result(NewList)

    if total == 0:
        total = len(result.processed)

    labels = result.labels
    no_labels = result.no_labels

    _summarise_labels(labels, printfirst)

    if no_labels and not return_no_labs:
        printe.output(f"a<<lightred>>> {len(no_labels)} cat in no_labels ")
        for idx, cat in enumerate(no_labels, start=1):
            printe.output(f'  {idx}:  "{cat}" : "",')

    logger.info("<<lightred>>> ^^^^^^^^^ event end ^^^^^^^^^ ")

    if return_no_labs:
        return labels, no_labels

    return labels


__all__ = ["event", "new_func_lab"]
