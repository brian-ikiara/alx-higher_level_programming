#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end='')
            c += 1
    except IndexError:
        print("Exceeds list's bounds")
    print()
    return c
