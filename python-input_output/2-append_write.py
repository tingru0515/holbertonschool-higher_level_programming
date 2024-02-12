#!/usr/bin/python3
"""This module provides append_write function"""


def append_write(filename: str = "", text: str = "") -> int:
    """This function append the text to the file at the last content"""
    with open(filename, mode='a+', encoding="utf-8") as file:
        count = file.write(text)
        return count
