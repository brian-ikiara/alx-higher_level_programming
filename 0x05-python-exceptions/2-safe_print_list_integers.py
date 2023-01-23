#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    for i in range(0,x):
        try:
            print("{:d}".format(my_list[i]), end='')
            c += 1
        except (TypeError, ValueError):
            continue
    print()
    return c
