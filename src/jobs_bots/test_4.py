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
import sys

# ---
from ..ma_lists_bots import (
    Multi_sport_for_Jobs,
    All_Nat,
    Nat_mens,
    Jobs_key_mens,
    Jobs_key_womens,
)

from ..media_bots.film_keys_bot import Films
from ..jobs_bots.get_helps import get_con_3

# ---
from ..o_bots import ethnic_bot
from ..helps.print_bot import output_test4, print_put
from ..jobs_bots.priffix_bot import Women_s_priffix_work, priffix_Mens_work

from .test4_bots.for_me import Work_for_me

# from .test4_bots.relegin_jobs import try_relegins_jobs
from .test4_bots.t4_2018_jobs import test4_2018_Jobs

Jobs_in_Multi_Sports_cash = {}
test4_2018_with_nat_cash = {}


def nat_match(cate, out=False, fa="", tab=None):
    """Match a category string to a localized sentiment label.

    This function takes a category string, processes it to identify if it
    matches any predefined sentiment patterns, and returns the corresponding
    localized sentiment label. It uses regular expressions to match patterns
    and replaces parts of the category string to generate the output label.
    If no match is found, an empty string is returned.

    Args:
        cate (str): The category string to be matched.
        out (bool?): A flag to control output behavior. Defaults to False.
        fa (str?): An additional parameter for future use. Defaults to an empty string.
        tab (dict?): A dictionary for additional context. Defaults to None.

    Returns:
        str: The localized sentiment label corresponding to the input category,
            or an empty string if no match is found.
    """

    # ---
    if not tab:
        tab = {}
    # ---
    cate2 = cate.lower().replace("category:", "")
    contry = ""
    mat_m = ""
    # ---
    output_test4(f'<<lightblue>> test_4: nat_match cate2 :: "{cate2}" ')
    # ---
    matchs = {
        r"^anti\-(\w+) sentiment$": "مشاعر معادية لل%s",
        # r"^anti\-(\w+) sentiment$": "مشاعر معادية لل%s",
        # r"^anti\-(\w+) sentiment$": "مشاعر معادية لل%s",
    }
    # ---
    for mat, matl in matchs.items():
        if re.match(mat, cate2):
            contry = re.sub(mat, r"\g<1>", cate2)
            mat_m = matl
    # ---
    """
    cate3 = cate2
    if mat_m == "" and cate3.endswith(" sentiment") :
        cate3 = cate3[:-len(" sentiment")]
        if cate2.startswith("anti-") or cate2.startswith("anti-") :
            cate3 = cate2[5:]
    output_test4('<<lightblue>> test_4: nat_match cate3 :: "%s" ' % cate3)
    """
    # ---
    if contry:
        output_test4(f'<<lightblue>> test_4: nat_match contry :: "{contry}" ')
    # ---
    contry_L = Nat_mens.get(contry, "")
    contry_lab = mat_m % contry_L if mat_m and contry_L else ""
    # ---
    if contry_lab:
        output_test4(f'<<lightblue>> test_4: nat_match contry_lab :: "{contry_lab}" ')
    # ---
    return contry_lab


def test4_2018_with_nat(cate, out=False, fa="", tab=None):
    # ---
    if not tab:
        tab = {}
    # ---
    if cate in test4_2018_with_nat_cash:
        return test4_2018_with_nat_cash[cate]
    # ---

    # ---
    output_test4(f"<<lightyellow>>>> test4_2018_with_nat >> cate:({cate}), fa:{fa}..")
    contry_lab = ""
    # ---
    # output_test4('test4_2018_with_nat "%s"' % cate)
    # ---
    cate = re.sub(r"_", " ", cate.lower())
    cate = re.sub(r"-", " ", cate)
    # ---
    if not contry_lab:
        contry_lab = Jobs_key_womens.get(cate, "")
    # ---
    if not contry_lab:
        contry_lab = Jobs_key_mens.get(cate, "")
    # ---
    con_3, nat = get_con_3(cate, All_Nat, "nat")
    # ---
    if con_3:
        # ---
        if not contry_lab:
            contry_lab = Work_for_me(cate, nat, con_3)
        # ---
        if not contry_lab:
            contry_lab = Films(cate, nat, con_3, fa=fa)
        # ---
        if not contry_lab:
            contry_lab = ethnic_bot.Ethnic(cate, nat, con_3)
        # ---
        if not contry_lab:
            contry_lab = nat_match(cate, nat, con_3)
    # ---
    if not contry_lab:
        contry_lab = priffix_Mens_work(cate)
    # ---
    if not contry_lab:
        contry_lab = Women_s_priffix_work(cate)
    # ---
    if contry_lab == "" and con_3 == "":
        contry_lab = Films(cate, "", "", fa=fa)
    # ---
    if contry_lab:
        if con_3:
            contry2 = ""
            output_test4(f'<<lightblue>> test4_2018_with_nat startswith({contry2}),con_3:"{con_3}"')
        output_test4(f'<<lightblue>> test_4: test4_2018_with_nat :: "{contry_lab}" ')
    # ---
    # Try with Jobs
    # ---
    test4_2018_with_nat_cash[cate] = contry_lab
    # ---
    return contry_lab


def Jobs_in_Multi_Sports(cate, out=False, tab=None):
    """Retrieve job information related to multiple sports based on the
    category.

    This function checks if the provided category exists in a cached
    dictionary of job information. If the category is not found, it
    processes the category to determine the relevant job and game labels.
    The function formats the output to provide a meaningful representation
    of the job in relation to the sport.

    Args:
        cate (str): The category string representing the sport or job type.
        out (bool?): A flag to control output behavior. Defaults to False.
        tab (dict?): A dictionary for additional parameters. Defaults to None.

    Returns:
        str: A formatted string representing the job information related to the
            specified category.
    """

    # ---
    if not tab:
        tab = {}
    # ---
    if cate in Jobs_in_Multi_Sports_cash:
        return Jobs_in_Multi_Sports_cash[cate]
    # ---
    # python3 core8/pwb.py make/test_4 Asian_Games_wrestlers
    # ---
    output_test4(f"<<lightyellow>>>> Jobs_in_Multi_Sports >> cate:({cate}) ")
    # ---
    Main_lab = ""
    # ---
    cate = re.sub(r"_", " ", cate)
    # ---
    # cate2_no_lower = cate
    cate2 = cate.lower()
    # ---
    job = ""
    job_lab = ""
    game_lab = ""
    for ga, game_lab in Multi_sport_for_Jobs.items():
        # ---
        game = f"{ga} "
        if cate.startswith(game):
            job = cate2[len(game):]
            output_test4(f'Jobs_in_Multi_Sports cate.startswith(game: "{game}") game_lab:"{game_lab}",job:"{job}". ')
            break
    # ---
    if not job_lab and job:
        job_lab = test4_2018_Jobs(job)
        # job_lab = Jobs_key_womens.get(job , "")
    # ---
    if job and game_lab and job_lab:
        Main_lab = f"{job_lab} في {game_lab}"
    # ---
    output_test4(f'end Jobs_in_Multi_Sports "{cate}" , Main_lab:"{Main_lab}"')
    # ---
    Jobs_in_Multi_Sports_cash[cate] = Main_lab
    # ---
    return Main_lab


def main():
    # ase = try_relegins_jobs("hindu apologists")
    # print_put(f"ase:{ase}")
    # ---
    # python3 core8/pwb.py make/bots/test_4 Afghan_men's_football_players testprint
    # ---
    if sys.argv and sys.argv[1]:
        La = sys.argv[1].lower()
        La = re.sub(r"_", " ", La)
        La = re.sub(r"Category:", "", La)
        so = test4_2018_Jobs(La, out=True)
        # ss = nat_match(La, out = True)
        # so = test4_2018_Jobs(La, out=True)
        # so = priffix_Mens_work(La)
        print_put(f"Lab: {La}")
        print_put(f"so :{so}")
        # print_put("yemeni :" +  Nat_mens.get("yemeni","")   )
        # print_put("so :" + so   )


if __name__ == "__main__":
    main()
