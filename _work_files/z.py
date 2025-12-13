import json
from pathlib import Path


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


genders_keys: dict[str, str] = {
    "{en} blind": "{ar} مكفوفات",
    "{en} deaf": "{ar} صم",
    "{en} deafblind": "{ar} صم ومكفوفات",
    "{en} killed-in-action": "{ar} قتلن في عمليات قتالية",
    "{en} killed in action": "{ar} قتلن في عمليات قتالية",
    "{en} murdered abroad": "{ar} قتلن في الخارج",
}

formatted_data = {}

for x, v in genders_keys.items():
    # writers blind
    formatted_data.update(
        one_Keys_more(x, v, add_women=True)
    )
formatted_data2 = {}

genders_keys2: dict[str, str] = {
    "blind": "مكفوفات",
    "deaf": "صم",
    "deafblind": "صم ومكفوفات",
    "killed-in-action": "قتلن في عمليات قتالية",
    "killed in action": "قتلن في عمليات قتالية",
    "murdered abroad": "قتلن في الخارج",
}


for x, v in genders_keys2.items():
    # writers blind
    formatted_data2.update(
        one_Keys_more_2(x, v, add_women=True)
    )

with open(Path(__file__).parent / "data.json", "w", encoding="utf-8") as f:
    json.dump(formatted_data, f, ensure_ascii=False, indent=4)

with open(Path(__file__).parent / "data2.json", "w", encoding="utf-8") as f:
    json.dump(formatted_data2, f, ensure_ascii=False, indent=4)
