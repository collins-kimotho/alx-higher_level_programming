#!/usr/bin/python3
"""This is the '7_base_geometry' module"""


class BaseGeometry:
    """
    This is the 'BaseGeometry' class

    The class contains two methods: 'area' and 'integer_validator'.
    """

    def area(self):
        """
        Raise an exception

        This method is meant to be overriden by subclasses.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the 'value' is a postive integer.

        Args:
            name: The name fo the value, assumed to be a string.
            value: The value to validate.

        Raises:
            TypeError: If 'value' is not an integer
            ValueError: If 'value' is les than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
