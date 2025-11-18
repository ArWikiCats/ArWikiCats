#!/usr/bin/python3
r"""
# ---
^(\s+),(".*?"\s*)$
$1$2,
# ---
,("[^\[\]]+"\s*)(\s*#[^\[\]]+|)$
,\s*("[^\[\]]+"\s*)(\s*#[^\[\]]+|)$

$1,$2

# ---
^(\s+#*\s*),(\s*".*?")(\s*#.*?|)$
$1$2,$3

# ---
(['"])\s+?$
$1
# ---
"""

import re
import functools

# ---
from ...translations import (
    Multi_sport_for_Jobs,
    Nat_mens,
    jobs_mens_data,
    short_womens_jobs,
)

from ..media_bots.film_keys_bot import Films
from .get_helps import get_con_3

# ---
from ..o_bots import ethnic_bot
from ...helps.print_bot import output_test4
from .priffix_bot import Women_s_priffix_work, priffix_Mens_work

from .te4_bots.for_me import Work_for_me

from .te4_bots.t4_2018_jobs import te4_2018_Jobs


def nat_match(
    category: str,
) -> str:
    """Match a category string to a localized sentiment label.

    This function takes a category string, processes it to identify if it
    matches any predefined sentiment patterns, and returns the corresponding
    localized sentiment label. It uses regular expressions to match patterns
    and replaces parts of the category string to generate the output label.
    If no match is found, an empty string is returned.

    Args:
        category (str): The category string to be matched.
        out (bool?): A flag to control output behavior. Defaults to False.
        reference_category (str?): An additional parameter for future use. Defaults to an empty string.

    Returns:
        str: The localized sentiment label corresponding to the input category,
            or an empty string if no match is found.
    """

    # ---
    category_lower = category.lower().replace("category:", "")
    matched_country_key = ""
    country_label_template = ""
    # ---
    output_test4(f'<<lightblue>> bot_te_4: nat_match normalized_category :: "{category_lower}" ')
    # ---
    country_templates = {
        r"^anti\-(\w+) sentiment$": "مشاعر معادية لل%s",
        # r"^anti\-(\w+) sentiment$": "مشاعر معادية لل%s",
        # r"^anti\-(\w+) sentiment$": "مشاعر معادية لل%s",
    }
    # ---
    for pattern, template in country_templates.items():
        if re.match(pattern, category_lower):
            matched_country_key = re.sub(pattern, r"\g<1>", category_lower)
            country_label_template = template
    # ---
    """
    sentiment_category = category_lower
    if not country_label_template and sentiment_category.endswith(" sentiment"):
        sentiment_category = sentiment_category[: -len(" sentiment")]
        if category_lower.startswith("anti-"):
            sentiment_category = category_lower[5:]
    output_test4(
        '<<lightblue>> bot_te_4: nat_match sentiment_category :: "%s" ' % sentiment_category
    )
    """
    # ---
    if matched_country_key:
        output_test4(
            f'<<lightblue>> bot_te_4: nat_match country_key :: "{matched_country_key}" '
        )
    # ---
    country_label_key = Nat_mens.get(matched_country_key, "")
    country_label = (
        country_label_template % country_label_key
        if country_label_template and country_label_key
        else ""
    )
    # ---
    if country_label:
        output_test4(f'<<lightblue>> bot_te_4: nat_match country_label :: "{country_label}" ')
    # ---
    return country_label


@functools.lru_cache(maxsize=None)
def te_2018_with_nat(
    category: str,
    reference_category: str="",
) -> str:
    # ---

    # ---
    output_test4(
        f"<<lightyellow>>>> te_2018_with_nat >> category:({category}), reference_category:{reference_category}.."
    )
    country_label = ""
    # ---
    # output_test4('te_2018_with_nat "%s"' % category)
    # ---
    normalized_category = category.lower().replace("_", " ").replace("-", " ")

    # ---
    if not country_label:
        country_label = short_womens_jobs.get(normalized_category, "")
    # ---
    if not country_label:
        country_label = jobs_mens_data.get(normalized_category, "")
    # ---
    con_3, nat = get_con_3(normalized_category, "nat")
    # ---
    if con_3:
        # ---
        if not country_label:
            country_label = Work_for_me(normalized_category, nat, con_3)
        # ---
        if not country_label:
            country_label = Films(
                normalized_category, nat, con_3, reference_category=reference_category
            )
        # ---
        if not country_label:
            country_label = ethnic_bot.ethnic(normalized_category, nat, con_3)
        # ---
        if not country_label:
            country_label = nat_match(normalized_category)
    # ---
    if not country_label:
        country_label = priffix_Mens_work(normalized_category)
    # ---
    if not country_label:
        country_label = Women_s_priffix_work(normalized_category)
    # ---
    if country_label == "" and con_3 == "":
        country_label = Films(
            normalized_category, "", "", reference_category=reference_category
        )
    # ---
    if country_label:
        if con_3:
            country2 = ""
            output_test4(f'<<lightblue>> te_2018_with_nat startswith({country2}),con_3:"{con_3}"')
        output_test4(f'<<lightblue>> bot_te_4: te_2018_with_nat :: "{country_label}" ')
    # ---
    # Try with Jobs
    # ---
    return country_label


@functools.lru_cache(maxsize=None)
def Jobs_in_Multi_Sports(
    category: str,
) -> str:
    """Retrieve job information related to multiple sports based on the
    category.

    This function processes the category to determine the relevant job and game labels.
    The function formats the output to provide a meaningful representation
    of the job in relation to the sport.

    Args:
        category (str): The category string representing the sport or job type.

    Returns:
        str: A formatted string representing the job information related to the
            specified category.
    """

    # ---
    # python3 core8/pwb.py make/bot_te_4 Asian_Games_wrestlers
    # ---
    output_test4(f"<<lightyellow>>>> Jobs_in_Multi_Sports >> category:({category}) ")
    # ---
    primary_label = ""
    # ---
    category = category.replace("_", " ")

    # ---
    # cate2_no_lower = cate
    category_lower = category.lower()
    # ---
    job_key = ""
    job_label = ""
    game_label = ""
    for sport_prefix, game_label in Multi_sport_for_Jobs.items():
        # ---
        game_prefix = f"{sport_prefix} "
        if category.startswith(game_prefix):
            job_key = category_lower[len(game_prefix) :]
            output_test4(
                f'Jobs_in_Multi_Sports category.startswith(game_prefix: "{game_prefix}") '
                f'game_label:"{game_label}",job:"{job_key}". '
            )
            break
    # ---
    if not job_label and job_key:
        job_label = te4_2018_Jobs(job_key)
        # job_lab = short_womens_jobs.get(job , "")
    # ---
    if job_key and game_label and job_label:
        primary_label = f"{job_label} في {game_label}"
    # ---
    output_test4(f'end Jobs_in_Multi_Sports "{category}" , primary_label:"{primary_label}"')
    # ---
    return primary_label
