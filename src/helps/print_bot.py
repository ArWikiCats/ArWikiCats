#!/usr/bin/python3
"""

"""

import sys
from .. import printe

PRINTING_DISABLED = "all_print_off" in sys.argv
PRINTING_ENABLED = "printall" in sys.argv
main_output_enabled = {1: False}
secondary_output_enabled = {1: False}
test_output_enabled = {1: False}
print_only_headers = {1: False}

if "printhead" in sys.argv:
    print_only_headers[1] = True


def output_test4(text):
    if PRINTING_DISABLED:
        return
    printe.log(text)


def output_main(text):
    if PRINTING_ENABLED:
        printe.output(text)
        return
    if PRINTING_DISABLED or print_only_headers[1]:
        return ""
    if main_output_enabled[1]:
        printe.output(text)


def print_def_head(text):
    if PRINTING_ENABLED:
        printe.output(text)
        return
    if PRINTING_DISABLED:
        return
    # if print_only_headers[1]:
    if main_output_enabled[1] or print_only_headers[1]:
        printe.output(text)


def print_put(text):
    if PRINTING_ENABLED:
        printe.output(text)
        return
    if PRINTING_DISABLED:
        return
    if "print_put" in sys.argv:
        printe.output(text)
    else:
        if print_only_headers[1]:
            return ""
        if secondary_output_enabled[1]:
            printe.output(text)


def output_test(text):
    if PRINTING_DISABLED:
        return
    if print_only_headers[1]:
        return ""
    printe.log(text)


def do_print_options(noprint="", printfirst="", printhead="", all_print_off="", tst_prnt_all=False):
    global print_only_headers, main_output_enabled, secondary_output_enabled, test_output_enabled
    if "printhead" in sys.argv:
        print_only_headers[1] = True
        main_output_enabled[1] = False
        secondary_output_enabled[1] = False
        test_output_enabled[1] = False
    else:
        if all_print_off:
            print_only_headers[1] = False
            main_output_enabled[1] = False
            secondary_output_enabled[1] = False
            test_output_enabled[1] = False
        elif tst_prnt_all:
            print_only_headers[1] = False
            main_output_enabled[1] = True
            secondary_output_enabled[1] = True
            test_output_enabled[1] = True
        else:
            if printfirst:
                print_only_headers[1] = False
                main_output_enabled[1] = False
                secondary_output_enabled[1] = False
                test_output_enabled[1] = False
            elif "printhead" in sys.argv or printhead:
                print_only_headers[1] = True
                main_output_enabled[1] = False
                secondary_output_enabled[1] = False
                test_output_enabled[1] = False

            elif noprint is True or noprint == "so":
                printe.output("<<lightred>>  noprint  \n\t\t>>  noprint  ")
                main_output_enabled[1] = True
                print_only_headers[1] = False
                secondary_output_enabled[1] = False
                test_output_enabled[1] = False

            elif noprint is False:
                printe.output("<<lightblue>>  print  \n\t\t>>  print  ")
                main_output_enabled[1] = True
                print_only_headers[1] = True
                secondary_output_enabled[1] = True
                test_output_enabled[1] = True

            if noprint == "so":
                main_output_enabled[1] = True
