#!/usr/bin/python3
"""Revised iplementation of issubclass()."""


def inherits_from(obj, a_class):
    """Check if obj is a subclass of a_class.

    Args:
        obj ('obj':'any'): The object
        a_class ('obj':'class'): The class

    Returns:
        True: issubclass(obj, a_class)
        False: !issubclass(obj, a_class)

    """
    return issubclass(obj, a_class)
