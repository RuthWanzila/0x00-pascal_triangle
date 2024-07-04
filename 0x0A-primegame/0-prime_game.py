#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
        x (int): The number of rounds.
        nums (list): A list of integers representing upper limit of each round.

    Returns:
        str: The name of the player that won the most rounds.
        None: If the winner cannot be determined.
    """
    if not x or not nums:
        return None

    winners = [0, 0]  # Maria, Ben

    for n in nums:
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False

        # Find all prime numbers up to n using the Sieve of Eratosthenes
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False

        available = [i for i in range(1, n + 1) if primes[i]]
        player = 0  # 0: Maria, 1: Ben

        while available:
            if not available:
                break

            if player == 0:  # Maria's turn
                for prime in available:
                    if all(num % prime != 0 for num in available):
                        available.remove(prime)
                        break
                else:
                    winners[1] += 1
                    break
            else:  # Ben's turn
                for prime in available:
                    if all(num % prime != 0 for num in available):
                        available.remove(prime)
                        break
                else:
                    winners[0] += 1
                    break

            player = 1 - player

    if winners[0] > winners[1]:
        return "Maria"
    elif winners[1] > winners[0]:
        return "Ben"
    else:
        return None
