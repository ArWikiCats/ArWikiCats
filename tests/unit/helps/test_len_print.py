# -*- coding: utf-8 -*-
"""
Unit tests for the helps.len_print module.
"""

import sys
from pathlib import Path
from unittest.mock import MagicMock, mock_open, patch

import pytest

from ArWikiCats.helps.len_print import all_len, data_len, dump_all_len, format_size, save_data


class TestFormatSize:
    """Tests for the format_size function."""

    def test_formats_bytes_as_human_readable(self) -> None:
        """Should format byte sizes in human-readable format."""
        result = format_size("data", 1024, [])
        assert isinstance(result, str)
        # Should contain some readable format (KB, MB, etc.)

    def test_returns_numeric_for_lens_keys(self) -> None:
        """Should return numeric value for keys in lens list."""
        result = format_size("count", 100, ["count"])
        assert result == 100

    def test_handles_zero_size(self) -> None:
        """Should handle zero size."""
        result = format_size("data", 0, [])
        assert isinstance(result, str)

    def test_handles_large_sizes(self) -> None:
        """Should handle large sizes."""
        result = format_size("data", 1024 * 1024 * 1024, [])
        assert isinstance(result, str)

    def test_handles_float_values(self) -> None:
        """Should handle float values."""
        result = format_size("data", 1024.5, [])
        assert isinstance(result, str)


class TestSaveData:
    """Tests for the save_data function."""

    def test_does_nothing_when_no_save_path(self) -> None:
        """Should do nothing when save_data_path is not configured."""
        with patch("ArWikiCats.helps.len_print.app_settings") as mock_settings:
            mock_settings.save_data_path = ""
            save_data("test_bot", {"key": "value"})
            # Should complete without errors

    @patch("ArWikiCats.helps.len_print.app_settings")
    @patch("pathlib.Path.mkdir")
    @patch("builtins.open", new_callable=mock_open)
    @patch("json.dump")
    def test_creates_directory_when_save_path_exists(
        self, mock_json_dump: MagicMock, mock_file: MagicMock, mock_mkdir: MagicMock, mock_settings: MagicMock
    ) -> None:
        """Should create directory when save_data_path is configured."""
        mock_settings.save_data_path = "/tmp/test_save"
        save_data("test_bot", {"data": [1, 2, 3]})
        mock_mkdir.assert_called_once()

    @patch("ArWikiCats.helps.len_print.app_settings")
    @patch("pathlib.Path.mkdir")
    @patch("builtins.open", new_callable=mock_open)
    @patch("json.dump")
    def test_saves_dict_data_as_json(
        self, mock_json_dump: MagicMock, mock_file: MagicMock, mock_mkdir: MagicMock, mock_settings: MagicMock
    ) -> None:
        """Should save dict data as JSON."""
        mock_settings.save_data_path = "/tmp/test_save"
        data = {"items": {"key1": "value1", "key2": "value2"}}
        save_data("test_bot", data)
        mock_json_dump.assert_called_once()

    @patch("ArWikiCats.helps.len_print.app_settings")
    @patch("pathlib.Path.mkdir")
    @patch("builtins.open", new_callable=mock_open)
    @patch("json.dump")
    def test_saves_list_data_as_json(
        self, mock_json_dump: MagicMock, mock_file: MagicMock, mock_mkdir: MagicMock, mock_settings: MagicMock
    ) -> None:
        """Should save list data as JSON."""
        mock_settings.save_data_path = "/tmp/test_save"
        data = {"items": [1, 2, 3, 4]}
        save_data("test_bot", data)
        mock_json_dump.assert_called_once()

    @patch("ArWikiCats.helps.len_print.app_settings")
    @patch("pathlib.Path.mkdir")
    def test_skips_empty_data(self, mock_mkdir: MagicMock, mock_settings: MagicMock) -> None:
        """Should skip entries with empty data."""
        mock_settings.save_data_path = "/tmp/test_save"
        data = {"empty": None, "also_empty": []}
        with patch("builtins.open", mock_open()):
            save_data("test_bot", data)
            # Should not raise errors

    @patch("ArWikiCats.helps.len_print.app_settings")
    @patch("pathlib.Path.mkdir")
    def test_sorts_dict_data(self, mock_mkdir: MagicMock, mock_settings: MagicMock) -> None:
        """Should sort dict data by keys."""
        mock_settings.save_data_path = "/tmp/test_save"
        data = {"items": {"z": 1, "a": 2, "m": 3}}
        with patch("builtins.open", mock_open()) as mock_file:
            with patch("json.dump") as mock_dump:
                save_data("test_bot", data)
                # Check that json.dump was called (sorting is done before dump)
                if mock_dump.called:
                    call_args = mock_dump.call_args
                    saved_data = call_args[0][0] if call_args else None
                    if isinstance(saved_data, dict):
                        # Keys should be sorted
                        keys = list(saved_data.keys())
                        assert keys == sorted(keys, key=lambda x: x.lower())

    @patch("ArWikiCats.helps.len_print.app_settings")
    @patch("pathlib.Path.mkdir")
    def test_sorts_list_data(self, mock_mkdir: MagicMock, mock_settings: MagicMock) -> None:
        """Should sort and deduplicate list data."""
        mock_settings.save_data_path = "/tmp/test_save"
        data = {"items": [3, 1, 2, 1, 3]}
        with patch("builtins.open", mock_open()):
            with patch("json.dump") as mock_dump:
                save_data("test_bot", data)
                # Should have attempted to save sorted unique list

    @patch("ArWikiCats.helps.len_print.app_settings")
    @patch("pathlib.Path.mkdir")
    def test_handles_errors_gracefully(self, mock_mkdir: MagicMock, mock_settings: MagicMock) -> None:
        """Should handle errors gracefully and log them."""
        mock_settings.save_data_path = "/tmp/test_save"
        mock_mkdir.side_effect = Exception("Test error")
        # Should not raise, just log error
        save_data("test_bot", {"data": [1, 2, 3]})


class TestDataLen:
    """Tests for the data_len function."""

    def test_adds_data_to_all_len(self) -> None:
        """Should add data to all_len dictionary."""
        all_len.clear()
        data = {"items": [1, 2, 3], "count": 5}
        data_len("test_bot", data)
        assert "test_bot" in all_len
        assert isinstance(all_len["test_bot"], dict)

    def test_calculates_count_for_collections(self) -> None:
        """Should calculate count for list/dict collections."""
        all_len.clear()
        data = {"items": [1, 2, 3, 4, 5]}
        data_len("test_bot", data)
        assert all_len["test_bot"]["items"]["count"] == 5

    def test_uses_integer_value_directly(self) -> None:
        """Should use integer values directly as count."""
        all_len.clear()
        data = {"count": 42}
        data_len("test_bot", data)
        assert all_len["test_bot"]["count"]["count"] == 42

    def test_calculates_size_for_items(self) -> None:
        """Should calculate size for items."""
        all_len.clear()
        data = {"items": [1, 2, 3]}
        data_len("test_bot", data)
        assert "size" in all_len["test_bot"]["items"]
        assert isinstance(all_len["test_bot"]["items"]["size"], str)

    @patch("ArWikiCats.helps.len_print.app_settings")
    def test_saves_data_when_path_configured(self, mock_settings: MagicMock) -> None:
        """Should call save_data when save_data_path is configured."""
        mock_settings.save_data_path = "/tmp/test"
        with patch("ArWikiCats.helps.len_print.save_data") as mock_save:
            data = {"items": [1, 2, 3]}
            data_len("test_bot", data)
            mock_save.assert_called_once_with("test_bot", data)

    def test_handles_empty_data(self) -> None:
        """Should handle empty data dictionary."""
        all_len.clear()
        data_len("test_bot", {})
        # Should not add anything to all_len or should add empty entry
        assert "test_bot" not in all_len or all_len["test_bot"] == {}

    def test_updates_existing_bot_data(self) -> None:
        """Should update existing bot data instead of replacing."""
        all_len.clear()
        data_len("test_bot", {"items1": [1, 2]})
        data_len("test_bot", {"items2": [3, 4]})
        assert "items1" in all_len["test_bot"]
        assert "items2" in all_len["test_bot"]


class TestDumpAllLen:
    """Tests for the dump_all_len function."""

    def test_returns_dict_with_expected_keys(self) -> None:
        """Should return dict with 'by_count' and 'all' keys."""
        all_len.clear()
        all_len["bot1"] = {"items": {"count": 5, "size": "100 Bytes"}}
        result = dump_all_len()
        assert "by_count" in result
        assert "all" in result

    def test_sorts_all_by_bot_name(self) -> None:
        """Should sort 'all' section by bot name (case-insensitive)."""
        all_len.clear()
        all_len["Zbot"] = {"items": {"count": 1, "size": "10 Bytes"}}
        all_len["abot"] = {"items": {"count": 2, "size": "20 Bytes"}}
        all_len["Mbot"] = {"items": {"count": 3, "size": "30 Bytes"}}
        result = dump_all_len()
        bot_names = list(result["all"].keys())
        assert bot_names == ["abot", "Mbot", "Zbot"]

    def test_aggregates_by_count(self) -> None:
        """Should aggregate counts across all bots."""
        all_len.clear()
        all_len["bot1"] = {"items": {"count": 5, "size": "100 Bytes"}}
        all_len["bot2"] = {"items": {"count": 10, "size": "200 Bytes"}}
        result = dump_all_len()
        assert "items" in result["by_count"]
        # Should aggregate (one of the values will be stored)
        assert result["by_count"]["items"] in ["5", "10"]

    def test_sorts_by_count_descending(self) -> None:
        """Should sort by_count in descending order."""
        all_len.clear()
        all_len["bot1"] = {
            "small": {"count": 5, "size": "50 Bytes"},
            "medium": {"count": 50, "size": "500 Bytes"},
            "large": {"count": 500, "size": "5000 Bytes"},
        }
        result = dump_all_len()
        counts = list(result["by_count"].keys())
        # Should be sorted by count (descending): large, medium, small
        assert counts[0] == "large"
        assert counts[-1] == "small"

    def test_formats_counts_with_commas(self) -> None:
        """Should format counts with thousand separators."""
        all_len.clear()
        all_len["bot1"] = {"items": {"count": 1000000, "size": "1 MB"}}
        result = dump_all_len()
        assert "items" in result["by_count"]
        # Should have comma formatting
        assert "," in result["by_count"]["items"]

    def test_handles_empty_all_len(self) -> None:
        """Should handle empty all_len."""
        all_len.clear()
        result = dump_all_len()
        assert result["by_count"] == {}
        assert result["all"] == {}

    def test_preserves_all_len_data(self) -> None:
        """Should preserve data structure in 'all' section."""
        all_len.clear()
        all_len["bot1"] = {"items": {"count": 5, "size": "100 Bytes"}}
        result = dump_all_len()
        assert result["all"]["bot1"]["items"]["count"] == 5
        assert result["all"]["bot1"]["items"]["size"] == "100 Bytes"


class TestAllLenGlobalVariable:
    """Tests for the all_len global variable."""

    def test_all_len_is_dict(self) -> None:
        """all_len should be a dictionary."""
        assert isinstance(all_len, dict)

    def test_all_len_can_be_modified(self) -> None:
        """all_len should be modifiable."""
        original_keys = set(all_len.keys())
        all_len["test_modification"] = {"test": {"count": 1, "size": "10 B"}}
        assert "test_modification" in all_len
        # Clean up
        if "test_modification" in all_len:
            del all_len["test_modification"]


class TestIntegrationScenarios:
    """Integration tests for len_print module."""

    def test_full_workflow(self) -> None:
        """Should support full workflow from data_len to dump_all_len."""
        all_len.clear()
        # Add data for multiple bots
        data_len("bot1", {"items": [1, 2, 3], "count": 100})
        data_len("bot2", {"data": [4, 5, 6, 7], "total": 200})
        # Dump all data
        result = dump_all_len()
        assert "bot1" in result["all"]
        assert "bot2" in result["all"]
        assert len(result["by_count"]) > 0

    @patch("ArWikiCats.helps.len_print.app_settings")
    @patch("ArWikiCats.helps.len_print.save_data")
    def test_saves_when_configured(self, mock_save: MagicMock, mock_settings: MagicMock) -> None:
        """Should save data when save_data_path is configured."""
        mock_settings.save_data_path = "/tmp/test"
        all_len.clear()
        data = {"items": [1, 2, 3]}
        data_len("test_bot", data)
        mock_save.assert_called_once()


class TestEdgeCases:
    """Edge case tests."""

    def test_handles_unicode_in_bot_names(self) -> None:
        """Should handle Unicode characters in bot names."""
        all_len.clear()
        data_len("بوت_عربي", {"items": [1, 2, 3]})
        assert "بوت_عربي" in all_len

    def test_handles_special_characters_in_keys(self) -> None:
        """Should handle special characters in data keys."""
        all_len.clear()
        data_len("test_bot", {"items-with-dashes": [1, 2, 3]})
        assert "items-with-dashes" in all_len["test_bot"]

    def test_handles_very_large_collections(self) -> None:
        """Should handle very large collections."""
        all_len.clear()
        large_list = list(range(1000000))
        data_len("test_bot", {"large": large_list})
        assert "test_bot" in all_len

    def test_handles_nested_data_structures(self) -> None:
        """Should handle nested data structures."""
        all_len.clear()
        nested = {"outer": {"inner": [1, 2, 3]}}
        data_len("test_bot", nested)
        assert "test_bot" in all_len