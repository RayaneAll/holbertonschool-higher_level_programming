#!/usr/bin/python3
"""Defines an empty class Square."""


class Square:
    """An empty class that defines a square."""
    def __init__(self, size=0):
        self.__size = size
        try:
            size is int
        except:
            raise TypeError("size must be an integer")
        try:
            size >= 0
        except:
            raise ValueError("size must be >= 0")
