#!/usr/bin/python3

"""Making Change Module"""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """Gets the fewest number of coins needed to meet a total
    Args:
        coins: The list of the values of coins
        total: Total needed to be met
    Returns:
        fewest number of coins else -1
    """
    if total <= 0:
        return 0
    # Using the Greedy Algorithm
    # Sort the list of coins in descending order
    sorted_coins = sorted(coins, reverse=True)

    # Counting the fewest number of coins
    count_coins = 0

    # Looping through the list of sorted coins
    for coin in sorted_coins:
        while total >= coin:
            total -= coin
            count_coins += 1
    if total == 0:
        return count_coins
    else:
        return -1

