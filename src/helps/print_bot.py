#!/usr/bin/python3
"""

"""
from . import printe
from ..config import print_settings

disable_all_printing = print_settings.disable_all_printing
force_all_printing = print_settings.force_all_printing
headline_only_preferences = print_settings.headline_only_preferences
enable_print_put = print_settings.enable_print_put

main_output_preferences = {1: False}
print_put_preferences = {1: False}
te_logging_preferences = {1: False}


def output_test4(text: str) -> None:
    if disable_all_printing:
        return
    printe.info(text)


def output_main(text: str) -> str | None:
    if force_all_printing:
        printe.output(text)
        return
    if disable_all_printing or headline_only_preferences:
        return ""
    if main_output_preferences[1]:
        printe.output(text)


def print_def_head(text: str) -> None:
    if force_all_printing:
        printe.output(text)
        return
    if disable_all_printing:
        return
    # if headline_only_preferences:
    if main_output_preferences[1] or headline_only_preferences:
        printe.output(text)


def print_put(text: str) -> str | None:
    if force_all_printing:
        printe.output(text)
        return
    if disable_all_printing:
        return
    if enable_print_put:
        printe.output(text)
    else:
        if headline_only_preferences:
            return ""
        if print_put_preferences[1]:
            printe.output(text)


def output_test(text: str) -> str | None:
    if disable_all_printing:
        return
    if headline_only_preferences:
        return ""
    printe.info(text)


def do_print_options(
    noprint: str="",
    printfirst: str="",
    printhead: str="",
    tst_prnt_all: bool=False,
) -> None:
    global headline_only_preferences, main_output_preferences, print_put_preferences, te_logging_preferences
    if headline_only_preferences:
        main_output_preferences[1] = False
        print_put_preferences[1] = False
        te_logging_preferences[1] = False
        return

    if tst_prnt_all:
        headline_only_preferences = False
        main_output_preferences[1] = True
        print_put_preferences[1] = True
        te_logging_preferences[1] = True
        return

    if printfirst:
        headline_only_preferences = False
        main_output_preferences[1] = False
        print_put_preferences[1] = False
        te_logging_preferences[1] = False
        return

    if headline_only_preferences or printhead:
        headline_only_preferences = True
        main_output_preferences[1] = False
        print_put_preferences[1] = False
        te_logging_preferences[1] = False
        return

    if noprint is True or noprint == "so":
        printe.output("<<lightred>>  noprint  \n\t\t>>  noprint  ")
        main_output_preferences[1] = True
        headline_only_preferences = False
        print_put_preferences[1] = False
        te_logging_preferences[1] = False
        return

    if noprint is False:
        printe.output("<<lightblue>>  print  \n\t\t>>  print  ")
        main_output_preferences[1] = True
        headline_only_preferences = True
        print_put_preferences[1] = True
        te_logging_preferences[1] = True
        return

    if noprint == "so":
        main_output_preferences[1] = True
