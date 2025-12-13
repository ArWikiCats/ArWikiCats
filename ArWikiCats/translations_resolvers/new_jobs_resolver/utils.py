

def one_Keys_more_2(x, v, add_women=False) -> dict[str, str]:
    data = {}
    # writers blind
    data[f"{{en_job}} {x}"] = f"{{ar_job}} {v}"

    # greek blind
    data[f"{{en_nat}} {x}"] = f"{{ar_nat}} {v}"

    # greek writers blind
    data[f"{{en_nat}} {{en_job}} {x}"] = f"{{ar_job}} {{ar_nat}} {v}"

    # writers greek blind
    data[f"{{en_job}} {{en_nat}} {x}"] = f"{{ar_job}} {{ar_nat}} {v}"

    if add_women:
        # female greek blind
        data[f"{{women}} {{en_nat}} {x}"] = f"{{ar_nat}} {v}"

        # female writers blind
        data[f"{{women}} {{en_job}} {x}"] = f"{{ar_job}} {v}"
        # female greek writers blind
        data[f"{{women}} {{en_nat}} {{en_job}} {x}"] = f"{{ar_job}} {{ar_nat}} {v}"

        # writers female greek blind
        data[f"{{en_job}} {{women}} {{en_nat}} {x}"] = f"{{ar_job}} {{ar_nat}} {v}"

        # female writers greek blind
        data[f"{{women}} {{en_job}} {{en_nat}} {x}"] = f"{{ar_job}} {{ar_nat}} {v}"

    return data


def nat_and_gender_keys(nat_job_key, key, gender_key, gender_label) -> dict[str, str]:
    data = {}

    # "Yemeni male muslims": "تصنيف:يمنيون مسلمون ذكور"
    # "Yemeni women's muslims": "تصنيف:يمنيات مسلمات"
    data[f"{nat_job_key} {gender_key} {key}"] = gender_label

    # "Yemeni muslims male": "تصنيف:يمنيون مسلمون ذكور"
    data[f"{nat_job_key} {key} {gender_key}"] = gender_label

    # "male Yemeni muslims": "تصنيف:يمنيون مسلمون ذكور"
    # "women's Yemeni muslims": "تصنيف:يمنيات مسلمات"
    data[f"{gender_key} {nat_job_key} {key}"] = gender_label

    return data


def filter_and_replace_gender_terms(formatted_data) -> dict:

    formatted_data_final = {x: v for x, v in formatted_data.items() if "{women}" not in x}

    # handle womens keys
    formatted_data_women = {x: v for x, v in formatted_data.items() if "{women}" in x}

    for x, v in formatted_data_women.items():
        formatted_data_final[x.replace("{women}", "women")] = v
        formatted_data_final[x.replace("{women}", "womens")] = v
        formatted_data_final[x.replace("{women}", "female")] = v

    return formatted_data_final


__all__ = [
    "nat_and_gender_keys",
    "filter_and_replace_gender_terms",
]
