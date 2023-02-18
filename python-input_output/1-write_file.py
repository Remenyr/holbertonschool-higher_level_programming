#!/usr/bin/python3
""" Writes a string to a text file """


def write_file(filename="", text=""):
    """
    Writes a string to filename (UTF8)
    and returns the number of characters written
    Args:
        filename: file to overwrite
        text: string that will be writed to filename
    """

    with open(filename, 'w', encoding='UTF8') as file:
        chars_writt = file.write(text)

    return chars_writt
