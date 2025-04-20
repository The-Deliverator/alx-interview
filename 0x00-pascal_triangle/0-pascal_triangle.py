#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Returns a list of lists representing 
    the Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        curr = triangle[i - 1]
        for j in range(1, i):
            row.append(curr[j - 1] + curr[j])
        row.append(1)
        triangle.append(row)

    return triangle
