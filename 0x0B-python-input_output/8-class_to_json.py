#!/usr/bin/python3
"""This blew my mind."""


def class_to_json(obj):
    """Lexiconically represent an object.

    Args:
        obj ('obj':'any'): Python object

    Returns:
        Dictionary representation ;)

    """
    return obj.__dict__
