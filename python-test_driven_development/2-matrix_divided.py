#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int/float): The divisor.

    Returns:
        list of lists: A new matrix with the divided elements, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats, 
                   or if div is not a number, or rows are not of the same size.
        ZeroDivisionError: If div is zero.
    """
    if (not isinstance(matrix, list) or 
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(el, (int, float)) for row in matrix for el in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(el / div, 2) for el in row] for row in matrix]
