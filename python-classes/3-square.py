#!/usr/bin/python3
"""This module creates an class Square that defines a square"""


class Square:
    """This class defines a square and validates if size is an integer """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Refer to the field size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Check if value for the size is an integer and positive"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def getArea(self):
        """Calculates the area of our square"""
        return int(self.__size) ** 2
