#!/usr/bin/python3
"""
from ..media_bots.film_keys_bot import get_Films_key_CAO, Films

"""
from typing import Dict
from ..ma_lists_bots import en_is_nat_ar_is_women

from ..ma_lists_bots import (
    Films_key_CAO,
    Films_key_For_nat,
    Films_key_CAO_new_format,
    television_keys_female,
    Films_key_333,
)
from ..ma_lists_bots import (
    Nat_women,
    Nat_mens,
)
from ..helps.print_bot import output_test4


get_Films_key_CAO_cash: Dict[str, str] = {}
Films_cash: Dict[str, str] = {}


def get_Films_key_CAO(con_3: str) -> str:
    # ---
    if con_3 in get_Films_key_CAO_cash:
        return get_Films_key_CAO_cash[con_3]
    # ---
    output_test4(f'<<lightblue>> get_Films_key_CAO : con_3 "{con_3}" ')
    con_33 = con_3.lower().strip()
    cas_lab = ""
    labr = ""
    for tyty, cas_lab in television_keys_female.items():
        # ---
        if con_33.endswith(tyty.lower()):
            cc = con_33[: -len(tyty)].strip()
            output_test4(f'<<lightblue>> cc:"{cc}", endswith:"{tyty}" ')
            # ---
            con_3_lab = Films_key_333.get(cc.strip(), "")
            # ---
            if con_3_lab:
                output_test4(f'<<lightblue>> get_Films_key_CAO : cc "{cc}" ')
                if "{}" in con_3_lab:
                    labr = con_3_lab.format(tyty=cas_lab)
                else:
                    labr = f"{cas_lab} {con_3_lab}"
                output_test4(f'<<lightblue>> get_Films_key_CAO: new labr "{labr}" ')
    # ---
    get_Films_key_CAO_cash[con_3] = labr
    # ---
    return labr


def Films(cate: str, Start: str, con_3: str, fa: str = "") -> str:
    # ---
    cash_key = f"{cate}, {Start}, {con_3}".lower().strip()
    # ---
    if cash_key in Films_cash:
        return Films_cash[cash_key]
    # ---
    contry = Start
    contry_lab = ""
    # ---
    if con_3:
        llab = Nat_mens[contry] if con_3 == "people" else Nat_women[contry]
        con_3_lab = en_is_nat_ar_is_women.get(con_3.strip(), "")
        if con_3_lab:
            contry_lab = con_3_lab.format(llab)
            output_test4(f'<<lightblue>> test_4:Films: new contry_lab  "{contry_lab}" ')
        # ---#Films_key_CAO
        if not contry_lab:
            con_3_lab = Films_key_CAO.get(con_3, get_Films_key_CAO(con_3))
            if con_3_lab:
                contry_lab = f"{con_3_lab} {llab}"
                # ---
                if con_3 in Films_key_CAO_new_format:
                    contry_lab = Films_key_CAO_new_format[con_3].format(llab)
                # ---
                output_test4(f'<<lightblue>> test_4:Films: new contry_lab "{contry_lab}" , con_3:{con_3} ')
        # ---#Films_key_For_nat
        if not contry_lab:
            con_3_lab = Films_key_For_nat.get(con_3, "")
            if con_3_lab:
                contry_lab = con_3_lab.format(llab)
                output_test4(f'<<lightblue>> Films_key_For_nat:Films: new contry_lab  "{contry_lab}" ')
    # ---#get_Films_key_CAO
    if not contry_lab:
        cate_lab = Films_key_CAO.get(cate, "")
        if cate_lab:
            contry_lab = cate_lab
            output_test4(f'<<lightblue>> test Films: contry_lab "{contry_lab}" ')
    # ---
    if not contry_lab:
        contry_lab = get_Films_key_CAO(cate)
        if contry_lab:
            output_test4(f'<<lightblue>> test Films: new contry_lab "{contry_lab}" ')
    # ---
    Films_cash[cash_key] = contry_lab
    # ---
    return contry_lab
