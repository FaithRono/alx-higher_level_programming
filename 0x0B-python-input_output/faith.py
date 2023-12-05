#!/usr/bin/python3
"""Reads from standard input and computes metrics."""


import sys


def print_metrics(total_size, status_codes):
    """
    Prints the computed metrics.

    Args:
        total_size (int): The total file size.
        status_codes (dict): A dictionary containing the count
        of each status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


total_size = 0
status_codes = {}

try:
    line_count = 0
    for line in sys.stdin:
        try:
            line = line.strip()
            ip = line.split(' ')[0]
            _, _, status_code, file_size = line.split(' ')[-3:]

            total_size += int(file_size)
            if status_code not in status_codes:
                status_codes[status_code] = 1
            else:
                status_codes[status_code] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)

        except (ValueError, IndexError):
            pass

except KeyboardInterrupt:
    print_metrics(total_size, status_codes)
