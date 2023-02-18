#!/usr/bin/python3
"""
Module ``pascal_triangle``
Generator of Pascal's triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n
    Args:
        - n: number of lines of Pascal's triangle
    """

    pascal = []
    numbers = []
    prev = []
    limit = 0

    if n <= 0:
        return pascal

    for line in range(n):
        numbers.append(1)

        if limit > 0:
            i = 0
            j = 1

            for index in range(limit - 1):
                numbers.append(prev[i] + prev[j])
                i += 1
                j += 1

            numbers.append(1)

        pascal.append(numbers)
        limit += 1
        prev = numbers
        numbers = []

    return pascal
