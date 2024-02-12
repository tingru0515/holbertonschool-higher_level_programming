#!/usr/bin/python3

"""This module provides Square class"""


Rectangle = __import__('9-rectangle').Rectangle

ATTR_NAMES = {
    "SIZE": "size"
}


class Square(Rectangle):
    """This class inherits from Square class"""

    def __init__(self, size: int) -> None:
        self.__size = self.integer_validator(
            ATTR_NAMES["SIZE"], size)
        super().__init__(size, size)

    def __str__(self) -> str:
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self._Rectangle__width,
                                   self._Rectangle__height)

    def area(self) -> int:
        return self.__size ** 2

    def integer_validator(self, name: str, value: int) -> int:
        super().integer_validator(name, value)
        return value
