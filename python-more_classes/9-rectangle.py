#!/usr/bin/python3
"""Used to create an empty class Rectangle that defines a rectangle"""


class Rectangle:
    """This class defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise Rectangle instances with parameters width and height"""
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Refer to the field width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Validate that width is a positive integer"""

        if not isinstance(value, int):
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

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints the rectangle with the character #"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rectangle = []
            for i in range(self.height):
                rectangle.append(str(self.print_symbol) * self.width)
            return "\n".join(rectangle)

    def __repr__(self):
        """Returns the string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Deletes the rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        elif Rectangle.area(rect_2) > Rectangle.area(rect_1):
            return rect_2

    def square(cls, size=0):
        """
        Class method that returns a new Rectangle instance
        """
        return cls(size)
