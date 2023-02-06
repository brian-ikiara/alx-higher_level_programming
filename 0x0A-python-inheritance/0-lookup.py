#!/usr/bin/python3
"""Returns more info about a Python object."""


def lookup(obj):
    """Return t.m.i.

    Args:
        obj ('obj':'list':'str'): The object

    Returns:
        t.m.i.

    """
    return list(dir(obj))
