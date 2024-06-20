#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Prototype: def makeChange(coins, total)
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    coins is a list of the values of the coins in your possession
    The value of a coin will always be an integer greater than 0
    You can assume you have an infinite number of each denomination of coin
    in the list
    """
    if total <= 0:
        return 0

    # Sort the coins in descending order to optimize the greedy approach
    coins.sort(reverse=True)

    # Initialize the number of coins needed
    num_coins = 0

    # Iterate through the sorted coins
    for coin in coins:
        # Calculate the number of the current coin needed
        count = total // coin
        num_coins += count

        # Update the remaining total
        total -= count * coin

    # If the total is still greater than 0, it cannot be met
    if total > 0:
        return -1

    return num_coins
