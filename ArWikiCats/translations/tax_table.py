#!/usr/bin/python3
""" """

from .utils.json_dir import open_json_file

Taxons_table = {}
# ---
Taxons = open_json_file("taxonomy/Taxons.json") or {}
Taxons2 = open_json_file("taxonomy/Taxons2.json") or {}
# ---
Taxons.update(Taxons2)
# ---
Taxons_table.update(Taxons)
# ---
for tax, taxlab in Taxons.items():
    Taxons_table[f"{tax} of"] = taxlab
    Taxons_table[f"fossil {tax}"] = f"{taxlab} أحفورية"
    Taxons_table[f"fossil {tax} of"] = f"{taxlab} أحفورية"
# ---
for taxe, lab in Taxons2.items():
    Taxons_table[f"{taxe} of"] = f"{lab} في"

__all__ = [
    "Taxons_table",
]
