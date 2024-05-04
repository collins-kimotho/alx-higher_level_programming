#!/usr/bin/python3
"""
Module containing from_json_string function
"""
import json


def from_json_string(my_str):
    """
    Function that returns an object rep by a JSON string.

    Args:
        my_str (str): The JSON string to convert to python object.
        
    Returns:
        The python data structure represented by my_str
    """
    return json.loads(my_str)
