#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        Area = self.width * self.height
        return Area

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.height == 0 or self.width == 0:
            return 0
        perimeter = (self.width * 2) + (self.height * 2)
        return perimeter

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.height == 0 or self.width == 0:
            return ""
        lists = []
        for i in range(0, self.height):
            for i in range(0, self.width):
                lists.append("#")
            if i != self.__height - 1:
                lists.append('\n')
        return ("".join(lists))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rectangle = "Rectangle(" + str(self.width) + ", "
        rectangle += str(self.height) + ")"
        return rectangle

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
