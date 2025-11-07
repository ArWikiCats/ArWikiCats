#!/usr/bin/python3
"""

"""

import sys
from .. import printe

disable_all_printing = "all_print_off" in sys.argv
force_all_printing = "printall" in sys.argv
main_output_preferences = {1: False}
print_put_preferences = {1: False}
test_logging_preferences = {1: False}
headline_only_preferences = {1: False}

if "printhead" in sys.argv:
    headline_only_preferences[1] = True


def output_test4(text: str) -> None:
    if disable_all_printing:
        return
    printe.log(text)


def output_main(text: str) -> str | None:
    if force_all_printing:
        printe.output(text)
        return
    if disable_all_printing or headline_only_preferences[1]:
        return ""
    if main_output_preferences[1]:
        printe.output(text)


def print_def_head(text: str) -> None:
    if force_all_printing:
        printe.output(text)
        return
    if disable_all_printing:
        return
    # if headline_only_preferences[1]:
    if main_output_preferences[1] or headline_only_preferences[1]:
        printe.output(text)


def print_put(text: str) -> str | None:
    if force_all_printing:
        printe.output(text)
        return
    if disable_all_printing:
        return
    if "print_put" in sys.argv:
        printe.output(text)
    else:
        if headline_only_preferences[1]:
            return ""
        if print_put_preferences[1]:
            printe.output(text)


def output_test(text: str) -> str | None:
    if disable_all_printing:
        return
    if headline_only_preferences[1]:
        return ""
    printe.log(text)


def do_print_options(
    noprint: str="",
    printfirst: str="",
    printhead: str="",
    all_print_off: str="",
    tst_prnt_all: bool=False,
) -> None:
    global headline_only_preferences, main_output_preferences, print_put_preferences, test_logging_preferences
    if "printhead" in sys.argv:
        headline_only_preferences[1] = True
        main_output_preferences[1] = False
        print_put_preferences[1] = False
        test_logging_preferences[1] = False
    else:
        if all_print_off:
            headline_only_preferences[1] = False
            main_output_preferences[1] = False
            print_put_preferences[1] = False
            test_logging_preferences[1] = False
        elif tst_prnt_all:
            headline_only_preferences[1] = False
            main_output_preferences[1] = True
            print_put_preferences[1] = True
            test_logging_preferences[1] = True
        else:
            if printfirst:
                headline_only_preferences[1] = False
                main_output_preferences[1] = False
                print_put_preferences[1] = False
                test_logging_preferences[1] = False
            elif "printhead" in sys.argv or printhead:
                headline_only_preferences[1] = True
                main_output_preferences[1] = False
                print_put_preferences[1] = False
                test_logging_preferences[1] = False

            elif noprint is True or noprint == "so":
                printe.output("<<lightred>>  noprint  \n\t\t>>  noprint  ")
                main_output_preferences[1] = True
                headline_only_preferences[1] = False
                print_put_preferences[1] = False
                test_logging_preferences[1] = False

            elif noprint is False:
                printe.output("<<lightblue>>  print  \n\t\t>>  print  ")
                main_output_preferences[1] = True
                headline_only_preferences[1] = True
                print_put_preferences[1] = True
                test_logging_preferences[1] = True

            if noprint == "so":
                main_output_preferences[1] = True
