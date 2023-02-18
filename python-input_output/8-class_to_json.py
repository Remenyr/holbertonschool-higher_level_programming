#!/usr/bin/python3
"""
Module ``8-class_to_json``
Returns the dictionary description
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    Args:
        obj: instance of a Class
    """
    return obj.__dict__
