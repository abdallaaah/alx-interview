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

count = 0
file_size = 0
status_code = []

for line in sys.stdin:
    line = line.rstrip()
    data = []
    count += 1
    for word in line.split():
        data.append(word)

    if len(data) != 9:
        print('There is a problem, breaking the loop.')
        break

    if data[7].isnumeric():
        status_code.append(int(data[7]))
        status_code.sort()

    file_size += int(data[-1])

    if count % 10 == 0:
        status_code_counts = count_status_code(status_code)
        print(f"File size: {file_size}")
        for key, value in status_code_counts.items():
            print(f"{key}: {value}")
        file_size = 0
        status_code = []

# Print any remaining data after the loop ends
if count % 10 != 0 and count > 0:
    status_code_counts = count_status_code(status_code)
    print(f"File size: {file_size}")
    for key, value in status_code_counts.items():
        print(f"{key}: {value}")
