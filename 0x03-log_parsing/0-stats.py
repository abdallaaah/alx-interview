#!/usr/bin/python3
"""This file works with stdin and performs some file calculations from the input lines."""
import sys
from typing import List, Dict


def count_status_code(status_codes: List[int]) -> Dict[int, int]:
    """Calculate the count of each status code in the list."""
    status_code_counts = {}
    for code in status_codes:
        if code in status_code_counts:
            status_code_counts[code] += 1
        else:
            status_code_counts[code] = 1
    return status_code_counts


def print_metrics(file_size: int, status_code_counts: Dict[int, int]):
    """Print the accumulated metrics."""
    print(f"File size: {file_size}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")


count = 0
file_size = 0
status_code = []

try:
    for line in sys.stdin:
        line = line.rstrip()
        parts = line.split()

        if len(parts) != 9 or not parts[-2].isdigit() or not parts[-1].isdigit():
            continue

        count += 1
        status_code.append(int(parts[-2]))
        file_size += int(parts[-1])

        if count % 10 == 0:
            status_code_counts = count_status_code(status_code)
            print_metrics(file_size, status_code_counts)
except KeyboardInterrupt:
    pass
finally:
    if count % 10 != 0 or count == 0:
        status_code_counts = count_status_code(status_code)
        print_metrics(file_size, status_code_counts)
