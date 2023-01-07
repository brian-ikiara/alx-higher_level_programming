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
l = len(argv)
if l != 1:
    if l > 2:
        print("{} arguments:".format(l - 1))
    else:
        print("{} argument:".format(l - 1))
    for c in argv[1:]:
        print("{}: {}".format(i, c))
        i += 1
else:
    print("{} arguments.".format(l - 1))
