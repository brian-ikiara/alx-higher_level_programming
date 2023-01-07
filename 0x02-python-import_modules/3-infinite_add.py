#!/usr/bin/python3
"""
    Import argv from sys module
    Declare and initialize sumArgs and lenArgs as 0 and
    length of argv respectively
    For elements at indices greater than 0, print
    the sum of addition
"""
from sys import argv

resArgs = 0

if __name__ == "__main__":
    for s in argv[1:]:
        resArgs += int(s)

    print("{:d}".format(resArgs))
