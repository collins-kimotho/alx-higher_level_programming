#!/usr/bin/python3
"""
Module containing the write file function
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text

    Args:
        filename (str): The name of the file to write to
        text (str): The text to write the file
    Returns:
        int: The number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
