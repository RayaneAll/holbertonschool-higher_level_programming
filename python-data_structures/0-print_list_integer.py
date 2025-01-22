#!/usr/bin/python3
# This script defines a function that prints all integers in a list.

def print_list_integer(my_list=[]):
    """
    Prints all integers in the provided list.

    Args:
        my_list (list): A list of integers. Defaults to an empty list.
    """
    for item in my_list:  # Iterate through each item in the list
        print('{:d}'.format(item))  # Print each item as a formatted integer
