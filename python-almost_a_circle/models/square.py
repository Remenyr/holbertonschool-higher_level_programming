#!/usr/bin/python3
"""
Module Name: square
Module Description:
This module contains only one Class
Module Classes:
- Square
Module Attributes:
- None
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class that represents a square.
    Attributes:
        Size (int): The size of the square.
        X (int): The x-coordinate of the square's top-left corner.
        Y (int): The y-coordinate of the square's top-left corner.
        Id (int): The unique identifier of the square.
    """
    def __init__(self, size: int, x=0, y=0, id=None):
        """
        Initializes a new Square instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self) -> int:
        """ Getter of the size of the square """
        return self.height

    @size.setter
    def size(self, value: int) -> None:
        """ Setter of the size of the square """
        self.width = value
        self.height = value

    def __str__(self) -> str:
        """
        Returns a string representation of the square.
        Returns:
            str: A string in the format "[Square] (<id>) <x>/<y> - <size>".
        """
        return_value = f"[{self.__class__.__name__}] ({self.id})"
        return f"{return_value} {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs) -> None:
        """
        The update method updates the attributes of the current Square
        instance based on given arguments or keyword arguments.
        Parameters
        ------------
        Self: The current instance of the Square class
        *args: An arbitrary number of positional arguments.
               These arguments should be in the following order:
               id, size, x, and y.
        **kwargs: An arbitrary number of keyword arguments.
                  These arguments should correspond to attributes
                  of the Square class. If the keyword matches an
                  attribute of the Square class, the value will be used
                  to update the attribute of the current instance.
        Returns
        ---------
        This method does not return anything. It simply
        updates the attributes of the current instance.
        """
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    self.__setattr__(key, value)

    def to_dictionary(self) -> dict:
        """
        Returns a dictionary representation of a Square instance.
        The dictionary contains the keys "x", "y", "id", and "size",
        with their corresponding values being the x and y coordinates,
        the unique id attribute, and the size of the square.
        This method takes no parameters, and simply returns the dictionary
        representation of the instance.
        """
        dictionary_representation = \
            {
                "x": self.x,
                "y": self.y,
                "id": self.id,
                "size": self.size
            }
        return dictionary_representation
