#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test cases for the max_integer function.
    """

    def test_return_value(self):
        """
        Test that the max_integer function returns the correct
        maximum value from a list of positive integers.
        """
        list = [1, 2, 3, 4]
        actual_value = max_integer(list)
        expected = 4
        self.assertEqual(actual_value, expected)

    def test_return_value2(self):
        """
        Test that the max_integer function returns the correct
        maximum value from a list of negative integers.
        """
        list = [-1, -2, -3, -4]
        actual_value = max_integer(list)
        expected = -1
        self.assertEqual(actual_value, expected)

    def test_return_value3(self):
        """
        Test that the max_integer function returns the correct
        maximum value from the list include a negative integer.
        """
        list = [1, 3000, -4]
        actual_value = max_integer(list)
        expected = 3000
        self.assertEqual(actual_value, expected)

    def test_max_in_middle(self):
        """
        Test that the max_integer function returns the correct
        maximum value where in the middle of the list
        """
        list = [1, 2, 600, 67, 3000, 4, 5, 9, 90]
        actual_value = max_integer(list)
        expected = 3000
        self.assertEqual(actual_value, expected)

    def test_return_value4(self):
        """
        Test that the max_integer function returns the correct
        maximum value if the list has just one value.
        """
        list = [1]
        actual_value = max_integer(list)
        expected = 1
        self.assertEqual(actual_value, expected)

    def test_empty_list(self):
        """
        Test that the max_integer function returns None when
        an empty list is provided.
        """
        actual_value = max_integer([])
        expected = None
        self.assertEqual(actual_value, expected)

    def test_no_arg(self):
        """
        Test that the max_integer function returns None when
        called with no arguments.
        """
        actual_value = max_integer()
        expected = None
        self.assertEqual(actual_value, expected)

    def test_not_int(self):
        """
        Test that the max_integer function raises a TypeError
        when a non-integer element is present in the list.
        """
        list = [1, 2, "3"]
        error_type = TypeError
        with self.assertRaises(error_type):
            max_integer(list)

    def test_tuple(self):
        """
        Test that the max_integer function correctly handles
        a tuple of integers.
        """
        tuple = (1, 2, 3)
        actual_value = max_integer(tuple)
        expected = 3
        self.assertEqual(actual_value, expected)
