#!/usr/bin/python3
"""
Module containing append write function
"""


def to_json_string(my_obj):
    """
    Function that appends a string at the end of a text file.

    Args:
        filename (str): The name of the file to append
        text (str): The text to append the file.
    Returns:
        int: The number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
