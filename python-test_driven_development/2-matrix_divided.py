#!/usr/bin/python3
"""write a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Parameters:
      matrix (list of lists): The matrix to be divided.
      div (int or float): The number to divide each element of the matrix.

    Returns:
      list of lists: A new matrix where each element is divided by div and rounded to 2 decimal places.

    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = []
    for row in matrix:
        if not all(isinstance(val, int) for val in row) or not all(isinstance(val, int) for val in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        new_row = [round(element / div, 2) for element in row]
        result_matrix.append(new_row)

    return result_matrix
