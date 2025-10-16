#!/usr/bin/python3
"""

"""

import sys
from .. import printe

all_the_print_off = "all_print_off" in sys.argv
all_the_print_on = "printall" in sys.argv
mainoutput = {1: False}
fafa2 = {1: False}
testprint = {1: False}
only_print_heads = {1: False}

if "printhead" in sys.argv:
    only_print_heads[1] = True


def output_test4(text):
    if all_the_print_off:
        return
    printe.log(text)


def output_main(text):
    if all_the_print_on:
        printe.output(text)
        return
    if all_the_print_off or only_print_heads[1]:
        return ""
    if mainoutput[1]:
        printe.output(text)


def print_def_head(text):
    if all_the_print_on:
        printe.output(text)
        return
    if all_the_print_off:
        return
    # if only_print_heads[1]:
    if mainoutput[1] or only_print_heads[1]:
        printe.output(text)


def print_put(text):
    if all_the_print_on:
        printe.output(text)
        return
    if all_the_print_off:
        return
    if "print_put" in sys.argv:
        printe.output(text)
    else:
        if only_print_heads[1]:
            return ""
        if fafa2[1]:
            printe.output(text)


def output_test(text):
    if all_the_print_off:
        return
    if only_print_heads[1]:
        return ""
    printe.log(text)


def do_print_options(noprint="", printfirst="", printhead="", all_print_off="", tst_prnt_all=False):
    global only_print_heads, mainoutput, fafa2, testprint
    if "printhead" in sys.argv:
        only_print_heads[1] = True
        mainoutput[1] = False
        fafa2[1] = False
        testprint[1] = False
    else:
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
