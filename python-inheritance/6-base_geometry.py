#!/usr/bin/python3
""" BaseGeometry class """


class BaseGeometry:
    """ Public instance method that raises an exception """
    def area(self):
        raise Exception("area() is not implemented")
