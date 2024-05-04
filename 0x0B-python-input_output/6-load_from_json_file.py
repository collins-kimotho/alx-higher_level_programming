#!/usr/bin/python3
"""
Module containing load from json file function
"""
import json


def load_from_json_file(filename):
    """
    Function that creates an object from a JSON file

    Args:
        filename (str): The name of the JSON file to read from.

    Return:
        The python data structure rep by the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
