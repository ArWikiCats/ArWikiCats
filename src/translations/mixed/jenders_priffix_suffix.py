

YEARS_LIST: list[int] = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]

people_priffix: dict[str, str] = {
    "assassinated": "{} مغتالون",
    "fictional": "{} خياليون",
    "native": "{} أصليون",
    "murdered": "{} قتلوا",
    "killed": "{} قتلوا",
    "contemporary": "{} معاصرون",
    "ancient": "{} قدماء",
}

Mens_suffix: dict[str, str] = {
    "male deaf": "{} صم ذكور",
    "blind": "{} مكفوفون",
    "deafblind": "{} صم ومكفوفون",
    "deaf": "{} صم",
    "missing-in-action": "{} فقدوا في عمليات قتالية",
    "missing in action": "{} فقدوا في عمليات قتالية",
    "killed-in-action": "{} قتلوا في عمليات قتالية",
    "killed in action": "{} قتلوا في عمليات قتالية",
    "murdered abroad": "{} قتلوا في الخارج",
}


Me_priffix: dict[str, str] = {
    "amputee": "{} مبتورو أحد الأطراف",
    "blind": "{} مكفوفون",
    "child": "{} أطفال",
    "children": "{} أطفال",
    "contemporary": "{} معاصرون",
    "deaf": "{} صم",
    "deafblind": "{} صم ومكفوفون",
    "disabled": "{} معاقون",
    "executed": "{} معدمون",
    "fictional": "{} خياليون",
    "latin": "{} لاتينيون",
    "lgbt male": "{} مثليون ذكور",
    "lgbt": "{} مثليون",
    "male child": "{} أطفال ذكور",
    "male deaf": "{} صم ذكور",
    "male": "{} ذكور",
    "men": "{} رجال",
    "military": "{} عسكريون",
    "mythological": "{} أسطوريون",
    "nautical": "{} بحريون",
    "political": "{} سياسيون",
    "religious": "{} دينيون",
    "romantic": "{} رومانسيون",
    # "male" : "ذكور {}",
}


Wo_priffix: dict[str, str] = {
    # "women of" : "{}",
    # "non-" : "غير {}",
    "women": "{}",
    "female": "{}",
    "women's": "{}",
    "blind": "{} مكفوفات",
    "deafblind": "{} صم ومكفوفات",
    "deaf": "{} صم",
    # "expatriate women's" : "{} مغتربات",
    # "expatriate female" : "{} مغتربات",
    # "expatriate women" : "{} مغتربات",
}


def _extend_men_prefixes() -> dict[str, str]:
    """
    Populate prefix variants used for male categories.
    # ,"kidnapped":  {"mens":"مختطفون", "womens":"مختطفات"}
    # """

    data = {
        "kidnapped": "{} مختطفون",
        "expatriate": "{} مغتربون",
        "renaissance": "{} عصر النهضة",
        "murdered": "{} قتلوا",
        "under-19": "{} تحت 19 سنة",
        "assassinated": "{} مغتالون",
        "sunni muslim": "{} مسلمون سنة",
    }
    for prefix, template in Me_priffix.items():
        data[prefix] = template
        data[f"expatriate {prefix}"] = f"{template} مغتربون"

    for year in YEARS_LIST:
        data[f"under-{year}"] = f"{{}} تحت {year} سنة"
        data[f"under–{year}"] = f"{{}} تحت {year} سنة"
    return data


def _extend_women_prefixes() -> dict[str, str]:
    """Populate prefix variants used for female categories."""

    data = {}

    for prefix, template in Wo_priffix.items():
        data[prefix] = template
        data[f"expatriate {prefix}"] = f"{template} مغتربات"
        data[f"kidnapped {prefix}"] = f"{template} مختطفات"
        # data["executed"] = "معدومات"
        # data["executed {}".format(prefix)] = "{template} معدومات"
    return data


Women_s_priffix: dict[str, str] = _extend_women_prefixes()
Mens_priffix: dict[str, str] = _extend_men_prefixes()


__all__ = [
    "Mens_priffix",
    "Women_s_priffix",
    "Mens_suffix",
]
