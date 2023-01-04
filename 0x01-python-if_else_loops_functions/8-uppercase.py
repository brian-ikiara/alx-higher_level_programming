#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for ch in str:
        ch = ord(ch)
        if ch in range(97, 123):
            ch -= 32
        upper += chr(ch)
    print(f"{upper:s}")
