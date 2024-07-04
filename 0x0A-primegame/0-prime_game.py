#!/usr/bin/python3

def is_prime(n):
    """
    Checks if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.
    
    Args:
        x (int): The number of rounds.
        nums (list): The array of n for each round.
    
    Returns:
        str: The name of the player who won the most rounds.
        None: If the winner cannot be determined.
    """
    if x <= 0 or any(n <= 0 for n in nums):
        return None
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        primes = [i for i in range(1, n+1) if is_prime(i)]
        while primes:
            if len(primes) % 2 == 1:
                ben_wins += 1
                primes = [p for p in primes if p > primes[0]]
            else:
                maria_wins += 1
                primes = [p for p in primes if p > primes[0]]
    
    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None
