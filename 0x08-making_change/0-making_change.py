#!/usr/bin/python3
"""makeChange function"""


def makeChange(coins, total):
    """If the total is zero or negative, no coins are needed"""
    if total <= 0:
        return 0

    """If the list of coins is empty, it's impossible to make change"""
    if not coins:
        return -1

    """Create a list to store the minimum coins needed for each amount"""
    """Start by assuming we can't make any amount (so we use 'infinity')"""
    """But we know that 0 coins are needed to make amount 0"""
    min_coins_needed = [float('inf')] * (total + 1)
    min_coins_needed[0] = 0

    """iterate through"""
    for coin in coins:
        """use this coin for every total from coin value up to the target"""
        for amount in range(coin, total + 1):
            """If using this coin gets us a better result, take it"""
            min_coins_needed[amount] = min(
                min_coins_needed[amount],
                min_coins_needed[amount - coin] + 1
            )

    """If we never found a good way to make 'total', return -1"""
    if min_coins_needed[total] == float('inf'):
        return -1

    """Otherwise, return the smallest number of coins needed"""
    return min_coins_needed[total]
