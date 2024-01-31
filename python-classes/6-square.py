#!/usr/bin/python3
"""Class that defines a square with size and position attributes."""


class Square:
    """Class that defines a square with size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization method with optional size and position attributes.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.

        Raises:
            TypeError: If size is not an integer or if position is
            not a tuple of 2 positive integers.
            ValueError: If size is less than 0 or if position values
            are not positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method to retrieve the value of size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the value of size.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the value of position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the value of position.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#' using position attribute."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
