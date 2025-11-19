#!/usr/bin/python3
"""
from .peoples import People_key

Query at: [People_key.sql](queries/People_key.sql)
"""
from ...helps import len_print

# ---
from ..utils.json_dir import open_json

People_key = open_json("peoples.json") or {}

len_print.data_len(
    "peoples.py",
    {
        "People_key": People_key,
    },
)
