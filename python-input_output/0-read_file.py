#!/usr/bin/python3
"""
Module 0-read_file
Reads a text file and prints it
"""


def read_file(filename=""):
    """
    This function reads a text file (UTF8) and prints it to stdout
    Args:
        filename: name of the file to read
    """

    with open(filename, encoding='UTF8') as file:
        content = file.read()
        print(content, end="")
