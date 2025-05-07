#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics:

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>.
(if the format is not this one, the line must be skipped).
After every 10 lines and/or a keyboard interruption (CTRL + C), print these
statistics from the beginning:
    Total file size: File size: <total size>
    where <total size> is the sum of all previous <file size> (format above)
    Number of lines by status code:
        possible status code: 200, 301, 400, 401, 403, 404, 405 and 500.
        if a status code doesn’t appear or is not an integer, don’t
        print anything for this status code.
        format: <status code>: <number>.
        status codes should be printed in ascending order.
"""

import sys
import signal

if __name__ == '__main__':

    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    total_size = 0
    line_count = 0


def print_stats():
    """Prints accumulated metrics"""
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Signal handler for KeyboardInterrupt (CTRL+C)"""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
"""Register signal handler"""
try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()

        if len(parts) < 9:
            continue

        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
        except ValueError:
            continue

        if status_code in status_codes:
            status_codes[status_code] += 1
            total_size += file_size

        line_count += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
