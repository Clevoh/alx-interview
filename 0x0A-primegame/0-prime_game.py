#!/usr/bin/python3
""" Prime Game Problem """


def isWinner(x, nums):
    """Function to get who has won in prime game"""
    max_n = max(nums)
    primes = generate_primes(max_n)

    mariaWinsCount = 0
    benWinsCount = 0

    def determine_winner(n):
        """Determine winner for a given value of n"""
        if n < 2:
            return "Ben"

        is_prime_set = [True] * (n + 1)
        num_of_primes = 0

        for p in primes:
            if p > n:
                break
            if is_prime_set[p]:
                num_of_primes += 1
                for multiple in range(p, n + 1, p):
                    is_prime_set[multiple] = False

        return "Maria" if num_of_primes % 2 == 1 else "Ben"

        for n in nums:
            winner = determine_winner(n)
        if winner == "Maria":
            mariaWinsCount += 1
        else:
            benWinsCount += 1

    if mariaWinsCount > benWinsCount:
        return "Winner: Maria"
    elif benWinsCount > mariaWinsCount:
        return "Winner: Ben"
    else:
        return None


def generate_primes(max_n):
    """Generate a list of prime numbers up to max_n"""
    is_prime = [True] * (max_n + 1)
    p = 2
    while (p * p <= max_n):
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, max_n + 1) if is_prime[p]]
