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
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
