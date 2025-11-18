#!/usr/bin/python3
"""
!
"""
import jsonlines
from pathlib import Path


def save(path, data) -> str:
    path = Path(path)
    # ---
    if isinstance(data, dict):
        data = [data]
    # ---
    if not path.parent.exists():
        path.parent.mkdir(parents=True)
        with jsonlines.open(path, mode='w') as writer:
            writer.write_all({})
    # ---
    with jsonlines.open(path, mode='a') as writer:
        writer.write_all(data)
