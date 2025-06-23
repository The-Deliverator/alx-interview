#!/usr/bin/python3
"""Prime game module"""


def isWinner(x, nums):
    def is_prime(num):
        """Return True if num is a prime number."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def prime_count(n):
        """Return the number of primes from 1 to n."""
        count = 0
        for i in range(1, n + 1):
            if is_prime(i):
                count += 1
        return count

    if not nums or x < 1:
        return None

    maria_score = 0
    ben_score = 0

    for n in nums:
        primes = prime_count(n)
        if primes % 2 == 1:
            maria_score += 1
        else:
            ben_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    return None

