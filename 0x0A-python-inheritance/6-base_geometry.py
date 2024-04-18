#!/usr/bin/python3
"""This is the '6-base_geometry' module"""


class BaseGeometry:
    """
    This class contains a method 'area'
    """
    def area(self):
        """
        Raise an Exeption with a message
        This method is meant to be overridden by subclasses
        """
        raise Exception("area() is not implemented")
