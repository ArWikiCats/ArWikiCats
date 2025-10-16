#!/usr/bin/python3
"""
from .pop_2018 import pop_All_2018

"""
# ---
from pathlib import Path
import json

# ---
Dir2 = Path(__file__).parent
# ---
pop_All_2018 = {}
# ---
with open(f"{Dir2}/jsons/pop_All_2018.json", "r", encoding="utf-8") as f:
    pop_All_2018 = json.load(f)
# ---
