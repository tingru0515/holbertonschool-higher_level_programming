#!/usr/bin/python3
"""This script add all arguments to list and save them to a file"""
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
args = sys.argv
python_list = []
try:
    python_list = load_from_json_file(filename)
    python_list += args[1:]
except FileNotFoundError:
    if len(args) > 1:
        python_list = args[1:]
except IndexError:
    pass
finally:
    save_to_json_file(python_list,  filename)
