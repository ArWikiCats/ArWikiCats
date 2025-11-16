import pytest
from unittest.mock import patch
from src.rules.year_rules import StartWithYearOrTypoRule

@patch("src.rules.year_rules.label_for_startwith_year_or_typeo")
def test_start_with_year_or_typo_rule(mock_label_for_startwith_year_or_typeo):
    """Test that the start with year or typo rule correctly identifies and transforms categories."""
    # Arrange
    mock_label_for_startwith_year_or_typeo.return_value = "تصنيف:foo"
    rule = StartWithYearOrTypoRule()

    # Act
    result = rule.apply("2022 foo")

    # Assert
    assert result == "تصنيف:foo"
