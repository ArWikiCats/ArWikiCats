"""
from  make.make2_bots.ma_bots import list_cat_format
# category_lab, list_of_cat = list_cat_format.list_of_cat_func(category_r, category_lab, list_of_cat, foot_ballers)

"""
from typing import Tuple
from ...helps.print_bot import print_put


def list_of_cat_func(category_r: str, category_lab: str, list_of_cat: str, foot_ballers: bool) -> Tuple[str, str]:
    category_lab_or = category_lab
    list_of_cat_x = list_of_cat.split("{}")[0].strip()
    print_put(f"<<lightblue>> list_of_cat_func {list_of_cat=}, {list_of_cat_x=}")
    if not category_lab.startswith(list_of_cat_x):
        category_lab = list_of_cat.format(category_lab)
    print_put(f"<<lightblue>> list_of_cat_func add {category_lab=}, {category_lab_or=}, {category_r=} ")
    # fix tab[Category:Guernsey footballers] = "تصنيف:لاعبو غيرنزي"
    if foot_ballers and "كرة" not in category_lab:
        list_of_cat = list_of_cat.replace("{}", " كرة قدم {}")
        category_lab = list_of_cat.format(category_lab_or)
        print_put(f'<<lightblue>> list_of_cat_func add list_of_cat:{list_of_cat}, category_lab:"{category_lab}", category_r:{category_r} ')
    return category_lab, list_of_cat
