#!/usr/bin/python3
"""
"""
import re

import sys
from pathlib import Path

# ---
from ..ma_lists_bots import ar_Nat_men
from ..ma_lists_bots import Jobs_new, Jobs_key_womens, Jobs_key_mens, Men_Womens_Jobs
from .. import printe

# ---
Dir = Path(__file__).parent
# ---
# Nat_Womens#Nat_mens
# def main():
# for nat in keysoo:
# printe.output("len %s %d" % (nat , len(keysoo[nat].keys()) ) )


def main2():
    # gogo = [ x for x in Jobs_key_mens]
    # gogo.sort()
    for k in Jobs_new:
        kaka = f'\t,"{k}": {Jobs_new[k]}\n'
        printe.output(kaka)
        with open(f"{str(Dir)}/aaaa.py", "a", encoding="utf-8") as logfile:
            logfile.write(kaka)


def main():
    # main.event(Facos , noprint =False )
    if sys.argv and sys.argv[1]:
        La = sys.argv[1].lower()
        La = re.sub(r"_", " ", La)
        print("=========================")
        print(f"lab: {La}")
        print(f"Jobs_new:{Jobs_new.get(La, 'no lab')}")
        print(f"Jobs_key_mens: {Jobs_key_mens.get(La, 'no lab')}")
        print(f"Jobs_key_womens: {Jobs_key_womens.get(La, 'no lab')}")


# ---
soso = """
    ,"{en}":[
        "men":      "{men}"
        ,"mens":      "{men}"
        ,"women":      "{women}"
        ,"womens":      "{women}"
        ,"en":      ""
        ,"ar":      ""
      ]"""
# ---
"""
d_list = {}
# ---
for ioi , b in Men_Womens_Jobs.items():
    io = b.get("mens",'').split(" ")[0]
    iw = b.get("womens",'').split(" ")[0]
    if io and io not in d_list:
        d_list[io] = []
    if io :
        if iw and iw not in d_list[io]:
            d_list[io].append(iw)
# ---
for ioi , b in d_list.items():
    df = " ".join([ "-like:%s" % x.replace(" ","_") for x in b if x.strip() ])
    printe.output("python3 core8/pwb.py asa/like addpro -ns:14 -project:أعلام -like:%s %s" % (ioi.replace(" ","_") , df ) )
# ---"""
translationsOccupations = {}

for x in translationsOccupations:
    x2 = re.sub(r"~ ", "", x)
    tt = translationsOccupations[x]
    ark = tt["ar"]["male"]
    # ---
    # if x.lower() in Men_Womens_Jobs.keys():
    # if ark in ar_Nat_men :
    # printe.output('Men_Womens_Jobs["%s"] = Men_Womens_Jobs["%s"]#%s' %  (x.lower() , ar_Nat_men[ark] , ark) )
    # ---
    if x2.lower() not in Men_Womens_Jobs.keys():
        if ark not in ar_Nat_men:
            printe.output(
                soso.format(
                    en=x,
                    men=tt["ar"]["male"],
                    women=tt["ar"]["female"],
                )
            )
# ---
if __name__ == "__main__":
    main()
# ---
