
import re
from dataclasses import dataclass
from ...format_bots import Tit_ose_Nmaes
from ....ma_lists.type_tables import basedtypeTable


def load_keys_to_pattern(data_List):
    data_List_sorted = sorted(data_List, key=lambda x: -x.count(" "))
    # ---
    data_pattern = '|'.join(map(re.escape, [n.lower() for n in data_List_sorted]))
    # ---
    return data_pattern


yy = (
    r"\d+(?:th|st|rd|nd)[−–\- ](?:millennium|century)?\s*(?:BCE*)?"
    r"|\d+(?:th|st|rd|nd)[−–\- ](?:millennium|century)?"
    r"|\d+[−–\-]\d+"
    r"|\d+s\s*(?:BCE*)?"
    r"|\d+\s*(?:BCE*)?"
).lower()

MONTHSTR2 = "(?:january|february|march|april|may|june|july|august|september|october|november|december) *"

safo = "|".join(list(basedtypeTable))
titttto = " |".join(x.strip() for x in Tit_ose_Nmaes.keys())

category_start = r"Category\:"
category_start = ""

tita_other_match = r"\s*(?P<typeo>" + safo.lower() + r"|)\s*(?P<in>" + titttto.lower() + r"|)\s*(?P<country>.*|).*"

reg_line_1_match = rf"{category_start}(?P<month>" + MONTHSTR2 + "|)(?P<year>" + yy + "|)" + tita_other_match


@dataclass
class Typies:
    year_at_first: str
    typeo: str
    In: str
    country: str
    cat_test: str


def get_cats(category_r):
    # cate = re.sub(r"[−–\-](millennium|century)", r" \g<1>", category_r, flags=re.I)
    cate = category_r
    # ---
    # cate = re.sub(r"[−–\-](millennium|century)", r" \g<1>", cate, flags=re.I)
    cate = re.sub(r"[−–\-](millennium|century)", r"-\g<1>", cate, flags=re.I)
    # ---
    cate3 = re.sub(r"category:", "", cate.lower(), flags=re.IGNORECASE)
    # ---
    # if not cate.lower().startswith("category:"): cate = f"Category:{cate}"
    # ---
    return cate, cate3


def get_reg_result(category_r: str) -> Typies:
    # ---
    cate, cate3 = get_cats(category_r)
    # ---
    if category_start:
        if not cate.lower().startswith("category:"):
            cate = f"Category:{cate}"
    else:
        cate = re.sub(r"category:", "", cate, flags=re.IGNORECASE)
    # ---
    cate_gory = cate.lower()
    # ---
    cat_test = cate3
    # ---
    match_it = re.search(reg_line_1_match, cate_gory, flags=re.I)
    # ---
    year_at_first = f"{match_it.group('month')}{match_it.group('year')}" if match_it else ""
    # ---
    typeo = match_it.group("typeo") if match_it else ""
    # ---
    if year_at_first and cate_gory.startswith(category_start + year_at_first):
        cat_test = cat_test.replace(year_at_first.lower(), "")
    # ---
    In = match_it.group("in") if match_it else ""
    # ---
    if In == cate_gory or In == cate3:
        In = ""
    # ---
    country = match_it.group("country") if match_it else ""
    # ---
    if In.strip() == "by":
        country = f"by {country}"
    # ---
    if not year_at_first and not typeo:
        country = ""
    # ---
    # if country.lower() == cate_gory.lower().replace("category:", ""): country = ""
    # ---
    # Category:january 2025 disasters during Covid-19
    # year_at_first='january 2025 ', typeo='disasters', In='during ', country='covid-19', cat_test='january 2025 disasters during covid-19'
    print(f"{year_at_first=}, {typeo=}, {In=}, {country=}, {cat_test=}\n" * 10)
    # ---
    return Typies(
        year_at_first=year_at_first,
        typeo=typeo,
        In=In,
        country=country,
        cat_test=cat_test,
    )
