#!/usr/bin/python3
"""Removes the characters c and C from a string.

Args:
    my_string: String

Returns:
    c_string. my_string with no c and/or C
"""


def no_c(my_string):
    return (my_string.translate({ord('c'): None, ord('C'): None}))
