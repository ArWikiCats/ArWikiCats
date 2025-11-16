import pytest
from unittest.mock import patch
from src.rules.general_rules import StubsRule

@patch("src.rules.general_rules.app_settings")
@patch("src.rules.general_rules.tmp_bot")
@patch("src.rules.general_rules.event_Lab_seoo")
def test_stubs_rule(mock_event_lab_seoo, mock_tmp_bot, mock_app_settings):
    """Test that the stubs rule correctly identifies and transforms stubs."""
    # Arrange
    mock_app_settings.find_stubs = True
    mock_event_lab_seoo.return_value = "جامعة"
    mock_tmp_bot.Work_Templates.return_value = "جامعة"
    rule = StubsRule()

    # Act
    result = rule.apply("University stubs")

    # Assert
    assert result == "بذرة جامعة"
