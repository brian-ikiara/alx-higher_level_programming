#!/usr/bin/python3
"""Introduction to JSON."""
import json


def load_from_json_file(filename):
    """Read from JSON file and create a Python object.

    Args:
        filename ('obj':'file'): File

    Returns:
        A Python object.

    """
    with open(filename, 'r', encoding='UTF-8') as myFile:
        return json.loads(myFile.read())
