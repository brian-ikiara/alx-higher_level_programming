#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy = a_dictionary.copy()
    keys = list(copy)
    for i in keys:
        copy[i] *= 2
    return copy
