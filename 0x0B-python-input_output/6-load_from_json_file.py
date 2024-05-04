#!/usr/bin/python3
"""
Module containing save_to_json_file function
"""
import json


def load_from_json_file(filename):
    """
    Function that writes an object to a text file, using JSON rep

    Args:
        my_obj: The object to write to the file
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
