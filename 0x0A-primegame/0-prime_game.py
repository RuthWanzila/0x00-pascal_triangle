#!/usr/bin/python3
"""Prime Game - Maria and Ben are playing a game"""


def isWinner(rounds, numbers):
    """
    Determine the winner of the Prime Game.

    Args:
        rounds (int): The number of rounds.
        numbers (list): The list of numbers for each round.

    Returns:
        str: The name of the player who won the most rounds.
        None: If the winner cannot be determined.
    """
    if rounds <= 0 or numbers is None:
        return None
    if rounds != len(numbers):
        return None

    ben_wins = 0
    maria_wins = 0

    # Create a list to store prime number flags
    prime_flags = [1 for _ in range(max(numbers) + 1)]
    prime_flags[0], prime_flags[1] = 0, 0
    for i in range(2, len(prime_flags)):
        remove_multiples(prime_flags, i)

    for num in numbers:
        if sum(prime_flags[:num + 1]) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if ben_wins > maria_wins:
        return "Ben"
    if maria_wins > ben_wins:
        return "Maria"
    return None


def remove_multiples(flags, x):
    """
    Remove multiples of a prime number from the prime_flags list.

    Args:
        flags (list): The list of prime number flags.
        x (int): The prime number.
    """
    for i in range(2, len(flags)):
        try:
            flags[i * x] = 0
        except (ValueError, IndexError):
            break
