#!/usr/bin/python3
"""Implementation of isinstance().

This will be interesting.

"""


def is_same_class(obj, a_class):
    """Check if object is an instance of a class.

    Args:
        obj ('obj':'any'): The object
        a_class ('obj':'class'): The class

    Returns:
        True: isinstance(obj, a_class)
        False: !isinstance(obj, a_class)

    """
    return type(obj) is a_class
