#!/usr/bin/python3
"""

Usage:
from .Sport_key import Sports_Keys_For_Label, Sports_Keys_For_Team, Sports_Keys_For_Jobs, Sports_Keys_For_olympic, fanco_line
"""

# ---
from ..utils.json_dir import open_json_file
from ...helps import len_print

Sports_Keys_New2 = {}
# ---
Sports_Keys_New = {}
# ---
Sports_Keys_New = open_json_file("Sports_Keys_New") or {}
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
    labll = Sports_Keys_New[kk]
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
Sports_Keys_New.update(dict(Sports_Keys_New2))
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
Sports_Keys_New_line = ""
# ---
PP = [[len(xy.split(" ")), xy] for xy in Sports_Keys_For_Jobs]
PP.sort(reverse=True)
# ---
textsnew = "22"
# ---
for lln, sp in PP:
    textsnew += f"|{sp}"
Sports_Keys_New_line = textsnew.replace("22|", "", 1)
# ---
Sports_Keys_New_line2 = Sports_Keys_New_line.replace("(", r"\(").replace(")", r"\)")
fanco_line = rf".*({Sports_Keys_New_line2}).*"
fanco_line = rf".*\s*({Sports_Keys_New_line2})\s*.*"
# ---
len_print.data_len("Sport_key.py", {
    "Sports_Keys_New2": Sports_Keys_New2,
    "Sports_Keys_New": Sports_Keys_New,
    "Sports_Keys_For_Jobs": Sports_Keys_For_Jobs,
    "Sports_Keys_For_Team": Sports_Keys_For_Team,
    "Sports_Keys_For_Label": Sports_Keys_For_Label,
})
# ---
del Sports_Keys_New

__all__ = [
    "fanco_line",
    "Sports_Keys_For_Jobs",
    "Sports_Keys_For_Team",
    "Sports_Keys_For_Label",
]
