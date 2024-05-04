#!/usr/bin/python3
"""
Module containing script that adds all args to a python list
"""
import sys
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an obj to a text file, using JSON rep

    Args:
        my_obj: The object to write to the file
        filename (str): The name fo the file to write to.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
