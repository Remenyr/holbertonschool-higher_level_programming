#!/usr/bin/python3
""" Rectangle class module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from BaseGeometry """

    def __init__(self, width, height):
        """ Instantiation of class with two args: width and height """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ Method that returns the Rectangle description """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """ Implementation of area() method inherited from BaseGeometry """
        return self.__width * self.__height
