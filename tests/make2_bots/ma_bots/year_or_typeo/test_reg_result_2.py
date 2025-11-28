"""
Tests
"""

from typing import Sequence

import pytest
from _pytest.mark.structures import ParameterSet

from ArWikiCats.make_bots.ma_bots.year_or_typeo.reg_result import (
    category_relation_mapping,
    get_reg_result,
)

# -----------------------------------------------------------
# 10) Stress-test with all category_relation_mapping keys
# -----------------------------------------------------------

# new dict with only 20 items from category_relation_mapping
category_relation_mapping_20 = {k: category_relation_mapping[k] for k in list(category_relation_mapping.keys())[:20]}


@pytest.mark.parametrize("eng", list(category_relation_mapping_20.keys()))
@pytest.mark.dict
def test_in(eng: ParameterSet | Sequence[object] | object):
    # [Category:2025 in Canada]: Typies(year_at_first='2025 ', typeo='', In='in ', country='canada', cat_test='in canada')
    # [Category:2025 by Canada]: Typies(year_at_first='2025 ', typeo='', In='by ', country='by canada', cat_test='by canada'
    category = f"Category:2025 {eng} Canada"
    out = get_reg_result(category)
    # typeo = out.typeo
    In = out.In.lower().strip()
    country = out.country.lower()
    country_expected = "by canada" if In.strip() == "by" else "canada"
    assert out.year_at_first == "2025 ", f"[{category}]: {str(out)}"
    # assert typeo == "", f"[{category}]: {str(out)}"
    # assert In == eng.lower().strip(), f"[{category}]: {str(out)}"

    assert country == country_expected, f"[{category}]: {str(out)}"
