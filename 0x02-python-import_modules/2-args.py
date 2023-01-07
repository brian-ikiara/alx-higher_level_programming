#!/usr/bin/python3
# Import the sys module
from sys import argv
"""
    Initialize l as length of sys.argv
    Check if length of sys.argv is not zero
    then print the length of sys.argv then
    print the cmd args; otherwise, print
    zero
"""
i = 1
length = len(argv)
if length != 1:
    if length > 2:
        print("{} arguments:".format(length - 1))
    else:
        print("{} argument:".format(length - 1))
    for c in argv[1:]:
        print("{}: {}".format(i, c))
        i += 1
else:
    print("{} arguments.".format(length - 1))
