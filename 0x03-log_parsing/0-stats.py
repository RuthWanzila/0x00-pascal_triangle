#!/usr/bin/python3

import sys
from collections import defaultdict

# Initialize variables
total_size = 0
status_codes = defaultdict(int)
line_count = 0

try:
    # Read input
    for line in sys.stdin:
        line = line.strip()

        # Check if line matches the expected format
        if not line.startswith('"GET /projects/260 HTTP/1.1"'):
            continue

        # Extract file size and status code from the line
        parts = line.split()
        if len(parts) < 8:
            continue

        file_size = int(parts[-2])
        status_code = int(parts[-3])

        # Update metrics
        total_size += file_size
        status_codes[status_code] += 1

        line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_codes.keys()):
                print(f"{code}: {status_codes[code]}")

    # Print final statistics
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print("Keyboard interruption detected")
