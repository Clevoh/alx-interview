#!/usr/bin/python3
"""
method that calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""

def minOperations(n):
    if n <= 1:
        return 0
    
    ops = 0
    current = 1 
    
    for i in range(2, n + 1):
        while n % i == 0:
            ops += i
            n //= i
    
    return ops
