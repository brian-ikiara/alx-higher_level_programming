#!/usr/bin/python3
for ch in range(122, 96, -1):
    a = 32
    if (ch % 2) == 0:
        a = 0
    print("{:c}".format(ch - a), end='')
