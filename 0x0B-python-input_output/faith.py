#!/usr/bin/python3
import sys

status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}

total_size = 0
count = 0

try:
    for i, line in enumerate(sys.stdin, 1):
        parts = line.split()
        if len(parts) > 2:
            try:
                code = parts[-2]
                file_size = int(parts[-1])
                if code in status_codes:
                    status_codes[code] += 1
                total_size += file_size
                count += 1
            except ValueError:
                pass

        if i % 10 == 0:
            print(f"File size: {total_size}")
            for key in sorted(status_codes.keys()):
                if status_codes[key] != 0:
                    print(f"{key}: {status_codes[key]}")
            print()

except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for key in sorted(status_codes.keys()):
        if status_codes[key] != 0:
            print(f"{key}: {status_codes[key]}")

