#!/usr/bin/python3

def pascal_triangle(n):
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