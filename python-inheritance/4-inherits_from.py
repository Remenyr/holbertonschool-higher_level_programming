#!/usr/bin/python3
"""
Checks if the object is an instance of a class
that inherited from the specified class.
"""


def inherits_from(obj, a_class):
    """
    If the object is an instance of a class that inherited from
    the specified class (directly or indirectly), returns True.
    Otherwise, returns False.
    """

    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
