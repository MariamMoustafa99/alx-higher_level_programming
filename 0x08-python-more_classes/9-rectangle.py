#!/usr/bin/python3
"""
Defines a class Rectangle.
"""


class Rectangle:
    """Representation of a rectangle."""

        number_of_instances = 0
        """int: The number of active instances"""

        print_symbol = '#'
        """type: Print symbol, can be any type"""

    def __init__(self, width=0, height=0):
        """Constructor.

                Args:
                        width: the width of the rectangle
                        height: the height of the rectangle
                """
        self.height = height
        self.width = width
                Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for the private instance attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns printable string representation of the rectangle"""
        if not self.__width or not self.__height:
                        return ""
        return ((str(self.print_symbol) * self.width + "\n") *
                self.height)[:-1]

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""
        return ("Rectangle: ({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Print a message for every deletion of a rectangle"""
        print("Bye rectangle...")
                Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger of two rectangles.

        Args:
            rect_1: first rectangle
            rect_2: second rectangle
        Raises:
            TypeError: If rect_1, rect_2 are not instances of Rectangle.
        Returns:
            The rectangle with the larger area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Instantiates a new square.

        Args:
            size: the size of the new square.
        """
        return cls(size, size)
