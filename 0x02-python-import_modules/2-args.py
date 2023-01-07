#!/usr/bin/python3
from sys import argv
i = 1
length = len(argv)

if __name__ == "__main__":
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
