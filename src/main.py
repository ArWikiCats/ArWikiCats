#!/usr/bin/python3
"""
python3 core8/pwb.py make/m test Category:People executed by the International Military Tribunal in Nuremberg

python3 core8/pwb.py -m cProfile -s ncalls make2/main.py

"""

from pathlib import Path
from typing import Optional, Any, Dict, List
from . import printe
from .helps.print_bot import do_print_options, print_put
from .event_processing import EventProcessor, new_func_lab

Dir_ma = Path(__file__).parent.parent


def _summarise_labels(labels: Dict[str, str], printfirst: bool) -> None:
    if not labels:
        printe.output("<<lightyellow>>> event: Labels == None len = 0")
        return

    for cat, cat_lab in labels.items():
        if printfirst:
            formatted = f'"{cat}"'.ljust(60)
            print(f"     {formatted} : \"{cat_lab}\",")


def _remove_labelled_from_no_labels(labels: Dict[str, str], no_labels: List[str]) -> List[str]:
    if not no_labels:
        return no_labels
    labelled_set = set(labels.keys())
    return [cat for cat in no_labels if cat not in labelled_set]


def event_result(
    NewList: List[str],
) -> Dict[str, str] | Dict[str, Dict[str, Any]] | tuple[Dict[str, str], List[str]]:

    processor = EventProcessor()
    result = processor.process(NewList)

    return result


def event(
    NewList: List[str],
    noprint: str="",
    printfirst: bool = False,
    Local: bool = False,
    printhead: bool = False,
    tst_prnt_all: Optional[bool]=None,
    return_no_labs: bool = False,
) -> Dict[str, str] | Dict[str, Dict[str, Any]] | tuple[Dict[str, str], List[str]]:
    """Process a list of categories and generate corresponding labels."""

    do_print_options(
        noprint=noprint,
        printfirst=printfirst,
        printhead=printhead,
        tst_prnt_all=tst_prnt_all,
    )

    try:
        total = len(NewList)
    except TypeError:
        total = 0

    print_put("<<lightred>> vvvvvvvvvvvv event start vvvvvvvvvvvv ")
    print_put(f"<<lightblue>> event work with >  {total} cats. ")

    result = event_result(NewList)

    if total == 0:
        total = len(result.processed)

    for index, item in enumerate(result.processed, start=1):
        toout = f'<<lightyellow>>> event ===  {index} / {total}  category_r:"{item.normalized}" === '

        if printfirst:
            printe.output(toout)
        else:
            print_put(toout)

    labels = result.labels
    no_labels = _remove_labelled_from_no_labels(labels, result.no_labels)

    _summarise_labels(labels, printfirst)

    if no_labels and not return_no_labs:
        printe.output(f"a<<lightred>>> {len(no_labels)} cat in NoLab_list ")
        for idx, cat in enumerate(no_labels, start=1):
            printe.output(f'  {idx}:  "{cat}" : "",')

    print_put("<<lightred>>> ^^^^^^^^^ event end ^^^^^^^^^ ")

    if return_no_labs:
        return labels, no_labels

    return labels


__all__ = [
    "event",
    "new_func_lab"
]
