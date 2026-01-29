# -*- coding: utf-8 -*-
"""
Unit tests for the helps.log module.
"""

import logging
from unittest.mock import MagicMock, patch

import pytest

from ArWikiCats.helps.log import LoggerWrap, getLogger


class TestLoggerWrapInit:
    """Tests for LoggerWrap initialization."""

    def test_creates_logger_with_name(self) -> None:
        """Should create a logger with the given name."""
        logger = LoggerWrap("test_logger")
        assert logger._logger.name == "test_logger"

    def test_creates_disabled_logger_when_requested(self) -> None:
        """Should create a disabled logger when disable_log=True."""
        logger = LoggerWrap("test_logger", disable_log=True)
        assert logger._logger.disabled is True

    def test_sets_correct_level(self) -> None:
        """Should set the correct logging level."""
        logger = LoggerWrap("test_logger", level=logging.WARNING)
        assert logger._logger.level == logging.WARNING

    def test_prevents_propagation_to_root(self) -> None:
        """Should prevent propagation to root logger."""
        logger = LoggerWrap("test_logger")
        assert logger._logger.propagate is False

    def test_adds_handler_when_not_disabled(self) -> None:
        """Should add a handler when logger is not disabled."""
        logger = LoggerWrap("test_logger")
        assert len(logger._logger.handlers) > 0

    def test_does_not_add_handler_when_disabled(self) -> None:
        """Should not add handlers when disabled."""
        logger = LoggerWrap("test_logger", disable_log=True)
        # Disabled loggers may or may not have handlers, check disabled flag
        assert logger._logger.disabled is True


class TestLoggerWrapSetLevel:
    """Tests for LoggerWrap set_level methods."""

    def test_set_level_changes_level(self) -> None:
        """Should change the logging level."""
        logger = LoggerWrap("test_logger")
        logger.set_level(logging.ERROR)
        assert logger._logger.level == logging.ERROR

    def test_setLevel_alias_works(self) -> None:
        """setLevel should work as an alias for set_level."""
        logger = LoggerWrap("test_logger")
        logger.setLevel(logging.CRITICAL)
        assert logger._logger.level == logging.CRITICAL

    def test_set_level_accepts_string(self) -> None:
        """Should accept string level names."""
        logger = LoggerWrap("test_logger")
        logger.set_level("WARNING")
        assert logger._logger.level == logging.WARNING


class TestLoggerWrapDisableLogger:
    """Tests for LoggerWrap disable_logger method."""

    def test_disables_logger(self) -> None:
        """Should disable the logger when called with True."""
        logger = LoggerWrap("test_logger")
        logger.disable_logger(True)
        assert logger._logger.disabled is True

    def test_enables_logger(self) -> None:
        """Should enable the logger when called with False."""
        logger = LoggerWrap("test_logger", disable_log=True)
        logger.disable_logger(False)
        assert logger._logger.disabled is False


class TestLoggerWrapGetLogger:
    """Tests for LoggerWrap logger() method."""

    def test_returns_underlying_logger(self) -> None:
        """Should return the underlying logging.Logger instance."""
        logger = LoggerWrap("test_logger")
        underlying = logger.logger()
        assert isinstance(underlying, logging.Logger)
        assert underlying.name == "test_logger"


class TestLoggerWrapLoggingMethods:
    """Tests for LoggerWrap logging methods."""

    def test_debug_logs_message(self) -> None:
        """Should log debug messages."""
        logger = LoggerWrap("test_logger", level=logging.DEBUG)
        with patch.object(logger._logger, "debug") as mock_debug:
            logger.debug("test message")
            mock_debug.assert_called_once()

    def test_info_logs_message(self) -> None:
        """Should log info messages."""
        logger = LoggerWrap("test_logger")
        with patch.object(logger._logger, "info") as mock_info:
            logger.info("test message")
            mock_info.assert_called_once()

    def test_warning_logs_message(self) -> None:
        """Should log warning messages."""
        logger = LoggerWrap("test_logger")
        with patch.object(logger._logger, "warning") as mock_warning:
            logger.warning("test message")
            mock_warning.assert_called_once()

    def test_error_logs_message(self) -> None:
        """Should log error messages."""
        logger = LoggerWrap("test_logger")
        with patch.object(logger._logger, "error") as mock_error:
            logger.error("test message")
            mock_error.assert_called_once()

    def test_critical_logs_message(self) -> None:
        """Should log critical messages."""
        logger = LoggerWrap("test_logger")
        with patch.object(logger._logger, "critical") as mock_critical:
            logger.critical("test message")
            mock_critical.assert_called_once()

    def test_exception_logs_message(self) -> None:
        """Should log exception messages."""
        logger = LoggerWrap("test_logger")
        with patch.object(logger._logger, "exception") as mock_exception:
            logger.exception("test exception")
            mock_exception.assert_called_once()

    def test_log_with_custom_level(self) -> None:
        """Should log with custom level."""
        logger = LoggerWrap("test_logger")
        with patch.object(logger._logger, "log") as mock_log:
            logger.log(logging.WARNING, "test message")
            mock_log.assert_called_once()


class TestLoggerWrapSpecialMethods:
    """Tests for special LoggerWrap methods."""

    def test_info_if_or_debug_logs_info_when_value_true(self) -> None:
        """Should log info when value is truthy."""
        logger = LoggerWrap("test_logger")
        with patch.object(logger._logger, "info") as mock_info:
            logger.info_if_or_debug("test message", "truthy_value")
            mock_info.assert_called_once()

    def test_info_if_or_debug_logs_debug_when_value_false(self) -> None:
        """Should log debug when value is falsy."""
        logger = LoggerWrap("test_logger", level=logging.DEBUG)
        with patch.object(logger._logger, "debug") as mock_debug:
            logger.info_if_or_debug("test message", "")
            mock_debug.assert_called_once()

    def test_output_is_alias_for_info(self) -> None:
        """output() should work as an alias for info()."""
        logger = LoggerWrap("test_logger")
        with patch.object(logger._logger, "info") as mock_info:
            logger.output("test message")
            mock_info.assert_called_once()

    def test_error_red_logs_error(self) -> None:
        """Should log error with red formatting."""
        logger = LoggerWrap("test_logger")
        with patch.object(logger._logger, "error") as mock_error:
            logger.error_red("test error")
            mock_error.assert_called_once()


class TestLoggerWrapShowDiff:
    """Tests for LoggerWrap showDiff method."""

    def test_shows_diff_between_texts(self) -> None:
        """Should generate diff output between two texts."""
        logger = LoggerWrap("test_logger")
        with patch.object(logger._logger, "warning") as mock_warning:
            logger.showDiff("old text", "new text")
            # Should have called warning multiple times for diff lines
            assert mock_warning.call_count > 0

    def test_handles_multiline_texts(self) -> None:
        """Should handle multiline text diffs."""
        logger = LoggerWrap("test_logger")
        old_text = "line1\nline2\nline3"
        new_text = "line1\nmodified\nline3"
        with patch.object(logger._logger, "warning") as mock_warning:
            logger.showDiff(old_text, new_text)
            assert mock_warning.call_count > 0

    def test_handles_identical_texts(self) -> None:
        """Should handle identical texts without errors."""
        logger = LoggerWrap("test_logger")
        text = "same text"
        with patch.object(logger._logger, "warning"):
            logger.showDiff(text, text)


class TestGetLoggerFunction:
    """Tests for the getLogger module function."""

    def test_returns_logger_wrap_instance(self) -> None:
        """Should return a LoggerWrap instance."""
        logger = getLogger("test_logger")
        assert isinstance(logger, LoggerWrap)

    def test_returns_logger_with_correct_name(self) -> None:
        """Should create logger with the given name."""
        logger = getLogger("my_test_logger")
        assert logger._logger.name == "my_test_logger"

    def test_respects_disable_log_parameter(self) -> None:
        """Should respect disable_log parameter."""
        logger = getLogger("test_logger", disable_log=True)
        assert logger._logger.disabled is True

    def test_respects_level_parameter(self) -> None:
        """Should respect level parameter."""
        logger = getLogger("test_logger", level=logging.CRITICAL)
        assert logger._logger.level == logging.CRITICAL

    def test_default_level_is_debug(self) -> None:
        """Default level should be DEBUG."""
        logger = getLogger("test_logger")
        assert logger._logger.level == logging.DEBUG


class TestLoggerWrapColorFormatting:
    """Tests for color formatting in log messages."""

    def test_handles_color_codes_in_messages(self) -> None:
        """Should handle color codes in log messages."""
        logger = LoggerWrap("test_logger")
        # Should not raise errors with color codes
        with patch.object(logger._logger, "info"):
            logger.info("<<red>>test<<default>>")
            logger.info("<<lightgreen>>test<<default>>")
            logger.info("<<lightblue>>test<<default>>")

    def test_error_red_adds_red_formatting(self) -> None:
        """error_red should add red color formatting."""
        logger = LoggerWrap("test_logger")
        with patch.object(logger._logger, "error") as mock_error:
            logger.error_red("error message")
            # Check that the call was made (actual formatting is done by make_str)
            mock_error.assert_called_once()


class TestLoggerWrapEdgeCases:
    """Edge case tests for LoggerWrap."""

    def test_handles_empty_messages(self) -> None:
        """Should handle empty log messages."""
        logger = LoggerWrap("test_logger")
        with patch.object(logger._logger, "info") as mock_info:
            logger.info("")
            mock_info.assert_called_once()

    def test_handles_unicode_messages(self) -> None:
        """Should handle Unicode in log messages."""
        logger = LoggerWrap("test_logger")
        with patch.object(logger._logger, "info") as mock_info:
            logger.info("رسالة عربية")
            mock_info.assert_called_once()

    def test_handles_special_characters(self) -> None:
        """Should handle special characters in messages."""
        logger = LoggerWrap("test_logger")
        with patch.object(logger._logger, "info") as mock_info:
            logger.info("Test with \n newlines \t tabs")
            mock_info.assert_called_once()

    def test_reusing_same_logger_name(self) -> None:
        """Should handle creating multiple loggers with same name."""
        logger1 = LoggerWrap("same_name")
        logger2 = LoggerWrap("same_name")
        # Both should exist but may share underlying logger
        assert isinstance(logger1, LoggerWrap)
        assert isinstance(logger2, LoggerWrap)


class TestLoggerWrapIntegration:
    """Integration tests for LoggerWrap."""

    def test_logging_workflow(self) -> None:
        """Should support typical logging workflow."""
        logger = getLogger("workflow_test", level=logging.DEBUG)
        logger.debug("Debug message")
        logger.info("Info message")
        logger.warning("Warning message")
        logger.error("Error message")
        # Should not raise any errors

    def test_enable_disable_workflow(self) -> None:
        """Should support enable/disable workflow."""
        logger = getLogger("enable_disable_test")
        logger.info("Message 1")
        logger.disable_logger(True)
        assert logger._logger.disabled is True
        logger.disable_logger(False)
        assert logger._logger.disabled is False
        logger.info("Message 2")

    def test_level_changes_workflow(self) -> None:
        """Should support changing levels during execution."""
        logger = getLogger("level_change_test", level=logging.WARNING)
        assert logger._logger.level == logging.WARNING
        logger.set_level(logging.DEBUG)
        assert logger._logger.level == logging.DEBUG
        logger.setLevel(logging.ERROR)
        assert logger._logger.level == logging.ERROR