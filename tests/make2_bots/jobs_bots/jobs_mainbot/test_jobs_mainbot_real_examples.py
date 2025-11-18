import os
import pytest
import jsonlines


from src.make2_bots.jobs_bots.jobs_mainbot import jobs_with_nat_prefix


def load_examples():
    """
    Load all real production examples from jobs_mainbot.jsonl
    and return them as a list of dicts.
    """

    # IMPORTANT:
    # Adjust path relative to repository structure
    root = os.path.dirname(__file__)
    path = os.path.join(root, "jobs_mainbot.jsonl")

    if not os.path.exists(path):
        raise FileNotFoundError(f"jobs_mainbot.jsonl not found at: {path}")

    examples = []
    with jsonlines.open(path) as reader:
        for item in reader.iter(skip_empty=True):
            examples.append(item)
    return examples


EXAMPLES = load_examples()


# -------------------------------------------------------
#  MAIN TEST — one test per real example
# -------------------------------------------------------
@pytest.mark.parametrize(
    "item",
    EXAMPLES,
    ids=[x.get("cate") for x in EXAMPLES]
)
def test_jobs_real_examples(item):
    """
    Validate jobs_with_nat_prefix() results using REAL data proven correct in production.

    Each JSON line example includes:
       cate
       country_prefix
       category_suffix
       mens
       womens
       country_lab   <-- expected output

    This ensures regression safety for any future refactoring.
    """

    cate = item.get("cate", "")
    start = item.get("country_prefix", "")
    con_3 = item.get("category_suffix", "")
    mens = item.get("mens", "")
    womens = item.get("womens", "")
    expected = item.get("country_lab", "")

    # Ensure clean cache per test
    jobs_with_nat_prefix.cache_clear()

    result = jobs_with_nat_prefix(cate, start, con_3, mens=mens, womens=womens)

    assert result == expected, (
        "\n\n"
        "------------------ FAILED CASE ------------------\n"
        f"Input cate:            {cate}\n"
        f"Input Start(country):  {start}\n"
        f"Input con_3:           {con_3}\n"
        f"Input mens override:   {mens}\n"
        f"Input womens override: {womens}\n"
        "-------------------------------------------------\n"
        f"Expected Output:\n{expected}\n\n"
        f"Actual Output:\n{result}\n"
        "-------------------------------------------------\n"
    )
