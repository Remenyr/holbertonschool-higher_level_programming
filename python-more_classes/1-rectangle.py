#!/usr/bin/python3
""" Class that defines a rectangle """


class Rectangle:
    """
    class defined by width and height
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    """ setter and getter of height property """
    @property
    def height(self):
        """ Retrieves the instance's height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ setter and getter of width property """
    @property
    def width(self):
        """ Retrieves the instance's width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
