#!/usr/bin/python3
"""Module for inherits_from method."""


def inherits_from(obj, a_class):
    """Check if obj is instance of a_class or a class that inherited from."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
