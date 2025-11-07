"""Legacy helpers for resolving 2018 job categories."""

from __future__ import annotations

import re
from collections.abc import Mapping

from ....helps.print_bot import print_put
from ....ma_lists import All_Nat, Jobs_key_mens, Jobs_key_womens, Main_priffix, Main_priffix_to, Nat_men, Nat_women, People_key, change_male_to_female, en_is_nat_ar_is_man, en_is_nat_ar_is_women, priffix_lab_for_2018
from ..get_helps import get_con_3
from ..jobs_mainbot import jobs
from ..priffix_bot import Women_s_priffix_work, priffix_Mens_work
from ..utils import cached_lookup, log_debug, normalize_cache_key
from .langs_w import Lang_work
from .relegin_jobs import try_relegins_jobs

TEST4_2018_JOBS_CACHE: dict[str, str] = {}

__all__ = ["test4_2018_Jobs"]


def test4_2018_Jobs(
    cate: str,
    out: bool = False,
    tab: Mapping[str, str] | None = None,
) -> str:  # noqa: N802
    """Retrieve job-related information based on the specified category."""

    del out, tab

    normalized_category = re.sub(r"_", " ", cate)
    cache_key = normalize_cache_key(normalized_category)
    return cached_lookup(
        TEST4_2018_JOBS_CACHE,
        (cache_key,),
        lambda: _resolve_test4_2018_jobs(normalized_category),
    )


def _resolve_test4_2018_jobs(category: str) -> str:
    """Perform the heavy lifting for :func:`test4_2018_Jobs`."""

    log_debug("<<lightyellow>>>> test4_2018_Jobs >> cate:(%s) ", category)

    main_prefix, main_template, trimmed_category = _extract_main_prefix(category)

    lower_category = trimmed_category.lower()
    category_for_people = "أشخاص" if lower_category == "people" else ""
    if category_for_people:
        return _finalise_label(main_prefix, main_template, category_for_people, "", "")

    label = _direct_category_label(lower_category)
    nationality_key = ""
    nationality = ""
    job_example_label = ""
    job_example_template = ""

    if not label:
        nationality_key, nationality = get_con_3(lower_category, All_Nat, "nat")

    if nationality_key:
        job_example_label, main_template, job_example_template = _apply_priffix_lab(
            main_prefix,
            nationality_key,
            nationality,
            main_template,
        )
        if job_example_label:
            label = job_example_label

    if nationality_key and not label:
        label = jobs(
            lower_category,
            nationality,
            nationality_key,
            category_type="nat",
        )

    if not label:
        label = Women_s_priffix_work(lower_category) or priffix_Mens_work(lower_category)

    if not label:
        label = Lang_work(lower_category)

    if not label:
        label = try_relegins_jobs(lower_category)

    return _finalise_label(
        main_prefix,
        main_template,
        label,
        nationality,
        job_example_template,
    )


def _extract_main_prefix(category: str) -> tuple[str, str, str]:
    """Extract the main prefix and adjust category text accordingly."""

    original_lower = category.lower()
    main_prefix = ""
    main_template = ""

    for prefix, template in Main_priffix.items():
        token = f"{prefix} "
        if original_lower.startswith(token.lower()):
            main_prefix = prefix
            trimmed_category = category[len(token) :]
            main_template = _adjust_template_for_gender(template, trimmed_category)
            log_debug(
                '<<lightblue>> test4_2018_Jobs Main_priffix cate.startswith(me2: "%s") cate:"%s",Main_lab:"%s". ',
                token,
                trimmed_category,
                main_template,
            )
            return main_prefix, main_template, trimmed_category

    return "", "", category


def _adjust_template_for_gender(template: str, category: str) -> str:
    """Adjust the prefix template for female categories when needed."""

    if category.endswith("women") or category.endswith("women's"):
        return change_male_to_female.get(template, template)
    if template and category.strip().startswith("female") and "fictional" in template:
        print_put("{} خياليات")
        return "{} خياليات"
    return template


def _direct_category_label(category: str) -> str:
    """Attempt simple lookups before invoking expensive helpers."""

    return People_key.get(category, "") or Jobs_key_womens.get(category, "") or Jobs_key_mens.get(category, "")


def _apply_priffix_lab(
    main_prefix: str,
    key: str,
    nationality: str,
    current_template: str,
) -> tuple[str, str, str]:
    """Apply prefix specific label templates when available."""

    if not main_prefix or main_prefix not in priffix_lab_for_2018:
        return "", current_template, ""

    template_info = priffix_lab_for_2018[main_prefix]

    female_template = en_is_nat_ar_is_women.get(key.strip(), "")
    if female_template:
        label = female_template.format(Nat_women[nationality])
        log_debug('<<lightblue>> test_4, new contry_lab "%s" ', label)
        return label, template_info["women"], female_template

    male_template = en_is_nat_ar_is_man.get(key.strip(), "")
    if male_template:
        label = male_template.format(Nat_men[nationality])
        log_debug('<<lightblue>> test_4, new contry_lab "%s" ', label)
        return label, template_info["men"], male_template

    return "", current_template, ""


def _finalise_label(
    main_prefix: str,
    main_template: str,
    label: str,
    nationality: str,
    job_example_template: str,
) -> str:
    """Combine prefix templates with the resolved label."""

    if not label:
        return ""

    if main_prefix and main_template:
        label = main_template.format(label)
        if main_prefix in Main_priffix_to and job_example_template:
            stripped_label = job_example_template.format("").strip()
            label = Main_priffix_to[main_prefix].format(
                nat=Nat_women.get(nationality, ""),
                t=stripped_label,
            )

    log_debug('end test4_2018_Jobs "%s" , contry_lab:"%s"', main_prefix, label)
    return label
