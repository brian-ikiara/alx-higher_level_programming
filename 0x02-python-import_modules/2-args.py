#!/usr/bin/python3
# Import the sys module
import sys
""" 
    Initialize l as length of sys.argv
    Check if length of sys.argv is not zero
    then print the length of sys.argv then
    print the cmd args; otherwise, print
    zero
"""
i = 1
l = len(sys.argv)
if l != 1:
    if l > 2:
        print("{} arguments:".format(l - 1))
    else:
        print("{} argument:".format(l - 1))
    for c in sys.argv[1:]:
        print("{}: {}".format(i, c))
        i += 1
else:
    print("{} arguments.".format(l - 1))
