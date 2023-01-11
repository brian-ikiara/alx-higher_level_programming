#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        c_i = my_list[0]
        for i in my_list:
            if c_i < i:
                c_i = i
        return c_i
