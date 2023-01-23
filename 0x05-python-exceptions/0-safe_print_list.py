#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    try:
        for i in my_list[:x]:
            print("{:d}".format(i), end='')
            c += 1
    except IndexError:
        print("Exceeds list's bounds")
    print()
    return c
