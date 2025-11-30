#!/usr/bin/python3
""" """

from .utils.json_dir import open_json_file

Taxons_table = {}
# ---
Taxons = open_json_file("taxonomy/Taxons.json") or {}
Taxons2 = open_json_file("taxonomy/Taxons2.json") or {}
Taxons3 = open_json_file("taxonomy/Taxons3.json") or {}
# ---
Taxons.update(Taxons2)
Taxons.update(Taxons3)
Taxons_table.update(Taxons)
# ---
for tax, taxlab in Taxons.items():
    Taxons_table[f"{tax} of"] = taxlab
    fossil_lab = f"{taxlab} أحفورية"
    Taxons_table[f"fossil {tax}"] = fossil_lab
    Taxons_table[f"fossil {tax} of"] = fossil_lab
# ---
for taxe, lab in Taxons2.items():
    Taxons_table[f"{taxe} of"] = f"{lab} في"
