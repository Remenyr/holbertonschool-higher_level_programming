#!/usr/bin/python3
""" Class MyList that inherits from list """


class MyList(list):
    """ Public instance method that prints the sorted list"""
    def print_sorted(self):
        print(sorted(self))
