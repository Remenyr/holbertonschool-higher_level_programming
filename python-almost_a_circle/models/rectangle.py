#!/usr/bin/python3
"""
Module Name: rectangle
Module Description:
This module contains only one Class
Module Classes:
- Rectangle
Module Attributes:
- None
"""
from models.base import Base


def check_integer(value, name):
    """
    Is a helper function to check if the passed parameter
    is an integer and raise an appropriate error message if it is not.
    Raises a TypeError if the value is not an integer.
    Raises a ValueError if the value is less than or equal to 0 for width
    and height properties, and less than 0 for x and y properties.
    """
    under_equals = ["width", "height"]
    under = ["y", "x"]

    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if name in under_equals:
        if value <= 0:
            raise ValueError(f"{name} must be > 0")
    if name in under:
        if value < 0:
            raise ValueError(f"{name} must be >= 0")


class Rectangle(Base):
    """
    Represents a rectangle with dimensions and coordinates,
    which is a subclass of Base.
    Attributes:
    ------------
    Width: The width of the rectangle.
    Height: The height of the rectangle.
    X: The x coordinate of the rectangle.
    Y: The y coordinate of the rectangle.
    """
    def __init__(self, width: int, height: int, x=0, y=0, id=None):
        """
        Initializes a new Rectangle object with
        the given dimensions and coordinates.
        Width: An integer representing the width of the rectangle.
        Height: An integer representing the height of the rectangle.
        X: An integer representing the x coordinate of the rectangle.
           Default is 0.
        Y: An integer representing the y coordinate of the rectangle.
           Default is 0.
        Id: An integer representing the unique identifier of the rectangle.
            Default is None.
        """
        check_integer(width, "width")
        check_integer(height, "height")
        check_integer(x, "x")
        check_integer(y, "y")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self) -> int:
        """Returns the value of the __width attribute"""
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        """Sets the value of the __width attribute"""
        check_integer(value, "width")
        self.__width = value

    @property
    def height(self) -> int:
        """Returns the value of the __height attribute"""
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        """Sets the value of the __height attribute"""
        check_integer(value, "height")
        self.__height = value

    @property
    def x(self) -> int:
        """Returns the value of the __x attribute"""
        return self.__x

    @x.setter
    def x(self, value: int) -> None:
        """Sets the value of the __x attribute"""
        check_integer(value, "x")
        self.__x = value

    @property
    def y(self) -> int:
        """Returns the value of the __y attribute"""
        return self.__y

    @y.setter
    def y(self, value: int) -> None:
        """Sets the value of the __y attribute"""
        check_integer(value, "y")
        self.__y = value

    def area(self) -> float:
        """
        Method that calculates the area of the
        rectangle and returns it as a float.
        """
        return self.__width * self.__height

    def display(self) -> None:
        """
        Method that prints out the rectangle using the print function.
        It first prints out the correct number of newlines based on the
        value of __y. Then, for each row of the rectangle, it prints out
        the correct number of spaces based on the value of __x, followed
        by the correct number of # characters based on the value of __width.
        """
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self) -> str:
        """
        Method that returns a string representation of the rectangle.
        The string is in the format [Rectangle] (<id>) <x>/<y> -
        <width>/<height>, where <id>, <x>, <y>, <width>,
        and <height> are replaced with the actual
        values of the corresponding instance variables.
        """
        return_value = f"[{self.__class__.__name__}] ({self.id})"
        return_value = f"{return_value} {self.__x}/{self.__y}"
        return_value = f"{return_value} - {self.__width}/{self.__height}"
        return return_value

    def update(self, *args, **kwargs) -> None:
        """
        Update the rectangle attributes.
        Args:
        ------
        *args: Variable length argument list representing
        the attributes in the following order:
            - id (optional): int
            - width (optional): int
            - height (optional): int
            - x (optional): int
            - y (optional): int
            Only the attributes included in the argument list will be updated.
        **kwargs: Arbitrary keyword arguments representing
                  the attributes and their values.
                  Only the attributes included in the keyword
                  argument list will be updated.
        Raises:
            TypeError: If any of the arguments have an incorrect type.
            ValueError: If any of the arguments have an incorrect value.
        Returns:
            None.
        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args:
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    self.__setattr__(key, value)

    def to_dictionary(self) -> dict:
        """
        Returns the dictionary representation of a Rectangle or Square instance
        Returns:
            A dictionary with keys:
            - "id": int - the id of the instance
            - "width": int - the width of the instance
            - "height": int - the height of the instance
            - "x": int - the x-coordinate of the instance
            - "y": int - the y-coordinate of the instance
        """
        dictionary_representation = \
            {
                "x": self.x,
                "y": self.y,
                "id": self.id,
                "height": self.height,
                "width": self.width
            }
        return dictionary_representation
