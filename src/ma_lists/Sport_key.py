#!/usr/bin/python3
"""

Usage:
from .Sport_key import Sports_Keys_For_Label, Sports_Keys_For_Team, Sports_Keys_For_Jobs, Sports_Keys_For_olympic, fanco_line
"""

# ---
Sports_Keys_New2 = {}
# ---
# ,"professional league":{"label":"دوري المحترفين", "team":"لدوري المحترفين", "jobs":"دوري محترفين"}
# ,"softball":{"label":"سوفتبول", "team":"للسوفتبول", "jobs":"سوفتبول"}
# ,"baseball3":{"label":"البيسبول", "team":"للبيسبول", "jobs":"بيسبول"}
# ,"sledding":{"label":"الكليات", "team":"للكليات", "jobs":"كليات"}
# ,"athletics indoor":{"label":"ألعاب القوى داخل الصالات", "team":"لألعاب القوى داخل الصالات", "jobs":"ألعاب قوى داخل صالات"}
# ---
import sys
from pathlib import Path
import json

# ---
Dir2 = Path(__file__).parent
# ---
Sports_Keys_New = {}
# ---
with open(f"{Dir2}/jsons/Sports_Keys_New.json", "r", encoding="utf-8") as f:
    Sports_Keys_New = json.load(f)
# ---
Sports_Keys_New["kick boxing"] = Sports_Keys_New["kickboxing"]
Sports_Keys_New["sport climbing"] = Sports_Keys_New["climbing"]
Sports_Keys_New["aquatic sports"] = Sports_Keys_New["aquatics"]
Sports_Keys_New["shooting"] = Sports_Keys_New["shooting sport"]
Sports_Keys_New["motorsports"] = Sports_Keys_New["motorsport"]
Sports_Keys_New["road race"] = Sports_Keys_New["road cycling"]
Sports_Keys_New["cycling road race"] = Sports_Keys_New["road cycling"]
Sports_Keys_New["road bicycle racing"] = Sports_Keys_New["road cycling"]
Sports_Keys_New["auto racing"] = Sports_Keys_New["automobile racing"]
Sports_Keys_New["bmx racing"] = Sports_Keys_New["bmx"]
Sports_Keys_New["equestrianism"] = Sports_Keys_New["equestrian"]
Sports_Keys_New["mountain bike racing"] = Sports_Keys_New["mountain bike"]
# ---
Table = {"label": {}, "jobs": {}, "team": {}, "olympic": {}}
# ---
for kk in Sports_Keys_New.keys():
    labll = Sports_Keys_New[kk]  #
    # ---
    Sports_Keys_New2[f"{kk} racing"] = {
        "label": f'سباق {labll["label"]}',
        "team": f'لسباق {labll["label"]}',
        "jobs": f'سباق {labll["jobs"]}',
        "olympic": f'سباق {labll["olympic"]}',
    }
    # ---
    Sports_Keys_New2[f"wheelchair {kk}"] = {
        "label": f'{labll["label"]} على الكراسي المتحركة',
        "team": f'{labll["label"]} على الكراسي المتحركة',
        "jobs": f'{labll["jobs"]} على كراسي متحركة',
        "olympic": f'{labll["olympic"]} على كراسي متحركة',
    }
    # ---
for cc, cclab in Sports_Keys_New2.items():
    # if cc not in Sports_Keys_New:
    # printe.output(cc)
    Sports_Keys_New[cc] = cclab
# ---
for kk in Sports_Keys_New.keys():
    for key in Sports_Keys_New[kk]:
        if key not in Table:
            Table[key] = {}
        if Sports_Keys_New[kk][key]:
            Table[key][kk.lower()] = Sports_Keys_New[kk][key]
# ---
Sports_Keys_For_Label = Table["label"]
Sports_Keys_For_Jobs = Table["jobs"]
Sports_Keys_For_Team = Table["team"]
Sports_Keys_For_olympic = Table["olympic"]
# ---
# for k in Sports_Keys_For_Label:
# kaka = '"%s":"%s"' % (k , Sports_Keys_For_Label[k] )
# printe.output(kaka)
# ---
"""
gogo = [x for x in Sports_Keys]
gogo.sort()
def main():
    for k in gogo:
        faso = '{\n\t\tu"label":"%s", \n\t\tu"jobs":"%s", \n\t\tu"team":"%s"\n\t}' % (Keys3.get(k , ""), teams.get(k , ""), jjobs.get(k , "") )
        kaka = '\t,"%s":%s\n' % (k , faso )
        printe.output(kaka)
        with open( "make/aaaa.py" ,"a", encoding="utf-8") as logfile:
            logfile.write(kaka)
"""
# ---
Sports_Keys_New_line = ""
# ---
PP = [[len(xy.split(" ")), xy] for xy in Sports_Keys_For_Jobs]
PP.sort(reverse=True)
# ---
textsnew = "22"
# ---
for lln, sp in PP:
    # printe.output('%d\t\t%s' % (lln,sp))
    textsnew += f"|{sp}"
Sports_Keys_New_line = textsnew.replace("22|", "", 1)
# ---
# printe.output("find:%d in %s :." % (len(table) , table_name) )
# printe.output("===================" )
# printe.output(Sports_Keys_New_line)
# printe.output("===================" )
# ---
Sports_Keys_New_line2 = Sports_Keys_New_line.replace("(", r"\(").replace(")", r"\)")
fanco_line = rf".*({Sports_Keys_New_line2}).*"
fanco_line = rf".*\s*({Sports_Keys_New_line2})\s*.*"
"""
taytay = {}
# ---
for x in Sports_Keys_For_Jobs.keys() :
    xlines = x.split(" ")
    if len(xlines) not in taytay:
        taytay[len(xlines)] = []
    taytay[len(xlines)].append(x)
# ---
faor = list(taytay.keys())
faor.sort(reverse = True)
# ---
#printe.output(faor)
for x in faor :
    #printe.output("x:%d" % x )
    #printe.output(taytay[x])
    Sports_Keys_New_line += "|".join([ cc for cc in taytay[x] ])
# ---
"""
# printe.output(Sports_Keys_New_line)
# ---
# python3 core8/pwb.py make/Sport_key
# ---
if __name__ == "__main__":
    print(PP)
# ---
# ---
Lenth1 = {
    "Sports_Keys_New": sys.getsizeof(Sports_Keys_New),
    "All_Nat Sports_Keys_For_Jobs": sys.getsizeof(Sports_Keys_For_Jobs),
}
# ---
from .helps import len_print

len_print.lenth_pri("Sport_key.py", Lenth1)
# ---
del Sports_Keys_New
# ---
