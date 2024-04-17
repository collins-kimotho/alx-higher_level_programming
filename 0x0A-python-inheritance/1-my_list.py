#!/usr/bin/python3
"""
This is the "my_list" module
"""


class MyList(list):
    """
    This is a class that inherits from the build in list class

    The class contains a method that prints the list in ascending order
    """

    def print_sorted(self):
        """
        Print the list in ascending order
        """
        print(sorted(self))
