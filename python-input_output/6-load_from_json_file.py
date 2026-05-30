#!/usr/bin/python3
"""Create an Object"""
import json


def load_from_json_file(filename):
    """
    Function creates an Object from a JSON file
    """
    with open(filename, encoding="utf-8") as myFile:
        json.load(myFile.read(myFile))
