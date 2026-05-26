#!/usr/bin/python3
"""Used to create an empty class Rectangle that defines a rectangle"""


class Rectangle:
    """This class defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialise Rectangle instances with parameters width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Refer to the field width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Validate that width is a positive integer"""

        if isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Refer to the field height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Validate that height is a positive integer"""

        if isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
