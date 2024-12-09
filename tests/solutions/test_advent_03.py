from pathlib import Path

from src.solutions.advent_03 import (
    add_multiplications,
    find_multiplications,
    find_multiplications_with_enabling,
    read_program_memory,
)


def test_find_multiplications():
    """Test finding multiplication expressions example file."""
    sample_input = Path("inputs") / "advent_03_example.txt"
    program_memory = read_program_memory(sample_input)
    multiplications = find_multiplications(program_memory)
    assert multiplications == [
        [2, 4],
        [5, 5],
        [11, 8],
        [8, 5],
    ]


def test_find_multiplications_with_enabling():
    """Test finding multiplication expressions example file."""
    sample_input = Path("inputs") / "advent_03_example_v2.txt"
    program_memory = read_program_memory(sample_input)
    multiplications = find_multiplications_with_enabling(program_memory)
    assert multiplications == [
        [2, 4],
        [8, 5],
    ]


def test_add_multiplications():
    multiplications = [
        [2, 4],
        [5, 5],
        [11, 8],
        [8, 5],
    ]
    assert add_multiplications(multiplications) == 161
