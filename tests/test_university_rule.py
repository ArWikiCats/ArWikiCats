import pytest
from unittest.mock import patch
from src.rules.university_rules import UniversityRule

@patch("src.rules.university_rules.univer")
def test_university_rule(mock_univer):
    """Test that the university rule correctly identifies and transforms university names."""
    # Arrange
    mock_univer.te_universities.return_value = "تصنيف:جامعة القاهرة"
    rule = UniversityRule()

    # Act
    result = rule.apply("Cairo University")

    # Assert
    assert result == "تصنيف:جامعة القاهرة"
