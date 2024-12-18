from pathlib import Path

from src.solutions.advent_02 import (
    is_report_safe,
    is_report_safe_with_tolerance,
    read_reports,
)


def test_read_reports():
    """Test reading report levels from file."""
    sample_input = Path("inputs") / "advent_02_example.txt"
    report_levels = read_reports(sample_input)
    assert report_levels == [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]


def test_is_report_safe():
    """Test safe report when empty."""
    assert is_report_safe([])

    """Test safe report when 1 value."""
    assert is_report_safe([2])

    """Test safe report when decreasing levels and distance between 1 and 3."""
    assert is_report_safe([7, 6, 4, 2, 1])

    """Test safe report when increasing levels and distance between 1 and 3."""
    assert is_report_safe([1, 3, 6, 7, 9])

    """Test NOT safe report when increasing levels and distance more than 1 and 3."""
    assert not is_report_safe([1, 2, 7, 8, 9])

    """Test NOT safe report when decreasing levels and distance more than 1 and 3."""
    assert not is_report_safe([9, 7, 6, 2, 1])

    """Test NOT safe report when mixing increasing and decreasing levels"""
    assert not is_report_safe([1, 3, 2, 4, 5])

    """Test NOT safe report when equal levels"""
    assert not is_report_safe([8, 6, 4, 4, 1])


def test_is_report_safe_with_tolerance():
    """Test safe report when empty."""
    assert is_report_safe_with_tolerance([])

    """Test safe report when 1 value."""
    assert is_report_safe_with_tolerance([2])

    """Test safe report when decreasing levels and distance between 1 and 3."""
    assert is_report_safe_with_tolerance([7, 6, 4, 2, 1])

    """Test safe report when increasing levels and distance between 1 and 3."""
    assert is_report_safe_with_tolerance([1, 3, 6, 7, 9])

    """Test NOT safe report when increasing levels and distance more than 1 and 3."""
    assert not is_report_safe_with_tolerance([1, 2, 7, 8, 9])

    """Test NOT safe report when decreasing levels and distance more than 1 and 3."""
    assert not is_report_safe_with_tolerance([9, 7, 6, 2, 1])

    """Test safe report when mixing increasing and decreasing levels. Skip once"""
    assert is_report_safe_with_tolerance([1, 3, 2, 4, 5])

    """Test safe report when mixing increasing and decreasing levels. Skip once.
    Ensure faulty skip"""
    assert is_report_safe_with_tolerance([1, 3, 2, 6, 7])

    """Test NOT safe report when mixing increasing and decreasing levels. Skip twice"""
    assert not is_report_safe_with_tolerance([1, 3, 2, 4, 3, 6])

    """Test safe report when equal levels. Skip once"""
    assert is_report_safe_with_tolerance([8, 6, 4, 4, 1])

    """Test safe report when faulty at the end"""
    assert is_report_safe_with_tolerance([8, 6, 4, 3, 1, 1])
