#!/usr/bin/python3
"""Append a string to a text file"""


def append_write(filename="", text=""):
    """Function appends a string at the end of a text file
    and returns the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        myfile.write(text)
        return len(text)
