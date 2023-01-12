#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(list(a_dictionary))
    for i in keys:
        print("{}: {}".format(i, a_dictionary.get(i)))
