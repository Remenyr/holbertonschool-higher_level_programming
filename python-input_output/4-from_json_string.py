#!/usr/bin/python3
"""
Module ``4-from_json_string``
Returns an object represented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    Rreturns an object (Python data structure) represented by a JSON string
    Args:
        my_str: representation to load from JSON
    """

    loaded = json.loads(my_str)

    return loaded
