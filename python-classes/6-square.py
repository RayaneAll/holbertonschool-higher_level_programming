#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a specific size.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square (x, y).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the size."""
        return self.__size

    @property
    def position(self):
        """Getter for the position."""
        return self.__position

    @size.setter
    def size(self, value):
        """Setter for the size.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Setter for the position.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
