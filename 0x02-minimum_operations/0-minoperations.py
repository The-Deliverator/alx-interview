#!/usr/bin/python3
"""
Defines a method that calculates the fewest number of operations
needed to result in eactly n H characters in the file.
"""


def minOperations(n):

    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
