#!/usr/bin/python3
"""
Defines a class Rectangle and inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This is the 'Rectangle class and inherits from the 'BaseGeometry' class.
    """

    def __init__(self, width, height):
        """
        Initialize a 'Recatangle' object

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
