#!/usr/bin/python3
"""This module provides MyList class inheited from list class"""


class MyList(list):
    """MyClass inherit from list class"""

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)