from pathlib import Path
from typing import List, TypeAlias

Report: TypeAlias = List[int]


def main() -> None:
    """Execute main program logic. Advent_02"""
    reports = read_reports(Path("inputs") / "advent_02_input.txt")
    safe_reports = count_safe_reports(reports)
    print(f"Part I - Safe reports: {safe_reports} \n")


def read_reports(file_path: str) -> List[Report]:
    """Read and parse reports from file.

    Args:
        file_path: Path to input file
    Returns:
        List of numeric reports
    """
    path = Path(file_path)
    try:
        return [
            [int(num) for num in line.split()]
            for line in path.read_text().splitlines()
            if line.strip()
        ]
    except FileNotFoundError as err:
        raise FileNotFoundError(f"Input file not found: {file_path}") from err


def count_safe_reports(reports: List[Report]) -> int:
    """Count reports meeting safety criteria."""
    return sum(1 for report in reports if is_report_safe(report))


def is_report_safe(report: Report) -> bool:
    """Check if report meets safety criteria.

    A report is safe if:
    - Empty or single value
    - All adjacent values differ by 1-3
    - Consistent increasing/decreasing pattern
    """
    if len(report) <= 1:
        return True

    should_increase = report[0] < report[1]
    for i in range(len(report) - 1):
        distance = abs(report[i] - report[i + 1])
        current_increasing = report[i] < report[i + 1]
        if not (1 <= distance <= 3 and current_increasing == should_increase):
            return False
    return True


if __name__ == "__main__":
    main()
