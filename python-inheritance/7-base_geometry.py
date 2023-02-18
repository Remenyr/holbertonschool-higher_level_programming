#!/usr/bin/python3
""" BaseGeometry class """


class BaseGeometry:
    """ Public instance method that raises an exception """
    def area(self):
        raise Exception("area() is not implemented")

    """
    Public instance method that validates if value is
    an integer and greater than zero
    """
    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if type(value) != int:
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
