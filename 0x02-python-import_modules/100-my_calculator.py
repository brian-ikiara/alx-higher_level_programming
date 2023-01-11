#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

lenArgs = len(sys.argv)

if __name__ == "__main__":
    if (lenArgs - 1) is not 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])
        if operator == "+":
            print("{:d} {} {:d} = {:d}".format(a, operator, b, add(a, b)))
        elif operator == "-":
            print("{:d} {} {:d} = {:d}".format(a, operator, b, sub(a, b)))
        elif operator == "*":
            print("{:d} {} {:d} = {:d}".format(a, operator, b, mul(a, b)))
        elif operator == "/":
            print("{:d} {} {:d} = {:d}".format(a, operator, b, div(a, b)))
        else:
            print("Unkown operator. Available operators: +, -, * and /")
            sys.exit(1)
