#!/usr/bin/python3
"""defines a square by based on 1-square.py"""


class Square:
    """private instance attribute size"""

    def __init__(self, size=0):
    def setter(self, new_value):
        if isinstance(new_value, int):
            if new_value < 0:
                raise ValueError("size must be >= 0")
            self.__size = new_value
        else:
            raise TypeError("size must be an integer")
