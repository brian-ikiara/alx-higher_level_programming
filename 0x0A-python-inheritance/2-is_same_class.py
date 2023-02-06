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
    if isinstance(obj, a_class) or issubclass(obj, a_class):
        return True
    else:
        return False
