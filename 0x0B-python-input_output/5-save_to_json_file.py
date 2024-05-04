#!/usr/bin/python3
"""
Module containing save to json file function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an object to a text file

    Args:
        my_obj: The object to write to the file.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
