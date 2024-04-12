#!/usr/bin/python3
"""
This is the '0-add_integer' module.

This module provides a function 'add_integer' that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Args:
        a (int/float): The first number to add.
        b (int/float, optional): The second number to add. Defaults to 98.

    Returns:
        int: The sum of a and b, casted to an integer.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
