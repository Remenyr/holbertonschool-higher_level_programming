#!/usr/bin/python3
""" Splits a string after these characters: ., ? or : """


def text_indentation(text):
    """
    text must be a string or an exception will be raised
    Prints a text with 2 new lines after each of the characters (., ? or :)
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    beg = 0
    for c in text:
        if beg == 1:
            if c == " ":
                continue
            beg = 0
        if c == '.' or c == '?' or c == ':':
            print(f"{c}\n")
            beg = 1
        else:
            print(c, end="")
