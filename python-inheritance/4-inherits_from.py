#!/usr/bin/python3

"""This module provides inherits_from function"""


def inherits_from(obj, a_class):
    """This function check obj is instace of a subclass inherits from a_class"""
    return issubclass(obj.__class__, a_class) and not obj.__class__ == a_class
