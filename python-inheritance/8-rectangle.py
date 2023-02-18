#!/usr/bin/python3
""" Rectrangle class module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class inherits from BaseGeometry """

    def __init__(self, width, height):
        """ Instantiation of class with two args: width and height """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
