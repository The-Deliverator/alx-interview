#!/usr/bin/python3
""" Module for  the Prime Game question """


def isWinner(x, nums):
    """Determines the winner of the prime number game"""
    if not nums or x < 1:
        return None

    max_num = max(nums)

    # Sieve of Eratosthenes to determine prime numbers up to max_num
    is_prime = [True] * (max(max_num + 1, 2))
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False

    # Build cumulative count of primes up to each index
    prime_count_up_to = [0] * len(is_prime)
    count = 0
    for i in range(len(is_prime)):
        if is_prime[i]:
            count += 1
        prime_count_up_to[i] = count

    # Determine who wins more rounds
    maria_wins = 0
    for num in nums:
        if prime_count_up_to[num] % 2 == 1:
            maria_wins += 1

    if maria_wins * 2 == len(nums):
        return None
    return "Maria" if maria_wins * 2 > len(nums) else "Ben"
