#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This is the Rectangle class that inherits from the BaseGeometry class.
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle object

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Return the area of the rectangle.

        Returns:
            The area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representaion of the rectangle

        Returns:
            The print() ad str() rep of the rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
