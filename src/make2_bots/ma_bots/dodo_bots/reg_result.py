
import re
from dataclasses import dataclass
from ...format_bots import Tit_ose_Nmaes
from ....ma_lists.type_tables import basedtypeTable
from ...reg_lines import tita, tita_year, ddd, tita_year_no_month
from ....new.time_to_arabic import match_time_en_first  # , convert_time_to_arabic, match_time_ar

safo = "|".join(list(basedtypeTable))

titttto = " |".join(x.strip() for x in Tit_ose_Nmaes.keys())
# for titf in Tit_ose_Nmaes.keys(): titttto += f"{titf.strip()} |"

en_literes = "[abcdefghijklmnopqrstuvwxyz]"
tita_other = r"\s*(" + safo + r"|)\s*(" + titttto + r"|)\s*(.*|).*"

reg_line_1 = tita.lower() + tita_other.lower()


@dataclass
class Typies:
    year: str
    typeo: str
    In: str
    country: str
    cat_test: str


def match_year(category):
    # ---
    Tita_year = tita_year
    # ---
    test_month = re.sub(ddd, "", category, flags=re.I)
    if test_month.lower() == category.lower():
        Tita_year = tita_year_no_month
    # ---
    year = re.sub(Tita_year, r"\g<1>\g<2>", category, flags=re.I)
    # ---
    if year.lower() == category.lower():
        year = ""
    # ---
    return year


def match_typeo(cate_gory, year):
    # ---
    typeo = re.sub(reg_line_1, r"\g<3>", cate_gory, flags=re.I)
    # ---
    if year and cate_gory.startswith("category:" + year):
        tita_n = "category:" + year + tita_other
        typeo = re.sub(tita_n, r"\g<1>", cate_gory, flags=re.I)
    # ---
    if typeo.lower() == cate_gory.lower():
        typeo = ""
    # ---
    return typeo


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
    if not cate.lower().startswith("category:"):
        cate = f"Category:{cate}"
    # ---
    cate_gory = cate.lower()
    # ---
    cat_test = cate3
    # ---
    year = match_year(cate_gory)
    # year = match_time_en_first(cate)
    # ---
    typeo = match_typeo(cate_gory, year)
    # ---
    if year and cate_gory.startswith("category:" + year):
        cat_test = cat_test.replace(year.lower(), "")
    # ---
    In = re.sub(reg_line_1, r"\g<4>", cate_gory, flags=re.I)
    # ---
    if In == cate_gory or In == cate3:
        In = ""
    # ---
    country = re.sub(reg_line_1, r"\g<5>", cate_gory, flags=re.I)
    # ---
    if country == cate_gory or country == cate3:
        country = ""
    # ---
    if In.strip() == "by":
        country = f"by {country}"
    # ---
    return Typies(
        year=year,
        typeo=typeo,
        In=In,
        country=country,
        cat_test=cat_test,
    )
