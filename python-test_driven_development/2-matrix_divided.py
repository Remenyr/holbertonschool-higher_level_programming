#!/usr/bin/python3
"""
Divides a matrix
"""


def matrix_divided(matrix, div):
    """
    matrix must be a list of lists
    Each row of the matrix must be of the same size
    div must be a number different to 0
    If any contition is false, an error will be raised
    """
    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
    elif div == float('inf'):
        raise OverflowError("cannot convert float infinity to integer")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) is not float and type(element) is not int:
                raise TypeError("matrix must be a \
matrix (list of lists) of integers/floats")
    new_m = [[round(element / div, 2) for element in row]for row in matrix]
    return new_m
