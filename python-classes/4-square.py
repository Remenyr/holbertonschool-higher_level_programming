#!/usr/bin/python3
""" Class that defines a square """


class Square:
    """ Instantiation with validatios """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ Public instance method """
    def area(self):
        area = pow(self.__size, 2)
        return area
