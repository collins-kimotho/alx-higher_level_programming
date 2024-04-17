#!/user/bin/python3
"""This is the '4-inherits_from' module"""


def inherits_from(obj, a_class):
    """
    Checks if an obj is an instance of a classs inherited from specified class

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True/ False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
