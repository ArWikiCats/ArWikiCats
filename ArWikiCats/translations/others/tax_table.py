#!/usr/bin/python3
"""
Taxonomic translations for the ArWikiCats project.
This module loads and processes taxonomic data to provide Arabic translations
for biological taxa, including fossil variants.
"""

from ..utils import open_json_file

TAXON_TABLE = {}
# ---
Taxons = open_json_file("taxonomy/Taxons.json") or {}
Taxons2 = open_json_file("taxonomy/Taxons2.json") or {}
# ---
Taxons.update(Taxons2)
# ---
TAXON_TABLE.update(Taxons)
# ---
for tax, taxlab in Taxons.items():
    TAXON_TABLE[f"{tax} of"] = taxlab
    TAXON_TABLE[f"fossil {tax}"] = f"{taxlab} أحفورية"
    TAXON_TABLE[f"fossil {tax} of"] = f"{taxlab} أحفورية"
# ---
for taxe, lab in Taxons2.items():
    TAXON_TABLE[f"{taxe} of"] = f"{lab} في"

__all__ = [
    "TAXON_TABLE",
]
