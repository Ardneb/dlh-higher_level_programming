#!/usr/bin/python3
"""Write a string to a text file"""


def write_file(filename="", text=""):
    """
    Function writes a string to a text file
    and returns the number of characters written
    """

    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)
        return len(text)
