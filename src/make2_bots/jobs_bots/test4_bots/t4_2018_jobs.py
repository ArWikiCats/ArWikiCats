#!/usr/bin/python3
"""

from .make2_bots.jobs_bots.test4_bots.t4_2018_jobs import test4_2018_Jobs

"""

import re

# ---
from ...ma_lists import (
    People_key,
    All_Nat,
    Nat_women,
    Nat_men,
    Jobs_key_mens,
    Jobs_key_womens,
)
from ...ma_lists import en_is_nat_ar_is_man, en_is_nat_ar_is_women, change_male_to_female, priffix_lab_for_2018, Main_priffix, Main_priffix_to

from ..get_helps import get_con_3

# ---
from ...helps.print_bot import output_test4, print_put
from ..priffix_bot import Women_s_priffix_work, priffix_Mens_work
from ..jobs_mainbot import Jobs  # , Jobs2

from .relegin_jobs import try_relegins_jobs
from .langs_w import Lang_work

test4_2018_Jobs_cash = {}


def test4_2018_Jobs(cate, out=False, tab=None):
    """Retrieve job-related information based on the specified category.

    This function processes the input category to determine the appropriate
    job-related label and returns it. It utilizes various mappings and
    conditions to derive the correct label based on prefixes, gender
    considerations, and other contextual information. The function also
    caches results for efficiency, avoiding redundant computations for
    previously queried categories.

    Args:
        cate (str): The category of jobs to retrieve information for.
        out (bool?): A flag to control output behavior. Defaults to False.
        tab (dict?): An optional dictionary for additional parameters. Defaults to None.

    Returns:
        str: The job-related label corresponding to the input category.
    """

    # ---
    if not tab:
        tab = {}
    # ---
    cate = re.sub(r"_", " ", cate)
    # ---
    cach_key = cate.lower().strip()
    # ---
    if cach_key in test4_2018_Jobs_cash:
        return test4_2018_Jobs_cash[cach_key]
    # ---
    output_test4(f"<<lightyellow>>>> test4_2018_Jobs >> cate:({cate}) ")
    # ---

    # ---
    cate2_no_lower = cate.lower()
    cate2 = cate.lower()
    # ---
    Main_Ss = ""
    Main_lab = ""
    # ---
    for me, melab in Main_priffix.items():
        me2 = f"{me} "
        if cate.lower().startswith(me2.lower()):
            Main_Ss = me
            cate = cate2_no_lower[len(me2):]
            # ---
            Main_lab = melab
            if cate.endswith("women") or cate.endswith("women's"):
                if Main_lab in change_male_to_female:
                    Main_lab = change_male_to_female[Main_lab]
            # ---
            output_test4(f'<<lightblue>> test4_2018_Jobs Main_priffix cate.startswith(me2: "{me2}") cate:"{cate}",Main_lab:"{Main_lab}". ')
    # ---
    cate2_no_lower = cate
    cate = cate.lower()
    # ---
    if cate != cate2:
        output_test4(f'<<lightblue>> test4_2018_Jobs cate:"{cate}",cate2:"{cate2}",Main_Ss:"{Main_Ss}". ')
    contry_lab = "أشخاص" if cate == "people" else ""
    # ---
    if Main_Ss.strip() == "fictional" and cate.strip().startswith("female"):
        Main_lab = "{} خياليات"
        print_put("{} خياليات")
    # ---
    if not contry_lab:
        contry_lab = People_key.get(cate, "")
    if not contry_lab:
        contry_lab = Jobs_key_womens.get(cate, "")
    # ---
    if not contry_lab:
        contry_lab = Lang_work(cate)
    # ---
    if not contry_lab:
        contry_lab = Jobs_key_mens.get(cate, "")
    # ---
    nat = ""
    job_example = ""
    # ---
    if not contry_lab:
        job_example, nat = get_con_3(cate, All_Nat, "nat")
    # ---
    job_example_lab = ""
    # ---
    # priffix_lab_for_2018
    if job_example and (Main_Ss in priffix_lab_for_2018) and contry_lab == "":
        # ---
        # en_is_nat_ar_is_women
        job_example_lab = en_is_nat_ar_is_women.get(job_example.strip(), "")
        if job_example_lab:
            contry_lab = job_example_lab.format(Nat_women[nat])
            output_test4(f'<<lightblue>> test_4, new contry_lab "{contry_lab}" ')
            Main_lab = priffix_lab_for_2018[Main_Ss]["women"]
        # ---
        # en_is_nat_ar_is_man
        if not contry_lab:
            job_example_lab = en_is_nat_ar_is_man.get(job_example.strip(), "")
            if job_example_lab:
                contry_lab = job_example_lab.format(Nat_men[nat])
                output_test4(f'<<lightblue>> test_4, new contry_lab "{contry_lab}" ')
                Main_lab = priffix_lab_for_2018[Main_Ss]["men"]
    # ---
    if job_example and contry_lab == "":
        contry_lab = Jobs(cate, nat, job_example, Type="nat")
    # ---
    if not contry_lab:
        contry_lab = Women_s_priffix_work(cate)
    # ---
    if not contry_lab:
        contry_lab = priffix_Mens_work(cate)
    # ---
    # Try with Jobs
    # ---
    if Main_Ss and Main_lab and contry_lab:
        contry_lab = Main_lab.format(contry_lab)
        # ---
        if Main_Ss in Main_priffix_to and job_example_lab:
            job_example_lab = job_example_lab.format("").strip()
            contry_lab = Main_priffix_to[Main_Ss].format(nat=Nat_women[nat], t=job_example_lab)
    # ---
    if not contry_lab:
        contry_lab = try_relegins_jobs(cate)
    # ---
    output_test4(f'end test4_2018_Jobs "{cate}" , contry_lab:"{contry_lab}", cate2:{cate2}')
    # ---
    test4_2018_Jobs_cash[cach_key] = contry_lab
    # ---
    return contry_lab
