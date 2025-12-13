import json
from pathlib import Path


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

with open(Path(__file__).parent / "data.json", "w", encoding="utf-8") as f:
    json.dump(formatted_data, f, ensure_ascii=False, indent=4)
