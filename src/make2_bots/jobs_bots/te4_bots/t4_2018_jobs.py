#!/usr/bin/python3
"""
!
"""

import functools

from ....translations import (
    People_key,
    Nat_women,
    Nat_men,
    jobs_mens_data,
    short_womens_jobs,
    en_is_nat_ar_is_man,
    en_is_nat_ar_is_women,
    change_male_to_female,
    priffix_lab_for_2018,
    Main_priffix,
    Main_priffix_to,
)
from .relegin_jobs import try_relegins_jobs_with_suffix
from .langs_w import Lang_work

from ..get_helps import get_con_3
from ..priffix_bot import Women_s_priffix_work, priffix_Mens_work
from ..jobs_mainbot import jobs_with_nat_prefix
from ....helps.log import logger


@functools.lru_cache(maxsize=None)
def te4_2018_Jobs(cate: str) -> str:
    """Retrieve job-related information based on the specified category.

    This function processes the input category to determine the appropriate
    job-related label and returns it. It utilizes various mappings and
    conditions to derive the correct label based on prefixes, gender
    considerations, and other contextual information. The function also
    caches results for efficiency, avoiding redundant computations for
    previously queried categories.

    Args:
        cate (str): The category of jobs to retrieve information for.

    Returns:
        str: The job-related label corresponding to the input category.
    """
    cate = cate.replace("_", " ")
    logger.debug(f"<<lightyellow>>>> te4_2018_Jobs >> cate:({cate}) ")
    cate2_no_lower = cate.lower()
    cate2 = cate.lower()
    Main_Ss = ""
    Main_lab = ""
    for me, melab in Main_priffix.items():
        me2 = f"{me} "
        if cate.lower().startswith(me2.lower()):
            Main_Ss = me
            cate = cate2_no_lower[len(me2):]
            Main_lab = melab
            if cate.endswith("women") or cate.endswith("women's"):
                if Main_lab in change_male_to_female:
                    Main_lab = change_male_to_female[Main_lab]
            logger.debug(f'<<lightblue>> te4_2018_Jobs Main_priffix cate.startswith(me2: "{me2}") cate:"{cate}",Main_lab:"{Main_lab}". ')
    cate2_no_lower = cate
    cate = cate.lower()
    if cate != cate2:
        logger.debug(f'<<lightblue>> te4_2018_Jobs cate:"{cate}",cate2:"{cate2}",Main_Ss:"{Main_Ss}". ')
    country_lab = "أشخاص" if cate == "people" else ""
    if Main_Ss.strip() == "fictional" and cate.strip().startswith("female"):
        Main_lab = "{} خياليات"
        logger.info("{} خياليات")
    if not country_lab:
        country_lab = People_key.get(cate, "")
    if not country_lab:
        country_lab = short_womens_jobs.get(cate, "")
    if not country_lab:
        country_lab = Lang_work(cate)
    if not country_lab:
        country_lab = jobs_mens_data.get(cate, "")
    country_prefix = ""
    category_suffix = ""
    if not country_lab:
        category_suffix, country_prefix = get_con_3(cate, "nat")
    job_example_lab = ""
    # priffix_lab_for_2018
    if category_suffix and (Main_Ss in priffix_lab_for_2018) and country_lab == "":
        # en_is_nat_ar_is_women
        job_example_lab = en_is_nat_ar_is_women.get(category_suffix.strip(), "")
        if job_example_lab:
            country_lab = job_example_lab.format(Nat_women[country_prefix])
            logger.debug(f'<<lightblue>> bot_te_4, new country_lab "{country_lab}" ')
            Main_lab = priffix_lab_for_2018[Main_Ss]["women"]
        # en_is_nat_ar_is_man
        if not country_lab:
            job_example_lab = en_is_nat_ar_is_man.get(category_suffix.strip(), "")
            if job_example_lab:
                country_lab = job_example_lab.format(Nat_men[country_prefix])
                logger.debug(f'<<lightblue>> bot_te_4, new country_lab "{country_lab}" ')
                Main_lab = priffix_lab_for_2018[Main_Ss]["men"]
    if category_suffix and country_lab == "":
        country_lab = jobs_with_nat_prefix(cate, country_prefix, category_suffix)
    if not country_lab:
        country_lab = Women_s_priffix_work(cate) or priffix_Mens_work(cate)
    # Try with jobs_with_nat_prefix
    if Main_Ss and Main_lab and country_lab:
        country_lab = Main_lab.format(country_lab)
        if Main_Ss in Main_priffix_to and job_example_lab:
            job_example_lab = job_example_lab.format("").strip()
            country_lab = Main_priffix_to[Main_Ss].format(nat=Nat_women[country_prefix], t=job_example_lab)
    if not country_lab:
        country_lab = try_relegins_jobs_with_suffix(cate)
    logger.debug(f'end te4_2018_Jobs "{cate}" , country_lab:"{country_lab}", cate2:{cate2}')
    return country_lab
