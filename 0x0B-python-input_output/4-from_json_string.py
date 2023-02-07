#!/usr/bin/python3
"""Introduction to JSON."""
import json


def from_json_string(my_str):
    """Deserialize JSON data.

    Args:
        my_str ('obj':'str':'JSON'): JSON data

    Returns:
        The Python object.

    """
    return json.loads(my_str)
