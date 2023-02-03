#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for key, x in a_dictionary.items():
        new[key] = x * 2
    return new
