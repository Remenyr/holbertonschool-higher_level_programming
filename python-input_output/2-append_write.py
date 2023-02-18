#!/usr/bin/python3
""" Appends a string to a text file """


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    Args:
        filename: file to appends the string
        text: string
    """

    with open(filename, 'a', encoding='UTF8') as file:
        chars_writt = file.write(text)

    return chars_writt
