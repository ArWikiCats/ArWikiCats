#!/usr/bin/python3
"""
from .peoples import People_key

Query at: [People_key.sql](queries/People_key.sql)
"""
# ---
from ..utils.json_dir import open_json
from ...helps import len_print

People_key = open_json("peoples.json") or {}

len_print.data_len(
    "peoples.py",
    {
        "People_key": People_key,
    },
)
