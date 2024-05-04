#!/usr/bin/python3
"""
Module containing the json to string function
"""
import json


def to_json_string(my_obj):
    """
    Function that returns the JSON rep of an object

    Args:
        my_obj: The object to convert to JSON string.

    Returns:
        str: The JSON representation of my_obj
    """
    return json.dumps(my_obj)
