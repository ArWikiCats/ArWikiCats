#!/usr/bin/python3
"""

python3 core8/pwb.py make/false_files
"""

import re
import os
from pathlib import Path

Dir = Path(__file__).parent.parent.parent.parent
# ---
lenthes = {}
# ---
# python3 core8/pwb.py make/read import
files_all = []
# ---
text = ""
# ---
dir_to_work = "make2"
# ---
for root, dirs, files in os.walk(Dir / dir_to_work, topdown=True):
    for f in files:
        # ---
        if not root.endswith(dir_to_work):
            continue
        # ---
        if not f.endswith(".py"):
            continue
        # ---
        skip = ["test_yy2.py", "len.py", "__init__.py", "false_files.py"]
        # ---
        if f in skip:
            continue
        # ---
        filepath = os.path.join(root, f)
        # ---
        with open(filepath, "r", encoding="utf-8") as f:
            fafax = f.read()
        # ---
        text += f"\n{fafax}"
        # ---
        files_all.append(f)
        # ---
# ---
# text = re.sub(rf'from\s*{dir_to_work}\s*import\s*', f'from {dir_to_work} import ', text)
# text = re.sub(rf'from\s*{dir_to_work}\.(.*?)\s*import', 'from ..$1 import ', text)
# ---
for x in files_all:
    x = x.replace(".py", "")
    # find if text has x like from make import x
    # find if text has x like from make2 import x
    test = text
    test = re.sub(rf"from\s*{dir_to_work}\s*import\s*%s" % x, "", test)
    test = re.sub(rf"from\s*{dir_to_work}.%s\s*import" % x, "", test)
    # ---
    if test == text:
        print(f"file:({x}.py)")
    # ---
# ---
