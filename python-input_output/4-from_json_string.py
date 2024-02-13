#!/usr/bin/python3
"""This module provides from_json_string function"""

import json


def from_json_string(my_str: str) -> object:
    """This function deserialize the my_str"""
    return json.loads(my_str)
