#!/usr/bin/python3
"""

from ..bots import ethnic_bot
# ---
ethnic_bot.output_test4 = output_test4
# ---
def Ethnic(cate, Start, con_3):
    return ethnic_bot.Ethnic(cate, Start, con_3)
# ---

"""
from typing import Dict
from ...ma_lists import Nat_women, Nat_men, Nat_mens
from ...ma_lists import en_is_nat_ar_is_women_2

from ...helps.print_bot import output_test4

Ethnic_culture_cash: Dict[str, str] = {}
Ethnic_cash: Dict[str, str] = {}


def Ethnic_culture(cate: str, Start: str, con_3: str) -> str:
    # ---
    cash_key = f"{cate}, {Start}, {con_3}".lower().strip()
    # ---
    if cash_key in Ethnic_culture_cash:
        return Ethnic_culture_cash[cash_key]
    # ---
    contry = Start
    cas = ""
    con_3_lab = ""
    cas_lab = ""
    contry_lab = ""
    # ---
    if Nat_women.get(contry, "") == "" and Nat_men.get(contry, "") == "":
        return contry_lab
    # ---
    _culture_table = {
        "culture": "ثقافة {}",
    }
    # ---
    if not cas and not cas_lab:
        contry_L = Nat_women.get(contry, "")
        for x, x_lab in en_is_nat_ar_is_women_2.items():
            if not cas_lab:
                xx = f" {x}"
                if con_3.endswith(xx):
                    cas = x
                    con_3 = con_3[: -len(xx)]
                    cas_lab = x_lab
                    con_3_lab = Nat_women.get(con_3, "")
    # ---
    male_table = {
        "history": "تاريخ {}",
        "descent": "أصل {}",
        "cuisine": "مطبخ {}",
        "literature": "أدب {}",
        "law": "قانون {}",
        "wine": "نبيذ {}",
        "diaspora": "شتات {}",
        "traditions": "تراث {}",
        "folklore": "فلكور {}",
        "television": "تلفاز {}",
    }
    # ---
    if cas == "" and cas_lab == "":
        contry_L = Nat_men.get(contry, "")
        for x, xlab in male_table.items():
            if not cas_lab:
                xx = f" {x}"
                if con_3.endswith(xx):
                    cas = x
                    con_3 = con_3[: -len(xx)]
                    cas_lab = xlab
                    con_3_lab = Nat_men.get(con_3, "")
    # ---history
    if cas and cas_lab:
        if con_3_lab:
            rz = f"{con_3_lab} {contry_L}"
            contry_lab = cas_lab.format(rz)
            output_test4(f'<<lightblue>> test Ethnic_culture: new contry_lab  "{contry_lab}" ')
    # ---
    Ethnic_culture_cash[cash_key] = contry_lab
    # ---
    return contry_lab


def Ethnic(cate: str, Start: str, con_3: str) -> str:
    # ---
    cash_key = f"{cate}, {Start}, {con_3}".lower().strip()
    # ---
    if cash_key in Ethnic_cash:
        return Ethnic_cash[cash_key]
    # ---
    contry = Start
    contry_lab = ""
    # ---
    if con_3.endswith(" people"):
        con_nat = con_3[: -len(" people")]
        if Nat_mens.get(con_nat):
            con_3 = con_3[: -len(" people")]
    # ---
    con_3_lab = Nat_mens.get(con_3, "")
    if con_3_lab:
        if Nat_mens.get(contry, "") != "":
            contry_lab = f"{con_3_lab} {Nat_mens.get(contry, '')}"
            output_test4(f'<<lightblue>> test Ethnic: new contry_lab  "{contry_lab}" ')
    # ---
    if not contry_lab:
        contry_lab = Ethnic_culture(cate, Start, con_3)
    # ---
    Ethnic_cash[cash_key] = contry_lab
    # ---
    return contry_lab
