#!/usr/bin/env python3
"""
task_00_basic_serialization.py:
Module to serialize a dictionary into a JSON file and deserialize it back.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary into a JSON file.
     Args:
        data (dict): Dictionary to serialize.
        filename (str): Filename to save the JSON data
    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def load_and_deserialize(filename):
    """
    Loads and deserializes a JSON file into a Python dictionary.
    Args:
        filename (str): The JSON file to read.
    Returns:
        dict: The deserialized dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
