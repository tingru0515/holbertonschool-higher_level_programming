#!/usr/bin/python3

"""This module provides Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

ATTR_NAMES = {
    "WIDTH": "width",
    "HEIGHT": "height"
}


class Rectangle(BaseGeometry):
    """This class inherits from BaseGeometry class"""

    def __init__(self, width: int, height: int) -> None:
        self.__width = self.integer_validator(
            ATTR_NAMES["WIDTH"], width)
        self.__height = self.integer_validator(
            ATTR_NAMES["HEIGHT"], height)

    def __str__(self) -> str:
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self) -> int:
        return self.__width * self.__height

    def integer_validator(self, name: str, value: int) -> int:
        super().integer_validator(name, value)
        return value
