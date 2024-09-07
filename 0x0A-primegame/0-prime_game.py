#!/usr/bin/python3
"""Prime Game Problem"""


def isWinner(x, nums):
    """Determines the winner between Maria and Ben."""
    if x < 1 or not nums:
        return None

    mariaWinsCount = 0
    benWinsCount = 0
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    for num in nums:
        roundsSet = list(range(1, num + 1))
        primesSet = [p for p in primes if p <= num]

        if not primesSet:
            benWinsCount += 1
            continue

        isMariaTurns = True

        while primesSet:
            smallestPrime = primesSet.pop(0)
            roundsSet.remove(smallestPrime)
            roundsSet = [x for x in roundsSet if x % smallestPrime != 0]

            isMariaTurns = not isMariaTurns

        # Determine the winner of this round
        if isMariaTurns:
            benWinsCount += 1
        else:
            mariaWinsCount += 1

    # Determine overall winner
    if mariaWinsCount > benWinsCount:
        return "Maria"
    elif benWinsCount > mariaWinsCount:
        return "Ben"
    return None


def sieve_of_eratosthenes(limit):
    """Returns a list of all primes up to the given limit."""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, limit + 1, start):
                sieve[multiple] = False

    return [num for num, is_prime in enumerate(sieve) if is_prime]

