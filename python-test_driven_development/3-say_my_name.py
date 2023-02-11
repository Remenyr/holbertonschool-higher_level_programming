#!/usr/bin/python3
""" Prints a full name """


def say_my_name(first_name, last_name=""):
    """
    first_name and last_name must be strings
    otherwise, it raises an exception
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
