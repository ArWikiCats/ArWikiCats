

def one_Keys_more(x, v, add_women=False) -> dict[str, str]:
    data = {}
    # writers blind
    data[x.format(en="{en_job}")] = v.format(ar="{ar_job}")

    # greek blind
    data[x.format(en="{en_nat}")] = v.format(ar="{ar_nat}")

    # greek writers blind
    data[x.format(en="{en_nat} {en_job}")] = v.format(ar="{ar_job} {ar_nat}")

    # writers greek blind
    data[x.format(en="{en_job} {en_nat}")] = v.format(ar="{ar_job} {ar_nat}")

    if add_women:
        # female greek blind
        data[x.format(en="{women} {en_nat}")] = v.format(ar="{ar_nat}")

        # female writers blind
        data[x.format(en="{women} {en_job}")] = v.format(ar="{ar_job}")
        # female greek writers blind
        data[x.format(en="{women} {en_nat} {en_job}")] = v.format(ar="{ar_job} {ar_nat}")

        # writers female greek blind
        data[x.format(en="{en_job} {women} {en_nat}")] = v.format(ar="{ar_job} {ar_nat}")

        # female writers greek blind
        data[x.format(en="{women} {en_job} {en_nat}")] = v.format(ar="{ar_job} {ar_nat}")

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
    "one_Keys_more",
    "nat_and_gender_keys",
    "filter_and_replace_gender_terms",
]
