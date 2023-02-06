#!/usr/bin/python3
"""Implementation of issubclass()."""


def is_kind_of_class(obj, a_class):
    """Check if is an instance or a subclass.

    Args:
        obj ('obj':'any'): The object
        a_class ('obj':'class'): The class

    Returns:
        True: issubclass(obj, a_class)
        False: !issubclass(obj, a_class)

    """
    if (type(obj) is a_class) and issubclass(obj, a_class):
        return True
    else:
        return False
