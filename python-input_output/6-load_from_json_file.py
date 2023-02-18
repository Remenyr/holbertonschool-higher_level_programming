#!/usr/bin/python3
"""
Module ``6-load_from_json_file.py
Creates an Object from a JSON file
"""


import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file
    Args:
        filename: JSON file to creates the Object from
    """

    with open(filename) as jfile:
        des_object = json.load(jfile)

    return des_object
