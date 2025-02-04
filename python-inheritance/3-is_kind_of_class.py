#!/usr/bin/python3
"""Module for is_kind_of_class method."""


def is_kind_of_class(obj, a_class):
    """Check if obj is instance of a_class or a class that inherited from."""
    return isinstance(obj, a_class)
