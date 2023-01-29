#!/usr/bin/python3
"""Simple integer addition."""


def add_integer(a, b=98):
    """Add a to b.

    Args:
        a (int, float): First number
        b (int, float): Second number

    Returns:
        The integral sum.

    """
    if (not isinstance(a, int)) and (not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int)) and (not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
