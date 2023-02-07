#!/usr/bin/python3
"""Introduction to JSON."""
import json


def to_json_string(my_obj):
    """Give JSON serialization of an object.

    Args:
        my_obj ('obj':'any'): Object

    Returns:
        JSON representation of my_obj.

    """
    return json.dumps(my_obj)
