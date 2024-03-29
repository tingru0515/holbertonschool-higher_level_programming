#!/usr/bin/python3
"""write a function that prints a square witht the character #"""


def print_square(size):
    """
    Prints a square with the character #.

    Parameters:
      size (int): The size length of the square.

    Raises:
      TypeError: If size is not an integer.
      ValueError: If size is less than 0.
      TypeError: If size is a float and is less than 0.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for i in range(size):
            print("#", end="")
        print()
