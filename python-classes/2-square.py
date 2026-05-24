#!/usr/bin/python3
"""This module creates an class Square that defines a square"""


class Square:
    """This class defines a square"""
    def __init__(self, size="0"):
        self.__size = size  # private attribute

    @size.setter
    def size(self, value):

        if isinstance(value, int):
            self.__size = value
        elif value < 0:
            print("size must be >= 0")
        else:
            print("size must be an integer")
