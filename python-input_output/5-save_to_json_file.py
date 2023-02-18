#!/usr/bin/python3
"""
Module ``5-save_to_json_file.py``
Writes an Object to a text file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file using a JSON representation
    Args:
        my_obj: object to represent in JSON and write to a text file
        filename: text file
    """

    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
