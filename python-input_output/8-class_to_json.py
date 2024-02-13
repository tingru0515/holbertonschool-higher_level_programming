#!/usr/bin/python3
"""This module provides class_to_json function"""


def class_to_json(obj: object) -> dict:
    """This function retrieve dict from the object"""
    obj_dict = obj.__dict__
    return obj_dict
