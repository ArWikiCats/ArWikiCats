"""A simple test script to validate the refactored translations module."""

from src.ma_lists.jobs import translations

def test_arabic_translations():
    """Tests that the ARABIC_TRANSLATIONS dictionary is not empty."""
    assert translations.ARABIC_TRANSLATIONS, "ARABIC_TRANSLATIONS is empty"

def test_formatable_strings():
    """Tests that the FORMATTABLE_STRINGS dictionary is not empty."""
    assert translations.FORMATTABLE_STRINGS, "FORMATTABLE_STRINGS is empty"

def test_nato_related_jobs():
    """Tests that the NATO_RELATED_JOBS dictionary is not empty."""
    assert translations.NATO_RELATED_JOBS, "NATO_RELATED_JOBS is empty"

def test_disability_related_jobs():
    """Tests that the DISABILITY_RELATED_JOBS dictionary is not empty."""
    assert translations.DISABILITY_RELATED_JOBS, "DISABILITY_RELATED_JOBS is empty"

def test_executive_roles():
    """Tests that the EXECUTIVE_ROLES dictionary is not empty."""
    assert translations.EXECUTIVE_ROLES, "EXECUTIVE_ROLES is empty"

def test_nationality_first_jobs():
    """Tests that the NATIONALITY_FIRST_JOBS list is not empty."""
    assert translations.NATIONALITY_FIRST_JOBS, "NATIONALITY_FIRST_JOBS is empty"
