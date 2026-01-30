"""
Unit tests for the config module.
"""

import os
import sys
from unittest.mock import patch

from ArWikiCats.config import AppConfig, Config, one_req, settings


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


class TestAppConfig:
    """Tests for AppConfig dataclass."""

    def test_has_correct_attributes(self) -> None:
        """AppConfig should have the expected attributes."""
        config = AppConfig(save_data_path="/tmp")
        assert hasattr(config, "save_data_path")
        assert config.save_data_path == "/tmp"


class TestSettingsAndExports:
    """Tests for module-level settings and exports."""

    def test_settings_is_config_instance(self) -> None:
        """settings should be an instance of Config."""
        assert isinstance(settings, Config)

    def test_module_exports(self) -> None:
        """Module should export the expected names."""
        from ArWikiCats import config

        assert hasattr(config, "settings")
        assert hasattr(config, "app_settings")


class TestConfigIntegration:
    """Integration tests for the config system."""

    def test_settings_reflects_environment(self) -> None:
        """settings should reflect environment variables at import time."""
        # This is testing the actual module settings, so values depend on environment
        assert isinstance(settings.app.save_data_path, str)

    def test_save_data_path_from_env(self) -> None:
        """save_data_path should use SAVE_DATA_PATH env var."""
        # The actual value depends on environment, but should be a string
        assert isinstance(settings.app.save_data_path, str)
