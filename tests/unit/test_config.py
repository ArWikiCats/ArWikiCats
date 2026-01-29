# -*- coding: utf-8 -*-
"""
Unit tests for the config module.
"""

import os
import sys
from unittest.mock import patch

import pytest

from ArWikiCats.config import AppConfig, Config, PrintConfig, all_params, one_req, print_settings, settings


class TestOneReq:
    """Tests for the one_req function."""

    def test_returns_false_by_default(self) -> None:
        """Should return False when neither env var nor command line flag is set."""
        with patch.dict(os.environ, {}, clear=False):
            with patch.object(sys, "argv", ["test.py"]):
                result = one_req("TEST_FLAG")
                assert result is False

    def test_returns_true_for_env_var_1(self) -> None:
        """Should return True when env var is set to '1'."""
        with patch.dict(os.environ, {"TEST_FLAG": "1"}):
            result = one_req("TEST_FLAG")
            assert result is True

    def test_returns_true_for_env_var_true(self) -> None:
        """Should return True when env var is set to 'true'."""
        with patch.dict(os.environ, {"TEST_FLAG": "true"}):
            result = one_req("TEST_FLAG")
            assert result is True

    def test_returns_true_for_env_var_yes(self) -> None:
        """Should return True when env var is set to 'yes'."""
        with patch.dict(os.environ, {"TEST_FLAG": "yes"}):
            result = one_req("TEST_FLAG")
            assert result is True

    def test_case_insensitive_env_var(self) -> None:
        """Should be case-insensitive for env var values."""
        with patch.dict(os.environ, {"TEST_FLAG": "TRUE"}):
            result = one_req("TEST_FLAG")
            assert result is True

    def test_returns_true_for_command_line_arg(self) -> None:
        """Should return True when flag is in command line args."""
        # Note: argv is checked at module load time, so we need to patch argv_lower
        from ArWikiCats import config

        with patch.object(config, "argv_lower", ["test.py", "test_flag"]):
            result = one_req("TEST_FLAG")
            assert result is True

    def test_appends_to_all_params(self) -> None:
        """Should append the parameter name to all_params."""
        initial_length = len(all_params)
        with patch.dict(os.environ, {}, clear=False):
            with patch.object(sys, "argv", ["test.py"]):
                one_req("UNIQUE_TEST_PARAM_12345")
        assert len(all_params) > initial_length
        assert "UNIQUE_TEST_PARAM_12345" in all_params

    def test_handles_false_values(self) -> None:
        """Should return False for env var values like 'false', '0', etc."""
        with patch.dict(os.environ, {"TEST_FLAG": "false"}):
            result = one_req("TEST_FLAG")
            assert result is False

        with patch.dict(os.environ, {"TEST_FLAG": "0"}):
            result = one_req("TEST_FLAG")
            assert result is False

        with patch.dict(os.environ, {"TEST_FLAG": "no"}):
            result = one_req("TEST_FLAG")
            assert result is False


class TestPrintConfig:
    """Tests for PrintConfig dataclass."""

    def test_is_frozen(self) -> None:
        """PrintConfig should be immutable (frozen)."""
        config = PrintConfig(noprint_formats=True, noprint=False)
        with pytest.raises(Exception):  # FrozenInstanceError in dataclasses
            config.noprint = True  # type: ignore

    def test_has_correct_attributes(self) -> None:
        """PrintConfig should have the expected attributes."""
        config = PrintConfig(noprint_formats=True, noprint=False)
        assert hasattr(config, "noprint_formats")
        assert hasattr(config, "noprint")
        assert config.noprint_formats is True
        assert config.noprint is False


class TestAppConfig:
    """Tests for AppConfig dataclass."""

    def test_is_frozen(self) -> None:
        """AppConfig should be immutable (frozen)."""
        config = AppConfig(find_stubs=True, makeerr=False, save_data_path="/tmp")
        with pytest.raises(Exception):  # FrozenInstanceError
            config.find_stubs = False  # type: ignore

    def test_has_correct_attributes(self) -> None:
        """AppConfig should have the expected attributes."""
        config = AppConfig(find_stubs=True, makeerr=False, save_data_path="/tmp")
        assert hasattr(config, "find_stubs")
        assert hasattr(config, "makeerr")
        assert hasattr(config, "save_data_path")
        assert config.find_stubs is True
        assert config.makeerr is False
        assert config.save_data_path == "/tmp"


class TestConfig:
    """Tests for Config dataclass."""

    def test_is_frozen(self) -> None:
        """Config should be immutable (frozen)."""
        print_cfg = PrintConfig(noprint_formats=False, noprint=False)
        app_cfg = AppConfig(find_stubs=False, makeerr=False, save_data_path="")
        config = Config(print=print_cfg, app=app_cfg)
        with pytest.raises(Exception):  # FrozenInstanceError
            config.print = print_cfg  # type: ignore

    def test_has_correct_attributes(self) -> None:
        """Config should contain print and app configurations."""
        print_cfg = PrintConfig(noprint_formats=True, noprint=False)
        app_cfg = AppConfig(find_stubs=False, makeerr=True, save_data_path="/data")
        config = Config(print=print_cfg, app=app_cfg)
        assert isinstance(config.print, PrintConfig)
        assert isinstance(config.app, AppConfig)


class TestSettingsAndExports:
    """Tests for module-level settings and exports."""

    def test_settings_is_config_instance(self) -> None:
        """settings should be an instance of Config."""
        assert isinstance(settings, Config)

    def test_print_settings_is_printconfig_instance(self) -> None:
        """print_settings should be an instance of PrintConfig."""
        assert isinstance(print_settings, PrintConfig)

    def test_all_params_is_list(self) -> None:
        """all_params should be a list."""
        assert isinstance(all_params, list)

    def test_module_exports(self) -> None:
        """Module should export the expected names."""
        from ArWikiCats import config

        assert hasattr(config, "settings")
        assert hasattr(config, "print_settings")
        assert hasattr(config, "app_settings")
        assert hasattr(config, "all_params")


class TestConfigIntegration:
    """Integration tests for the config system."""

    def test_settings_reflects_environment(self) -> None:
        """settings should reflect environment variables at import time."""
        # This is testing the actual module settings, so values depend on environment
        assert isinstance(settings.print.noprint, bool)
        assert isinstance(settings.print.noprint_formats, bool)
        assert isinstance(settings.app.find_stubs, bool)
        assert isinstance(settings.app.makeerr, bool)
        assert isinstance(settings.app.save_data_path, str)

    def test_save_data_path_from_env(self) -> None:
        """save_data_path should use SAVE_DATA_PATH env var."""
        # The actual value depends on environment, but should be a string
        assert isinstance(settings.app.save_data_path, str)

    def test_config_consistency(self) -> None:
        """print_settings should match settings.print."""
        assert settings.print.noprint == print_settings.noprint
        assert settings.print.noprint_formats == print_settings.noprint_formats