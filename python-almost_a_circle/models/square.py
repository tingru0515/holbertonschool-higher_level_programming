#!/usr/bin/python3

""" This module provides square class.
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square.

    Attributes:
        size (int): The side length of the square.
        x (int): X-coordinate of the square's position.
        y (int): Y-coordinate of the square's position.
        id: An optional identifier for the square.
    """

    ATTR_NAMES = {
        "ID": "id",
        "SIZE": "size",
        "X": 'x',
        "Y": 'y'
    }

    def __init__(self, size: int, x: int = 0, y: int = 0, id: int = None):
        """
        Initializes an instance of the Square class.

        Parameters:
        - size (int): The side length of the square.
        - x (int): X-coordinate of the square's position (default is 0).
        - y (int): Y-coordinate of the square's position (default is 0).
        - id (int): An optional identifier for the square (default is None).

        Returns:
        None
        """
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """
        Returns a string representation of the square.

        Returns:
        str: String representation of the square.
        """
        return "[{}] ({}) {}/{} - {}".format(
            __class__.__name__, self.id, self.x,
            self.y, self.height)

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
        int: The side length of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Parameters:
        - value: New value for the size attribute.

        Returns:
        None
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs) -> None:
        """
        Updates attributes of the square based on positional
        and keyword arguments.

        Parameters:
        - *args: Positional arguments representing ID, size, x, and y.
        - **kwargs: Keyword arguments representing attributes to be updated.

        Returns:
        None
        """
        ATTR_NAMES = {
            "ID": "id",
            "SIZE": "size",
            "X": 'x',
            "Y": 'y'
        }
        if len(args):
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        elif len(kwargs.keys()):
            for key, val in kwargs.items():
                if key == ATTR_NAMES["ID"]:
                    self.id = val
                elif key == ATTR_NAMES["X"]:
                    self.x = val
                elif key == ATTR_NAMES["Y"]:
                    self.y = val
                elif key == ATTR_NAMES["SIZE"]:
                    self.size = val

    def to_dictionary(self):
        """
        Returns a dictionary representation of the square.

        Returns:
        dict: Dictionary representation of the square.
        """
        temp_dict = {}
        for i in Square.ATTR_NAMES.values():
            temp_dict[i] = getattr(self, i)
        return temp_dict
