#!/usr/bin/python3
"""
Function that returns True if the object is
an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    If the object is exactly an instance, returns True
    otherwise, returns false
    """
    if type(obj) is a_class:
        return True
    else:
        return False
