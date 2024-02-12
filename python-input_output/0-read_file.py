#!/usr/bin/python3
"""This module provides read_file function"""


def read_file(filename: str = ""):
    """This function read the file contents and print it"""
    with open(filename, mode='r', encoding="utf-8") as file:
        contest = file.read()
        print(contest, end="")
