#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)
    sumElem = 0
    for i in unique:
        sumElem += i
    return sumElem