#!/usr/bin/python3
"""
Make change
"""

def makeChange(coins, total):
    """ 
    Determines the minimum number of coins needed
    to meet the given total amount using a greedy approach.
    
    Args:
        - coins: List of the values of the coins you possess.
        - total: The amount of change required.
        
    Returns:
        - The minimum number of coins needed to make the change,
          or -1 if the total cannot be met by any combination of coins.
    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)

    coins_needed = 0

    for coin in coins:
        if total // coin > 0:
            coins_needed += total // coin
            total %= coin

        if total == 0:
            break

    if total != 0 or coins_needed == 0:
        return -1

    return coins_needed

