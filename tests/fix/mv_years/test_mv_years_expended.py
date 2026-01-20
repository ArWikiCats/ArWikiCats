"""Comprehensive pytest suite for move_years module."""

import pytest

from ArWikiCats.fix.mv_years import move_by_in, move_years, move_years_first


@pytest.mark.parametrize(
    "text,expected",
    [
        # --- Simple year movement ---
        ("1989 في اتحاد الرجبي", "اتحاد الرجبي في 1989"),
        ("2020 في كرة القدم", "كرة القدم في 2020"),
        ("2010–11 في الموسيقى", "الموسيقى في 2010–11"),
        ("200 قبل الميلاد في الإمبراطورية الرومانية", "الإمبراطورية الرومانية في 200 قبل الميلاد"),
        ("2019 في الأفلام", "2019 في الأفلام"),  # skip_it case
        ("الأفلام في 2019", "الأفلام في 2019"),  # already correct
        # --- No match ---
        ("اتحاد الرجبي 1989", "اتحاد الرجبي 1989"),
        ("القرن العشرين في أوروبا", "القرن العشرين في أوروبا"),
        # --- With 'حسب' clause ---
        ("1989 في اتحاد الرجبي حسب البلد", "اتحاد الرجبي في 1989 حسب البلد"),
        ("2020 في الرياضة حسب النوع", "الرياضة في 2020 حسب النوع"),
        # --- BCE variants ---
        ("200 ق.م في مصر", "مصر في 200 ق م"),
        ("عقد 1990 في الفنون", "الفنون في عقد 1990"),
    ],
)
def test_move_years_first_o(text: str, expected: str) -> None:
    """Test move_years_first for all expected patterns."""
    assert move_years_first(text) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        # --- Simple reorder with 'حسب' clause ---
        ("اتحاد الرجبي حسب البلد في 1989", "اتحاد الرجبي في 1989 حسب البلد"),
        ("كرة القدم حسب الموسم في 2020", "كرة القدم في 2020 حسب الموسم"),
        # --- BCE and century variants ---
        ("المعارك حسب المنطقة في 300 ق.م", "المعارك في 300 ق م حسب المنطقة"),
        ("الممالك حسب الحكم في القرن 19", "الممالك في القرن 19 حسب الحكم"),
        # --- With underscores ---
        ("اتحاد_الرجبي_حسب_البلد_في_1989", "اتحاد الرجبي في 1989 حسب البلد"),
        # --- No match ---
        ("اتحاد الرجبي في 1989 حسب البلد", "اتحاد الرجبي في 1989 حسب البلد"),
    ],
)
def test_move_by_in(text: str, expected: str) -> None:
    """Test move_by_in for year and century reordering."""
    assert move_by_in(text) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        # --- Category namespace handling ---
        ("تصنيف:1989 في اتحاد الرجبي", "تصنيف:اتحاد الرجبي في 1989"),
        ("تصنيف:اتحاد الرجبي حسب البلد في 1989", "تصنيف:اتحاد الرجبي في 1989 حسب البلد"),
        # --- BCE handling inside category ---
        ("تصنيف:200 ق.م في مصر", "تصنيف:مصر في 200 ق م"),
        # --- When already normalized ---
        ("تصنيف:اتحاد الرجبي في 1989", "تصنيف:اتحاد الرجبي في 1989"),
        ("تصنيف:الموسيقى في 2010–11", "تصنيف:الموسيقى في 2010–11"),
        # --- Fallback from first to by_in ---
        ("تصنيف:كرة القدم حسب الموسم في 2020", "تصنيف:كرة القدم في 2020 حسب الموسم"),
    ],
)
def test_move_years_with_category_namespace(text: str, expected: str) -> None:
    """Test category namespace preservation."""
    assert move_years(text) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        # --- Simple text ---
        ("1989 في اتحاد الرجبي", "اتحاد الرجبي في 1989"),
        ("اتحاد الرجبي حسب البلد في 1989", "اتحاد الرجبي في 1989 حسب البلد"),
        # --- No match cases ---
        ("القرن 20 في أوروبا", "أوروبا في القرن 20"),
        ("تصنيف:الأفلام في 2019", "تصنيف:الأفلام في 2019"),
        # --- Complex BCE and underscore ---
        ("تصنيف:200 ق.م في الإمبراطورية_الرومانية", "تصنيف:الإمبراطورية الرومانية في 200 ق م"),
    ],
)
def test_move_years_combined(text: str, expected: str) -> None:
    """Full integration tests combining both functions."""
    assert move_years(text) == expected


@pytest.mark.parametrize(
    "text",
    [
        "random text with no match",
        "تصنيف:random text",
        "اتحاد الرجبي فقط",
        "في 2020 فقط",
        "حسب الموسم فقط",
    ],
)
def test_no_modifications(text) -> None:
    """Ensure unrelated strings remain unchanged."""
    assert move_years(text) == text
