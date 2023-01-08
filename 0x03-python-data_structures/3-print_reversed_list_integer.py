#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list != None:
        lenList = len(my_list) - 1
        while lenList >= 0:
            print("{:d}".format(my_list[lenList]))
            lenList -= 1
