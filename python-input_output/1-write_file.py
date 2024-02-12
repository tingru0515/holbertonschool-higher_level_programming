#!/usr/bin/python3
"""This module provides write_file function"""


def write_file(filename: str = "", text: str = "") -> int:
    """This function write the text to the file"""
    with open(filename, mode='w', encoding="utf-8") as file:
        count = file.write(text)
        return count
