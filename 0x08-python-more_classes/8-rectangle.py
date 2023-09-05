#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            for j in range(0, self.width):
                lists.append(str(self.print_symbol))
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
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.
        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        rec1 = Rectangle.area(rect_1)
        rec2 = Rectangle.area(rect_2)
        if rec1 > rec2:
            return rect_1
        elif rec1 == rec2:
            return rect_1
        else:
            return rect_2
