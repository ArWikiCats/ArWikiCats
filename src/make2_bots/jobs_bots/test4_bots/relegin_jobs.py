"""Religious category helpers for job labels."""

from __future__ import annotations

from ....ma_lists import religious_keys_PP
from ..get_helps import get_con_3
from ..jobs_mainbot import jobs
from ..utils import cached_lookup, log_debug, normalize_cache_key

RELIGION_CACHE: dict[str, str] = {}

__all__ = ["try_relegins_jobs"]


def try_relegins_jobs(cate: str) -> str:  # noqa: N802
    """Attempt to resolve religious job categories using nationality helpers."""

    cache_key = normalize_cache_key(cate, "religion")
    return cached_lookup(
        RELIGION_CACHE,
        (cache_key,),
        lambda: _resolve_religion_job(cate),
    )


def _resolve_religion_job(cate: str) -> str:
    """Resolve a religious job label without referencing caches."""

    log_debug("\t xx start: <<lightred>>try_relegins_jobs >> <<lightpurple>> cate:%s", cate)

    job_example, nat = get_con_3(cate, religious_keys_PP.keys(), "religions")
    if not job_example:
        log_debug("\t xx end: <<lightred>>try_relegins_jobs <<lightpurple>> cate:%s, contry_lab:%s ", cate, "")
        return ""

    tab = religious_keys_PP.get(nat, {})
    label = jobs(cate, nat, job_example, category_type="rel", overrides=tab)
    log_debug("\t xx end: <<lightred>>try_relegins_jobs <<lightpurple>> cate:%s, contry_lab:%s ", cate, label)
    return label
