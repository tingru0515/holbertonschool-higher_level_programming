#!/usr/bin/python3
"""Module: 0-square.py

This module provides a simple implementation of a Square class.

Classes:
    Square: Represents a square shape.

Usage:
    Square = __import__('0-square').Square

    # Example usage
    square = Square()
"""


class Square:
    """Represents a square shape.

    Attributes:
        None

    Methods:
        None

    Usage:
        from square import Square

        # Create a square object
        square = Square()
    """

    def __init__(self, size):
        self.__size = size
