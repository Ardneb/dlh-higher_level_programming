#!/usr/bin/python3
"""Load, add, save"""
import json
import sys


"""Use the functions created earlier"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

"""Load the json file"""
try:
    items = load_from_json_file("add_item.json")
except OSError:
    items = []

"""Add the arguments"""
for arg in sys.argv[1:]:
    items.append(arg)

"""Save added arguments to file"""
save_to_json_file(items, "add_item.json")
