#!/usr/bin/python3
"""

Usage:
from .helps.print_bot import mainoutput, fafa2, testprint, only_print_heads
from .helps.print_bot import do_print_options, print_def_head, output_main, print_put, output_test, output_test4
# do_print_options(noprint="", printfirst="", printhead="", all_print_off="", tst_prnt_all=False)
"""

# from .helps import printe
from . import printe
import sys

mainoutput = {1: False}
fafa2 = {1: False}
testprint = {1: False}
only_print_heads = {1: False}
print_test4 = {1: False}

if "printhead" in sys.argv:
    only_print_heads[1] = True


if "testprint" in sys.argv:
    print_test4[1] = True
    printe.output("<<lightgreen>> test_4.py print_test4[1] = True")
    printe.output("<<lightgreen>> test_4.py print_test4[1] = True")


def output_test4(string):
    if print_test4[1]:
        printe.output(string)


def output_main(string):
    if only_print_heads[1]:
        return ""
    if mainoutput[1]:
        printe.output(string)


def print_def_head(string):
    # if only_print_heads[1]:
    if mainoutput[1] or only_print_heads[1]:
        printe.output(string)


def print_put(string):
    if "print_put" in sys.argv:
        printe.output(string)
    else:
        if only_print_heads[1]:
            return ""
        if fafa2[1]:
            printe.output(string)


def output_test(string):
    if only_print_heads[1]:
        return ""
    if testprint[1]:
        printe.output(string)


def do_print_options(noprint="", printfirst="", printhead="", all_print_off="", tst_prnt_all=False):
    global only_print_heads, mainoutput, fafa2, testprint
    if all_print_off:
        only_print_heads[1] = False
        mainoutput[1] = False
        fafa2[1] = False
        testprint[1] = False
    elif tst_prnt_all:
        only_print_heads[1] = False
        mainoutput[1] = True
        fafa2[1] = True
        testprint[1] = True
    else:
        if printfirst:
            only_print_heads[1] = False
            mainoutput[1] = False
            fafa2[1] = False
            testprint[1] = False
        elif "printhead" in sys.argv or printhead:
            only_print_heads[1] = True
            mainoutput[1] = False
            fafa2[1] = False
            testprint[1] = False

        elif noprint is True or noprint == "so":
            printe.output("<<lightred>>  noprint  \n\t\t>>  noprint  ")
            mainoutput[1] = True
            only_print_heads[1] = False
            fafa2[1] = False
            testprint[1] = False

        elif noprint is False:
            printe.output("<<lightblue>>  print  \n\t\t>>  print  ")
            mainoutput[1] = True
            only_print_heads[1] = True
            fafa2[1] = True
            testprint[1] = True

        if noprint == "so":
            mainoutput[1] = True


for arg in sys.argv:
    if arg == "noprint":
        printe.output("<<lightred>>>>  noprint  \n\t\t>>  noprint  ")
        mainoutput[1] = True
        fafa2[1] = False
        testprint[1] = False

    if arg == "testprint" or arg == "-testprint":
        printe.output("<<lightred>>>>  testprint  ")
        testprint[1] = True
