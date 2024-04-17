#!/usr/bin/python3
"""
This module demonstrates the creation of a python project
"""

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        List of available attributes and methods of an object.
    """
    return dir(obj)
