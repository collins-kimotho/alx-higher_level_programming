#!/usr/bin/python3
""" This is the '2-is_same_class' module"""


def is_same_class(obj, a_class):
    """
    Checks if an obj is exactly an instance of the specified class.

    Args:
        obj: The object to check
        a_class: The class to check against.

    Returns:
        True if the obj is exactly an instance, otherwise False.
    """
    return type(obj) is a_class
