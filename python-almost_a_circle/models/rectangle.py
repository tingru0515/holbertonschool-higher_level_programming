#!/usr/bin/python3

""" This module proivides Rectangle class inherited from Base class.
"""

from .base import Base


class Rectangle(Base):
    """
    This class inherits Base class, and create
    an instance representing rectangle.

    Constructor(self, width: int, height: int, x: int = 0,
    y: int = 0, id: int = None) -> None):
        create an instance representing rectangle.

    Methods:
        - width: this is property to return and set __width attribute.
        - height: this is property to return and set __height attribute.
        - x: this is property to return and set __x attribute.
        - y: this is property to return and set __y attribute.
        - area(self) -> int: calculate width and height and return the area.
        - display(self) -> None: print rectangle with #.
    """
    ATTR_NAMES = {
        "ID": "id",
        "WIDTH": "width",
        "HEIGHT": "height",
        "X": 'x',
        "Y": 'y'
    }

    def __init__(self, width: int, height: int, x: int = 0,
                 y: int = 0, id: int = None) -> None:
        """
        Initializes an instance representing a rectangle.

        Parameters:
        - width (int): Width of the rectangle.
        - height (int): Height of the rectangle.
        - x (int): X-coordinate of the rectangle (default is 0).
        - y (int): Y-coordinate of the rectangle (default is 0).
        - id (int): Identifier for the rectangle (default is None).

        Returns:
        None
        """
        self.validator(**{"width": width, "height": height, 'x': x, 'y': y})
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def validator(self, **kwargs: dict) -> None:
        """
        Validates input values for specific attributes.

        Parameters:
        - **kwargs (dict): Keyword arguments representing
        attribute names and their values.

        Raises:
        - TypeError: If the value is not an integer for
        the specified attribute.
        - ValueError: If the value is less than or equal
        to 0 for 'width' or 'height',
        or less than 0 for 'x' or 'y'.

        Returns:
        None
        """
        for key, val in kwargs.items():
            if type(val) is not int:
                raise TypeError(
                    "{} must be an integer".format(key))
            if key in ("width", "height") and val <= 0:
                raise ValueError("{} must be > 0".format(key))
            if key in ('x', 'y') and val < 0:
                raise ValueError("{} must be >= 0".format(key))

    def __str__(self) -> str:
        """
        Returns a string representation of the rectangle.

        Returns:
        str: String representation of the rectangle.
        """

        return "[{}] ({}) {}/{} - {}/{}".format(
            __class__.__name__, self.id, self.__x,
            self.__y, self.__width, self.__height)

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
        int: Width of the rectangle.
        """

        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        """
        Setter method for the width attribute.

        Parameters:
        - value (int): New value for the width attribute.

        Returns:
        None
        """

        self.validator(**{"width": value})
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
        int: Height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        """
        Setter method for the height attribute.

        Parameters:
        - value (int): New value for the height attribute.

        Returns:
        None
        """

        self.validator(**{"height": value})
        self.__height = value

    @property
    def x(self):
        """
        Getter method for the x attribute.

        Returns:
        int: X-coordinate of the rectangle.
        """

        return self.__x

    @x.setter
    def x(self, value: int) -> None:
        """
        Setter method for the x attribute.

        Parameters:
        - value (int): New value for the x attribute.

        Returns:
        None
        """

        self.validator(**{'x': value})
        self.__x = value

    @property
    def y(self):
        """
        Getter method for the y attribute.

        Returns:
        int: Y-coordinate of the rectangle.
        """

        return self.__y

    @y.setter
    def y(self, value: int) -> None:
        """
        Setter method for the y attribute.

        Parameters:
        - value (int): New value for the y attribute.

        Returns:
        None
        """

        self.validator(**{'y': value})
        self.__y = value

    def area(self) -> int:
        """
        Calculates and returns the area of the rectangle.

        Returns:
        int: Area of the rectangle.
        """

        return self.__height * self.__width

    def display(self) -> None:
        """
        Prints a representation of the rectangle using '#'.

        Returns:
        None
        """

        for _ in range(self.__y):
            print()
        x = ' ' * self.__x
        for _ in range(self.__height):
            print(x, end='')
            for _ in range(self.__width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs) -> None:
        """
        Updates attributes of the rectangle based
        on positional and keyword arguments.

        Parameters:
        - *args: Positional arguments representing ID, width, height, x, and y.
        - **kwargs: Keyword arguments representing attributes to be updated.

        Returns:
        None
        """

        ATTR_NAMES = {
            "ID": "id",
            "WIDTH": "width",
            "HEIGHT": "height",
            "X": 'x',
            "Y": 'y'
        }
        if len(args):
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]

        if len(kwargs.keys()):
            for key, val in kwargs.items():
                if key == ATTR_NAMES["ID"]:
                    self.id = val
                elif key == ATTR_NAMES["X"]:
                    self.x = val
                elif key == ATTR_NAMES["Y"]:
                    self.y = val
                elif key == ATTR_NAMES["WIDTH"]:
                    self.width = val
                elif key == ATTR_NAMES["HEIGHT"]:
                    self.height = val

    def to_dictionary(self):
        """
        Returns a dictionary representation of the rectangle.

        Returns:
        dict: Dictionary representation of the rectangle.
        """

        temp_dict = {}
        for i in Rectangle.ATTR_NAMES.values():
            temp_dict[i] = getattr(self, i)
        return temp_dict
