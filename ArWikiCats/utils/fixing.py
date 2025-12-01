import re


def fix_minor(arlabel: str, ar_separator: str = "") -> str:
    """Clean up duplicate spaces and repeated prepositions in labels."""

    arlabel = " ".join(arlabel.strip().split())

    sps_list = [
        "من",
        "في",
        "و",
    ]

    ar_separator = ar_separator.strip()

    if ar_separator not in sps_list:
        sps_list.append(ar_separator)

    for ar_separator in sps_list:
        arlabel = re.sub(rf" {ar_separator}\s+{ar_separator} ", f" {ar_separator} ", arlabel)
        if ar_separator == "و":
            arlabel = re.sub(rf" {ar_separator} ", f" {ar_separator}", arlabel)

    arlabel = " ".join(arlabel.strip().split())

    return arlabel
