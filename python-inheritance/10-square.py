#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """A class with attributes and methods for geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a given value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A class with attributes and methods for a rectangle."""

    def __init__(self, width, height):
        """Instantiation with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns string representation of rectangle using #."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def print(self):
        """Prints the rectangle using #."""
        print(str(self))


class Square(Rectangle):
    """A class with attributes and methods for a square."""

    def __init__(self, size):
        """Instantiation with size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the Square."""
        return self.__size ** 2
