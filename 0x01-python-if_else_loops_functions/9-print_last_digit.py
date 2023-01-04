#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        div = 10
    else:
        div = -10
    return number % div
