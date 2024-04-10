#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Function to add two numbers

    Parameters
    a (int, float): the first number
    b (int, float): the second number, default is 98

    Returns:
    int: The sum of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
