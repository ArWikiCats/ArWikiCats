"""
Tests
"""
from typing import Sequence
from _pytest.mark.structures import ParameterSet
import pytest

from src.make2_bots.ma_bots.dodo_bots.reg_result import get_reg_result
from src.make2_bots.ma_bots.dodo_bots.reg_result import Tit_ose_Nmaes

# -----------------------------------------------------------
# 10) Stress-test with all Tit_ose_Nmaes keys
# -----------------------------------------------------------

# new dict with only 20 items from Tit_ose_Nmaes
Tit_ose_Nmaes_20 = {k: Tit_ose_Nmaes[k] for k in list(Tit_ose_Nmaes.keys())[:20]}


@pytest.mark.parametrize("eng", list(Tit_ose_Nmaes_20.keys()))
def test_in(eng: ParameterSet | Sequence[object] | object):
    # [Category:2025 in Canada]: Typies(year_at_first='2025 ', typeo='', In='in ', country='canada', cat_test='in canada')
    # [Category:2025 by Canada]: Typies(year_at_first='2025 ', typeo='', In='by ', country='by canada', cat_test='by canada'
    # ---
    category = f"Category:2025 {eng} Canada"
    # ---
    out = get_reg_result(category)
    # ---
    # typeo = out.typeo
    In = out.In.lower().strip()
    country = out.country.lower()
    # ---
    country_expected = "by canada" if In.strip() == "by" else "canada"
    # ---
    assert out.year_at_first == '2025 ', f"[{category}]: {str(out)}"
    # assert typeo == "", f"[{category}]: {str(out)}"
    # assert In == eng.lower().strip(), f"[{category}]: {str(out)}"

    assert country == country_expected, f"[{category}]: {str(out)}"
