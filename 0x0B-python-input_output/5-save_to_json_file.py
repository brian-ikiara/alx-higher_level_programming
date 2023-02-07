#!/usr/bin/python3
"""Introduction to JSON."""
import json


def save_to_json_file(my_obj, filename):
    """Write JSON data into a file.

    Args:
        my_obj ('obj':'any'): Python object
        filename ('obj':'file':'UTF-8'): File

    Returns:
        A JSON file.

    """
    with open(filename, 'w', encoding='UTF-8') as myFile:
        return myFile.write(json.dumps(my_obj))
