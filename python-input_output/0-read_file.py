#!/usr/bin/python3
def read_file(filename=""):
    """function reads a text file and prints it"""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read())
