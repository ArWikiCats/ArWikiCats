
import re
from dataclasses import dataclass
from ...format_bots import Tit_ose_Nmaes
from ....ma_lists.type_tables import basedtypeTable
from ...reg_lines import tita, tita_year, ddd, tita_year_no_month

safo = "|".join(list(basedtypeTable))

titttto = " |".join(x.strip() for x in Tit_ose_Nmaes.keys())
# for titf in Tit_ose_Nmaes.keys(): titttto += f"{titf.strip()} |"

en_literes = "[abcdefghijklmnopqrstuvwxyz]"
tita_other = r"\s*(" + safo + r"|)\s*(" + titttto + r"|)\s*(.*|).*"


@dataclass
class Typies:
    year: str
    typeo: str
    In: str
    country: str
    cat_test: str


def get_reg_result(category: str, _category_: str, category3: str, cat_test: str) -> Typies:
    # ---
    Tita_year = tita_year
    # ---
    test_month = re.sub(ddd, "", category.lower())
    # ---
    if test_month == category:
        Tita_year = tita_year_no_month
    # ---
    reg_line_1 = tita + tita_other
    reg_line_1 = reg_line_1.lower()
    # ---
    year = re.sub(Tita_year, r"\g<1>\g<2>", _category_)
    typeo = re.sub(reg_line_1, r"\g<3>", _category_)
    # ---
    if year == _category_ or year == category3:
        year = ""
    elif year and _category_.startswith("category:" + year):
        cat_test = cat_test.replace(year.lower(), "")
        tita_n = "category:" + year + tita_other
        typeo = re.sub(tita_n, r"\g<1>", _category_)

    if typeo == _category_ or typeo == category3:
        typeo = ""
    # ---
    In = re.sub(reg_line_1, r"\g<4>", _category_)
    # ---
    if In == _category_ or In == category3:
        In = ""
    # ---
    country = re.sub(reg_line_1, r"\g<5>", _category_)
    # ---
    if country == _category_ or country == category3:
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
