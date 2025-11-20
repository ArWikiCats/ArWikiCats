import re


def fix_minor(arlabel, sps):
    # ---
    if sps:
        sps = sps.strip()
        arlabel = re.sub(rf" {sps}\s+{sps} ", f" {sps} ", arlabel)
        if sps == "و":
            arlabel = re.sub(rf" {sps} ", f" {sps}", arlabel)
    # ---
    return arlabel
