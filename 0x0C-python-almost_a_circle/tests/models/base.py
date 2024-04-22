#!/usr/bin/python3
"""This is the base module"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base Class

        Args:
            id (int, optional): Id of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
