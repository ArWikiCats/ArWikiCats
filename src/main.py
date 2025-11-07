#!/usr/bin/python3
"""
python3 core8/pwb.py make/m test Category:People executed by the International Military Tribunal in Nuremberg

python3 core8/pwb.py -m cProfile -s ncalls make2/main.py

"""

import importlib.util
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List

if importlib.util.find_spec("tqdm") is not None:
    from tqdm import tqdm  # type: ignore
else:

    def tqdm(iterable: Iterable[Any] | None=None, *args: Any, **kwargs: Any) -> Iterable[Any]:
        """Fallback replacement for :func:`tqdm` when the package is unavailable."""

        return iterable if iterable is not None else []

from . import printe
from .event_processing import EventProcessor, EventProcessorConfig, get_shared_event_cache, new_func_lab
from .helps.print_bot import do_print_options, print_put

Dir_ma = Path(__file__).parent.parent


def _iterable_with_progress(categories: Iterable[str]) -> Iterable[str]:
    if "all_print_off" in sys.argv:
        return tqdm(categories)
    return categories


def _append_printfirst_entry(category: str) -> None:
    err_file = Dir_ma / "textfiles" / "make2-err.txt"
    err_file.parent.mkdir(parents=True, exist_ok=True)
    with err_file.open("a", encoding="utf-8") as handle:
        handle.write(f"{category}\n")


def _summarise_labels(labels: dict, printfirst: bool) -> None:
    if not labels:
        printe.output("<<lightyellow>>> event: Labels == None len = 0")
        return

    for cat, cat_lab in labels.items():
        if printfirst:
            formatted = f'"{cat}"'.ljust(60)
            print(f"     {formatted} : \"{cat_lab}\",")


def _remove_labelled_from_no_labels(labels: dict, no_labels: List[str]) -> List[str]:
    if not no_labels:
        return no_labels
    labelled_set = set(labels.keys())
    return [cat for cat in no_labels if cat not in labelled_set]


def event(
    NewList: Iterable[str],
    noprint: str="",
    maketab: bool=False,
    Use_main_s: bool=False,
    printfirst: bool = False,
    Local: bool = False,
    printhead: bool = False,
    all_print_off: bool = False,
    tst_prnt_all: bool | None=None,
    return_no_labs: bool = False,
) -> Dict[str, str] | Dict[str, Dict[str, Any]] | tuple[Dict[str, str], List[str]]:
    """Process a list of categories and generate corresponding labels."""

    config = EventProcessorConfig(
        make_tab=maketab,
        event_cache=get_shared_event_cache(),
    )
    if Local:
        config.find_from_wikidata = False

    if Use_main_s:
        config.use_main_s = True

    do_print_options(
        noprint=noprint,
        printfirst=printfirst,
        printhead=printhead,
        all_print_off=all_print_off,
        tst_prnt_all=tst_prnt_all,
    )

    if Use_main_s:
        printe.output("<<lightblue>>  Use_main_s ")

    preview = ""
    try:
        if len(NewList) < 10:
            preview = ",".join(NewList)
    except TypeError:
        pass

    try:
        total = len(NewList)
    except TypeError:
        total = 0

    print_put("<<lightred>> vvvvvvvvvvvv event start vvvvvvvvvvvv ")
    print_put(f"<<lightblue>> event work with >  {total} cats. {preview} ")

    processor = EventProcessor(config)
    result = processor.process(_iterable_with_progress(NewList))

    if total == 0:
        total = len(result.processed)

    for index, item in enumerate(result.processed, start=1):
        toout = f'<<lightyellow>>> event ===  {index} / {total}  category_r:"{item.normalized}" === '

        if printfirst:
            printe.output(toout)
            _append_printfirst_entry(item.normalized)
        else:
            print_put(toout)

    labels = result.labels
    no_labels = _remove_labelled_from_no_labels(labels, result.no_labels)

    if config.make_tab:
        print_put("<<lightred>>> ^^^^^^^^^ event end ^^^^^^^^^ ")
        return result.tables

    _summarise_labels(labels, printfirst)

    if no_labels and not return_no_labs:
        printe.output(f"a<<lightred>>> {len(no_labels)} cat in NoLab_list ")
        for idx, cat in enumerate(no_labels, start=1):
            printe.output(f'  {idx}:  "{cat}" : "",')

    print_put("<<lightred>>> ^^^^^^^^^ event end ^^^^^^^^^ ")

    if return_no_labs:
        return labels, no_labels

    return labels


__all__ = ["event", "new_func_lab"]
