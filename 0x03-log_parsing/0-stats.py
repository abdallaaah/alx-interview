#!/usr/bin/python3
"""this file work with the stdin and make some file calculation from line"""
import sys
from typing import List, Dict


def count_status_code(status_code: List[int]) -> Dict[int, int]:
    """this function calculate count of each number in the list"""
    status_code_counts = {}
    for code in status_code:
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
    if (data[7].isnumeric()):
        status_code.append(data[7])
        status_code.sort()
    if (len(data) != 9):
        print('the is a problem i will break')
        break
    file_size += int(data[-1])
    if (count % 10 == 0 and count != 0):
        status_code_countss = count_status_code(status_code)
        print(f"File size: {file_size}")
        for key, value in status_code_countss.items():
            print(f"{key}: {value}")
        file_size = 0
        status_code = []
