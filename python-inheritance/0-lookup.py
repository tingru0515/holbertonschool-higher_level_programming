#!/usr/bin/python3

"""Returns a list of attributes and methods"""


def lookup(obj: object) -> list:
    """Return a list of attriibutes"""
    return dir(obj)