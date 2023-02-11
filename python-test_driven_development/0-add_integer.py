#!/usr/bin/python3
"""
Adds two integers
Returns the result
"""


def add_integer(a, b=98):
    """
    a and b must be an integer or an TypeError will be raised
    """
    try:
        if type(a) is float:
            a = int(a)
        elif type(b) is float:
            b = int(b)
        result = a + b
    except TypeError:
        if type(a) is not int:
            raise TypeError("a must be an integer")
        if type(b) is not int:
            raise TypeError("b must be an integer")
    return result
