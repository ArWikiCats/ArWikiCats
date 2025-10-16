import re
from ... import printe

BBlcak: list[str] = [
    "Disambiguation",
    "wikiproject",
    "sockpuppets",
    "without a source",
    "images for deletion",
]
# ---
blcak_starts: list[str] = [
    "Clean-up",
    "Cleanup",
    "Uncategorized",
    "Unreferenced",
    "Unverifiable",
    "Unverified",
    "Wikipedia",
    "Wikipedia articles",
    "Articles about",
    "Articles containing",
    "Articles covered",
    "Articles lacking",
    "Articles needing",
    "Articles prone",
    "Articles requiring",
    "Articles slanted",
    "Articles sourced",
    "Articles tagged",
    "Articles that",
    "Articles to",
    "Articles with",
    "use ",
    "User pages",
    "Userspace",
]


def filter_cat(cat: str) -> bool:
    for x in BBlcak:
        if x in cat.lower():
            printe.output(f"<<lightred>> find ({x}) in cat")
            return False
    # ---
    cat2 = cat.lower().replace("category:", "")
    # ---
    for x in blcak_starts:
        if cat2.startswith(x.lower()):
            printe.output(f"<<lightred>> cat.startswith({x})")
            return False
    # ---
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    # ---
    for x in months:
        # match the end of cat like month \d+
        matt = rf"^.*? from {x.lower()} \d+$"
        if re.match(matt, cat2):
            printe.output(f"<<lightred>> cat.match({matt})")
            return False
    # ---
    return True
