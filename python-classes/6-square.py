#!/usr/bin/python3
"""This module creates a class Square that defines a square"""


class Square:
    """This class defines a square and validates if size is an integer"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance with an optional size parameter"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Refer to the field position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Check if position is a tuple of 2 positive integers"""

        if (not isinstance(value, tuple) or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates the area of our square"""
        return self.__size ** 2

    def my_print(self):
        """prints the square with the character #"""
        if self.size == 0:
            print()
        elif self.position[1] > 0:
            for i in range(self.position[1]):
                print()
        elif self.position[0] > 0:
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
