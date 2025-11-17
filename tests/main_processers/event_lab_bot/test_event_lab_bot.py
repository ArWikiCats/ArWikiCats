"""
Tests
"""
import pytest

from src.main_processers.event_lab_bot import event_Lab

def test_event_lab():
    # Test with a basic input
    result = event_Lab("test event")
    assert isinstance(result, str)

    # Test with different input
    result_various = event_Lab("sports event")
    assert isinstance(result_various, str)

    # Test with empty string
    result_empty = event_Lab("")
    assert isinstance(result_empty, str)
