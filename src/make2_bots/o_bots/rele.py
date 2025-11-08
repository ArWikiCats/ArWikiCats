"""Resolve labels for relations between countries."""

from __future__ import annotations

import re
from typing import Mapping, Tuple
from ... import printe
from ...helps.print_bot import print_put
from .utils import apply_arabic_article

from ...ma_lists import All_contry_ar, All_contry_with_nat_keys_is_en, Nat_men, Nat_women

P17_PREFIXES: Mapping[str, str] = {
    " conflict": "صراع {}",
    " proxy conflict": "صراع {} بالوكالة",
}

RELATIONS_FEMALE: Mapping[str, str] = {
    " military relations": "العلاقات {} العسكرية",
    " joint economic efforts": "الجهود الاقتصادية المشتركة {}",
    " relations": "العلاقات {}",
    " border crossings": "معابر الحدود {}",
    " border towns": "بلدات الحدود {}",
    " border": "الحدود {}",
    " clashes": "الاشتباكات {}",
    " wars": "الحروب {}",
    " war": "الحرب {}",
}

RELATIONS_MALE: Mapping[str, str] = {
    " conflict video games": "ألعاب فيديو الصراع {}",
    " conflict legal issues": "قضايا قانونية في الصراع {}",
    " conflict": "الصراع {}",
    " football rivalry": "التنافس {} في كرة القدم",
}


def work_relations(value: str) -> str:
    """Return the label for relations between two countries.

    Args:
        value: Category describing the relationship between two countries.

    Returns:
        The resolved Arabic label or an empty string when the relation cannot
        be interpreted.
    """

    value = value.lower()
    print_put(f"start work_relations: value:{value}")
    # ---
    gen_key = "women"
    dodo = All_contry_with_nat_keys_is_en
    nat_tab = Nat_women
    pp_priffix = RELATIONS_FEMALE
    # ---
    first_part = ""
    end_part = ""
    # ---
    suus_lab = ""
    # ---
    # الحصول على الجزء الأخير
    for pri_ff in RELATIONS_FEMALE:
        if value.endswith(pri_ff):
            print_put(f'\t\t>>>><<lightblue>> work_relations :"{value}".endswith({pri_ff})')
            end_part = pri_ff
            first_part = value[: -len(pri_ff)]
            break
    # ---
    if first_part == "" and end_part == "":
        for pri_ff in RELATIONS_MALE:
            if value.endswith(pri_ff):
                print_put(f'\t\t>>>><<lightblue>> work_relations :"{value}".endswith({pri_ff})')
                end_part = pri_ff
                first_part = value[: -len(pri_ff)]
                # ---
                nat_tab = Nat_men
                gen_key = "men"
                pp_priffix = RELATIONS_MALE
                # ---
                break

    if first_part:
        printe.output(f'\t\t>>>><<lightblue>> first_part :"{first_part}"')
        # space = "–"
        space = "-"
        if first_part.find("–") != -1 or first_part.find("-") != -1:
            print_put(f'\t\t>>>><<lightblue>> first_part.find(space) :"{first_part.find(space)}" ')

            Mash = "^(.*)(?:–|-|−)(.*)$"
            co1 = re.sub(Mash, r"\g<1>", first_part.lower())
            co2 = re.sub(Mash, r"\g<2>", first_part.lower())

            if co2 == first_part:
                co2 = ""
            if co1 == first_part:
                co1 = ""

            printe.output(f'\t\t>>>><<lightblue>> end_part:"{end_part}", co1:"{co1}", co2:"{co2}"')

            co1_lab = dodo.get(co1, {}).get(gen_key) or nat_tab.get(co1, "")

            co2_lab = dodo.get(co2, {}).get(gen_key) or nat_tab.get(co2, "")

            # if co1 == "nato" : co1_lab = "الناتو"
            # if co2 == "nato" : co2_lab = "الناتو"

            if not co1_lab:
                printe.output(f'\t\t>>>><<lightblue>> cant find lab for:"{co1}"')

            if not co2_lab:
                printe.output(f'\t\t>>>><<lightblue>> cant find lab for:"{co2}"')
            else:
                print_put(f'\t\t>>>><<lightblue>> co2_lab:{co2}"{co2_lab}"')

            if co1_lab and co2_lab:
                # uuu_lab = co1_lab + " " + co2_lab
                uuu_lab = f"{co1_lab} {co2_lab}"
                popo = sorted([co1_lab, co2_lab])
                uuu_lab = " ".join(popo)
                uuu_lab = re.sub(r" ", " ال", f" {uuu_lab}")
                print_put(f'\t\t>>>><<lightblue>> value.endswith end_part("{end_part}"), uuu_lab:"{uuu_lab}"')
                # ---
                suus_lab = pp_priffix[end_part].format(uuu_lab)
                # ---
                # suus_lab = re.sub(r" ", " ال", suus_lab )
                print_put(f'\t\t>>>> suus_lab:"{suus_lab}"')

            if end_part == " relations" and "nato" in [co2, co1]:
                lab = All_contry_ar.get(co1, "")
                if co1 == "nato":
                    lab = All_contry_ar.get(co2, "")
                if lab:
                    suus_lab = f"علاقات الناتو و{lab}"
                    print_put(f'\t\t>>>> suus_lab:"{suus_lab}"')

    # dodo2 = All_contry_ar
    if not suus_lab:
        U_44 = ""
        pri_o = ""
        for pri_dd in P17_PREFIXES:
            if not U_44:
                if value.endswith(pri_dd):
                    printe.output(f'\t\t>>>><<lightblue>> work_relations :"{value}".endswith({pri_dd})')
                    pri_o = pri_dd
                    U_44 = value[: -len(pri_dd)]
        # ---
        if U_44:
            print_put(f'\t\t>>>><<lightblue>> U_44 :"{U_44}"')
            # space = "–"
            space = "-"
            if U_44.find("–") != -1 or U_44.find("-") != -1 or U_44.find("−") != -1:
                print_put(f'\t\t>>>><<lightblue>> U_44.find(space) :"{U_44}" ')

                Mash2 = "^(.*)(?:–|-|−)(.*)$"
                co11 = re.sub(Mash2, r"\g<1>", U_44)
                co22 = re.sub(Mash2, r"\g<2>", U_44)

                if co22 == U_44:
                    co22 = ""
                if co11 == U_44:
                    co11 = ""

                print_put(f'\t\t>>>><<lightblue>> co11:"{co11}", co22:"{co22}"')
                co11_lab = All_contry_ar.get(co11, "")
                co22_lab = All_contry_ar.get(co22, "")

                if not co11_lab:
                    print_put(f'\t\t>>>><<lightblue>> cant find lab for:"{co11}"')

                if not co22_lab:
                    print_put(f'\t\t>>>><<lightblue>> cant find lab for:"{co22}"')
                else:
                    print_put(f'\t\t>>>><<lightblue>> co22_lab:{co22}"{co22_lab}"')

                if co11_lab and co22_lab:
                    # uuu_lab = co11_lab + " " + co22_lab
                    uuu_lab = f"{co11_lab} و{co22_lab}"
                    popo = sorted([co11_lab, co22_lab])
                    uuu_lab = " و".join(popo)

                    print_put(f'\t\t>>>><<lightyellow>> value.endswith pri_o("{pri_o}"), uuu_lab:"{uuu_lab}"')
                    suus_lab = P17_PREFIXES[pri_o].format(uuu_lab)

                    print_put(f'\t\t>>>> suus_lab:"{suus_lab}"')

    return suus_lab


__all__ = [
    "work_relations"
]
