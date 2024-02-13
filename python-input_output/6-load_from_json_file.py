#!/usr/bin/python3
"""This module provides load_from_json_file"""
import json


def load_from_json_file(filename: str) -> object:
    """This function opem the file and create python object"""
    with open(filename, mode='r', encoding="utf-8") as file:
        python_obj = json.load(file)

        return python_obj
