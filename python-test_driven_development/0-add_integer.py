#!/usr/bin/python3
"""write a function that add 2 integers"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
      a (int or float): The first integer.
      b (int or float): The second integer (default is 98).

    Returns:
      int: The sum of a and b.

    Raises:
      TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise ValueError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise ValueError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
