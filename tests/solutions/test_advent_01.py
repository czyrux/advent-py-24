from pathlib import Path

from src.solutions.advent_01 import calculate_distance_between_list, read_input


def test_read_input():
    """Test reading full input content."""
    sample_input = Path("inputs") / "advent_01_example.txt"
    left_list, right_list = read_input(sample_input)
    assert left_list == [1, 2, 3, 3, 3, 4]
    assert right_list == [3, 3, 3, 4, 5, 9]


def test_calculate_distance_between_lists():
    """Test distance calculation between two lists."""
    # Test basic positive numbers
    assert calculate_distance_between_list([1, 2, 3], [4, 5, 6]) == 9

    # Test with negative numbers
    assert calculate_distance_between_list([-1, -2], [1, 2]) == 6

    # Test with zeros
    assert calculate_distance_between_list([0, 0], [1, 1]) == 2

    # Test single element
    assert calculate_distance_between_list([1], [2]) == 1

    # Test empty lists
    assert calculate_distance_between_list([], []) == 0
