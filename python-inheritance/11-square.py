#!/usr/bin/python3
""" Square class module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle class """

    def __init__(self, size):
        """ Instantiation of class whit an arg: size of the Square """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """ Magic method that returns Square description """
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """ Method that returns the Square area """
        return self.__size ** 2
