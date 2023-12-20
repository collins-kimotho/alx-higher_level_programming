#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Rep a Square."""

    def __init__(self, size=0):
        """Initailize a new Square.

        Args:
            size (int): The size of the new square. Defaults to 0.

        Raises:
            TypeError: if suze is not an integer.
            ValueError: if size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
