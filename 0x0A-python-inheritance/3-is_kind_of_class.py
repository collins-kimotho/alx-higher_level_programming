#!/usr/bin/python3
""" This is the '3-is_kinf_of_class' module"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an ob is an instance, or if obj is an instance of a class

    Args:
        obj: The object to check
        a_class: The class to check against.

    Returns:
        True if the obj is an instance, or if the obj is an instance of a class
    """
    return isinstance(obj, a_class)
