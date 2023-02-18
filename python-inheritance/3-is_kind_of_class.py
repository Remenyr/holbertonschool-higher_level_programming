#!/usr/bin/python3
""" Check if an object is an instance of a class """


def is_kind_of_class(obj, a_class):
    """
    If the object is an instance of the specified class or if the object
    is an instance of a class that inherited from, returns True
    Otherwise, returns False
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
