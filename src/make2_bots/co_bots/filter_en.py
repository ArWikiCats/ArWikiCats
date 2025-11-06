import re
from ... import printe

blacklisted_substrings: list[str] = [
    "Disambiguation",
    "wikiproject",
    "sockpuppets",
    "without a source",
    "images for deletion",
]
# ---
blacklisted_prefixes: list[str] = [
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
    for x in blacklisted_substrings:
        if x in cat.lower():
            printe.output(f"<<lightred>> find ({x}) in cat")
            return False
    # ---
    cat2 = cat.lower().replace("category:", "")
    # ---
    for x in blacklisted_prefixes:
        if cat2.startswith(x.lower()):
            printe.output(f"<<lightred>> cat.startswith({x})")
            return False
    # ---
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    # ---
    for x in months:
        # match the end of cat like month \d+
        month_year_pattern = rf"^.*? from {x.lower()} \d+$"
        if re.match(month_year_pattern, cat2):
            printe.output(f"<<lightred>> cat.match({month_year_pattern})")
            return False
    # ---
    return True
