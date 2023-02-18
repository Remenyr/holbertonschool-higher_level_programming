#!/usr/bin/python3
""" JSON representation of an object """


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)
    Args:
        my_obj: object to be represented in JSON
    """

    repres = json.dumps(my_obj)

    return repres
