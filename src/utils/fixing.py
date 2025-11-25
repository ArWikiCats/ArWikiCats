import re


def fix_minor(arlabel: str, sps: str = "") -> str:
    """Clean up duplicate spaces and repeated prepositions in labels."""

    arlabel = " ".join(arlabel.strip().split())

    sps_list = ["من", "في", "و",]

    sps = sps.strip()

    if sps not in sps_list:
        sps_list.append(sps)

    for sps in sps_list:
        arlabel = re.sub(rf" {sps}\s+{sps} ", f" {sps} ", arlabel)
        if sps == "و":
            arlabel = re.sub(rf" {sps} ", f" {sps}", arlabel)

    arlabel = " ".join(arlabel.strip().split())

    return arlabel
