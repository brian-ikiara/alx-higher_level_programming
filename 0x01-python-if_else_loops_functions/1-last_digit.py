#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Handle negative values of number
if number > 0:
    div = 10
else:
    div = -10
# Store last digit as ldig
ldig = number % div
# Perform the necessary conditions
if ldig > 5:
    print(f"Last digit of {number:d} is {ldig:d} and is greater than 5")
elif (ldig <= 5) and (ldig != 0):
    print(f"Last digit of {number:d} is {ldig:d} and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {ldig:d} and is 0")
