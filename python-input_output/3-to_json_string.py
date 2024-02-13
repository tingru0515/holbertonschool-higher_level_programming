#!/usr/bin/python3
"""This module provides to_json_string function"""


import json


def to_json_string(my_obj: object) -> str:
    """ This function serialize the my_obj"""
    return json.dumps(my_obj)
