#!/usr/bin/python3
"""
Tests for model_data_base.py module.

This module provides tests for FormatDataBase abstract class which is the foundation
for all single-element category translation formatters.
"""

import pytest

from ArWikiCats.translations_formats.DataModel.model_data_base import FormatDataBase


class TestFormatDataBaseAbstractMethods:
    """Tests for abstract methods that raise NotImplementedError."""

    def test_apply_pattern_replacement_raises(self):
        """Test apply_pattern_replacement raises NotImplementedError in base class."""

        bot = FormatDataBase(
            formatted_data={},
            data_list={},
            key_placeholder="{sport}",
        )
        with pytest.raises(NotImplementedError):
            bot.apply_pattern_replacement("template", "label")

    def test_replace_value_placeholder_raises(self):
        """Test replace_value_placeholder raises NotImplementedError in base class."""

        bot = FormatDataBase(
            formatted_data={},
            data_list={},
            key_placeholder="{sport}",
        )
        with pytest.raises(NotImplementedError):
            bot.replace_value_placeholder("label", "value")
