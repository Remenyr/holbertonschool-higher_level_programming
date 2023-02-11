#!/usr/bin/python3
""" Prints a square with the character # """


def print_square(size):
    """
    size is the size of the square
    size must be an integer greater than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()
