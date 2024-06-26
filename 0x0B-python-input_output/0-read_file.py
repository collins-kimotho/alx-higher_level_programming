#!/usr/bin/python3
"""
Module containing read file function
"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): The name of the file to read.
    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
