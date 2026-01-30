import logging
import re

logger = logging.getLogger(__name__)

REGEX_WOMENS = re.compile(r"\b(womens|women)\b", re.I)
REGEX_THE = re.compile(r"\b(the)\b", re.I)


def fix_keys(category: str) -> str:
    original_category = category
    category = category.replace("'", "").lower()
    category = REGEX_THE.sub("", category)
    category = re.sub(r"\s+", " ", category)

    replacements = {
        "expatriates": "expatriate",
        "canadian football": "canadian-football",
    }

    for old, new in replacements.items():
        category = category.replace(old, new)

    category = REGEX_WOMENS.sub("female", category)
    logger.debug(f"fix_keys: {original_category} -> {category}")
    return category.strip()


def one_Keys_more_2(
    x,
    v,
    ar_nat_key="{ar_nat}",
    en_nat_key="{en_nat}",
    ar_job_key="{ar_job}",
    en_job_key="{en_job}",
    women_key="{women}",
    add_women=False,
) -> dict[str, str]:
    data = {}

    if not add_women:
        # Executed police officers / deaf triathletes
        data[f"{x} {en_job_key}"] = f"{ar_job_key} {v}"

        # writers blind
        data[f"{en_job_key} {x}"] = f"{ar_job_key} {v}"

        # greek blind
        data[f"{en_nat_key} {x}"] = f"{ar_nat_key} {v}"

        # Executed Albanian
        data[f"{x} {en_nat_key}"] = f"{ar_nat_key} {v}"

        # Executed Albanian police officers
        data[f"{x} {en_nat_key} {en_job_key}"] = f"{ar_job_key} {ar_nat_key} {v}"

        # greek writers blind
        data[f"{en_nat_key} {en_job_key} {x}"] = f"{ar_job_key} {ar_nat_key} {v}"

        # writers greek blind
        data[f"{en_job_key} {en_nat_key} {x}"] = f"{ar_job_key} {ar_nat_key} {v}"

        # Dutch political artists
        data[f"{en_nat_key} {x} {en_job_key}"] = f"{ar_job_key} {ar_nat_key} {v}"
    if add_women:
        # Executed Albanian women
        data[f"{x} {en_nat_key} {women_key}"] = f"{ar_nat_key} {v}"

        # female greek blind
        data[f"{women_key} {en_nat_key} {x}"] = f"{ar_nat_key} {v}"

        # female writers blind
        data[f"{women_key} {en_job_key} {x}"] = f"{ar_job_key} {v}"

        # Mauritanian female writers abolitionists
        data[f"{en_nat_key} {women_key} {en_job_key} {x}"] = f"{ar_job_key} {ar_nat_key} {v}"

        # female greek writers blind
        data[f"{women_key} {en_nat_key} {en_job_key} {x}"] = f"{ar_job_key} {ar_nat_key} {v}"

        # writers female greek blind
        data[f"{en_job_key} {women_key} {en_nat_key} {x}"] = f"{ar_job_key} {ar_nat_key} {v}"
        # female writers greek blind
        data[f"{women_key} {en_job_key} {en_nat_key} {x}"] = f"{ar_job_key} {ar_nat_key} {v}"

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


__all__ = [
    "nat_and_gender_keys",
]
