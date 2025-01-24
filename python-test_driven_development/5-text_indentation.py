#!/usr/bin/python3
"""
This module provides a function to print text with 2 new lines
after certain characters (., ?, :).
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':'.

    Args:
        text (str): The input text to process.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    special_chars = ".?:"
    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in special_chars:
            result += "\n\n"
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1  # Skip extra spaces
        i += 1

    print(result.strip())
