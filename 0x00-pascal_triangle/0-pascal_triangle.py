#!/usr/bin/python3
"""
This module contains a function to generate Pascal's Triangle.
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        list of lists: A list containing lists, each representing a row of Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        temp = [1]
        for j in range(1, i):
            temp.append(triangle[i-1][j-1] + triangle[i-1][j])
        temp.append(1)
        triangle.append(temp)

    return triangle