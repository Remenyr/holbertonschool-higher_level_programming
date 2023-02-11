#!/usr/bin/python3
""" Class with validations and method """


class Square:
    """ Instantiation with validatios """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """ Public instance method """
    def area(self):
        area = pow(self.__size, 2)
        return area
