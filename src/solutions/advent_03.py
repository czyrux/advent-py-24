import re
from pathlib import Path
from typing import List, Tuple


def main() -> None:
    """Execute main program logic. Advent_03"""
    program_memory_instructions = read_program_memory(
        Path("inputs") / "advent_03_input.txt"
    )

    multiplications = find_multiplications(program_memory_instructions)
    multiplications_v2 = find_multiplications_with_enabling(program_memory_instructions)

    print(f"I - Result: {add_multiplications(multiplications)} \n")
    print(f"II - Result: {add_multiplications(multiplications_v2)} \n")


def read_program_memory(file_path: str) -> List[str]:
    path = Path(file_path)
    try:
        return [line for line in path.read_text().splitlines() if line.strip()]
    except FileNotFoundError as err:
        raise FileNotFoundError(f"Input file not found: {file_path}") from err


def find_multiplications(
    program_memory_instructions: List[str],
) -> List[Tuple[int, int]]:
    """Find all multiplication expressions in instructions.

    Pattern: mul(X,Y) where X,Y are numbers
    """
    if not program_memory_instructions:
        return []

    pattern = r"mul\((\d+),(\d+)\)"  # Matches mul(X,Y) where X,Y are numbers
    return [
        [int(match.group(1)), int(match.group(2))]
        for instruction in program_memory_instructions
        for match in re.finditer(pattern, instruction)
    ]


def find_multiplications_with_enabling(
    program_memory_instructions: List[str],
) -> List[Tuple[int, int]]:
    """Find all multiplication expressions in instructions."""
    if not program_memory_instructions:
        return []

    pattern = r"""(?x)
    (?:                              # Second case
        do\(\)                       # Match do()
        (?:(?!don't\(\)).)*?        # Match until don't()
        mul\((\d+),(\d+)\)          # Match mul after do()
    )
    """

    # add initial do as we should consider enable by default
    instruction = "do()" + "".join(program_memory_instructions)
    return [
        [int(match.group(1)), int(match.group(2))]
        for match in re.finditer(pattern, instruction)
    ]


def add_multiplications(multiplications: List[Tuple[int, int]]) -> int:
    return sum(left * right for left, right in multiplications)


if __name__ == "__main__":
    main()
